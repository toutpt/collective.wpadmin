import logging

from Acquisition import aq_inner
from zope import interface
from zope import schema
from z3c.form.interfaces import ISubForm, IFormLayer
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.z3cform.interfaces import IWrappedForm, IFormWrapper
from plone.z3cform import z2

from collective.wpadmin import i18n

_ = i18n.messageFactory
logger = logging.getLogger('collective.wpadmin')

class IWidget(interface.Interface):
    """Define a widget for the WP Admin view"""

    name = schema.ASCIILine(title=_(u"Widget name"))
    title = schema.TextLine(title=_(u"Title"))
    description = schema.TextLine(title=_(u"Description"))
    settings = schema.Object(interface.Interface, title=_(u"Settings"))

class Widget(object):
    interface.implements(IWidget)
    columns = 6
    index = ViewPageTemplateFile("widget.pt")
    title = u"Widget"
    description = u""
    settings = None

    def __init__(self, page):
        self.page = page
        self.context = page.context
        self.request = page.request
        self.cached_tools = {}
        self.cached_components = {}

    def __call__(self):
        self.update()
        return self.index()

    def update(self):
        pass

    def get_tool(self, tool_id):
        if tool_id not in self.cached_tools:
            self.cached_tools[tool_id] = getToolByName(self.context, tool_id)
        return self.cached_tools[tool_id]

    def query_catalog(self, query):
        catalog = self.get_tool('portal_catalog')
        logger.info(query)
        return catalog(**query)

    def get_query(self):
        query = {}
        query['path'] = '/'.join(self.context.getPhysicalPath())
        return query

    def get_types(self):
        return self.get_tool('portal_types')

    def get_workflows(self):
        return self.get_tools('portal_workflows')

    def get_portal_status(self):
        cid = "plone_portal_status"
        if cid not in self.cached_components:
            self.cached_components[cid] = component.getMultiAdapter(
                                            (self.context, self.request),
                                            name=cid)
        return self.cached_components[cid]


class WidgetFormWrapper(Widget):
    interface.implements(IFormWrapper)

    form = None # override this with a form class.
    request_layer = IFormLayer

    def __init__(self, page):
        super(WidgetFormWrapper, self).__init__(page)
        if self.form is not None:
            self.form_instance = self.form(
                aq_inner(self.context), self.request)
            self.form_instance.__name__ = self.name
            self.form_instance.parent_widget = self

    def update(self):
        if not ISubForm.providedBy(self.form_instance):
            interface.alsoProvides(self.form_instance, IWrappedForm)

        # If a form action redirected, don't render the wrapped form
        if self.request.response.getStatus() in (302, 303):
            self.contents = ""
            return

        z2.switch_on(self, request_layer=self.request_layer)
        self.form_instance.update()

        # A z3c.form.form.AddForm does a redirect in its render method.
        # So we have to render the form to see if we have a redirection.
        # In the case of redirection, we don't render the layout at all.
        self.contents = self.form_instance.render()
