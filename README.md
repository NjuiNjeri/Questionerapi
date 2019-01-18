
[![Build Status](https://travis-ci.com/NjuiNjeri/Questionerapi.svg?branch=Develop)](https://travis-ci.com/NjuiNjeri/Questionerapi)
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage)](https://codeclimate.com/github/codeclimate/codeclimate/test_coverage)

[![Coverage Status](https://coveralls.io/repos/github/NjuiNjeri/Questionerapi/badge.svg)](https://coveralls.io/github/NjuiNjeri/Questionerapi)

# Endpoints

GET/api/v1/questions  

POST/api/v1/questions

GET/api/v1/meetups

POST/api/v1/meetups

GET/api/v1/allquestions

# Questionerapi

## usage

all responses will have the form

'''json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
'''

Subsequent response definitions will show the expected value of the 'data field'

### list of all meetups

***Definitions***

'GET/meetups'

***Response***

- '200 ok' on success

'''json'''
[
    {
        "Identifier": "Meetup",

    }
]
'''

### Creating a new meetup

***Definition***

'POST/MEETUP'

***Arguments***

'"Identifier:string' a category for the meetup
'"name:string' a title or name for the meetup
'"date & time:integer' a set date and time for the meetup
'"name:string' location for the meetup
'"gateway:string' IP address

If a meetup alreaady exists, the existing one will be overwritten

***Responses***

'201 created' on success

'''json
[
    {
        "Identifier": "Meetup",

    }
]
'''

### Lookup meetup details

'GET/meetup/[identifier]'

***Responses***

'404 not found' if the meetup does not exist
'200 ok' on success

'''json
[
    {
        "Identifier": "Meetup",

    }
]
'''

## Delete a meetup

'DELETE/meetup/[identifier]

***Responses***

'404 not found' if the meetup does not exist
'204 no content'succesful action, but no data to be returned

The Available endpoints include

Api/v1/questions
