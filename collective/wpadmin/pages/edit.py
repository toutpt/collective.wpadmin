from Acquisition import aq_inner
from zope import interface
from z3c.form import form, button
from z3c.form.interfaces import ISubForm, IFormLayer
from Products.Five.browser import BrowserView
from Products.statusmessages.interfaces import IStatusMessage

from plone import api
from plone.autoform.form import AutoExtensibleForm
from plone.z3cform.interfaces import IWrappedForm
from plone.z3cform import z2

from collective.wpadmin.pages.page import Page, PloneActionModal
from collective.wpadmin import i18n
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

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


class BaseEdit(PloneActionModal):
    action = "base_edit"
    ajax_load = False


class Rename(PloneActionModal):
    action = "object_rename"


class WPDeleteForm(AutoExtensibleForm, form.Form):
    """delete confirmation form"""
    schema = interface.Interface

    @button.buttonAndHandler(_(u"delete"))
    def action_delete(self, action):
        self.next_url()
        self.delete_item()

    @button.buttonAndHandler(_(u"cancel"))
    def action_cancel(self, action):
        self.next_url()

    def delete_item(self):
        """Delete the context and add a message"""
        api.content.delete(self.context)
        msg = "%s has been deleted" % self.context.Title()
        IStatusMessage(self.request).add(msg, "info")

    def next_url(self):
        url = self.request['HTTP_REFERER']
        self.request.response.redirect(url)


class WPDeleteFormView(BrowserView):
    form = WPDeleteForm
    request_layer = IFormLayer
    index = ViewPageTemplateFile('../templates/wpform.pt')
    description = u"If you validate it will be deleted"

    @property
    def title(self):
        return u"Delete %s" % self.context.Title()

    def __init__(self, context, request):
        super(WPDeleteFormView, self).__init__(context, request)
        if self.form is not None:
            self.form_instance = self.form(
                aq_inner(self.context), self.request)
            self.form_instance.__name__ = self.__name__

    def update(self):
        if not ISubForm.providedBy(self.form_instance):
            interface.alsoProvides(self.form_instance, IWrappedForm)

        # If a form action redirected, don't render the wrapped form
        if self.request.response.getStatus() in (302, 303):
            self.contents = ""
            return

        z2.switch_on(self, request_layer=self.request_layer)
        self.form_instance.update()

    def __call__(self):
        self.update()
        return self.index()

