# File: voter_analytics/models.py
# Author: Victoria Mulugeta (vmulu@bu.edu), 10/31/2025
# Description: Defines the database models for the Voter application, including the Voter model.
from django.db import models

# Create your models here.

class Voter(models.Model):
    """
    model class for Voter object
    """

    # name
    last_name = models.TextField()
    first_name = models.TextField()
    # address
    street_number = models.IntegerField()
    street_name = models.TextField()
    apartment_number = models.IntegerField(null=True, blank=True)
    zip_code = models.IntegerField()
    # birth
    dob = models.DateField()
    # registration date
    dor = models.DateField()
    # party
    party_affiliation = models.CharField(max_length=2)
    # precinct num
    precinct_num = models.TextField()
    # whether or not a given voter participated in several recent elections:
    v20state = models.BooleanField()
    v21town = models.BooleanField()
    v21primary = models.BooleanField()
    v22general = models.BooleanField()
    v23town = models.BooleanField()
    # indicating how many of the past 5 elections the voter participated in.
    voter_score = models.IntegerField()

    def __str__(self):
        '''Return a string representation of this model instance.'''
        return f'{self.first_name} {self.last_name}'

def load_data():
    """
    process the CSV data file, and load Voters into your Django database
    """

    ## very dangerous line it cleans out the whole database
    #Voter.objects.all().delete()

    filename = '/Users/victoriamulugeta/Desktop/newton_voters.csv'
    f = open(filename)
    f.readline() # discard headers

    for line in f:
        fields = line.split(',')

        try:
            # create a new instance of Result object with this record from CSV
            result = Voter(
                            last_name=fields[1],
                            first_name=fields[2],

                            street_number = fields[3],
                            street_name = fields[4],
                            apartment_number = fields[5] if fields[5] else None,
                            zip_code = fields[6],

                            dob = fields[7],

                            dor = fields[8],

                            party_affiliation = fields[9],

                            precinct_num = fields[10],

                            v20state = fields[11] == 'TRUE',
                            v21town = fields[12] == 'TRUE',
                            v21primary = fields[13] == 'TRUE',
                            v22general = fields[14] == 'TRUE',
                            v23town = fields[15] == 'TRUE',

                            voter_score = fields[16],
                        )

            result.save() # commit to database
            print(f'Created result: {result}')

        except Exception as e:
            print(f"Skipped: {fields} due to error: {e}")

    print(f'Done. Created {len(Voter.objects.all())} Results.')