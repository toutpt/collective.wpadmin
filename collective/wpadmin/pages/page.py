from zope import component
from zope import interface
from zope import schema
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from collective.wpadmin.widgets.widget import IWidget


class IPage(interface.Interface):
    """a page is a set of wigets which provide administration screens"""

    id = schema.ASCIILine(title=u"Page ID")
    title = schema.TextLine(title=u"Title")
    description = schema.Text(title=u"Description")

    widgets = schema.List(title=u"Widgets")


class Page(object):
    """Default implementation of IPage"""
    index = ViewPageTemplateFile("page.pt")
    title = u"Default page"
    description = u""
    widget_ids = []

    def __init__(self, wpadmin):
        self.wpadmin = wpadmin
        self.context = wpadmin.context
        self.request = wpadmin.request
        self.widgets = []

    def __call__(self):
        self.update()
        return self.index()

    def update(self):
        for widget_id in self.widget_ids:
            widget = component.getAdapters(self, IWidget)
            widget.update()
            self.widgets.append(widget)
