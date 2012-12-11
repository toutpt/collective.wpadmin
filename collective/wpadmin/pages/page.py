from zope import component
from zope import interface
from zope import schema
from zope.publisher.interfaces.browser import IBrowserRequest
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView

from plone.app.layout.globals.interfaces import IViewView
from plone.app.customerize import registration

from collective.wpadmin.widgets.widget import IWidget


class IPage(interface.Interface):
    """a page is a set of wigets which provide administration screens"""

    id = schema.ASCIILine(title=u"Page ID")
    title = schema.TextLine(title=u"Title")
    description = schema.Text(title=u"Description")

    left_widgets = schema.List(title=u"Left widgets")
    right_widgets = schema.List(title=u"Right widgets")

    def get_url():
        """Return the page URL"""


class Page(BrowserView):
    """Default implementation of IPage"""
    interface.implements(IPage)
    index = ViewPageTemplateFile("page.pt")
    title = u"Default page"
    description = u""
    left_widget_ids = []
    right_widget_ids = []

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.left_widgets = []
        self.right_widgets = []
        self.all_widgets = {}
        self.cached_components = {}

    def __call__(self):
        self.update()
        return self.index()

    def update(self):
        self.request['plone.leftcolumn'] = False
        self.request['plone.rightcolumn'] = False
        pstate = self.get_portal_state()
        self.site_url = pstate.navigation_root_url()
        self.context_url = self.context.absolute_url()
        #for widget_id in self.widget_ids:
        if not self.left_widgets and not self.right_widgets:
            widgets = list(component.getAdapters((self,), IWidget))

            for name, widget in widgets:
                widget.update()
                self.all_widgets[name] = widget

            self._sort_widgets()

    def _sort_widgets(self):
        for position in ('left', 'right'):
            for widget_id in getattr(self, '%s_widget_ids'%position, []):
                if widget_id in self.all_widgets:
                    widget = self.all_widgets[widget_id]
                    getattr(self, '%s_widgets'%position).append(widget)

    def main_title(self):
        return self.context.Title()

    def get_portal_state(self):
        cid = "plone_portal_state"
        if cid not in self.cached_components:
            self.cached_components[cid] = component.getMultiAdapter(
                                            (self.context, self.request),
                                            name=cid)
        return self.cached_components[cid]

    def get_menu(self):
        menu = []
        #http://developer.plone.org/views/browserviews.html#listing-available-views
        views = registration.getViews(IBrowserRequest)
        pages = [view.factory for view in views \
                 if IPage.implementedBy(view.factory)]

        for page in pages:
            menu.append({'id': page.id,
                         'title': page.title})
        return menu

    def get_url(self):
        return '%s/wp-admin-%s' % (self.context.absolute_url(), self.id)
