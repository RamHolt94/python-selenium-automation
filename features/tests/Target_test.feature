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