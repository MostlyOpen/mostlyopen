#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

import base

import xmlrpclib


def Data_Administrator_groups_id_clv_base():

    '''
    Reference: http://help.openerp.com/question/18704/hide-menu-for-existing-group/

    There are actually0-6 numbers for representing each job for a many2many/ one2many field

        (0, 0, { values }) -- link to a new record that needs to be created with the given values dictionary
        (1, ID, { values }) -- update the linked record with id = ID (write values on it)
        (2, ID) -- remove and delete the linked record with id = ID (calls unlink on ID, that will delete the
                   object completely, and the link to it as well)
        (3, ID) -- cut the link to the linked record with id = ID (delete the relationship between the two
                   objects but does not delete the target object itself)
        (4, ID) -- link to existing record with id = ID (adds a relationship)
        (5) -- unlink all (like using (3,ID) for all linked records)
        (6, 0, [IDs]) -- replace the list of linked IDs (like using (5) then (4,ID) for each ID in the list of IDs)
    '''

    print 'Executing Data_Administrator_groups_id_clv_base...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_base
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'User (clv)')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Super User (clv)')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Manager (clv)')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Register Manager (clv)')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Super Manager (clv)')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_tag():

    print 'Executing Data_Administrator_groups_id_clv_tag...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_tag
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Tag User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Tag Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_annotation():

    print 'Executing Data_Administrator_groups_id_clv_annotation...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_annotation
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Annotation User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Annotation Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Annotation Category Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_document():

    print 'Executing Data_Administrator_groups_id_clv_document...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_document
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Document User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Document Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Document Approver')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_professional():

    print 'Executing Data_Administrator_groups_id_clv_professional...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_professional
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Professional User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Professional Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Professional Category Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_address():

    print 'Executing Data_Administrator_groups_id_clv_address...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_address
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Address User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Address Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Address Category Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_residence():

    print 'Executing Data_Administrator_groups_id_clv_residence...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_residence
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Residence User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Residence Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_file():

    print 'Executing Data_Administrator_groups_id_clv_file...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_file
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'File User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'File Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'File Category Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_place():

    print 'Executing Data_Administrator_groups_id_clv_place...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_place
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Place User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Place Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Place Category Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_batch():

    print 'Executing Data_Administrator_groups_id_clv_batch...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_batch
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Batch User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Batch Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    # values = {
    #     'groups_id': [(
    #         4, sock.execute(base.dbname, uid, base.admin_user_pw,
    #                         'res.groups', 'search', [('name', '=', 'Batch Category Manager')]
    #                         )[0]
    #     )],
    # }
    # sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_person():

    print 'Executing Data_Administrator_groups_id_clv_person...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_person
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Person User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Person Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Person Category Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_family():

    print 'Executing Data_Administrator_groups_id_clv_family...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_family
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Family User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Family Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Family Category Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Family Member Role Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Family Member Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_community():

    print 'Executing Data_Administrator_groups_id_clv_community...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_community
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Community User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Community Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Community Category Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Community Person Role Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Community Person Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_patient():

    print 'Executing Data_Administrator_groups_id_clv_patient...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_patient
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Patient User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Patient Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_person_mng():

    print 'Executing Data_Administrator_groups_id_clv_person_mng...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_person_mng
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Person Management User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Person Management Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_insured():

    print 'Executing Data_Administrator_groups_id_clv_insured...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_insured
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Insured User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Insured Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Insured Category Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_insured_card():

    print 'Executing Data_Administrator_groups_id_clv_insured_card...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_insured_card
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Insured Card User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Insured Card Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    # values = {
    #     'groups_id': [(
    #         4, sock.execute(base.dbname, uid, base.admin_user_pw,
    #                         'res.groups', 'search', [('name', '=', 'Insured Card Category Manager')]
    #                         )[0]
    #     )],
    # }
    # sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_insured_mng():

    print 'Executing Data_Administrator_groups_id_clv_insured_mng...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_insured_mng
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Insured Management User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Insured Management Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_insured_ext():

    print 'Executing Data_Administrator_groups_id_clv_insured_ext...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_insured_ext
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Insured (Ext) User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Insured (Ext) Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_insurance_client():

    print 'Executing Administrator_groups_id_clv_insurance_client...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_insurance_client
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Insurance Client User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Insurance Client Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    # values = {
    #     'groups_id': [(
    #         4, sock.execute(base.dbname, uid, base.admin_user_pw,
    #                         'res.groups', 'search', [('name', '=', 'Insurance Client Category Manager')]
    #                         )[0]
    #     )],
    # }
    # sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_insurance_plan():

    print 'Executing Administrator_groups_id_clv_insurance_plan...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_insurance_plan
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Insurance Plan User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Insurance Plan Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    # values = {
    #     'groups_id': [(
    #         4, sock.execute(base.dbname, uid, base.admin_user_pw,
    #                         'res.groups', 'search', [('name', '=', 'Insurance Plan Category Manager')]
    #                         )[0]
    #     )],
    # }
    # sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_pharmacy():

    print 'Executing Data_Administrator_groups_id_clv_pharmacy...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_pharmacy
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Pharmacy User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Pharmacy Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    # values = {
    #     'groups_id': [(
    #         4, sock.execute(base.dbname, uid, base.admin_user_pw,
    #                         'res.groups', 'search', [('name', '=', 'Pharmacy Category Manager')]
    #                         )[0]
    #     )],
    # }
    # sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_medicament():

    print 'Executing Data_Administrator_groups_id_clv_medicament...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_medicament
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Medicament User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Medicament Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Medicament Form Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Medicament UOM Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Medicament Category Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Medicament Active Component Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Medicament Manufacturer Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_medicament_list():

    print 'Executing Administrator_groups_id_clv_medicament_list...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_medicament_list
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Medicament List User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Medicament List Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Medicament List Category Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Medicament List Version Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Medicament List Item Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_clv_medicament_group():

    print 'Executing Administrator_groups_id_clv_medicament_group...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # clv_medicament_group
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Medicament Group User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Medicament Group Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    # values = {
    #     'groups_id': [(
    #         4, sock.execute(base.dbname, uid, base.admin_user_pw,
    #                         'res.groups', 'search', [('name', '=', 'Medicament Group Category Manager')]
    #                         )[0]
    #         )],
    #     }
    # sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_l10n_br_clv_cmed_medicament():

    print 'Executing Administrator_groups_id_l10n_br_clv_cmed_medicament...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # l10n_br_clv_cmed_medicament
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'CMED Medicament User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'CMED Medicament Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_l10n_br_clv_abcfarma_medicament():

    print 'Executing Administrator_groups_id_l10n_br_clv_abcfarma_medicament...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # l10n_br_clv_abcfarma_medicament
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'ABCFarma Medicament User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'ABCFarma Medicament Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_l10n_br_clv_orz_medicament():

    print 'Executing Administrator_groups_id_l10n_br_clv_orz_medicament...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # l10n_br_clv_orz_medicament
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'ORZ Medicament User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'ORZ Medicament Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def Data_Administrator_groups_id_l10n_br_clv_grm_medicament():

    print 'Executing Administrator_groups_id_l10n_br_clv_grm_medicament...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Data Administrator'), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # l10n_br_clv_grm_medicament
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'GRM Medicament User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'GRM Medicament Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'
