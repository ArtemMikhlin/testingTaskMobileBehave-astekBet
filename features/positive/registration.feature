Feature: Registration

  Scenario: create account in one click
    Given app is open and 'events' screen appears

    When open 'registration' screen from 'burger menu'
    And choose 'in one click' registration option
    Then 'in one click' registration screen appears

    When confirm privacy policy
    And click on button accept
    Then 'registration successful' popup appears

    When click on button next
    Then 'login' screen appears

    When click on 'Log in' button
    Then 'events' screen appears

    When open 'my account' screen
    Then 'my account' screen appears
