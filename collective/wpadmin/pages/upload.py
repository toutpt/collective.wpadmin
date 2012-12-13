from collective.wpadmin.pages.page import Page
from collective.wpadmin import i18n

_ = i18n.messageFactory


class Media(Page):
    """Media page"""
    id = "upload"
    title = _(u"Media")
    description = _(u"Manage your medias")
    icon = "icon-picture"

    content_template_name = "upload.pt"

    def get_all_media(self):
        query = self.get_query()
        query['portal_type'] = ['File', 'Image']
        return self.query_catalog(query)

    def quickupload_url(self):
        return '%s/media/@@quick_upload' % self.context.absolute_url()
