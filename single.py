import logging

import sentry_sdk

from config import settings

logger = logging.getLogger(__name__)

sentry_sdk.init(
    settings.SENTRY_KEY,

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    release='1.0.0',
    environment='single',
    server_name='server',
)


def broken_function():
    variable = {str(i): i for i in range(10000)}
    logger.debug('This is debug')
    logger.info('This is info')
    logger.warning('This is warning')
    logger.error('This is error')
    logger.critical('This is critical')

    raise ValueError('This is my error')


def my_function():
    broken_function()


my_function()
