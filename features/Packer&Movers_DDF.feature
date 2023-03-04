Feature: Packers and Movers

  Background:
     Given chrome is opened and MagicBricks website is opened
     When User clicks on 20% off on home shifting Button
     When user clicks on between cities tab


  Scenario: verify Between the city functionality
    And User enters name <uname> and number <number>
    And User clicks on relocating from field
    And User selects location from the drop-down list
    And User clicks on relocating to field
    And User selects location to below the drop-down list
    And User clicks on request a call back link
    Then It displays a popup Enter your Details


  Scenario: verify Between the city functionality
    And User enter name <name> and number <m_number>
    And User clicks on relocating from field
    And User selects location from the drop-down list
    And User clicks on relocating to field
    And User selects location to below the drop-down list
    And User clicks on request a call back link
    Then It displays a popup Enter your Details



