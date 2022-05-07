Feature: Authorisation

  Scenario: login into current account
    Given app is open and 'events' screen appears

    When open 'login' screen from 'burger menu'
    Then 'login' screen appears

    When input login id '424172117' and password 'iPbCs445' in auth fields
    And click on 'Log in' button
    Then 'events' screen appears

    When open 'my account' screen
    Then account with id '424172117' appears


  Scenario: logout from current account
    Given completed login into current account with login id '424172117' and password 'iPbCs445'

    When click on 'logout' option from burger menu
    Then 'Log out' alert appears

    When click on button 'YES' from alert
    Then 'events' screen appears

    When open 'my account' screen
    Then 'login' screen appears
