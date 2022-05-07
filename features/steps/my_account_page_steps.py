from behave import Then, When, Given


@Then("'my account' screen appears")
def my_account_screen_appears(context):
    context.app.my_account_page.check_page_visible()


@Then("account with id '{account_id}' appears")
def my_account_screen_appears(context, account_id):
    context.app.my_account_page.check_account_id(account_id)
