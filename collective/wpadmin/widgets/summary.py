from collective.wpadmin.widgets import widget
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class SummaryWidget(widget.Widget):
    """
    * total number of published blog posts
    * total number of comments
    * last drafts
    """
    index = ViewPageTemplateFile("summary.pt")

    def how_many_published_post(self):
        query = self.get_query()
        query['review_state'] = 'published'
        return len(self.query_catalog(**query))

    def how_many_comments(self):
        query = self.get_query()
        query['portal_type'] = 'Discussion'
        return len(self.query_catalog(**query))

    def get_last_drafts(self):
        query = self.get_query()
        query['review_state'] = 'draft'
        return self.query_catalog(**query)
