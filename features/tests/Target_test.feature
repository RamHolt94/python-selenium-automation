# Created by rholt at 4/4/2024
Feature: Check target cart
  Verify sign in text
  # Enter feature description here

  Scenario: User can verify sign in page
  # Enter scenario name here
    Given Open Target main page
    When Find sign in
    Then Click sign in on nav side bar
    # Enter steps here

  Scenario:User can verify that cart is empty
    Given Open Target main page
    When Click on the cart icon
    Then Verify the cart is empty