from collective.wpadmin.widgets import widget


class Analytics(widget.Widget):
    name = "analytics"
    title = u"Analytics"
    content_template_name = "analytics.pt"

    def update(self):
        pass
