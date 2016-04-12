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


def Data_Administrator_groups_id_clv_medicament_list():

    print 'Executing Administrator_groups_id_clv_medicament_list...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', 'Administrator'), ]
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
    # values = {
    #     'groups_id': [(
    #         4, sock.execute(base.dbname, uid, base.admin_user_pw,
    #                         'res.groups', 'search', [('name', '=', 'Medicament List Category Manager')]
    #                         )[0]
    #         )],
    #     }
    # sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

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
