from collective.wpadmin.pages.page import Page
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Comments(Page):
    """Dashboard page"""
    id = "edit-comments"
    title = u"Comments"
    description = u"Manage your comments"

    contents = ViewPageTemplateFile("editcomments.pt")
