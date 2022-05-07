from behave import Then, When, Given


@Given("account created with option '{registration_option}'")
def create_account_in_one_click(context, registration_option):
    context.app.events_page.check_page_visible()

    context.app.events_page.click_on_burger_button()
    context.app.events_page.click_on_registration_option()
    context.app.registration_type_page.click_on_option(registration_option)

    if registration_option == 'in one click':
        context.app.one_click_registration_page.check_page_visible()
        context.app.one_click_registration_page.click_on_checkbox_confirm_pp()
        context.app.one_click_registration_page.click_on_button_accept()
        context.app.one_click_registration_page.check_popup_registration_successful_visible()
        context.app.one_click_registration_page.click_on_button_next()

    context.app.login_page.check_page_visible()


@Given("completed login into current account with login id '{login_id}' and password '{password}'")
def completed_login_into_current_account(context, login_id, password):
    context.app.events_page.check_page_visible()

    context.app.events_page.click_on_burger_button()
    context.app.events_page.click_on_login_option()
    context.app.login_page.check_page_visible()

    context.app.login_page.input_login(login_id)
    context.app.login_page.input_password(password)
    context.app.login_page.click_on_button_login()
    context.app.events_page.check_page_visible()




