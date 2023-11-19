*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Run Keywords
...    Go To Register Page



*** Test Cases ***
Register With Valid Username And Password
    Register User  kalle  kalle123  kalle123
    Submit Credentials
    Page Should Contain    Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Reset The Databse
    Register User  ka  kalle123  kalle123
    Submit Credentials
    Page Should Contain    Username needs to be at least 3 characters long

Register With Valid Username And Invalid Password
    Reset The Databse
    Register User  kalle  kalle  kalle
    Submit Credentials
    Page Should Contain    Password must contain at least one special character and be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Reset The Databse
    Register User  kalle  kalle123  wrong_one
    Submit Credentials
    Page Should Contain    Password Confirmation does not match the given password    

Login After Successful Registration
    Register User  kalle  kalle123  kalle123
    Submit Credentials
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Click Button    Login
    Page Should Contain    Ohtu Application main page

Login After Failed Registration
    Register User  kalle  kalle123  kalle
    Submit Credentials
    Go To Login Page
    Set Username  kalle
    Set Password  kalle321
    Click Button    Login
    Page Should Contain    Invalid username or password




*** Keywords ***
Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Register User
    [Arguments]  ${username}  ${password}  ${password_confirmation}
    Set Username    ${username}
    Set Password    ${password}
    Set Password Confirmation  ${password_confirmation}