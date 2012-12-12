import logging

from zope import component
from zope.publisher.interfaces.browser import IBrowserRequest
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView

from plone.app.customerize import registration
from plone import api

from Products.statusmessages.interfaces import IStatusMessage

logger = logging.getLogger('collective.wpadmin')


class Core(BrowserView):
    """Default implementation of IPage"""
    template_name = ""

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.cached_components = {}
        self.cached_tools = {}

    @property
    def index(self):
        return ViewPageTemplateFile(self.template_name)

    def __call__(self):
        self.update()
        return self.index()

    def update(self):
        pass

    def get_tool(self, tool_id):
        if tool_id not in self.cached_tools:
            tool = api.portal.get_tool(name='portal_catalog')
            self.cached_tools[tool_id] = tool
        return self.cached_tools[tool_id]

    def query_catalog(self, query):
        catalog = self.get_tool('portal_catalog')
        return catalog(**query)

    def get_query(self):
        query = {}
        query['path'] = '/'.join(self.context.getPhysicalPath())
        return query

    def get_portal_state(self):
        cid = "plone_portal_state"
        if cid not in self.cached_components:
            self.cached_components[cid] = component.getMultiAdapter(
                                            (self.context, self.request),
                                            name=cid)
        return self.cached_components[cid]

    def get_views(self, interface=None):
        #http://developer.plone.org/views/browserviews.html
        views = registration.getViews(IBrowserRequest)
        self.cached_components['views'] = views

    def get_messages(self):
        return IStatusMessage(self.request).show()

    def log(self, message, mtype="info"):
        log = getattr(logger, mtype)
        log(message)
