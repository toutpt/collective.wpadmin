from collective.wpadmin.pages.page import Page


class Comments(Page):
    """Dashboard page"""
    id = "edit-comments"
    title = u"Comments"
    description = u"Manage your comments"

    content_template_name = "editcomments.pt"
