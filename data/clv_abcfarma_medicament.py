#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2016-Today  Carlos Eduardo Vercelino - CLVsol
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

from __future__ import print_function

import argparse
import getpass

from odoo_api import *


def get_arguments():

    global server
    global username
    global password
    global dbname

    parser = argparse.ArgumentParser()
    parser.add_argument('--server', action="store", dest="server")
    parser.add_argument('--user', action="store", dest="username")
    parser.add_argument('--pw', action="store", dest="password")
    parser.add_argument('--db', action="store", dest="dbname")

    args = parser.parse_args()
    print('%s%s' % ('--> ', args))

    if args.server is not None:
        server = args.server
    elif server == '*':
        server = raw_input('server: ')

    if args.dbname is not None:
        dbname = args.dbname
    elif dbname == '*':
        dbname = raw_input('dbname: ')

    if args.username is not None:
        username = args.username
    elif username == '*':
        username = raw_input('username: ')

    if args.password is not None:
        password = args.password
    elif password == '*':
        password = getpass.getpass('password: ')


def secondsToStr(t):

    return "%d:%02d:%02d.%03d" % reduce(lambda ll, b: divmod(ll[0], b) + ll[1:], [(t * 1000,), 1000, 60, 60])


if __name__ == '__main__':

    server = 'http://localhost:8069'
    # server = '*'

    username = 'username'
    # username = '*'
    password = 'password'
    # password = '*'

    dbname = 'odoo'
    # dbname = '*'

    print()
    print('--> clv_abcfarma_medicament.py...')
    print('--> server:', server)

    get_arguments()

    from time import time
    start = time()

    client = erppeek.Client(server, dbname, username, password)

    # list_name = 'TABELA_2015_09'
    # print('-->', client, list_name)
    # print('--> Executing clv_abcfarma_medicament_list_unlink()...')
    # clv_abcfarma_medicament_list_unlink(client, list_name)

    # medicament_args = []
    # print('-->', client, medicament_args)
    # print('--> Executing clv_abcfarma_medicament_unlink()...')
    # clv_abcfarma_medicament_unlink(client, medicament_args)

    # ########## 2016-05-06 ##########

    # file_name = '/opt/openerp/abcfarma/TABELA_2016_04.dbf'
    # list_name = 'TABELA_2016_04'
    # updt_medicament_data = True
    # updt_item_data = True
    # print('-->', client, file_name, list_name,
    #       updt_medicament_data, updt_item_data)
    # print('--> Executing clv_abcfarma_medicament_import()...')
    # clv_abcfarma_medicament_import(client, file_name, list_name,
    #                         updt_medicament_data, updt_item_data)

    # file_name = '/opt/openerp/abcfarma/TABELA_2016_05.dbf'
    # list_name = 'TABELA_2016_05'
    # updt_medicament_data = True
    # updt_item_data = True
    # print('-->', client, file_name, list_name,
    #       updt_medicament_data, updt_item_data)
    # print('--> Executing clv_abcfarma_medicament_import()...')
    # clv_abcfarma_medicament_import(client, file_name, list_name,
    #                         updt_medicament_data, updt_item_data)

    # file_name = '/opt/openerp/abcfarma/TABELA_2016_03.dbf'
    # list_name = 'TABELA_2016_03'
    # updt_medicament_data = False
    # updt_item_data = False
    # print('-->', client, file_name, list_name,
    #       updt_medicament_data, updt_item_data)
    # print('--> Executing clv_abcfarma_medicament_import()...')
    # clv_abcfarma_medicament_import(client, file_name, list_name,
    #                         updt_medicament_data, updt_item_data)

    # ########## 2016-05-08 ##########

    abcfarma_medicament_args = []
    db_path = 'data/mostlyopen.sqlite'
    print('-->', client, abcfarma_medicament_args, db_path)
    print('--> Executing clv_abcfarma_medicament_export_sqlite()...')
    print()
    clv_abcfarma_medicament_export_sqlite(client, abcfarma_medicament_args, db_path)

    print()
    print('--> clv_abcfarma_medicament.py', '- Execution time:', secondsToStr(time() - start))
    print()
