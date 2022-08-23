from behave import *

@given(u'have number 9')
def step_impl(context):
    context.firstNumber = 9


@when(u'take away 4')
def step_impl(context):
    context.secondNumber = 4
    context.actualResult = 9-4


@then(u'result is 5')
def step_impl(context):
    context.expected = 5
    assert (context.expected == context.actualResult)

