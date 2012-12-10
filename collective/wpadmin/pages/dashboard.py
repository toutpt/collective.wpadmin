from collective.wpadmin.pages.page import Page


class Dashboard(Page):
    """Dashboard page"""
    name = "dashboard"
    title = u"Dashboard"
    description = u"Get all you need"

    widget_ids = ["summary", "quickpress", "statistics"]
