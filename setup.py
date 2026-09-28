#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Setup file for devhelp dash plugin
'''

from distutils.core import setup
from DistUtilsExtra.command import build_extra
from DistUtilsExtra.command import build_i18n

setup(name='unity-scope-devhelp',
      version='0.1',
      author='Mark Tully',
      author_email='markjtully@gmail.com',
      url='http://launchpad.net/ubuntu-scopes',
      license='GNU General Public License (GPL)',
      data_files=[('share/dbus-1/services', ['data/unity-scope-devhelp.service']),
                  #('share/icons/unity-icon-theme/places/svg', ['data/icons/service-devhelp.svg']),
                  ('share/unity-scopes/devhelp', ['src/unity_devhelp_daemon.py']),
                  ('share/unity-scopes/devhelp', ['src/__init__.py']), ],
      cmdclass={'build': build_extra.build_extra,
                'build_i18n': build_i18n.build_i18n, })
