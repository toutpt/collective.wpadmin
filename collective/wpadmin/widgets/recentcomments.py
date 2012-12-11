from collective.wpadmin.widgets import widget
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class RecentComments(widget.Widget):
    name="recentcomments"
    title = u"Recent comments"
    content = ViewPageTemplateFile("recentcomments.pt")

    def update(self):
        pass
