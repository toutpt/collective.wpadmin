from collective.wpadmin.pages.page import Page
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView


class Media(Page):
    """Media page"""
    id = "upload"
    title = u"Media"
    description = u"Manage your medias"

    contents = ViewPageTemplateFile("upload.pt")

    def get_all_media(self):
        query = self.get_query()
        query['portal_type'] = ['File', 'Image']
        return self.query_catalog(query)


    def quickupload_url(self):
        return '%s/media/@@quick_upload' % self.context.absolute_url()
