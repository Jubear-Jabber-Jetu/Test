Feature: Search and Access a Toy Item on WallTouchBD

  Scenario: Login and search for a toy
    Given I navigate to the WallTouchBD login page
    When I enter valid credentials
    And I click the login button
    Then I should be logged in successfully
    When I search for "toys"
    Then I should see search results
    When I access the first item in the search results
    Then I should be on the item's detail page
