from behave import Then, When, Given


@When("click on 'Log in' button")
def click_on_login_button(context):
    context.app.login_page.click_on_button_login()


@When("input login id '{login_id}' and password '{password}' in auth fields")
def input_login_id_and_password_in_auth_fields(context, login_id, password):
    context.app.login_page.input_login(login_id)
    context.app.login_page.input_password(password)


@Then("'login' screen appears")
def login_screen_appears(context):
    context.app.login_page.check_page_visible()