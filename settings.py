from os import environ

SESSION_CONFIGS = [
    dict(
        name='socmob_spectators',
        app_sequence=['task_online_spectators', 'questions_online_spectators', 'socmob_online_spectators', 'results_socmob_spectators'],
        num_demo_participants=20,
        time_to_solve=180,
    ),
]

ROOMS = [
    dict(
        name='experiment',
        display_name='Experiment',
        # participant_label_file='_rooms/experiment.txt'
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['total_order', 'q_order', 'performance', 'prob', 'position_order', 'task_solved', 'task_total_time', 'treatment']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '1323315948621'
