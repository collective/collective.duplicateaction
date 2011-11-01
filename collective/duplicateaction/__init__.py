# -*- coding: utf-8 -*-

from zope.i18nmessageid import MessageFactory
from plone.theme.interfaces import IDefaultPloneLayer

_ = MessageFactory('collective.duplicateaction')

class IBrowserLayer(IDefaultPloneLayer):

    """ Marker interface that defines a Zope 3 browser layer. """
