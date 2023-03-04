from behave import *
from hamcrest import *
from features.pages.Packers_MoversPageClass import Packers_Movers_Class


@step("User enters invalid data Name {invalidname} and Your Mobile number {invalidnum}")
def step_impl(context, invalidname, invalidnum):

    context.name = Packers_Movers_Class(context.driver)
    context.name.enter_invalid_name(invalidname)

    context.number = Packers_Movers_Class(context.driver)
    context.number.enter_mobile_number(invalidnum)

@then("It shows error message")
def step_impl(context):
    context.error_msg = Packers_Movers_Class(context.driver)
    expectedError = "Numbers or Special characters not allowed."
    actualError = context.error_msg.display_error_message()
    print("THE ERROR MESSAGE IS  :", actualError)
    assert_that(expectedError, equal_to(actualError))


