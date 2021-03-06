import peewee
from peewee import *

from mocrud.exceptions import ImproperlyConfigured
from mocrud.utils import load_class


class Database(object):
    def __init__(self, config):
#        self.app = app
        self.database_config = config
        self.load_database()
#        self.register_handlers()

        self.Model = self.get_model_class()

    def load_database(self):
#        self.database_config = dict(self.app.config['DATABASE'])
        try:
            self.database_name = self.database_config.pop('name')
            self.database_engine = self.database_config.pop('engine')
        except KeyError:
            raise ImproperlyConfigured('Please specify a "name" and "engine" for your database')

        try:
            self.database_class = load_class(self.database_engine)
            assert issubclass(self.database_class, peewee.Database)
        except ImportError:
            raise ImproperlyConfigured('Unable to import: "%s"' % self.database_engine)
        except AttributeError:
            raise ImproperlyConfigured('Database engine not found: "%s"' % self.database_engine)
        except AssertionError:
            raise ImproperlyConfigured('Database engine not a subclass of peewee.Database: "%s"' % self.database_engine)

        self.database = self.database_class(self.database_name, **self.database_config)

    def get_model_class(self):
        class CrudModel(Model):
            class Meta:
                database = self.database

        return CrudModel

    def connect_db(self):
        self.database.connect()

    def close_db(self, exc):
        if not self.database.is_closed():
            self.database.close()

    def register_handlers(self):
        self.app.before_request(self.connect_db)
        self.app.teardown_request(self.close_db)
        
from mocrud import conf
db = Database(conf.crud_db_config)
        
class CrudModel(Model):
    class Meta:
        database = db.database
