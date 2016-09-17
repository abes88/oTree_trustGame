from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class BigFive(Page):

    form_model = models.Player
    form_fields = [
        'is_talkative',
        'tends_to_find_fault_with_others',
        'does_a_thorough_job',
        'is_depressed_blue',
        'is_original_comes_up_with_new_ideas',
        'is_reserved',
        'is_helpful_and_unselfish_with_others',
        'can_be_somewhat_careless',
        'is_relaxed_handles_stress_well',
        'is_curious_about_many_different_things',
        'is_full_of_energy',
        'starts_quarrels_with_others',
        'is_a_reliable_worker',
        'can_be_tense',
        'is_ingenious_a_deep_thinker',
        'generates_a_lot_of_enthusiasm',
        'has_a_forgiving_nature',
        'tends_to_be_disorganized',
        'worries_a_lot',
        'has_an_active_imagination',
        'tends_to_be_quiet',
        'is_generally_trusting',

        'tends_to_be_lazy',
        'is_emotionally_stable_not_easily_upset',
        'is_inventive',
        'has_an_assertive_personality',
        'can_be_cold_and_aloof',
        'perseveres_until_the_task_is_finished',
        'can_be_moody',
        'values_artistic_aesthetic_experiences',
        'is_sometimes_shy_inhibited',
        'is_considerate_and_kind_to_almost_everyone',
        'does_things_efficiently',
        'remains_calm_in_tense_situations',
        'prefers_work_that_is_routine',
        'is_outgoing_sociable',
        'is_sometimes_rude_to_others',
        'makes_plans_and_follows_through_with_them',
        'gets_nervous_easily',
        'likes_to_reflect_play_with_ideas',
        'has_few_artistic_interests',
        'likes_to_cooperate_with_others',
        'is_easily_distracted',
        'is_sophisticated_in_art_music_or_literature'
    ]

    def vars_for_template(self):
        return {"agree_levels": sorted(Constants.agree_level_desc.items())}



page_sequence = [
    BigFive
]
