# -*- coding: utf-8 -*-
"""
	Onename API
	Copyright 2014 Halfmoon Labs, Inc.
	~~~~~
"""

import os, re

if 'DYNO' in os.environ:
	# Debugging
	DEBUG = True

	# Secret settings
	for env_variable in os.environ:
		env_value = os.environ[env_variable]
		exec(env_variable + " = '" + env_value + "'")

	MONGODB_URI = MONGOLAB_URI

	parts = re.split(':|/|@|mongodb://', MONGOLAB_URI)
	_, MONGODB_USERNAME, MONGODB_PASSWORD, MONGODB_HOST, MONGODB_PORT, MONGODB_DB = parts
	print parts
	
else:
	APP_URL = 'localhost:5000'

	# Debugging
	DEBUG = True

	MONGOLAB_URI = 'mongodb://heroku_app31056693:6murjo28mdlii99edk2hho2h86@ds049130.mongolab.com:49130/heroku_app31056693'

	parts = re.split(':|/|@|mongodb://', MONGOLAB_URI)
	_, MONGODB_USERNAME, MONGODB_PASSWORD, MONGODB_HOST, MONGODB_PORT, MONGODB_DB = parts
	print parts

	# Database
	MONGODB_HOST = 'localhost'
	MONGODB_PORT = 27017
	MONGODB_DB = 'onename_api'

	# Secret settings
	from .secrets import *

	MONGODB_URI = 'mongodb://' + MONGODB_HOST + ':' + str(MONGODB_PORT) + '/' + MONGODB_DB

MAIL_USERNAME = 'support@onename.io'
