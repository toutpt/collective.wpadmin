from collective.wpadmin.pages.page import Page


class Dashboard(Page):
    """Dashboard page"""
    id = "dashboard"
    title = u"Dashboard"
    description = u"Get all you need"

    left_widget_ids = ["summary", "recentcomments"]
    right_widget_ids = ["quickpress", "analytics"]
