# Created by rholt at 4/4/2024
Feature: Check target cart
  Verify sign in text


  Scenario: User can verify sign in page
    Given Open Target main page
    When Find sign in
    Then Click sign in on nav side bar


  Scenario:User can verify that cart is empty
    Given Open Target main page
    When Click on the cart icon
    Then Verify the cart is empty


  Scenario: User can find all benefit cells.
    Given Open Target Circle page
    When Count the benefit cells


  Scenario: User can add product to cart and verify the the total price.
    Given Open Target main page
    When Click search bar
    And Search for UNbrush
    And Click search icon
    Then Add product to cart
    And Click second button to add
    And Click view cart and check out
    Then Find the $25.43


