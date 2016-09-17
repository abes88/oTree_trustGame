from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class BigFive(Page):
    pass

     form_model = models.Player
    form_fields = [
        "is_talkative",  "has_an_active_imagination",
        "tends_to_find_fault_with_others",  "tends_to_be_quiet",
        "does_a_thorough_job", "is_generally_trusting",
        "is_depressed,_blue", "tends_to_be_lazy",
        "is_original,_comes_up_with_new_ideas",
        "is_emotionally_stable,_not_easily_upset",
        "is_reserved", "is_inventive",
        "is_helpful_and_unselfish_with_others",
        "has_an_assertive_personality",
        "can_be_somewhat_careless",
        "can_be_cold_and_aloof",
        "is_relaxed,_handles_stress_well.",
        "perseveres_until_the_task_is_finished",
        "is_curious_about_many_different_things",
        "can_be_moody",
        "is_full_of_energy",
        "values_artistic,_aesthetic_experiences",
        "starts_quarrels_with_others",
        "is_sometimes_shy,_inhibited",
        "is_a_reliable_worker",
        "is_considerate_and_kind_to_almost",
        "can_be_tense_everyone",
        "is_ingenious,_a_deep_thinker",
        "does_things_efficiently",
        "generates_a_lot_of_enthusiasm",
        "remains_calm_in_tense_situations",
        "has_a_forgiving_nature",
        "prefers_work_that_is_routine",
        "tends_to_be_disorganized",
        "is_outgoing,_sociable",
        "worries_a_lot",
        "is_sometimes_rude_to_others",
        "makes_plans_and_follows_through_with_them",
        "gets_nervous_easily",
        "likes_to_reflect,_play_with_ideas",
        "has_few_artistic_interests",
        "likes_to_cooperate_with_others",
        "is_easily_distracted",
        "is_sophisticated_in_art,_music,_or_literature",
    ]



page_sequence = [
    BigFive
]
