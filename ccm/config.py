from .extentions import login_manager

class DefaultConfig(object):
	"""DefaultConfig includes common configurations for flask app.
	Other config objects inheret these common properties from it.
	"""
	DEBUG = False
	TESTING = False
	DB_SERVER = "127.0.0.1"
	SECRET_KEY = "dev"
	CSRF_ENABLED = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	EXTENTIONS = ['db','login_manager']
	BLUEPRINTS = [
		('ccm.blueprints.auth.authentication','auth_bp'),
		('ccm.blueprints.portal.dashboard','dash_bp')
	]
	login_manager.login_view = 'auth.authentication.login'
	USE_SESSION_FOR_NEXT = True

	# @property
	# def DATABASE_URI(self):
	# 	return 'mysql://user@{}/foo'.format(self.DB_SERVER)
	

class ProductionConfig(DefaultConfig):
	pass

class DevelopmentConfig(DefaultConfig):
	DEVELOPMENT = True
	TESTING = True
	DEBUG = True
	

class TestingConfig(DefaultConfig):
	DEBUG = True
	


		
		