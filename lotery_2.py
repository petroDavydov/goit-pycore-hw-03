import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    finish_result = []
    if min < 1 or max > 1000 or quantity > (max-min + 1) or quantity <= 0:
        return finish_result

    lottery_numbers = random.sample(range(min, max + 1), quantity)
    lottery_numbers.sort()
    return lottery_numbers


print(get_numbers_ticket(1, 56, 10))
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
