from collective.wpadmin.pages.page import Page


class Tags(Page):
    """edit-tags page"""
    id = "edit-tags"
    title = u"Tags"
    description = u"Manage your tags"

    content_template_name = "edittags.pt"
