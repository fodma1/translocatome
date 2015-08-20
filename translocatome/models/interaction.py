from django.db import models

from .node import Node


class InteractionSubtype(models.Model):
    value = models.CharField(max_length=50)


class InteractionType(models.Model):
    value = models.CharField(max_length=50)
    subtype = models.ManyToManyField(InteractionSubtype)


BIOLOGICAL_PROCESS_VALUE_APOPTOSIS = 0
BIOLOGICAL_PROCESS_VALUE_CRI = 1
BIOLOGICAL_PROCESS_VALUE_DDR = 2
BIOLOGICAL_PROCESS_VALUE_HYPOXIA = 3
BIOLOGICAL_PROCESS_VALUE_MAPK = 4
BIOLOGICAL_PROCESS_VALUE_PLC = 5
BIOLOGICAL_PROCESS_VALUE_PROLIF = 6

BIOLOGICAL_PROCESS = (
    (BIOLOGICAL_PROCESS_VALUE_APOPTOSIS, 'apoptosis'),
    (BIOLOGICAL_PROCESS_VALUE_CRI, 'cri'),
    (BIOLOGICAL_PROCESS_VALUE_DDR, 'ddr'),
    (BIOLOGICAL_PROCESS_VALUE_HYPOXIA, 'hypoxia'),
    (BIOLOGICAL_PROCESS_VALUE_MAPK, 'mapk'),
    (BIOLOGICAL_PROCESS_VALUE_PLC, 'plc'),
    (BIOLOGICAL_PROCESS_VALUE_PROLIF, 'prolif'),
)


class BiologicalProcess(models.Model):
    value = models.SmallIntegerField(choices=BIOLOGICAL_PROCESS)


EDGE_TYPES_VALUES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
)

DIRECTNESS_DIRECT = 0
DIRECTNESS_INDIRECT = 1
DIRECTNESS_UNKNOWN = 2
DIRECTNESS_DIRECT_AND_INDIRECT = 3

DIRECTNESS_VALUES = (
    (DIRECTNESS_DIRECT, 'direct'),
    (DIRECTNESS_INDIRECT, 'indirect'),
    (DIRECTNESS_UNKNOWN, 'unknown'),
    (DIRECTNESS_DIRECT_AND_INDIRECT, 'direct_and_indirect')
)

EFFECT_POSITIVE = 0
EFFECT_NEUTRAL = 1
EFFECT_NEGATIVE = 2
EFFECT_BOTH = 3
EFFECT_UNKNOWN = 4
EFFECT_MINIMAL_POSITIVE = 5
EFFECT_MINIMAL_NEGATIVE = 6

EFFECT_VALUES = (
    (EFFECT_NEGATIVE, 'negative'),
    (EFFECT_NEUTRAL, 'neutral'),
    (EFFECT_POSITIVE, 'positive'),
    (EFFECT_BOTH, 'both'),
    (EFFECT_UNKNOWN, 'unknown'),
    (EFFECT_MINIMAL_POSITIVE, 'minimal_positive'),
    (EFFECT_MINIMAL_NEGATIVE, 'minimal_negative'),
)

SCORE_VALUE_ZERO = 0
SCORE_VALUE_ONE = 1
SCORE_VALUE_TWO = 2
SCORE_VALUE_UNKNOWN = 3
SCORE_VALUE_NA = 4


SCORE_VALUES = (
    (SCORE_VALUE_ZERO, 'zero'),
    (SCORE_VALUE_ONE, 'one'),
    (SCORE_VALUE_TWO, 'two'),
    (SCORE_VALUE_UNKNOWN, 'unknown'),
    (SCORE_VALUE_NA, 'not_applicable'),
)


class Interaction(models.Model):
    source_node = models.ForeignKey(Node, related_name='source')
    target_node = models.ForeignKey(Node, related_name='target')
    interaction_type = models.ManyToManyField(InteractionType)
    edge_type = models.PositiveSmallIntegerField(choices=EDGE_TYPES_VALUES)
    directness = models.PositiveSmallIntegerField(choices=DIRECTNESS_VALUES)
    effect_all = models.PositiveSmallIntegerField(choices=EFFECT_VALUES)
    effect_final = models.PositiveSmallIntegerField(choices=EFFECT_VALUES)
    biological_process = models.ManyToManyField(BiologicalProcess)
    score = models.SmallIntegerField(choices=SCORE_VALUES)

    # might not needed in the future
    int_abrev = models.CharField(max_length=13)
    # rename to total?
    is_in_full = models.BooleanField(default=False)
    is_in_medium = models.BooleanField(default=False)
    is_in_small = models.BooleanField(default=False)
    is_in_skeleton = models.BooleanField(default=False)
