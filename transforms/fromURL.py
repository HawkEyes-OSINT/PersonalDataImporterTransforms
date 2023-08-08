from maltego_trx.transform import DiscoverableTransform
from maltego_trx.entities import Alias, Person, Email, PhoneNumber, URL, Location, Phrase 
from extensions import registry, TransformSet
from data_retrevial import from_url



@registry.register_transform(display_name="fromURL [PD]", 
                             input_entity=URL, 
                             description="Retreive leaked data from a URL", 
                             output_entities=[Alias, Person, Email, PhoneNumber, Location, Phrase],
                             transform_set=TransformSet)
class fromURL(DiscoverableTransform):

    @classmethod
    def create_entities(cls, request, response):
        req_value = request.Value

        # get data list
        data = from_url(req_value)

        """ create entities """
        # names
        for name in data['names']:
            ent = response.addEntity(Person, name[0])
            ent.setLinkLabel('PD')
            ent.setLinkThickness(1)

        # passwords
        for pwd in data['passwords']:
            ent = response.addEntity(Phrase, pwd[0])
            ent.setLinkLabel('PD')
            ent.setLinkThickness(1)
            ent.addCustomLinkProperty('source', 'Source', pwd[1])

        # emails
        for email in data['emails']:
            ent = response.addEntity(Email, email[0])
            ent.setLinkLabel('PD')
            ent.setLinkThickness(1)
            ent.addCustomLinkProperty('source', 'Source', email[1])

        # phone numbers
        for phone in data['phones']: 
            ent = response.addEntity(PhoneNumber, phone[0])
            ent.setLinkLabel('PD')
            ent.setLinkThickness(1)
            ent.addCustomLinkProperty('source', 'Source', phone[1])

        # usernames
        for username in data['usernames']:
            ent = response.addEntity(Alias, username[0])
            ent.setLinkLabel('PD')
            ent.setLinkThickness(1)
            ent.addCustomLinkProperty('source', 'Source', username[1])

        # locations
        for location in data['addresses']:
            ent = response.addEntity(Location, location[0])
            ent.setLinkLabel('PD')
            ent.setLinkThickness(1)
            ent.addCustomLinkProperty('source', 'Source', location[1])  


