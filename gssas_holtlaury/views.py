from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class GSSAS(Page):
    pass


page_sequence = [
    GSSAS,
]
