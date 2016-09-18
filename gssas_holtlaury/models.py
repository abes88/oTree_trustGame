from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, safe_json
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'gssas_holtlaury'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # GSS
    people_try_to_take_advantage_of_you_if_they_got_a_chance = models.CharField(
        max_length=1, choices=[("A", 'A. Would take advantage of you'), ("B", 'B. Would try to be fair')], widget=widgets.RadioSelectHorizontal(),
        verbose_name="Do you think most people would try to take advantage of you if they got a chance, or would they try to be fair?")

    most_of_the_time_people_try_to_be_helpful = models.CharField(
        max_length=1, choices=[("A", 'A. Try to be helpful'), ("B", 'B. Just look out for themselves')], widget=widgets.RadioSelectHorizontal(),
        verbose_name="Would you say that most of the time people try to be helpful, or that they are mostly just looking out for themselves?")

    that_most_people_can_be_trusted = models.CharField(
        max_length=1, choices=[("A", 'A. Most people can be trusted'), ("B", "B. Can't be too careful")], widget=widgets.RadioSelectHorizontal(),
        verbose_name="Generally speaking, would you say that most people can be trusted or that you can't be too careful in dealing with people?")

    # HOLT LAURIE
    decision_1 = models.CharField(
        max_length=1, widget=widgets.RadioSelectHorizontal(), verbose_name="Decision 1",
        choices=[("A",  "A. $2.00 if Card is 1\n$1.60 if Card is 2-10"),
                 ("B",  "B. $3.85 if Card is 1\n$0.10 if Card is 2-10")])
    decision_2 = models.CharField(
        max_length=1, widget=widgets.RadioSelectHorizontal(), verbose_name="Decision 2",
        choices=[("A",  "A. $2.00 if Card is 1-2\n$1.60 if Card is 3-10"),
                 ("B",  "B. $3.85 if Card is 1-2\n$0.10 if Card is 3-10")])
    decision_3 = models.CharField(
        max_length=1, widget=widgets.RadioSelectHorizontal(), verbose_name="Decision 3",
        choices=[("A",  "A. $2.00 if Card is 1-3\n$1.60 if Card is 4-10"),
                 ("B",  "B. $3.85 if Card is 1-3\n$0.10 if Card is 4-10")])
    decision_4 = models.CharField(
        max_length=1, widget=widgets.RadioSelectHorizontal(), verbose_name="Decision 4",
        choices=[("A",  "A. $2.00 if Card is 1-4\n$1.60 if Card is 5-10"),
                 ("B",  "B. $3.85 if Card is 1-4\n$0.10 if Card is 5-10")])
    decision_5 = models.CharField(
        max_length=1, widget=widgets.RadioSelectHorizontal(), verbose_name="Decision 5",
        choices=[("A",  "A. $2.00 if Card is 1-5\n$1.60 if Card is 6-10"),
                 ("B",  "B. $3.85 if Card is 1-5\n$0.10 if Card is 6-10")])
    decision_6 = models.CharField(
        max_length=1, widget=widgets.RadioSelectHorizontal(), verbose_name="Decision 6",
        choices=[("A",  "A. $2.00 if Card is 1-6\n$1.60 if Card is 7-10"),
                 ("B",  "B. $3.85 if Card is 1-6\n$0.10 if Card is 7-10")])
    decision_7 = models.CharField(
        max_length=1, widget=widgets.RadioSelectHorizontal(), verbose_name="Decision 7",
        choices=[("A",  "A. $2.00 if Card is 1-7\n$1.60 if Card is 8-10"),
                 ("B",  "B. $3.85 if Card is 1-7\n$0.10 if Card is 8-10")])
    decision_8 = models.CharField(
        max_length=1, widget=widgets.RadioSelectHorizontal(), verbose_name="Decision 8",
        choices=[("A",  "A. $2.00 if Card is 1-8\n$1.60 if Card is 9-10"),
                 ("B",  "B. $3.85 if Card is 1-8\n$0.10 if Card is 9-10")])
    decision_9 = models.CharField(
        max_length=1, widget=widgets.RadioSelectHorizontal(), verbose_name="Decision 9",
        choices=[("A",  "A. $2.00 if Card is 1-9\n$1.60 if Card is 10"),
                 ("B",  "B. $3.85 if Card is 1-9\n$0.10 if Card is 10")])
    decision_10 = models.CharField(
        max_length=1, widget=widgets.RadioSelectHorizontal(), verbose_name="Decision 10",
        choices=[("A",  "A. $2.00 if Card is 1-10"),
                 ("B",  "B. $3.85 if Card is 1-10")])
