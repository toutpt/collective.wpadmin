from collective.wpadmin.pages.page import Page


class Dashboard(Page):
    """Dashboard page"""
    name = "dashboard"

    widget_ids = ["summary", "quickpress", "statistics"]
