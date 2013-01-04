from zope import component
from zope import interface
from zope import schema
from z3c.form import form, button

from plone import api
from plone.autoform.form import AutoExtensibleForm
from plone.namedfile.field import NamedImage
from Products.statusmessages.interfaces import IStatusMessage

from collective.wpadmin.widgets import widget
from collective.wpadmin import i18n

_ = i18n.messageFactory


class IPressFormSchema(interface.Interface):
    """Press form schema"""
    title = schema.TextLine(title=_(u"Title"),
                            required=True)
#    directives.widget(body='plone.app.z3cform.wysiwyg.WysiwygFieldWidget')
    body = schema.Text(title=_(u"Body"))
    image = NamedImage(
            title=_(u"Please upload an image"),
            required=False)
    tags = schema.TextLine(title=_(u"Tags"))


class PressForm(AutoExtensibleForm, form.Form):
    schema = IPressFormSchema

    @button.buttonAndHandler(_(u"reset"))
    def action_reset(self, action):
        self.next_url()

    @button.buttonAndHandler(_(u"save"))
    def action_save(self, action):
        self.next_url()
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            for error in errors:
                IStatusMessage(self.request).add(error.message, "error")
            return False
        self.create_post(data)

    @button.buttonAndHandler(_(u"publish"))
    def action_publish(self, action):
        self.next_url()
        data, errors = self.extractData()
        if errors:
            return False
        post = self.create_post(data)
        self.publish_post(post)

    def create_post(self, data):
        if not hasattr(self, 'post_type'):
            self.post_type = 'News Item'
        post = api.content.create(type=self.post_type,
                                  title=data['title'],
                                  container=self.context)
        post.setText(data['body'].encode('utf-8'))
        tags = []
        for rawtag in data['tags'].split(','):
            tags.append(rawtag.strip())
        if tags:
            post.setSubject(tags)
        status = IStatusMessage(self.request)
        status.add("Post created", "info")
        return post

    def publish_post(self, post):
        api.content.transition(obj=post,
                               transition='publish')

    def next_url(self):
        #add status message
        self.request.response.redirect(self.parent_widget.page.get_url())


class EmptyPressFormAdapter(object):
    interface.implements(IPressFormSchema)
    component.adapts(interface.Interface)

    def __init__(self, context):
        self.context = context
        self.title = u""
        self.body = u""
        self.tags = u""


class IQuickPressSettings(interface.Interface):
    """settings for quickpress widget"""
    default_type = schema.ASCIILine(title=u"Default content type",
                                    default="News Item")


class QuickPress(widget.WidgetFormWrapper):
    name = "quickpress"
    title = _(u"Quick Press")
    form = PressForm
    content_template_name = "quickpress.pt"
