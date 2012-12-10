from collective.wpadmin.widgets import widget
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Analytics(widget.Widget):
    name="analytics"
    title = u"Analytics"
    content = ViewPageTemplateFile("analytics.pt")

    def update(self):
        pass
