from collective.wpadmin.widgets import widget
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


#TODO: add a quickpress form here using plone.autoform
class PressForm:
    pass

class QuickPressWidget(widget.Widget):
    index = ViewPageTemplateFile("quickpress.pt")
    def update(self):
        self.press_form = PressForm()
        #TODO:Z2switch ...
        self.press_form.update()
