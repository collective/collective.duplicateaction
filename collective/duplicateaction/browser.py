# -*- coding: utf-8 -*-

import transaction

from zope.component import getMultiAdapter
from zope.security import checkPermission

from AccessControl import Unauthorized
from Acquisition import aq_inner
from Acquisition import aq_parent
from OFS.CopySupport import CopyError
from ZODB.POSException import ConflictError

from Products.CMFPlone.utils import transaction_note, safe_unicode
from Products.Five import BrowserView

from collective.duplicateaction import _

class DuplicateView(BrowserView):

    def duplicate(self):
        context = aq_inner(self.context)
        plone_utils = context.plone_utils
        title = safe_unicode(context.title_or_id())

        if not self.allowed():
            msg = _(u'Permission denied to duplicate ${title}.', mapping={u'title' : title})
            plone_utils.addPortalMessage(msg, 'error')
            raise Unauthorized, msg

        parent = aq_parent(context)

        try:
            parent.manage_copyObjects(context.getId(), self.request)
        except CopyError:
            message = _(u'${title} is not duplicable.', mapping={u'title' : title})
            plone_utils.addPortalMessage(message, 'error')
        
        transaction_note('Copied object %s' % context.absolute_url())

        msg=_(u'Duplicate failed to copy item.')

        redirect = self.request.RESPONSE.redirect

        if parent.cb_dataValid():
            try:
                paste = parent.manage_pasteObjects(parent.REQUEST['__cp'])
                transaction_note('Pasted item to %s' % (parent.absolute_url()))
                plone_utils.addPortalMessage(_(u'Item duplicated.'))
                return redirect(parent.absolute_url() + '/' + paste[0]['new_id'])
            except ConflictError:
                raise
            except ValueError:
                msg=_(u'Disallowed to duplicate item.')
            except Unauthorized:
                msg=_(u'Unauthorized to duplicate item.')
            except: # fallback
                transaction.abort() # in case of error in redirecting to new duplicated item
                msg=_(u'Duplicate failed to paste item.')

        
        plone_utils.addPortalMessage(msg, 'error')
        return redirect(context.absolute_url())
        

    def allowed(self):
        context = aq_inner(self.context)
        if not checkPermission('zope2.CopyOrMove', context):
            return False

        parent = aq_parent(context)
        factories = getMultiAdapter((parent, self.request),
                                    name='folder_factories')
        return self.context.portal_type in [factory['id'] for factory in
                factories.addable_types()]

