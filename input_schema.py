INPUT_SCHEMA = {
    "text_input": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["There is a fine house in the forest"]
    },
    "min_length": {
        'datatype': 'INT16',
        'required': False,
        'shape': [1],
        'example': [256]
    },
    "max_new_tokens": {
        'datatype': 'INT16',
        'required': False,
        'shape': [1],
        'example': [256]
    }
}
