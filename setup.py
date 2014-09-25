# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

setup(
    service = ['test_service'],
    zipfile = None,
    options = {
        'py2exe': {
            'optimize': 2,
            'compressed': True,
            'bundle_files': 0,
            'excludes': [
                'readline', 
                'sets', 
                '__pypy__', 
                'Cheetah', 
                'Cookie', 
                'UserDict', 
                'bjoern', 
                'cherrypy', 
                'diesel', 
                'django', 
                'dummy_thread', 
                'eventlet', 
                'fapws', 
                'flup', 
                'gevent', 
                'google', 
                'gunicorn', 
                'jinja2.debugrenderer', 
                'mako', 
                'meinheld', 
                'paste', 
                'pretty', 
                'rocket', 
                'simplejson', 
                'socketio', 
                'thread', 
                'tornado', 
                'twisted', 
                'urllib.quote', 
                'urllib.unquote', 
                'urllib.urlencode', 
                'waitress'
            ]
        }
    }
)
