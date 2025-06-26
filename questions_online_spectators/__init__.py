from otree.api import *
import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'questions_spec'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    prolific_id = models.StringField(
        label="Please write you Prolific ID (24 alphanumerical characters)",
        initial=""
    )

    error_q_1_spec = models.BooleanField(initial=False)
    error_q_2_spec = models.BooleanField(initial=False)
    error_q_3_spec = models.BooleanField(initial=False)

    q_1_spec = models.StringField(label="1) Can your decisions impact the others’ payoffs?",
                                  choices=["a. Yes.",
                                           "b. No"],
                                  widget=widgets.RadioSelect)
    q_2_spec = models.StringField(label="2) How many members who scored in the top (resp. bottom) half of the task can have high status parents?",
                                  choices=["a. Zero.",
                                           "b. One.",
                                           "c. More than one."],
                                  widget=widgets.RadioSelect)
    q_3_spec = models.StringField(label="3) Does the number of participants per each status change depending on the social mobility you choose?",
                                  choices=["a. Yes.",
                                           "b. No."],
                                  widget=widgets.RadioSelect)

    top_half = models.IntegerField(label="Likelihood of being in the top-half")
    bottom_half = models.IntegerField(label="Likelihood of being in the bottom-half")

    stars = models.IntegerField()
    performance = models.FloatField()
    treatment = models.StringField()

def q_1_spec_error_message(player, value):
    if value != "a. Yes.":
        player.error_q_1_spec = True  # Record the error
        return 'This answer is wrong'


def q_2_spec_error_message(player, value):
    if value != "b. One.":
        player.error_q_2_spec = True  # Record the error
        return 'This answer is wrong'


def q_3_spec_error_message(player, value):
    if value != "b. No.":
        player.error_q_3_spec = True  # Record the error
        return 'This answer is wrong'

def prolific_id_error_message(player, value):
    if len(value) != 24 or not value.isalnum():
        return 'Prolific ID must be exactly 24 alphanumeric characters.'

class Intro_2(Page):
    form_model = 'player'
    form_fields = ['q_1_spec',
                   'q_2_spec',
                   'q_3_spec',
                   'prolific_id'
                   ]

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Intro_4(Page):
    form_model = 'player'
    form_fields = ['top_half',
                   'bottom_half']

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    @staticmethod
    def error_message(player, values):
        if values['top_half'] + values['bottom_half'] != 100:
            return 'The likelihood must add up to 100'


class Intro_6(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Intro_7(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Intro_8(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Intro_9(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Intro_10(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Intro_11(Page):
    form_model = 'player'
    form_fields = ['q_1_spec',
                   'q_2_spec',
                   'q_3_spec',
                   ]

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


page_sequence = [Intro_4, Intro_2]
