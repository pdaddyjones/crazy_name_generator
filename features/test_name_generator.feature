Feature: Testing de la clase NameGenerator

    Scenario Outline: Testing de la clase NameGenerator al ser llamada
        Given I call the NameGenerator class
        When I receive a name
        Then I should get a valid name back

