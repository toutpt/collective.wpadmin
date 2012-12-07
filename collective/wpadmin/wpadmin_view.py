from zope import component
from zope import interface
from zope import schema
from Products.Five.browser import BrowserView

from collective.wpadmin import i18n
from collective.wpadmin.pages.page import IPage
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

_ = i18n.messageFactory


class IWPAdminView(interface.Interface):
    """WPAdmin view interface"""
    menu = schema.List(title=_(u"Menu"))
    page_id = schema.ASCIILine(title=u"Page")
    page = schema.Object(title=u"Page object")


class WPAdminView(BrowserView):
    """WPAdmin view"""
    interface.implements(IWPAdminView)
    index = ViewPageTemplateFile("wpadmin.pt")

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.menu = []
        self.page_id = request.get("page", "dashboard")
        self.page = None

    def __call__(self):
        self.update()
        return self.index()

    def update(self):
        #remove plone portlets columns
        self.request['plone.leftcolumn'] = False
        self.request['plone.rightcolumn'] = False
        self.page = component.getAdapter(self,
                                         interface=IPage,
                                         name=self.page_id)
        self.page.update()

