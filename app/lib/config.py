import pathlib
import configparser


PATH = pathlib.Path(__file__).parent.parent.parent

config = configparser.ConfigParser()
config.read(PATH / 'config.ini')
config['database']['uri'] = (
    'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(
        config['database']['username'],
        config['database']['password'],
        config['database']['host'],
        config['database']['port'],
        config['database']['name']
    )
)
