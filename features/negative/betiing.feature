Feature: Betting

  Scenario: Bet with zero balance
    Given account created with option 'in one click'

    When click on 'Log in' button
    Then 'events' screen appears

    When open 'single bet' screen
    Then 'single bet' screen appears

    When input 100 in 'stake amount' field
    And click on 'Bet' button
    Then 'Not enough funds' alert appears
