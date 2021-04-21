import logging
import random
import time

import sentry_sdk
from flask import Flask
from sentry_sdk import set_user
from sentry_sdk.integrations.flask import FlaskIntegration
from config import settings

logger = logging.getLogger(__name__)

sentry_sdk.init(
    settings.SENTRY_KEY,
    integrations=[FlaskIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    release='1.0.0',
    environment='single',
    server_name='server',
)

app = Flask(__name__)


@app.route('/')
def index():
    users = ['a@a.com', 'b@b.com']
    set_user({'email': random.choice(users)})
    variable = {'a': 1, 'b': 2}
    logger.debug('This is debug')
    logger.info('This is info')
    logger.warning('This is warning')
    logger.error('This is error')
    logger.critical('This is critical')

    raise ValueError('This is my error')


@app.route('/good')
def good_page():
    time.sleep(5)
    return 'OK'
