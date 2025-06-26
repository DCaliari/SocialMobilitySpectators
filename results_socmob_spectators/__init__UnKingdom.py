import csv
from otree.api import *
import random
import numpy
import math
import time
import pandas as pd


class C(BaseConstants):
    NAME_IN_URL = 'your_app_name'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    RESULTS_FILE_PATH = r'C:\Users\caliari\Dropbox\PC\Desktop\otreecourse\course\results_socmob\results.csv'  # Updated CSV file path.


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
        label="3) In which region do you live?",
        choices=["North East (England)",
                 "North West (England)",
                 "Yorkshire and The Humber (England)",
                 "East Midlands (England)",
                 "West Midlands (England)",
                 "East (England)",
                 "London (England)",
                 "South East (England)",
                 "South West (England)",
                 "Wales",
                 "Scotland",
                 "Northern Ireland"
                 ],
        widget=widgets.RadioSelect)

    q_4 = models.StringField(
        label="4) What was the monthly income of your household, after taxes, on average last year (2024)?",
        choices=["Less than 500",
                 "£500 - £1,500",
                 "£1,500 - £2,000",
                 "£2,000 - £3,000",
                 "£3,000 - £4,000",
                 "£4,000 - £5,000",
                 "£5,000 - £6,000",
                 "£6,000 - £8,000",
                 "£8,000 - £10,000",
                 "£10,000 - £12,000",
                 "More than £12,000"],
        widget=widgets.RadioSelect)

    q_5 = models.StringField(
        label="5) Please indicate your marital status",
        choices=["Single.",
                 "Married.",
                 "Other."],
        widget=widgets.RadioSelect)

    q_6 = models.StringField(
        label="6) How many children do you have?",
        choices=["I do not have children.",
                 "1.",
                 "2.",
                 "3.",
                 "4.",
                 "5 or more."],
        widget=widgets.RadioSelect)

    q_7 = models.StringField(
        label="7) Were you born in the United Kingdom?",
        choices=["Yes.",
                 "No."],
        widget=widgets.RadioSelect)

    q_8 = models.StringField(
        label="8) Were both of your parents born in the UK?",
        choices=["Yes.",
                 "No."],
        widget=widgets.RadioSelect)

    q_9 = models.StringField(
        label="9) Where was your father born?")

    q_10 = models.StringField(
        label="10) Where was your mother born?")

    q_11 = models.StringField(
        label="11) Which category best describes your highest level of education?",
        choices=["Primary education or less",
                 "Secondary education",
                 "Attended university, without obtaining a degree",
                 "Attended university and obtained a degree",
                 "Master's degree",
                 "Doctoral Degree"],
        widget=widgets.RadioSelect)

    q_12 = models.StringField(
        label="12) Which category best describes your father's highest level of education?",
        choices=["Primary education or less",
                 "Secondary education",
                 "Attended university, without obtaining a degree",
                 "Attended university and obtained a degree",
                 "Master's degree",
                 "Doctoral Degree"],
        widget=widgets.RadioSelect)

    q_13 = models.StringField(
        label="13) Which category best describes your mother's highest level of education?",
        choices=["Primary education or less",
                 "Secondary education",
                 "Attended university, without obtaining a degree",
                 "Attended university and obtained a degree",
                 "Master's degree",
                 "Doctoral Degree"],
        widget=widgets.RadioSelect)

    q_14 = models.StringField(
        label="14) What is your current employment status?",
        choices=["Full-time employee",
                 "Part-time employee",
                 "Self-employed or small business owner",
                 "Unemployed and looking for work",
                 "Student",
                 "Not in labor force (example: retired, or full-time parent"],
        widget=widgets.RadioSelect)

    q_15 = models.StringField(
        label="15) If you compare your job (or your last job if you currently don't have a job) with the job your father had while you were growing up, would you say that the level of status of your job is:",
        choices=["Much higher than my father's",
                 "Higher than my father's",
                 "About equal to my father's",
                 "Lower than my father's",
                 "Much lower than my father's",
                 "My father did not have a job while I was growing up OR I come from a single parent family"],
        widget=widgets.RadioSelect)

    q_16 = models.StringField(
        label="16) If you compare your job (or your last job if you currently don't have a job) with the job your mother had while you were growing up, would you say that the level of status of your job is:",
        choices=["Much higher than my mother's",
                 "Higher than my mother's",
                 "About equal to my mother's",
                 "Lower than my mother's",
                 "Much lower than my mother's",
                 "My mother did not have a job while I was growing up OR I come from a single parent family"],
        widget=widgets.RadioSelect)

    q_17 = models.StringField(
        label="17) When you were growing up, compared with families in the UK back then, would you say your family income was: ",
        choices=["Far below average",
                 "Below average",
                 "Average",
                 "Above average",
                 "Far above average"],
        widget=widgets.RadioSelect)

    q_18 = models.StringField(
        label="18) Right now, compared with families in the UK, would you say your own household income is: ",
        choices=["Far below average",
                 "Below average",
                 "Average",
                 "Above average",
                 "Far above average"],
        widget=widgets.RadioSelect)

    q_19 = models.StringField(
        label="19) On economic policy matters, where do you see yourself on the left/right spectrum?",
        choices=["Left",
                 "Centre-left",
                 "centre",
                 "Centre-right",
                 "Right"],
        widget=widgets.RadioSelect)

    q_20 = models.StringField(
        label="20) Before proceeding to the next set of questions, we want to ask for your feedback about the responses you provided so far. It is vital to our study that we only include responses from people who devoted their full attention to this study. This will not affect in any way the payment you will receive for taking this survey. In your honest opinion, should we use your responses, or should we discard your responses since you did not devote your full attention to the questions so far?",
        choices=[
            "Yes, I have devoted full attention to the questions so far and I think you should use my responses for your study.",
            "No, I have not devoted full attention to the questions so far and I think you should not use my responses for your study."],
        widget=widgets.RadioSelect)

    q_21 = models.StringField(
        label="21) Do you think the economic system in the United Kingdom is:",
        choices=[
            "Basically fair, since all Britons have an equal opportunity to succeed regardless their parent's income.",
            "Basically unfair, since all Britons do not have an equal opportunity to succeed because success depends on parent's income."],
        widget=widgets.RadioSelect)

    q_31 = models.StringField(
        label="21) Thinking about the economic system in the United Kingdom, to succeed in life, how important is coming from a wealthy family",
        choices=[
            "Essential",
            "Very important",
            "Fairly important",
            "Not very important",
            "Not important at all"],
        widget=widgets.RadioSelect)

    q_32 = models.StringField(
        label="21c) Thinking about the economic system in the United Kingdom, to succeed in life, how important is having well-educated parents",
        choices=[
            "Essential",
            "Very important",
            "Fairly important",
            "Not very important",
            "Not important at all"],
        widget=widgets.RadioSelect)

    q_33 = models.StringField(
        label="21d) Thinking about the economic system in the United Kingdom, to succeed in life, how important is hard work",
        choices=[
            "Essential",
            "Very important",
            "Fairly important",
            "Not very important",
            "Not important at all"],
        widget=widgets.RadioSelect)

    q_22 = models.StringField(
        label="22) Which has more to do with why a person is poor?",
        choices=[
            "Lack of effort on his or her own part.",
            "Circumstances beyond his or her control."],
        widget=widgets.RadioSelect)

    q_23 = models.StringField(
        label="23) Which has more to do with why a person is rich?",
        choices=[
            "Because she or he worked harder than others.",
            "Because she or he had more advantages than others."],
        widget=widgets.RadioSelect)

    q_24 = models.StringField(
        label="24) How much of the time do you think you can trust the government to do what is right?",
        choices=[
            "Never",
            "Only some of the time",
            "Most of the time",
            "Always"],
        widget=widgets.RadioSelect)

    q_25 = models.StringField(
        label="25) If children from poor and rich backgrounds have unequal opportunities in life, do you think this is:",
        choices=[
            "Not a problem at all",
            "A small problem",
            "A problem",
            "A serious problem",
            "A very serious problem"],
        widget=widgets.RadioSelect)

    q_26 = models.StringField(
        label="26) To reduce the inequality of opportunities between children born in poor and rich families, the government has the ability and the tools to do: ",
        choices=[
            "Nothing at all",
            "Not much",
            "Some",
            "A lot"],
        widget=widgets.RadioSelect)

    q_27 = models.StringField(
        label="27) Suppose the government has the ability and the tools to reduce the inequality of opportunities between children born in poor and rich families, how much do you agree that it should reduce it: ",
        choices=[
            "Strongly agree",
            "Agree",
            "Neither agree nor disagree",
            "Disagree",
            "Strongly disagree"],
        widget=widgets.RadioSelect)

    q_28 = models.StringField(
        label="28) How do you feel about the following statement? In the United Kingdom everybody has a chance to make it and be economically successful",
        choices=[
            "Strongly agree",
            "Agree",
            "Neither agree nor disagree",
            "Disagree",
            "Strongly disagree"],
        widget=widgets.RadioSelect)

    q_29 = models.StringField(
        label="29) Do you support more policies to increase the opportunities for children born in poor families and to foster more equality of opportunity, such as education policies? Naturally, to finance an expansion of policies promoting equal opportunity, it would have to be the case that either other policies are scaled down or taxes are raised. ",
        choices=[
            "I very strongly oppose more policies promoting equality of opportunity",
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
                   'q_6'
                   ]  # Player only inputs their ID here

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Survey_2(Page):
    form_model = 'player'
    form_fields = ['q_7',
                   'q_8',
                   'q_9',
                   'q_10', ]  # Player only inputs their ID here

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Survey_3(Page):
    form_model = 'player'
    form_fields = ['q_11',
                   'q_12',
                   'q_13']  # Player only inputs their ID here

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Survey_4(Page):
    form_model = 'player'
    form_fields = ['q_14',
                   'q_15',
                   'q_16',
                   'q_17',
                   'q_18']  # Player only inputs their ID here

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Survey_5(Page):
    form_model = 'player'
    form_fields = ['q_19',
                   'q_20']  # Player only inputs their ID here

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Survey_6(Page):
    form_model = 'player'
    form_fields = ['q_21',
                   'q_31',
                   'q_32',
                   'q_33']  # Player only inputs their ID here

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Survey_7(Page):
    form_model = 'player'
    form_fields = ['q_22',
                   'q_23',
                   'q_24',
                   'q_25',
                   'q_26',
                   'q_27',
                   'q_28',
                   'q_29']  # Player only inputs their ID here

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


page_sequence = [Survey, Survey_2, Survey_3, Survey_4, Survey_5, Survey_6, Survey_7, InputID, Results]
