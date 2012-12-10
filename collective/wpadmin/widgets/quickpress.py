from collective.wpadmin.widgets import widget
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


#TODO: add a quickpress form here using plone.autoform
class PressForm:
    def update(self):
        pass

class QuickPress(widget.Widget):
    index = ViewPageTemplateFile("quickpress.pt")
    name="quickpress"
    def update(self):
        self.press_form = PressForm()
        #TODO:Z2switch ...
        self.press_form.update()
