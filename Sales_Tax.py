__author__ = 'dwight'

# Write a program that will ask the user to enter the amount of a purchase. The program should then compute the state
# and county sales tax. Assume the state sales tax is 4 percent and the county sales tax is 2 percent. The program
# should display the amount of the purchase, the state sales tax, the county sales tax, the total sales tax, and the
# total of the sale (which is the sum of the amount of purchase plus the total sales tax).


def main():
    purchase_amount = float(input('Enter purchase amount: $'))

    print('\nPurchase Amount: $', purchase_amount, sep='')

    print('State Sales Tax (4%): $', format_cash(calc_state_sales_tax(purchase_amount)), sep='')

    print('County Sales Tax (2%): $', format_cash(calc_county_sales_tax(purchase_amount)), sep='')

    print('Total Tax: $', format_cash(calc_total_tax(purchase_amount)), sep='')

    print('Total Sale: $', format_cash(calc_total_sale(purchase_amount)), sep='')


def calc_state_sales_tax(purchase_amount):
    state_sales_tax_rate = 0.04
    return purchase_amount * state_sales_tax_rate


def calc_county_sales_tax(purchase_amount):
    county_sales_tax_rate = 0.02
    return purchase_amount * county_sales_tax_rate


def calc_total_tax(purchase_amount):
    return calc_state_sales_tax(purchase_amount) + calc_county_sales_tax(purchase_amount)


def calc_total_sale(purchase_amount):
    return purchase_amount + calc_total_tax(purchase_amount)


def format_cash(money):
    return format(money, ',.2f')


main()