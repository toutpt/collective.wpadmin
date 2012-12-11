from collective.wpadmin.pages.page import Page
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Tags(Page):
    """edit-tags page"""
    id = "edit-tags"
    title = u"Tags"
    description = u"Manage your tags"

    contents = ViewPageTemplateFile("edittags.pt")
