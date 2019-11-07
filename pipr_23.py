
products_list = [['Banana', 327, 1], ['Apple', 30, 2], ['Pear', 620, 3], ['Mango', 999, 2], ['Cherry', 25, 50]]

list_of_numbers = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def get_average_of_multiples_of_number(numbers_list, divider):
    multiples = [n for n in numbers_list if n % divider is 0]
    return sum(multiples) / len(multiples)


def find_lowest_price_of_product(products_dict):
    item = min(products_dict.items(), key=lambda x: x[1])
    return item[0], item[1][0]


def update_quantity(item_name, quantity=1):
    new_index = -1
    for index, item in enumerate(products_list):
        if item[0] == item_name:
            new_index = index
            break
    try:
        products_list[new_index][2] = quantity
    except IndexError:
        print("No item in list. Please add new item before updating it")


def price_to_dollars_and_cents(price):
    return price // 100, price % 100


def get_one_line(index, name, price, quantity):
    prop_price = price_to_dollars_and_cents(price * quantity)
    return f"{index + 1:2}.{name:20}*{quantity:>2}{prop_price[0]:>4},{prop_price[1]:02} zł"


def print_all_lines(products, sort_by_price=False, descending=False):
    if sort_by_price:
        products.sort(key=lambda x: x[1] * x[2], reverse=descending)
    total_price = 0

    for index, product in enumerate(products):
        quantity = product[2]
        price = product[1]
        print(get_one_line(index, *product))
        total_price += price * quantity

    proper_total_price = price_to_dollars_and_cents(total_price)
    print('-' * 37)
    print(f'TOTAL:{proper_total_price[0]:24},{proper_total_price[1]:02} zł')


if __name__ == "__main__":
    print(get_average_of_multiples_of_number(list_of_numbers, 3))
    # print(find_lowest_price_of_product(products_dict))
    update_quantity('Banana', 7)
    print_all_lines(products_list, True)
