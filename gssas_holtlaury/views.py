from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class GSSAS(Page):

    form_model = models.Player
    form_fields = [
        "people_try_to_take_advantage_of_you_if_they_got_a_chance",
        "most_of_the_time_people_try_to_be_helpful",
        "that_most_people_can_be_trusted"
    ]

class HoltLaury(Page):

    form_model = models.Player
    form_fields = [
        'decision_1',
        'decision_2',
        'decision_3',
        'decision_4',
        'decision_5',
        'decision_6',
        'decision_7',
        'decision_8',
        'decision_9',
        'decision_10'
    ]


page_sequence = [
    GSSAS,
    HoltLaury
]
