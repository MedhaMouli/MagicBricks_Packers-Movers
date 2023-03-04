from behave import *
from features.pages.Packers_MoversPageClass import Packers_Movers_Class
from features.utility.ConfigClass import ConfigClass
from datafiles import ExcelUtils

@when("user clicks on between cities tab")
def step_impl(context):

    context.cities = Packers_Movers_Class(context.driver)
    context.cities.select_bwt_cities()

@step("User enters name {uname} and number {number}")
def step_impl(context, uname, number):

    ExcelUtils.get_row_count(ConfigClass.excelPath, "Sheet1")
    uname = ExcelUtils.read_data(ConfigClass.excelPath, "Sheet1", 2, 1)

    ExcelUtils.get_row_count(ConfigClass.excelPath, "Sheet1")
    number = ExcelUtils.read_data(ConfigClass.excelPath, "Sheet1", 2, 2)

    username = Packers_Movers_Class(context.driver)
    username.enter_Name(uname)

    mob_no = Packers_Movers_Class(context.driver)
    mob_no.enter_Mobile_number(number)

@step("User clicks on relocating to field")
def step_impl(context):

    context.relocate = Packers_Movers_Class(context.driver)
    context.relocate.click_relocation_to()

@step("User selects location to below the drop-down list")
def step_impl(context):

    context.relocate_cn = Packers_Movers_Class(context.driver)
    context.relocate_cn.click_relocate_city_to()

# scenario 2

@step("User enter name {u_name} and number {m_number}")
def step_impl(context, u_name, m_number):

    ExcelUtils.get_row_count(ConfigClass.excelPath, "Sheet1")
    u_name = ExcelUtils.read_data(ConfigClass.excelPath, "Sheet1", 3, 1)

    ExcelUtils.get_row_count(ConfigClass.excelPath, "Sheet1")
    m_number = ExcelUtils.read_data(ConfigClass.excelPath, "Sheet1", 3, 2)

    username = Packers_Movers_Class(context.driver)
    username.enter_name(u_name)

    mob_no = Packers_Movers_Class(context.driver)
    mob_no.enter_mobile_number(m_number)




