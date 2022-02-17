import pytest

from introduction_fixtextures import Address, Gender, Person

@pytest.fixture
def address():
    return Address(street_address='Example Street 12',
                   postal_code='123456',
                   city='Exmple city',
                   country='EX')
    
    
@pytest.fixture
def person(address):
    return Person(first_name='John',
                  last_name='Doe',
                  gender=Gender.NON_BINARY,
                  birthdate='1991-01-01',
                  interests=['sports','cooking'],
                  address=address)  


def test_address_country(address):
    assert address.country == 'EX'


def test_person_interests(person):
    assert person.interests == ['sports','cooking']


def test_person_address(person):
    assert person.address.country == 'EX'


def test_person_address_street_address(person):
    assert person.address.street_address == 'Example Street 12'
 
    
def test_person_address_postal_code(person):
    assert person.address.postal_code == '123456'
    

def test_person_address_city(person):
    assert person.address.city == 'Exmple city'
 
    



                          