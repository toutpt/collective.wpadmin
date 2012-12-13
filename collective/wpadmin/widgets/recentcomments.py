from collective.wpadmin.widgets import widget
from collective.wpadmin import i18n

_ = i18n.messageFactory


class RecentComments(widget.Widget):
    name = "recentcomments"
    title = _(u"Recent comments")
    content_template_name = "recentcomments.pt"
