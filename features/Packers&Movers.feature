Feature: Packers and Movers


  Background:
     Given chrome is opened and MagicBricks website is opened
     When User clicks on 20% off on home shifting Button


  Scenario: Verify user navigates to packers and movers page
    Then It shows packers and movers webpage


  Scenario Outline: verify Within the city functionality with valid data
    And User enters Name <validname> and Your Mobile number <validnum>
    And User clicks on relocating from field
    And User selects location from the drop-down list
    And User clicks on request a call back link
    Then It displays a popup Enter your Details

  Examples:
    | validname   || validnum    |
    | Chris       || 9848812689  |
    | Evans       || 7893462789  |


  Scenario Outline: verify within the city functionality with invalid data
    And  User enters invalid data Name <invalidname> and Your Mobile number <invalidnum>
    Then It shows error message

    Examples:
      | invalidname  | | invalidnum  |
      | ***          | | Tom         |
      | $$$          | | Holland     |
