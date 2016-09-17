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
        max_length=100, choices=('Would take advantage of you', 'Would try to be fair'), widget=widgets.RadioSelect(),
        verbose_name="Do you think most people would try to take advantage of you if they got a chance, or would they try to be fair?")

    most_of_the_time_people_try_to_be_helpful = models.CharField(
        max_length=100, choices=('Try to be helpful', 'Just look out for themselves'), widget=widgets.RadioSelect(),
        verbose_name="Would you say that most of the time people try to be helpful, or that they are mostly just looking out for themselves?")

    that_most_people_can_be_trusted = models.CharField(
        max_length=100, choices=('Most people can be trusted', "Can't be too careful"), widget=widgets.RadioSelect(),
        verbose_name="Generally speaking, would you say that most people can be trusted or that you can't be too careful in dealing with people?")
