*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  user  password!
    Output Should Contain  New user registered
Register With Already Taken Username And Valid Password
    Input Credentials  testuser  testpassword!
    Output Should Contain  User with username testuser already exists
Register With Too Short Username And Valid Password
    Input Credentials  abc  password!
    Output Should Contain  Username should be atleast 4 characters long
Register With Valid Username And Too Short Password
    Input Credentials  user  pass!
    Output Should Contain  Password should be atleast 8 characters long
Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  user  password
    Output Should Contain  Password should contain atleast one symbol

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  testuser  testpassword!
