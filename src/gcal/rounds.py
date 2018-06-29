

def get_text(fname):
    with open(fname) as f:
        text = f.read()
    return text


romans = ['I', 'II', 'III', 'FINAL']
rounds = [
    {
        summary: 'Part {} of Demo Training'.format(romans[i]),
        description: get_text('{}.txt'.format(i+1))
    } for i in range(4)
]

a = {
    'start': {
        'dateTime': '2015-05-28T09:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
    },
    'end': {
        'dateTime': '2015-05-28T17:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
    },
    'attendees': [
        {'email': 'lpage@example.com'},
        {'email': 'sbrin@example.com'},
    ],
}
