from maltego_trx.transform import DiscoverableTransform
from maltego_trx.entities import Alias, Person, Email, PhoneNumber, URL, Location, Phrase 
from extensions import registry, TransformSet
from data_retrevial import from_email



@registry.register_transform(display_name="fromEmail [PD]", 
                             input_entity=Email, 
                             description="Retreive leaked data from an email", 
                             output_entities=[Alias, Person, PhoneNumber, URL, Location, Phrase],
                             transform_set=TransformSet)
class fromEmail(DiscoverableTransform):

    @classmethod
    def create_entities(cls, request, response):
        req_value = request.Value

        # get data list
        data = from_email(req_value)

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

        # phone numbers
        for phone in data['phones']: 
            ent = response.addEntity(PhoneNumber, phone[0])
            ent.setLinkLabel('PD')
            ent.setLinkThickness(1)
            ent.addCustomLinkProperty('source', 'Source', phone[1])

        # urls
        for url in data['sm_urls']:
            sm_url = url[0]
            try:
                platform = sm_url.split('/')[2]
            except:
                platform = 'unknown'

            ent = response.addEntity(URL, platform)
            ent.addProperty('url', 'URL', 'loose', sm_url)
            ent.setLinkLabel('PD')
            ent.setLinkThickness(1)
            ent.addCustomLinkProperty('source', 'Source', url[1])

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


