import unittest2 as unittest
from collective.wpadmin.tests import base, utils
from ZPublisher.tests.testPublish import Request
from collective.wpadmin.pages import page


class UnitTestPage(base.UnitTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def setUp(self):
        super(UnitTestPage, self).setUp()
        self.context = utils.FakeContext()
        self.request = Request()
        self.view = page.Page(self.context, self.request)

    def test_main_title(self):
        self.assertEqual(self.view.main_title(), 'a title')


class IntegrationTestPage(base.IntegrationTestCase):
    def setUp(self):
        super(IntegrationTestPage, self).setUp()
        self.setRole('Manager')
        self.view = self.folder.restrictedTraverse('')


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
