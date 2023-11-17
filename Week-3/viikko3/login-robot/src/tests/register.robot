*** Settings ***
Resource  resource.robot
Test Setup  Input Register Command


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered
    Input Register Command
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username needs to be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  ka23232  kalle123
    Output Should Contain  Username should consist of lowercase letters only

Register With Valid Username And Too Short Password
    Input Credentials  kalle  k
    Output Should Contain  Password must contain at least one special character and be at least 8 characters long


Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kalajoki
    Output Should Contain  Password must contain at least one special character and be at least 8 characters long

*** Keywords ***
Create New User
    Input Register Command