Feature: Google Search

    Scenario: Search for a term on Google
        Given the user is on the Google homepage
        When the user searches for the "Selenium-BDD Tutorial"
        Then the results page should show results