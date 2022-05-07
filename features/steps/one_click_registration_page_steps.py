from behave import Then, When, Given


@When("confirm privacy policy")
def confirm_privacy_policy(context):
    context.app.one_click_registration_page.click_on_checkbox_confirm_pp()


@When("click on button accept")
def click_on_button_accept(context):
    context.app.one_click_registration_page.click_on_button_accept()


@When("click on button next")
def click_on_button_next(context):
    context.app.one_click_registration_page.click_on_button_next()


@Then("'in one click' registration screen appears")
def in_one_click_registration_screen_appears(context):
    context.app.one_click_registration_page.check_page_visible()


@Then("'registration successful' popup appears")
def registration_successful_alert_appears(context):
    context.app.one_click_registration_page.check_popup_registration_successful_visible()
