from zope import interface
from zope import schema

from collective.wpadmin import i18n
from Products.CMFCore.utils import getToolByName

_ = i18n.messageFactory


class IWidget(interface.Interface):
    """Define a widget for the WP Admin view"""

    title = schema.TextLine(title=_(u"Title"))
    description = schema.TextLine(title=_(u"Description"))


class Widget(object):
    def __init__(self, page):
        self.page = page
        self.wpadmin = page.wpadmin
        self.context = page.context
        self.request = page.request
        self.cached_tools = {}
        self.cached_components = {""}

    def __call__(self):
        self.update()
        return self.index()

    def index(self):
        raise NotImplementedError('widget should implement this')

    def get_tool(self, tool_id):
        if tool_id not in self.cached_tools:
            self.cached_tools[tool_id] = getToolByName(self.context, tool_id)
        return self.cached_tools[tool_id]

    def query_catalog(self, query):
        catalog = self.get_tool('portal_catalog')
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
