from behave import Then, When, Given


@When("choose '{registration_option}' registration option")
def choose_registration_option(context, registration_option):
    context.app.registration_type_page.click_on_option(registration_option)

