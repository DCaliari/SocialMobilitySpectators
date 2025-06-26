from otree.api import *
import random
import numpy
import math
import time

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'socmob_spec'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 3
    Char_limit = 500

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    selected_image = models.StringField()

    randomized_order = models.StringField()

    question = models.StringField()

    error_q_11 = models.BooleanField(initial=False)
    error_q_5_spec = models.BooleanField(initial=False)
    error_q_6_spec = models.BooleanField(initial=False)
    error_q_7_spec = models.BooleanField(initial=False)

    def shuffle_questions(player):
        questions = [
            "Question1",  # Replace this with actual values related to images
            "Question2",
            "Question3"
        ]
        random.shuffle(questions)
        player.participant.vars['ordered_questions'] = questions



    q_11 = models.StringField(
        label="11) Is it possible to learn the results in the task of the members of the society by knowing their parents status?",
        choices=["a. Yes.",
                 "b. No."],
        widget=widgets.RadioSelect)
    q_5_spec = models.StringField(
        label="5) May good results in the task impact the final payoffs of the members of the society in the next question?",
        choices=["a. Yes, they may impact positively.",
                 "b. Yes, they may impact negatively.",
                 "c. No."],
        widget=widgets.RadioSelect)
    q_6_spec = models.StringField(
        label="6) May good results in the task impact the final payoffs of the members of the society in the next question?",
        choices=["a. Yes, they may impact positively.",
                 "b. Yes, they may impact negatively.",
                 "c. No."],
        widget=widgets.RadioSelect)
    q_7_spec = models.StringField(
        label="7) May good results in the task impact the final payoffs of the members of the society in the next question?",
        choices=["a. Yes, they may impact positively.",
                 "b. Yes, they may impact negatively.",
                 "c. No."],
        widget=widgets.RadioSelect)

    q_final_1 = models.LongStringField(
        label="Were the experimental instructions and the design clear? If anything was unclear about the instructions/design, e.g. how you will be paid, the role of the opening task, etc…, please describe briefly. (max 500 char.)")
    q_final_2 = models.LongStringField(label="What do you think is the purpose of the experiment? (max 500 char.)")
    q_final_3 = models.LongStringField(
        label="Did you answer each question independently from other questions or did you consider your answers to previous choices? Reply with “Yes or No” and please briefly explain why. (max 500 char.)")
    q_final_4 = models.LongStringField(
        label="Can you briefly motivate all or some of your choices? E.g. “I care about re-assigning the bonus because…”, “I wanted to maximize my own payoff, therefore…”, “I wanted to reward members who did well in the task, therefore…”, “I wanted to punish members who did badly in the task, therefore… (max 500 char.)”")

    parent = models.StringField()

    performance = models.FloatField()

    stars = models.IntegerField()

    child = models.StringField()

    chosen = models.StringField()



def q_11_error_message(player, value):
    if value != "b. No.":
        player.error_q_11 = True  # Record the error
        return 'This answer is wrong'

def q_5_spec_error_message(player, value):
    if value != "c. No.":
        player.error_q_5_spec = True  # Record the error
        return 'This answer is wrong'

def q_6_spec_error_message(player, value):
    if value != "a. Yes, they may impact positively.":
        player.error_q_6_spec = True  # Record the error
        return 'This answer is wrong'

def q_7_spec_error_message(player, value):
    if value != "b. Yes, they may impact negatively.":
        player.error_q_7_spec = True  # Record the error
        return 'This answer is wrong'


def q_final_1_error_message(player, value):
    if len(value) > C.Char_limit:
        return 'Character limit is ' + str(C.Char_limit)


def q_final_2_error_message(player, value):
    if len(value) > C.Char_limit:
        return 'Character limit is ' + str(C.Char_limit)


def q_final_3_error_message(player, value):
    if len(value) > C.Char_limit:
        return 'Character limit is ' + str(C.Char_limit)


def q_final_4_error_message(player, value):
    if len(value) > C.Char_limit:
        return 'Character limit is ' + str(C.Char_limit)


# Questions to be shuffled
questions_info = [
    {'decision': 'Decision 1', 'control': ['q_11', 'q_5_spec']},
    {'decision': 'Decision 2', 'control': ['q_11', 'q_6_spec']},
    {'decision': 'Decision 3', 'control': ['q_11', 'q_7_spec']},
]


def creating_session(subsession):
    for player in subsession.get_players():
        # Randomly assign "green" or "red" to player.parent
        set_randomized_questions(player)  # Ensure questions are set upon session creation


def set_randomized_questions(player):
    # Shuffle the questions_info list specifically for this player
    randomized_questions_info = questions_info[:]  # Create a copy of the global list
    random.shuffle(randomized_questions_info)  # Shuffle the copied list

    # Store the shuffled order in the player's randomized_order field
    player.randomized_order = ', '.join(info['decision'] for info in randomized_questions_info)

    player.participant.vars['questions_info'] = randomized_questions_info  # Assign shuffled questions to this player


class Setup(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1  # Show only in the first round

    @staticmethod
    def before_next_page(player: Player):
        set_randomized_questions(player)  # Initialize the questions here


class Quest(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number <= C.NUM_ROUNDS

    @staticmethod
    def get_form_fields(player: Player):
        """ Dynamically get the form fields based on randomized control questions. """
        question_index = player.round_number - 1  # Get the correct round index
        control_questions = player.participant.vars['questions_info'][question_index]['control']

        return control_questions  # Dynamically return correct fields

    form_fields = get_form_fields  # Set the form fields dynamically

    @staticmethod
    def vars_for_template(player: Player):
        if 'questions_info' not in player.participant.vars:
            raise Exception("questions_info not initialized.")  # Error handling
        question_index = player.round_number - 1  # Map round number to question index
        questions_info = player.participant.vars['questions_info']
        control_questions = questions_info[question_index]['control']  # Control questions for the current decision
        question = questions_info[question_index]['decision']

        player.question = question  # Store the question in the player object

        return dict(
            round=player.round_number,
            control_questions=control_questions,  # Pass the correct control questions to the template
            question=question,
        )


class Decision(Page):
    form_model = 'player'
    form_fields = ['selected_image']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number <= C.NUM_ROUNDS

    @staticmethod
    def vars_for_template(player: Player):
        if 'questions_info' not in player.participant.vars:
            raise Exception("questions_info not initialized.")  # Error handling

        question = player.question

        question_image1 = 'Online1.png'
        if question == 'Decision 1':
            question_image2 = 'Online4.png'
        elif question == 'Decision 2':
            question_image2 = 'Online2.png'
        else:
            question_image2 = 'Online3.png'

        # Create a list of images and shuffle their order
        images = [question_image1, question_image2]
        random.shuffle(images)  # Randomizes the order of images

        return dict(
            image_1=images[0],
            image_2=images[1],
            question=question,  # Decision question text
        )


class Decision_simple(Page):
    form_model = 'player'
    form_fields = ['selected_image']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number <= C.NUM_ROUNDS

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # Get the selected option from the POST request
        # selected_image_value = player.selected_image  # This retrieves the value selected from the form
        # We expect player.selected_image to populate with the value from the radio button
        # print(f'Selected Image: {selected_image_value}')  # Debugging output to check value

       # Check if `selected_image` is not None
        if not player.selected_image:
            print("Error: No option was selected.")  # This helps debug if no value was captured


    @staticmethod
    def vars_for_template(player: Player):
        if 'questions_info' not in player.participant.vars:
            raise Exception("questions_info not initialized.")  # Error handling
        question_index = player.round_number - 1  # Map round number to question index
        questions_info = player.participant.vars['questions_info']
        question = questions_info[question_index]['decision']

        question_image1 = 'NoMobility.png'
        if question == 'Decision 1':
            question_image2 = 'FullMobilityNeu.png'
        elif question == 'Decision 2':
            question_image2 = 'FullMobilityPos.png'
        else:
            question_image2 = 'FullMobilityNeg.png'

        # Create a list of images and shuffle their order
        images = [question_image1, question_image2]
        random.shuffle(images)  # Randomizes the order of images

        return dict(
            image_1=images[0],
            image_2=images[1],
            question=question  # Decision question text
        )


class Quest_Final(Page):
    form_model = 'player'
    form_fields = ['q_final_1', 'q_final_2', 'q_final_3', 'q_final_4']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


# PAGES
page_sequence = [Decision_simple, Quest_Final]
