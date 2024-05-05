# Created by rholt at 5/3/2024
Feature: Test scenarios for looping through colors on a product

  Scenario: Create a loop to go over product colors
   Given Open Target main page
    When Search for Levi's Mens Carson Synthetic Leather Casual
    And Click search icon
    And Click product
    Then Check product color
