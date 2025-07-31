# Created by sasha at 7/22/25
@smoke
Feature: Filter Out of Stock Products

  Scenario: User can filter by Out of Stock

Given Open the main page https://soft.reelly.io
When Log in to the page
And Click on “Off-plan” at the left side menu
Then Verify the right page opens
When Filter by sale status of “Out of Stock”
Then Verify each product contains the Out of Stock