from django.db import models

from authentication.models import Account

from interaction import Interaction


class Source(models.Model):
    value = models.CharField(max_length=32)


REFERENCE_TYPE_PUBMED = 0
REFERENCE_TYPE_BOOK = 1
REFERENCE_TYPE_MANUAL = 2

REFERENCE_TYPES = (
    (REFERENCE_TYPE_PUBMED, 'pubmed'),
    (REFERENCE_TYPE_BOOK, 'book'),
    (REFERENCE_TYPE_MANUAL, 'manual'),
)

class Reference(models.Model):
    reference_type = models.SmallIntegerField(choices=REFERENCE_TYPES)
    value = models.CharField(max_length=50)

DATA_SOURCE_VALUE_BASE_PPI = 0
DATE_SOURCE_VALUE_MANUAL_CURATION = 1
DATA_SOURCE_TYPE_SIGNALING_POOL = 2

DATA_SOURCE_VALUES = (
    (DATA_SOURCE_VALUE_BASE_PPI, 'base_ppi'),
    (DATE_SOURCE_VALUE_MANUAL_CURATION, 'manual_curation'),
    (DATA_SOURCE_TYPE_SIGNALING_POOL, 'signaling_pool'),
)


class DataSource(models.Model):
    value = models.SmallIntegerField(choices=DATA_SOURCE_VALUES)

ENTRY_STATE_INTEGRATED = 0
ENTRY_STATE_MANUALLY_REVIEWED = 1
ENTRY_STATE_DELETED = 2
ENTRY_STATE_REWIRED = 3

ENTRY_STATES = (
    (ENTRY_STATE_INTEGRATED, 'integrated'),
    (ENTRY_STATE_MANUALLY_REVIEWED, 'manually_rewired'),
    (ENTRY_STATE_DELETED, 'deleted'),
    (ENTRY_STATE_REWIRED, 'rewired'),
)


class Meta(models.Model):
    interaction = models.ForeignKey(Interaction)
    data_source = models.ManyToManyField(DataSource)
    sources = models.ManyToManyField(Source)
    references = models.ManyToManyField(Reference)
    comment = models.CharField(max_length=500)
    entry_state = models.SmallIntegerField(choices=ENTRY_STATES)
    curator_name = models.ForeignKey(Account)
    reviewed = models.BinaryField()
    curators_comment = models.CharField(max_length=500)

