# def is_user_input_even(userInput):
#     result = userInput%2==0
#     if result == True:
#         print(f"{userInput} is EVEN")
#     else:
#         print(f"{userInput} is FALSE")
# print(is_user_input_even(int(input("Please enter a number: "))))


# def is_even(number):
#     return number%2==0
#
# print(is_even(10))


# def check_even_list(num_list):
#
#     even_numbers = []
#
#     for number in num_list:
#         if number % 2 == 0:
#             even_numbers.append(number)
#         else:
#             pass
#     return even_numbers
#
# print(check_even_list([1,2,4,6]))


# stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]

# for (item = 0, item < stock_prices.length: item++){
#     text += stock_prices[item] + "\n"
# }

# for item in stock_prices:
#     print(item)
#
# for ticker,price in stock_prices:
#     print(ticker)
#
# for ticker,price in stock_prices:
#     print(price)
#
# for ticker,price in stock_prices:
#     if ticker == 'GOOG':
#         print(f"{ticker} is ${price}")
#     elif ticker == 'MSFT':
#         print(f"{ticker} is ${price}")
#     elif ticker == 'APPL':
#         print(f"{ticker} is ${price}")
#     else:
#         print("Ticker Not Found")


work_hours = [('Abby',1000), ('Cassie',8000), ('Billy',40000)]


def employee_check(work_hours):
    current_max_hours = 0
    employee_of_the_month = ''
    for name, hour in work_hours:
        if hour > current_max_hours:
            current_max_hours = hour
            employee_of_the_month = name
        else:
            pass
    print(f"{employee_of_the_month} has worked {current_max_hours} hours!")


employee_check(work_hours)