import content
"""
Ein Dictionary, das die einzelnen Abschnitte des Kapitels enthält.
Jeder Abschnitt enthält:
- content: den Text des Abschnitts
- options: die möglichen nächsten Abschnitte
- text_options: die Textoptionen für den Benutzer
"""
chapter = {
    'abs1': {
        'content': content.abs1,
        'options': {
            '1': 'abs72',
            '2': 'abs76'
        },
        'text_options': {
            '1': 'Versuche zu fliehen',
            '2': 'Untersuche deine Umgebung'
        }
    },
    'abs72': {
        'content': content.abs72,
        'options': {
            '1': 'abs55',
            '2': 'abs92'
        },
        'text_options': {
            '1': 'Fliehe durch den Gang',
            '2': 'Kehre um'
        }
    },
    'abs76': {
        'content': content.abs76,
        'options': {
            '1': 'abs35',
            '2': 'abs40'
        },
        'text_options': {
            '1': 'Fliehe durch die Tür',
            '2': 'Verstecke dich'
        }
    },
    'abs55': {
        'content': content.abs55,
        'options': {
            '1': 'abs71',
            '2': 'abs90'
        },
        'text_options': {
            '1': 'Fliehe durch das Fenster',
            '2': 'Klettere auf den Baum'
        }
    },
    'abs92': {
        'content': content.abs92,
        'options': {
            '1': 'abs65',
            '2': 'abs11'
        },
        'text_options': {
            '1': 'Fliehe durch den Hof',
            '2': 'Untersuche den Tempel',
        }
    },
    'abs35': {
        'content': content.abs35,
        'options': {
            '1': 'abs60',
            '2': 'abs16'
        },
        'text_options': {
            '1': 'Fliehe durch den Tempel',
            '2': 'Verstecke dich'
        }
    },
    'abs40': {
        'content': content.abs40,
        'options': {
            '1': 'abs89',
            '2': 'abs58'
        },
        'text_options': {
            '1': 'Verstecke dich',
            '2': 'Fliehe durch den Tempel'
        }
    },
    'abs71': {
        'content': content.abs71,
        'options': {
            '1': 'abs33',
            '2': 'abs13'
        },
        'text_options': {
            '1': 'Untersuche die Verletzung',
            '2': 'Fliehe in den Wald'
        }
    },
    'abs90': {
        'content': content.abs90,
        'options': {
            '1': 'abs38',
            '2': 'abs100'
        },
        'text_options': {
            '1': 'Untersuche das Brandmal',
            '2': 'Verstecke dich'
        }
    },
    'abs65': {
        'content': content.abs65,
        'options': {
            '1': 'abs11',
            '2': 'abs60'
        },
        'text_options': {
            '1': 'Fliehe durch den Tempel',
            '2': 'Untersuche den Tempel'
        }
    },
    'abs11': {
        'content': content.abs11,
        'options': {
            '1': 'abs16',
            '2': 'abs89'
        },
        'text_options': {
            '1': 'Fliehe zum Tempel',
            '2': 'Verstecke dich hinter der Statue'
        }
    },
    'abs60': {
        'content': content.abs60,
        'options': {
            '1': 'abs38',
            '2': 'abs100'
        },
        'text_options': {
            '1': 'Betrete den Tempel',
            '2': 'Verstecke dich'
        }
    },
    'abs16': {
        'content': content.abs16,
        'options': {
            '1': 'abs89',
            '2': 'abs58'
        },
        'text_options':{
            '1': 'Verstecke dich',
            '2': 'Untersuche den Hebel'
        }
    },
    'abs89': {
        'content': content.abs89,
        'options': {
            '1': 'abs58',
            '2': 'abs33'
        },
        'text_options': {
            '1': 'Untersuche die Orgel',
            '2': 'Untersuche die Statue'
        }
    },
    'abs58': {
        'content': content.abs58,
        'options': {
            '1': 'abs38',
            '2': 'abs100'
        },
        'text_options': {
            '1': 'Untersuche die Orgel',
            '2': 'Untersuche die Statue'
        }
    },
    'abs33': {
        'content': content.abs33,
        'options': {
            '1': 'abs13',
            '2': 'abs1'
        },
        'text_options': {
            '1': 'Untersuche den Bolzen',
            '2': 'Fliehe zurück'
        }
    },
    'abs13': {
        'content': content.abs13,
        'options': {
            '1': 'abs38',
            '2': 'abs100'
        },
        'text_options': {
            '1': 'Untersuche die Särge',
            '2': 'Öffne die Truhe'
        }
    },
    'abs38': {
        'content': content.abs38,
        'options': {
            '1': 'abs100',
            '2': 'abs1'
        },
        'text_options': {
            '1': 'Stelle dich dem Feind',
            '2': 'Suche nach Verbündeten'
        }

    },
    'abs100': {
        'content': content.abs100,
        'options': {
            '1': 'abs1',
            '2': 'abs72'
        },
        'text_options': {
            '1': 'Reflektiere über deine Entscheidungen',
            '2': 'Plane deine nächste Reise'
        }
    }
}