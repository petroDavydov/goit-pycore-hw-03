import re


def normalize_phone(phone_number: str) -> str:
    ptrn_normalize_number = re.sub(
        r"\D", "", phone_number)  # remove not need symbols

    if not ptrn_normalize_number.startswith("+"):  # check if start +
        ptrn_normalize_number = "+38" + ptrn_normalize_number.lstrip("38")

        return ptrn_normalize_number


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки: \n", sanitized_numbers)
