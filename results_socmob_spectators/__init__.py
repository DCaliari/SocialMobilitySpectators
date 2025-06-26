import csv
from otree.api import *
import random
import numpy
import math
import time
import pandas as pd


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    prolific_id = models.StringField(label="Enter your Prolific ID")
    children_status = models.StringField()
    selected_mobility = models.StringField()
    signal = models.StringField()

    q_1 = models.StringField(label="1) What is your gender?",
                             choices=["Male.",
                                      "Female."
                                      ],
                             widget=widgets.RadioSelect)

    q_2 = models.StringField(label="2) What is your age?")

    q_3 = models.StringField(
        label="3) In which state do you live?")

    q_4 = models.StringField(
        label="3) In which ZIP code do you live?")

    q_5 = models.StringField(
        label="4) What was the annual total income of your household, before taxes, on average last year (2024)?",
        choices=["0 - $ 9,999",
                 "$ 10,000 - $ 14,999",
                 "$ 15,000 - $ 19,999",
                 "$ 20,000 - $ 29,999",
                 "$ 30,000 - $ 39,999",
                 "$ 40,000 - $ 49,999",
                 "$ 50,000 - $ 69,999",
                 "$ 70,000 - $ 89,999",
                 "$ 90,000 - $ 109,999",
                 "$ 110,000 - $ 149,999",
                 "$ 150,000 - $ 199,999",
                 "More than $ 200,000",],
        widget=widgets.RadioSelect)

    q_6 = models.StringField(
        label="6) Please indicate your marital status",
        choices=["Single.",
                 "Married.",
                 "Other."],
        widget=widgets.RadioSelect)

    q_7 = models.StringField(
        label="7) How many children do you have?",
        choices=["I do not have children.",
                 "1.",
                 "2.",
                 "3.",
                 "4.",
                 "5 or more."],
        widget=widgets.RadioSelect)

    q_8 = models.StringField(
        label="8) How would you describe your ethnicity/race?",
        choices=["European American/White",
                 "African American/Black",
                 "Hispanic/Latino",
                 "Asian/Asian American",
                 "Other"],
        widget=widgets.RadioSelect)

    q_9 = models.StringField(
        label="9) Were you born in the United States?",
        choices=["Yes.",
                 "No."],
        widget=widgets.RadioSelect)

    q_10 = models.StringField(
        label="10) Were both of your parents born in the United States?",
        choices=["Yes.",
                 "No."],
        widget=widgets.RadioSelect)

    q_11 = models.StringField(label="11) Where was your father born?")

    q_12 = models.StringField(label="12) Where was your mother born?")

    q_13 = models.StringField(
        label="13) Which category best describes your highest level of education?",
        choices=["Eighth grade or less",
                 "Some high school",
                 "High school degree/ GED",
                 "Some college",
                 "2-year college degree",
                 "4-year college degree",
                 "Master's degree",
                 "Doctoral degree",
                 "Professional degree (JD, MD, MBA)"],
        widget=widgets.RadioSelect)

    q_14 = models.StringField(
        label="14) Which category best describes your father's highest level of education?",
        choices=["Eighth grade or less",
                 "Some high school",
                 "High school degree/ GED",
                 "Some college",
                 "2-year college degree",
                 "4-year college degree",
                 "Master's degree",
                 "Doctoral degree",
                 "Professional degree (JD, MD, MBA)",
                 "I come from a single parent family and my father was not present"],
        widget=widgets.RadioSelect)

    q_15 = models.StringField(
        label="15) Which category best describes your mother's highest level of education?",
        choices=["Eighth grade or less",
                 "Some high school",
                 "High school degree/ GED",
                 "Some college",
                 "2-year college degree",
                 "4-year college degree",
                 "Master's degree",
                 "Doctoral degree",
                 "Professional degree (JD, MD, MBA)",
                 "I come from a single parent family and my mother was not present"],
        widget=widgets.RadioSelect)

    q_16 = models.StringField(
        label="16) What is your current employment status?",
        choices=["Full-time employee",
                 "Part-time employee",
                 "Self-employed or small business owner",
                 "Unemployed and looking for work",
                 "Student",
                 "Not in labor force (example: retired, or full-time parent"],
        widget=widgets.RadioSelect)

    q_17 = models.StringField(
        label="17) If you compare your job (or your last job if you currently don't have a job) with the job your father had while you were growing up, would you say that the level of status of your job is:",
        choices=["Much higher than my father's",
                 "Higher than my father's",
                 "About equal to my father's",
                 "Lower than my father's",
                 "Much lower than my father's",
                 "My father did not have a job while I was growing up OR I come from a single parent family"],
        widget=widgets.RadioSelect)

    q_18 = models.StringField(
        label="18) If you compare your job (or your last job if you currently don't have a job) with the job your mother had while you were growing up, would you say that the level of status of your job is:",
        choices=["Much higher than my mother's",
                 "Higher than my mother's",
                 "About equal to my mother's",
                 "Lower than my mother's",
                 "Much lower than my mother's",
                 "My mother did not have a job while I was growing up OR I come from a single parent family"],
        widget=widgets.RadioSelect)

    q_19 = models.StringField(
        label="19) When you were growing up, compared with American families back then, would you say your family income was:",
        choices=["Far below average",
                 "Below average",
                 "Average",
                 "Above average",
                 "Far above average"],
        widget=widgets.RadioSelect)

    q_20 = models.StringField(
        label="20) Right now, compared with American families, would you say your own household income is:",
        choices=["Far below average",
                 "Below average",
                 "Average",
                 "Above average",
                 "Far above average"],
        widget=widgets.RadioSelect)

    q_21 = models.StringField(
        label="21) On economic policy matters, where do you see yourself on the left/right spectrum?",
        choices=["Very liberal",
                 "Liberal",
                 "Moderate",
                 "Conservative",
                 "Very conservative"],
        widget=widgets.RadioSelect)

    q_22 = models.StringField(
        label="22) Before proceeding to the next set of questions, we want to ask for your feedback about the responses you provided so far...",
        choices=[
            "Yes, I have devoted full attention to the questions so far and I think you should use my responses for your study.",
            "No, I have not devoted full attention to the questions so far and I think you should not use my responses for your study."],
        widget=widgets.RadioSelect)

    q_23 = models.StringField(
        label="23) Do you think the economic system in the United States is:",
        choices=[
            "Basically fair, since all Americans have an equal opportunity to succeed regardless their parent's income.",
            "Basically unfair, since all Americans do not have an equal opportunity to succeed because success depends on parent's income."],
        widget=widgets.RadioSelect)

    q_24 = models.StringField(
        label="24) Thinking about the economic system in the United States, to succeed in life, how important is coming from a wealthy family",
        choices=["Essential",
                 "Very important",
                 "Fairly important",
                 "Not very important",
                 "Not important at all"],
        widget=widgets.RadioSelect)

    q_25 = models.StringField(
        label="25) Thinking about the economic system in the United States, to succeed in life, how important is having well-educated parents",
        choices=["Essential",
                 "Very important",
                 "Fairly important",
                 "Not very important",
                 "Not important at all"],
        widget=widgets.RadioSelect)

    q_26 = models.StringField(
        label="26) Thinking about the economic system in the United States, to succeed in life, how important is hard work",
        choices=["Essential",
                 "Very important",
                 "Fairly important",
                 "Not very important",
                 "Not important at all"],
        widget=widgets.RadioSelect)

    q_27 = models.StringField(
        label="27) Which has more to do with why a person is poor?",
        choices=["Lack of effort on his or her own part.",
                 "Circumstances beyond his or her control."],
        widget=widgets.RadioSelect)

    q_28 = models.StringField(
        label="28) Which has more to do with why a person is rich?",
        choices=["Because she or he worked harder than others.",
                 "Because she or he had more advantages than others."],
        widget=widgets.RadioSelect)

    q_29 = models.StringField(
        label="29) How much of the time do you think you can trust the government to do what is right?",
        choices=["Never",
                 "Only some of the time",
                 "Most of the time",
                 "Always"],
        widget=widgets.RadioSelect)

    q_30 = models.StringField(
        label="30) If children from poor and rich backgrounds have unequal opportunities in life, do you think this is:",
        choices=["Not a problem at all",
                 "A small problem",
                 "A problem",
                 "A serious problem",
                 "A very serious problem"],
        widget=widgets.RadioSelect)

    q_31 = models.StringField(
        label="31) To reduce the inequality of opportunities between children born in poor and rich families, the government has the ability and the tools to do:",
        choices=["Nothing at all",
                 "Not much",
                 "Some",
                 "A lot"],
        widget=widgets.RadioSelect)

    q_32 = models.StringField(
        label="32) Suppose the government has the ability and the tools to reduce the inequality of opportunities between children born in poor and rich families, how much do you agree that it should reduce it:",
        choices=["Strongly agree",
                 "Agree",
                 "Neither agree nor disagree",
                 "Disagree",
                 "Strongly disagree"],
        widget=widgets.RadioSelect)

    q_33 = models.StringField(
        label="33) How do you feel about the following statement? In the United States everybody has a chance to make it and be economically successful",
        choices=["Strongly agree",
                 "Agree",
                 "Neither agree nor disagree",
                 "Disagree",
                 "Strongly disagree"],
        widget=widgets.RadioSelect)

    q_34 = models.StringField(
        label="34) Do you support more policies to increase the opportunities for children born in poor families and to foster more equality of opportunity...",
        choices=["I very strongly oppose more policies promoting equality of opportunity",
                 "I oppose more policies promoting equality of opportunity",
                 "I am indifferent",
                 "I support more policies equality of opportunity",
                 "I very strongly support more policies equality of opportunity"],
        widget=widgets.RadioSelect)


def prolific_id_error_message(player, value):
    # Open the CSV file and check if the entered value exists
    found = False
    try:
        with open(C.RESULTS_FILE_PATH, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['prolific_id'] == value:
                    found = True
                    break
    except Exception as e:
        print(f'Error reading the CSV file: {e}')

    # If the ID is not found in the CSV, return an error message
    if not found:
        return 'The entered Prolific ID is not found. Please enter a valid ID.'

    return None  # No error if everything is fine


class Survey(Page):
    form_model = 'player'
    form_fields = ['q_1',
                   'q_2',
                   'q_3',
                   'q_4',
                   'q_5',
                   'q_6',
                   'q_7',
                   'q_8'
                   ]  # Player only inputs their ID here

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Survey_2(Page):
    form_model = 'player'
    form_fields = ['q_9',
                   'q_10',
                   'q_11',
                   'q_12', ]  # Player only inputs their ID here

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Survey_3(Page):
    form_model = 'player'
    form_fields = ['q_13',
                   'q_14',
                   'q_15']  # Player only inputs their ID here

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Survey_4(Page):
    form_model = 'player'
    form_fields = ['q_16',
                   'q_17',
                   'q_18',
                   'q_19',
                   'q_20']  # Player only inputs their ID here

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Survey_5(Page):
    form_model = 'player'
    form_fields = ['q_21',
                   'q_22']  # Player only inputs their ID here

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Survey_6(Page):
    form_model = 'player'
    form_fields = ['q_23',
                   'q_24',
                   'q_25',
                   'q_26']  # Player only inputs their ID here

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Survey_7(Page):
    form_model = 'player'
    form_fields = ['q_27',
                   'q_28',
                   'q_29',
                   'q_30',
                   'q_31',
                   'q_32',
                   'q_33',
                   'q_34']  # Player only inputs their ID here

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class InputID(Page):
    form_model = 'player'
    form_fields = ['prolific_id']  # Player only inputs their ID here

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player, timeout_happened):
        id = player.prolific_id
        found = False

        # Initialize default values in case the ID is not found
        player.children_status = None
        player.selected_mobility = None
        player.signal = None

        with open(C.RESULTS_FILE_PATH, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)  # Print each row as a dictionary

                # Reset the file pointer to read again
            csvfile.seek(0)
            for row in reader:
                if row['prolific_id'] == id:
                    player.children_status = row['children status']
                    player.selected_mobility = row['selected mobility']
                    player.signal = row['signal']
                    found = True
                    break

        if not found:
            player.prolific_id = None

        else:
            # Print the retrieved values for debugging
            print(f"Retrieved values for ID {id}:")
            print(f"Children Status: {player.children_status}")
            print(f"Selected Mobility: {player.selected_mobility}")
            print(f"Signal: {player.signal}")

class Results(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'children_status': player.children_status,
            'selected_mobility': player.selected_mobility,
            'signal': player.signal,
        }


page_sequence = [Survey, Survey_2, Survey_3, Survey_4, Survey_5, Survey_6, Survey_7]
