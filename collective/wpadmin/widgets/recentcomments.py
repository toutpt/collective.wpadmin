from collective.wpadmin.widgets import widget


class RecentComments(widget.Widget):
    name = "recentcomments"
    title = u"Recent comments"
    content_template_name = "recentcomments.pt"
