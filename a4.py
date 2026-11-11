adult = 15
senior = 12
child = 5

num_of_adults = 0
num_of_seniors = 0
num_of_children = 0

show_time = 00

def calculate_ticket_price(num_of_children, num_of_adults, num_of_seniors, show_time):
    if num_of_adults >= 2 and num_of_children >= 2:
        total_price = (num_of_adults * adult) + (num_of_children * child)
        discounted_price = total_price - 10
        return discounted_price
    elif num_of_seniors >= 1 and num_of_children >= 1:
        total_price = (num_of_seniors * senior) + (num_of_children * child)
        discounted_price = total_price - 5
        return discounted_price
    elif num_of_adults >= 2 and num_of_seniors >= 1 and num_of_children >= 2:
        total_price = (num_of_adults * adult) + (((num_of_seniors * senior)/100)*50) + (num_of_children * child)
        discounted_price = total_price - 10
        return discounted_price
    elif show_time < 15:
        total_price = (num_of_adults * adult) + (num_of_seniors * senior) + (num_of_children * child)
        discounted_price = total_price - ((total_price/100)*5)
        return discounted_price
    elif num_of_adults < 0 or num_of_seniors < 0 or num_of_children < 0 or show_time < 0:
        return None
print(calculate_ticket_price(num_of_adults, num_of_seniors, num_of_children, show_time))