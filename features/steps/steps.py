from behave import *

@given(u'have number {number:d}')
def step_impl(context, number):
    context.firstNumber = number

@given(u'any first number is {number:d}')
def step_impl(context, number):

    context.firstNumber = number

@when(u'another number {number:d}')
def step_impl(context, number):
    context.secondNumber = number
    context.actualResult = context.firstNumber + context.secondNumber

@when(u'add {number:d}')
def step_impl(context, number):
    print("********before print****************")
    print(type(number))
    print("********after print****************")
    context.secondNumber = number
    context.actualResult = context.firstNumber + context.secondNumber

@then(u'result {result:d}')
def step_impl(context, result):
    assert (context.actualResult == result)



