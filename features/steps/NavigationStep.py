
from hamcrest import *
from behave import *
from features.pages.NavigationClass import Packers_Movers


@given("chrome is opened and MagicBricks website is opened")
def step_impl(context):

    expectedTitle = "Real Estate | Property in India | Buy/Sale/Rent Properties | MagicBricks"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

@when("User clicks on 20% off on home shifting Button")
def step_impl(context):

    packers_Movers = Packers_Movers(context.driver)
    packers_Movers.click_packers_movers_button()
    context.driver.implicitly_wait(10)

@then("It shows packers and movers webpage")
def step_impl(context):

    expectedTitle = "Packers and Movers Services: Books Packers & Movers Near Your City"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))



