BROKER_URL = 'amqp://guest@localhost//'

CELERY_TIMEZONE = 'Europe/Moscow'

CELERYD_MAX_TASKS_PER_CHILD = 1

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'