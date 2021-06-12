
class EventSchema:
    def eventSchema(self):
        event_schema = {
            'event-id': {
                'type': 'Number',
                'minlength': 1,
                'required': True,
            },
            'event-type': {
                'type': 'String',
                'minlength': 1,
                'required': True,
            },
            'event-location': {
                'type': 'String',
                'minlength': 1,
                'required': True,
            },
            'event-description': {
                'type': 'String',
                'minlength': 1,
                'required': True,
            },
            'event-image': {
                'name': 'String',
                'desc': "String",
                'img':
                    {
                        'data': 'Buffer',
                        'contentType': 'String'
                    }
            },
        }
        return event_schema
