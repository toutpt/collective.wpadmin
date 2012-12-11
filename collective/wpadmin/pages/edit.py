from collective.wpadmin.pages.page import Page
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Posts(Page):
    """Dashboard page"""
    id = "edit"
    title = u"Posts"
    description = u"Manage your posts"

    contents = ViewPageTemplateFile("edit.pt")
