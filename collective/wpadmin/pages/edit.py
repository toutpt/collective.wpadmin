from collective.wpadmin.pages.page import Page, PloneActionModal
from collective.wpadmin import i18n

_ = i18n.messageFactory


class Posts(Page):
    """Dashboard page"""
    id = "edit"
    title = _(u"Posts")
    description = _(u"Manage your posts")
    icon = "icon-folder-open"

    content_template_name = "edit.pt"

    def get_all_posts(self):
        query = self.get_query()
        query['portal_type'] = self.settings['blog_type']
        return self.query_catalog(query)


class DeleteConfirmation(PloneActionModal):
    action = "delete_confirmation"
    ajax_load = False


class BaseEdit(PloneActionModal):
    action = "base_edit"
    ajax_load = False


class Rename(PloneActionModal):
    action = "object_rename"
