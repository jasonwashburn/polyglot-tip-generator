from typing import Union

from rich import print


def calculate_tip(total_bill: Union[float, int], tip_percent: int) -> float:
    return total_bill * tip_percent / 100


def split_bill(total_bill: Union[float, int], num_people: int) -> float:
    return round(total_bill / num_people, 2)


def main():
    print("Welcome to the tip calculator.")
    total_bill = float(input("What was the total bil? $"))
    tip_percent = int(
        input("What percentage tip would you like to give? 10, 12, or 15? ")
    )
    num_people = int(input("How many people to split the bill? "))

    subtotal = total_bill + calculate_tip(
        total_bill=total_bill, tip_percent=tip_percent
    )
    split_amount = split_bill(total_bill=subtotal, num_people=num_people)

    print(f"Each person should pay: ${split_amount:.2f}")


if __name__ == "__main__":
    main()
