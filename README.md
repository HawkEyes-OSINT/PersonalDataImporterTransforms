# PersonalDataImporterTransforms
Maltego transform set to retreive data from a database created by PersonalDataImporter
https://github.com/HawkEyes-OSINT/PersonalDataImporter

## Installation
Open a command line in the directory you want to contain the repository.
Run the following commands:

    git clone https://github.com/HawkEyes-OSINT/PersonalDataImporterTransforms.git
    pip install -r requirements.txt

To provide the location of your database run:

    python setup.py

Now, to create a configuration file for your Maltego client, run:

    python project.py run

Open your Maltego client and click on the Import/Export tab.
Click on the 'Import Config' button and select: PersonalData.mtz

You should now have the PersonalDataImporterTransforms set available in your Maltego client.

## Transform Overview

fromEmail

    input_entity=Email, 
    description="Retreive leaked data from an email", 
    output_entities=[Alias, Person, PhoneNumber, URL, Location, Phrase]

fromName

    input_entity=Person, 
    description="Retreive leaked data from a person's name", 
    output_entities=[Alias, Email, PhoneNumber, URL, Location, Phrase]

fromPassword

    input_entity=Phrase, 
    description="Retreive leaked data from a password", 
    output_entities=[URL, Person, Email, PhoneNumber, Location, Alias]

fromPhone

    input_entity=PhoneNumber, 
    description="Retreive leaked data from an phone number", 
    output_entities=[Alias, Person, Email, URL, Location, Phrase]

fromURL

    input_entity=URL, 
    description="Retreive leaked data from a URL", 
    output_entities=[Alias, Person, Email, PhoneNumber, Location, Phrase]

fromUsername

    input_entity=Alias, 
    description="Retreive leaked data from a username", 
    output_entities=[URL, Person, Email, PhoneNumber, Location, Phrase]