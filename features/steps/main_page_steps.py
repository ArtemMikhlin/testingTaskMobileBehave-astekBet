from behave import Then, When, Given


@When("complete logout from current account")
def logout_from_current_account(context):
    context.app.events_page.click_on_burger_button()
    context.app.events_page.click_on_logout_option()
    context.app.events_page.check_title_from_alert_logout()

    context.app.events_page.click_on_button_yes_from_alert()
    context.app.events_page.check_page_visible()


@When("open 'single bet' screen")
def open_single_bet_screen(context):
    context.app.events_page.click_on_field_betting_odds()
    context.app.events_page.check_bottomsheet_betting_odds_visible()
    context.app.events_page.click_on_place_bet_option()


@When("open 'registration' screen from 'burger menu'")
def open_registration_screen(context):
    context.app.events_page.click_on_burger_button()
    context.app.events_page.click_on_registration_option()


@When("open 'login' screen from 'burger menu'")
def open_login_screen(context):
    context.app.events_page.click_on_burger_button()
    context.app.events_page.click_on_login_option()


@When("click on 'logout' option from burger menu")
def click_on_logout_option(context):
    context.app.events_page.click_on_burger_button()
    context.app.events_page.click_on_logout_option()


@When("open 'my account' screen")
def open_my_account_screen(context):
    context.app.events_page.click_on_burger_button()
    context.app.events_page.click_on_my_account_option()


@Given("app is open and 'events' screen appears")
def app_is_open_and_events_screen_appears(context):
    context.app.events_page.check_page_visible()


@When("open option menu")
def open_option_menu(context):
    context.app.events_page.click_on_button_burger()


@When("open 'bottomsheet' with bet odds")
def open_bottomsheet_with_bet_odds(context):
    context.app.events_page.click_on_field_betting_odds()


@When("click on button 'YES' from alert")
def click_on_button_yes_from_alert(context):
    context.app.events_page.click_on_button_yes_from_alert()


@Then("'events' screen appears")
def events_screen_appears(context):
    context.app.events_page.check_page_visible()


@Then("'bet odds' bottomsheet appears")
def bet_odds_bottomsheet_appears(context):
    context.app.events_page.check_bottomsheet_betting_odds_visible()


@Then("'Log out' alert appears")
def logout_alert_appears(context):
    context.app.events_page.check_title_from_alert_logout()
