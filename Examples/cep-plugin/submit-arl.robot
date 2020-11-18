*** Settings ***
Library    PuppeteerLibrary
Library    String
Test Setup    Connect CEP browser
Suite Teardown    Close Puppeteer

*** Variables ***
${CEP_DEBUGGER_URL}  http://localhost:7777/

*** Test Cases ***
Submit ARL
    Input Text    id=appLocation    /Users/chris/projects/sdvi/plover/dist
    Click Element    xpath=//input[@class='formbtn']
    Log to console   test done!!!!

*** Keywords ***
Get CEP web service endpoint
    ${HEADLESS} =    Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${CEP_DEBUGGER_URL}    browser=chrome    options=${options}
    ${fullUrl} =  Execute Javascript    document.querySelector('a').getAttribute('href');
    Close browser
    ${wsUrlFrag} =  Fetch from right  ${fullUrl}   ?ws=
    ${wsUrl} =  Format string  {}{}  ws://  ${wsUrlFrag}
    [return]  ${wsUrl}

Connect CEP browser
    ${wsUrl} =  Get CEP web service endpoint
    ${HEADLESS} =    Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Log to console  about to connect
    Connect browser    ${wsUrl}    options=${options}
    Log to Console  connected to ${wsUrl}
