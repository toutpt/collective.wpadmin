from Acquisition import aq_inner
from zope import component
from zope import interface
from zope import schema
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from z3c.form import form, button

from plone.autoform.form import AutoExtensibleForm
from plone.autoform import directives
from plone.z3cform import z2

from collective.wpadmin.widgets import widget
from z3c.form.interfaces import IFormLayer
from plone.z3cform.interfaces import IWrappedForm


class IPressFormSchema(interface.Interface):
    """Press form schema"""
    title = schema.TextLine(title=u"Title")
#    directives.widget(body='plone.app.z3cform.wysiwyg.WysiwygFieldWidget')
    body = schema.Text(title=u"Body")
    tags = schema.TextLine(title=u"Tags")


class PressForm(AutoExtensibleForm, form.Form):
    schema = IPressFormSchema

    @button.buttonAndHandler(u"save")
    def action_save(self, action):
        pass

    @button.buttonAndHandler(u"reset")
    def action_reset(self, action):
        pass

    @button.buttonAndHandler(u"publish")
    def action_publish(self, action):
        pass


class EmptyPressFormAdapter(object):
    interface.implements(IPressFormSchema)
    component.adapts(interface.Interface)
    def __init__(self, context):
        self.context = context
        self.title = u""
        self.body = u""
        self.tags = u""


class QuickPress(widget.Widget):
    name="quickpress"
    title = u"Quick Press"
    content = ViewPageTemplateFile("quickpress.pt")

    def update(self):
        z2.switch_on(self, request_layer=IFormLayer)
        self.press_form = PressForm(aq_inner(self.context), self.request)
        interface.alsoProvides(self.press_form, IWrappedForm)  
        self.press_form.update()
