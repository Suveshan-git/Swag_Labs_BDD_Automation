Feature: Home Page
  Scenario: View Home Page Main Menu
    Given I have my browser open
    When I enter the PHP URL and press enter
    Then I should land on the PHP Home Page
    And on the menu, I should see the Demo tab
    And I should see the Pricing tab
    And I should see the Features tab
    And I should see the Product tab
    And I should see the Integrations tab
    And I should see the Docs tab
    And I should see the Blog tab
    And I should see the Company tab
    And I should see the Login button