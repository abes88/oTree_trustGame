from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, safe_json
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'big_five'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    is_talkative = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Is talkative")
    has_an_active_imagination = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Has an active imagination")
    tends_to_find_fault_with_others = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Tends to find fault with others")
    tends_to_be_quiet = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Tends to be quiet")
    does_a_thorough_job = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Does a thorough job")
    is_generally_trusting = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Is generally trusting")
    is_depressed_blue = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Is depressed, blue")
    tends_to_be_lazy = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Tends to be lazy")
    is_original_comes_up_with_new_ideas = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Is original, comes up with new ideas")
    is_emotionally_stable_not_easily_upset = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Is emotionally stable, not easily upset")
    is_reserved = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Is reserved")
    is_inventive = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Is inventive")
    is_helpful_and_unselfish_with_others = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Is helpful and unselfish with others")
    has_an_assertive_personality = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Has an assertive personality")
    can_be_somewhat_careless = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Can be somewhat careless")
    can_be_cold_and_aloof = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Can be cold and aloof")
    is_relaxed_handles_stress_well = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Is relaxed, handles stress well")
    perseveres_until_the_task_is_finished = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Perseveres until the task is finished")
    is_curious_about_many_different_things = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Is curious about many different things")
    can_be_moody = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Can be moody")
    is_full_of_energy = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Is full of energy")
    values_artistic_aesthetic_experiences = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Values artistic, aesthetic experiences")
    starts_quarrels_with_others = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Starts quarrels with others")
    is_sometimes_shy_inhibited = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Is sometimes shy, inhibited")
    is_a_reliable_worker = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Is a reliable worker")
    is_considerate_and_kind_to_almost = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Is considerate and kind to almost")
    can_be_tense_everyone = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Can be tense everyone")
    is_ingenious_a_deep_thinker = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Is ingenious, a deep thinker")
    does_things_efficiently = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Does things efficiently")
    generates_a_lot_of_enthusiasm = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Generates a lot of enthusiasm")
    remains_calm_in_tense_situations = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Remains calm in tense situations")
    has_a_forgiving_nature = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Has a forgiving nature")
    prefers_work_that_is_routine = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Prefers work that is routine")
    tends_to_be_disorganized = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Tends to be disorganized")
    is_outgoing_sociable = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Is outgoing, sociable")
    worries_a_lot = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Worries a lot")
    is_sometimes_rude_to_others = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Is sometimes rude to others")
    makes_plans_and_follows_through_with_them = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Makes plans and follows through with them")
    gets_nervous_easily = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Gets nervous easily")
    likes_to_reflect_play_with_ideas = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Likes to reflect, play with ideas")
    has_few_artistic_interests = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Has few artistic interests")
    likes_to_cooperate_with_others = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Likes to cooperate with others")
    is_easily_distracted = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Is easily distracted")
    is_sophisticated_in_art_music_or_literature = models.PositiveIntegerField(
        choices= (1, 2, 3, 4, 5),
        verbose_name="Is sophisticated in art, music, or literature")
