"""Functions for calculating steps in exchanging currency.

Python numbers documentation: 
https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: 
https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    if not isinstance(budget, (int, float)) or not isinstance(exchange_rate, (int, float)):
        raise ValueError("Error!")
    exchanged_amount = budget / exchange_rate
    return float(exchanged_amount)


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    if not isinstance(budget, (int, float)) or not isinstance(exchanging_value, (int, float)):
        raise ValueError("Error!")
    amount = budget - exchanging_value
    return float(amount)


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """

    if not isinstance(denomination, int) or not isinstance(number_of_bills, int):
        raise ValueError("Both denomination and bills must be integers.")
    total_value = denomination * number_of_bills
    return total_value


def get_number_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

    if not isinstance(amount, int) or not isinstance(denomination, int):
        raise ValueError("Error Code Here")
    total_value = amount // denomination
    return int(total_value)


def get_leftover_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """

    if not isinstance(amount, float) or not isinstance(denomination, int):
        raise ValueError("Ground Control to Major Tom")
    total_value = amount % denomination
    return float(total_value)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    # Adjust the exchange rate by applying the spread percentage
    adjusted_rate = exchange_rate * (1 + spread / 100)
    # Calculate the exchanged amount in the new currency
    exchanged_amount = budget / adjusted_rate
    # Calculate the maximum whole number of bills that can be received
    max_value_in_whole_units = (exchanged_amount // denomination) * denomination
    # Return the result as an integer
    return int(max_value_in_whole_units)
