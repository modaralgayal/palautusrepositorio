*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5001
${DELAY}  0.2 seconds
${HOME_URL}  http://${SERVER}
${LOGIN_URL}  http://${SERVER}/login
${REGISTER_URL}  http://${SERVER}/register
${RESET}  http://${SERVER}/tests/reset

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    # seuraava rivi on kommentoitu toistaiseksi pois
    #Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Login Page Should Be Open
    Title Should Be  Login

Main Page Should Be Open
    Title Should Be  Ohtu Application main page

Go To Login Page
    Go To  ${LOGIN_URL}

Go To Starting Page
    Go to  ${HOME_URL}

Go To Register Page
    Go to  ${REGISTER_URL}

Reset The Databse
    Reset Application

Register Page Should Be Open
    Go to  ${REGISTER_URL}