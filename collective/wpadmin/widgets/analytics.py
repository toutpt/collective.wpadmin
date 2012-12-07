from collective.wpadmin.widgets import widget
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class AnalyticsWidget(widget.Widget):
    index = ViewPageTemplateFile("analytics.pt")
    def update(self):
        pass
