from collective.wpadmin.widgets import widget
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Summary(widget.Widget):
    """
    * total number of published blog posts
    * total number of comments
    * last drafts
    """
    content = ViewPageTemplateFile("summary.pt")
    name = "summary"
    title = u"Summary"

    def how_many_published_post(self):
        query = self.get_query()
        query['review_state'] = 'published'
        query['portal_type'] = ['News Item', 'Event', 'Document']
        return len(self.query_catalog(query))

    def how_many_comments(self, state=None):
        query = self.get_query()
        query['portal_type'] = 'Discussion'
        if state:
            query['review_state'] = state
        return len(self.query_catalog(query))

    def how_many_published_comments(self):
        return self.how_many_comments(state="published")

    def how_many_pending_comments(self):
        return self.how_many_comments(state="pending")

    def how_many_tags(self):
        catalog = self.get_tool('portal_catalog')
        return len(catalog.uniqueValuesFor('Subject'))

    def get_last_drafts(self):
        query = self.get_query()
        query['review_state'] = 'draft'
        return self.query_catalog(query)
