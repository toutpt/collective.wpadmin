from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from collective.wpadmin.pages.page import Page, PloneActionModal


class Posts(Page):
    """Dashboard page"""
    id = "edit"
    title = u"Posts"
    description = u"Manage your posts"

    content_template_name = "edit.pt"

    def get_all_posts(self):
        query = self.get_query()
        query['portal_type'] = ['News Item', 'Document', 'Event']
        return self.query_catalog(query)


class DeleteConfirmation(PloneActionModal):
    action = 'delete_confirmation'


class Rename(PloneActionModal):
    action = "rename"
