RAW_EFFECT_VALUE_BOTH = '1 | -1'
RAW_EFFECT_VALUE_UNKNOWN = '?'
# Should delete this!
EFFECT_TO_VALUE = {
    '-1': 'negative',
    '-0.1': 'minimal_negative',
    '0': 'neutral',
    '0.1': 'minimal_positive',
    '1': 'positive',
    '1 | -1': 'both',
    '?': 'unknown',
    '-3': 'negative',
}

FIELD_NAME_TO_INDEX = [
    'Source_UniProtAC',
    'Source_GeneName',
    'InteractionType',
    'Edge_type',
    'Target_UniProtAC',
    'Target_GeneName',
    'Directness',
    'Effect_ALL',
    'Effect_FINAL',
    'Sources',
    'References',
    'Comment',
    'DataSource',
    'EntryType',
    'Biol_Process',
    'Score',
    'Curator_Name',
    'Reviewed',
    'Personal_Comment',
    'Int_Abrev',
    '#FULL',
    '#MEDIUM',
    '#SMALL',
    '#SIG',
]

DIRECTNESS_TRANSLATIONS = {
    'DIRECT': 0,
    'INDIRECT': 1,
    'UNKNOWN': 2,
    'INDIRECT | DIRECT': 3,
}

BIOLOGICAL_PROCESSES_VALUES = {
    'APOPTOSIS': 0,
    'CRI': 1,
    'DDR': 2,
    'HYPOXIA': 3,
    'MAPK': 4,
    'PLC': 5,
    'PROLIF': 6,
}
