*** Settings ***
Library           ElasticLibrary

*** Tasks ***
Minimal task
    ${result}=    Elastic Authenticate
    Log To Console    result: ${result}
    ${document}=    Create Dictionary
    ...    character=Gandalt
    ...    quote=A wizard is never late, nor is he early.
    ${result}=    Elastic Index    name=lord-of-the-rings    document=${document}
    Log To Console    result: ${result}
    ${result}=    Elastic Refresh Index    lord-of-the-rings
    Log To Console    result: ${result}
    ${query}=    Create Dictionary    quote=early
    ${result}=    Elastic Search    lord-of-the-rings    ${query}
    Log To Console    result: ${result}
    Log    Done.
