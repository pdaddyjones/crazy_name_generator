Feature: Testing de la clase NameGenerator

    Scenario: Testing de la clase NameGenerator al ser llamada
        Given I call the NameGenerator class
        When I generate a name
        Then I should get a valid name back
