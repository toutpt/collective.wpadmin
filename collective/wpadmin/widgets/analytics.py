from collective.wpadmin.widgets import widget
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Analytics(widget.Widget):
    index = ViewPageTemplateFile("analytics.pt")
    name="analytics"

    def update(self):
        pass
