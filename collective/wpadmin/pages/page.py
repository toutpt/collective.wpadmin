from zope import component
from zope import interface
from zope import schema
from zope.publisher.interfaces.browser import IBrowserRequest
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from collective.wpadmin.widgets.widget import IWidget
from collective.wpadmin.utils import Core
from plone.app.customerize import registration


class IPage(interface.Interface):
    """a page is a set of wigets which provide administration screens"""

    id = schema.ASCIILine(title=u"Page ID")
    title = schema.TextLine(title=u"Title")
    description = schema.Text(title=u"Description")

    def get_url():
        """Return the page URL"""


class Page(Core):
    """Default implementation of IPage"""
    interface.implements(IPage)
    template_name = "page.pt"
    content_template_name = ""
    title = u"Default page"
    description = u""

    def __init__(self, context, request):
        Core.__init__(self, context, request)
        self.all_widgets = {}

    def update(self):
        self.request['plone.leftcolumn'] = False
        self.request['plone.rightcolumn'] = False
        pstate = self.get_portal_state()
        self.site_url = pstate.navigation_root_url()
        self.context_url = self.context.absolute_url()
        if self.content_template_name:
            template_name = '../templates/%s' % self.content_template_name
            self.contents = ViewPageTemplateFile(template_name)(self)

    def main_title(self):
        return self.context.Title()

    def get_menu(self):
        menu = []
        #http://developer.plone.org/views/browserviews.html
        views = registration.getViews(IBrowserRequest)
        pages = [view.factory for view in views \
                 if IPage.implementedBy(view.factory)]

        for page in pages:
            menu.append({'id': page.id,
                         'title': page.title})
        return menu

    def get_url(self):
        return '%s/wp-admin-%s' % (self.context.absolute_url(), self.id)


class IWidgetsContainer(IPage):
    left_widgets = schema.List(title=u"Left widgets")
    right_widgets = schema.List(title=u"Right widgets")


class WidgetsContainer(Page):
    left_widget_ids = []
    right_widget_ids = []
    content_template_name = "widgetscontainer_contents.pt"

    def __init__(self, context, request):
        super(WidgetsContainer, self).__init__(context, request)
        self.left_widgets = []
        self.right_widgets = []

    def update(self):
        if not self.left_widgets and not self.right_widgets:
            widgets = list(component.getAdapters((self,), IWidget))

            for name, widget in widgets:
                widget.update()
                self.all_widgets[name] = widget

            self._sort_widgets()
        super(WidgetsContainer, self).update()

    def _sort_widgets(self):
        for position in ('left', 'right'):
            for widget_id in getattr(self, '%s_widget_ids' % position, []):
                if widget_id in self.all_widgets:
                    widget = self.all_widgets[widget_id]
                    getattr(self, '%s_widgets' % position).append(widget)


class PloneActionModal(BrowserView):
    action = ""

    def __call__(self):
        self.request['ajax_load'] = True
        return self.context.restrictedTraverse(self.action)()
