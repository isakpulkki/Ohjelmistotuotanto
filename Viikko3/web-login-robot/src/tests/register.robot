*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set username  user
    Set Password  password123
    Set Password Confirmation  password123
    Click Button  Register
    Title Should Be  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set username  usr
    Set Password  password123
    Set Password Confirmation  password123
    Click Button  Register
    Page Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Set username  user
    Set Password  pass1
    Set Password Confirmation  pass1
    Click Button  Register
    Page Should Contain  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set username  user
    Set Password  password123
    Set Password Confirmation  password321
    Click Button  Register
    Page Should Contain  Passwords were not the same

Login After Successful Registration
    Set Username  testuser
    Set Password  password123
    Set Password Confirmation  password123
    Click Button  Register
    Title Should Be  Welcome to Ohtu Application!
    Go to Login Page
    Login Page Should Be Open
    Set Username  user
    Set Password  password123
    Submit Credentials
    Main Page Should Be Open

Login After Failed Registration
    Set Username  tst
    Set Password  password123
    Set Password Confirmation  password123
    Click Button  Register
    Page Should Contain  Username is too short
    Go to Login Page
    Login Page Should Be Open
    Set Username  usr
    Set Password  password123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login
