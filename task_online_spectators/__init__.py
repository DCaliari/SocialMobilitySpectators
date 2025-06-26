from otree.api import *
import time
import math
import numpy

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'task_spec'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 50


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    task_solution = models.IntegerField()
    task_answer = models.IntegerField()
    time_start = models.FloatField()
    time_end = models.FloatField()
    time_performance = models.FloatField()
    time_total_performance = models.FloatField()

    task_solved = models.IntegerField()
    task_total_time = models.FloatField()

def task_answer_error_message(player, value):
    if value != player.task_solution:
        return 'This Answer is incorrect'


class Intro_1(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Intro_3(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Setup(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    def before_next_page(player, timeout_happened):
        # Set time_start when they click the next button to go to the next page
        player.time_start = time.time()  # Capture the current time when the button is clicked


class Task(Page):
    form_model = 'player'
    form_fields = ['task_answer']

    @staticmethod
    def is_displayed(player):
        player_in_1 = player.in_round(1)
        time_to_solve = player.session.config['time_to_solve']
        return time.time() < player_in_1.time_start + time_to_solve

    @staticmethod
    def js_vars(player):
        random_matrix_1 = player.session.vars["random_matrices"][player.round_number - 1][0]
        random_matrix_2 = player.session.vars["random_matrices"][player.round_number - 1][1]
        max_element1 = 0
        for i in range(10):
            for j in range(10):
                if random_matrix_1[i][j] > max_element1:
                    max_element1 = random_matrix_1[i][j]

        max_element2 = 0
        for i in range(10):
            for j in range(10):
                if random_matrix_2[i][j] > max_element2:
                    max_element2 = random_matrix_2[i][j]

        player.task_solution = max_element1 + max_element2
        print(player.task_solution)
        return dict(
            random_matrix_1=random_matrix_1,
            random_matrix_2=random_matrix_2
        )

    @staticmethod
    def get_timeout_seconds(player):
        time_to_solve = player.session.config['time_to_solve']
        return time_to_solve - (time.time() - player.in_round(1).time_start)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.time_end = time.time()
        player_in_1 = player.in_round(1)
        player.time_performance = player.time_end - player_in_1.time_start
        time_to_solve = player.session.config['time_to_solve']

        if timeout_happened:
            if player.round_number == 1:
                player.participant.vars["task_total_time"] = time_to_solve
                player_in_1.task_total_time = time_to_solve
            else:
                player_in_last = player.in_round(player.round_number - 1)
                player.participant.vars["task_total_time"] = player_in_last.time_end - player_in_1.time_start
                player_in_1.task_total_time = player_in_last.time_end - player_in_1.time_start

            if not ("task_solved" in player.participant.vars):
                player.participant.vars["task_solved"] = 0
                player_in_1.task_solved = 0
            performance = (-1) * (player_in_1.task_solved - (player_in_1.task_total_time / 1000))
            player.participant.vars["performance"] = performance
            player_in_1.time_total_performance = performance
        else:
            player.participant.vars["task_solved"] = player.round_number
            player_in_1.task_solved = player.round_number


page_sequence = [Intro_1, Intro_3, Setup, Task]


def creating_session(subsession):
    if subsession.round_number == 1:
        subsession.session.vars["random_matrices"] = []
    random_matrix_1 = [[math.floor(numpy.random.triangular(10, 55, 100)) for _ in range(10)],
                       [math.floor(numpy.random.triangular(10, 55, 100)) for _ in range(10)],
                       [math.floor(numpy.random.triangular(10, 55, 100)) for _ in range(10)],
                       [math.floor(numpy.random.triangular(10, 55, 100)) for _ in range(10)],
                       [math.floor(numpy.random.triangular(10, 55, 100)) for _ in range(10)],
                       [math.floor(numpy.random.triangular(10, 55, 100)) for _ in range(10)],
                       [math.floor(numpy.random.triangular(10, 55, 100)) for _ in range(10)],
                       [math.floor(numpy.random.triangular(10, 55, 100)) for _ in range(10)],
                       [math.floor(numpy.random.triangular(10, 55, 100)) for _ in range(10)],
                       [math.floor(numpy.random.triangular(10, 55, 100)) for _ in range(10)]]
    random_matrix_2 = [[math.floor(numpy.random.triangular(10, 55, 100)) for _ in range(10)],
                       [math.floor(numpy.random.triangular(10, 55, 100)) for _ in range(10)],
                       [math.floor(numpy.random.triangular(10, 55, 100)) for _ in range(10)],
                       [math.floor(numpy.random.triangular(10, 55, 100)) for _ in range(10)],
                       [math.floor(numpy.random.triangular(10, 55, 100)) for _ in range(10)],
                       [math.floor(numpy.random.triangular(10, 55, 100)) for _ in range(10)],
                       [math.floor(numpy.random.triangular(10, 55, 100)) for _ in range(10)],
                       [math.floor(numpy.random.triangular(10, 55, 100)) for _ in range(10)],
                       [math.floor(numpy.random.triangular(10, 55, 100)) for _ in range(10)],
                       [math.floor(numpy.random.triangular(10, 55, 100)) for _ in range(10)]]
    subsession.session.vars["random_matrices"] = subsession.session.vars["random_matrices"] + [
        [random_matrix_1, random_matrix_2]]
