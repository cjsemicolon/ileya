def convert_number_to_array(card_number):
    card_digits = []

    for digit in str(card_number):
        card_digits.append(int(digit))

    return card_digits


def get_card_type(card_digits):
    if len(card_digits) == 0:
        return "Unknown Card"

    if card_digits[0] == 4:
        return "Visa Card"

    if card_digits[0] == 5:
        return "MasterCard"

    if card_digits[0] == 6:
        return "Discover Card"

    if len(card_digits) > 1 and card_digits[0] == 3 and card_digits[1] == 7:
        return "American Express Card"

    return "Unknown Card"


def calculate_sum_of_doubled_even_position_digits(card_digits):
    doubled_digit_sum = 0

    for current_index in range(len(card_digits) - 2, -1, -2):
        doubled_digit = card_digits[current_index] * 2

        if doubled_digit > 9:
            tens_digit = doubled_digit // 10
            units_digit = doubled_digit % 10

            doubled_digit = tens_digit + units_digit

        doubled_digit_sum += doubled_digit

    return doubled_digit_sum


def calculate_sum_of_odd_position_digits(card_digits):
    odd_position_digit_sum = 0

    for current_index in range(len(card_digits) - 1, -1, -2):
        odd_position_digit_sum += card_digits[current_index]

    return odd_position_digit_sum


def is_valid_card(card_digits):
    doubled_digit_sum = calculate_sum_of_doubled_even_position_digits(card_digits)

    odd_position_digit_sum = calculate_sum_of_odd_position_digits(card_digits)

    total_sum = doubled_digit_sum + odd_position_digit_sum

    validity_status = total_sum % 10 == 0

    return validity_status

#def main():
#
#    credit_card_number = int(input("Enter credit card number: "))
#
#    card_digits = convert_number_to_array(credit_card_number)
#
#    card_type = get_card_type(card_digits)
#
#    validity_status = is_valid_card(card_digits)
#
#    print("Card Type:", card_type)
#
#    print("Validity Status:", validity_status)
#
#main()





