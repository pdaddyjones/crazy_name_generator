from behave import *
from crazy_name_generator import NameGenerator
from crazy_name_generator.dataset import dataset

@given('I call the NameGenerator class')
def step_impl(context):
    context.name_generator = NameGenerator()

@when('I generate a name')
def step_impl(context):
    context.name = context.name_generator.name

@then('I should get a valid name back')
def step_impl(context):
    assert context.name.count('-') == 2
    assert len(context.name.split('-')) == 3

    for part in context.name.split('-'):
        assert part.isalnum()

    for part in context.name.split('-'):
        assert part in dataset['places'] or part in dataset['people_and_adjectives'] or part in dataset['animals']
        assert part in dataset['places'] or part in dataset['people_and_adjectives'] or part in dataset['animals']
        assert part in dataset['places'] or part in dataset['people_and_adjectives'] or part in dataset['animals']
