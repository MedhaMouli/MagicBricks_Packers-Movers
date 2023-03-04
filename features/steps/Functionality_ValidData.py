
from behave import *
from hamcrest import *
from features.pages.Packers_MoversPageClass import Packers_Movers_Class

@step("User enters Name {validname} and Your Mobile number {validnum}")
def step_impl(context, validname, validnum):

    context.name = Packers_Movers_Class(context.driver)
    context.name.enter_name(validname)

    context.number = Packers_Movers_Class(context.driver)
    context.number.enter_mobile_number(validnum)

@step("User clicks on relocating from field")
def step_impl(context):

    context.relocate = Packers_Movers_Class(context.driver)
    context.relocate.click_relocation_from()

@step("User selects location from the drop-down list")
def step_impl(context):

    context.relocate_cn = Packers_Movers_Class(context.driver)
    context.relocate_cn.click_relocate_city_from()

@step("User clicks on request a call back link")
def step_impl(context):

    context.get_quotes = Packers_Movers_Class(context.driver)
    context.get_quotes.click_Request_CallBack()

@then("it displays a popup Enter your Details")
def step_impl(context):

    context.texts = Packers_Movers_Class(context.driver)
    expectedTitle = True
    actualTitle = context.texts.display_text()
    print("The value is", actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

