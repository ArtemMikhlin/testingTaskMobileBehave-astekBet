from behave import Then, When, Given


@When("input {stake} in 'stake amount' field")
def input_stake_in_stake_amount_field(context, stake: int):
    context.app.single_bet_page.input_amount(stake)


@When("click on 'Bet' button")
def click_on_bet_button(context):
    context.app.single_bet_page.click_on_button_bet()


@Then("'single bet' screen appears")
def single_bet_screen_appears(context):
    context.app.single_bet_page.check_page_visible()


@Then("'Not enough funds' alert appears")
def not_enough_funds_alert_appears(context):
    context.app.single_bet_page.check_text_from_alert_not_enough_funds()
