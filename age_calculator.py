from datetime import date


def calculate_age(birth_year: int, birth_month: int, birth_day: int) -> int:
    today = date.today()
    age = today.year - birth_year
    if (today.month, today.day) < (birth_month, birth_day):
        age -= 1
    return age


def get_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")


def main() -> None:
    print("Age Calculator")
    print("Enter your date of birth:")
    year = get_int("Year (YYYY): ")
    month = get_int("Month (1-12): ")
    day = get_int("Day (1-31): ")

    try:
        age = calculate_age(year, month, day)
        print(f"You are {age} years old.")
    except ValueError as error:
        print(f"Invalid date: {error}")


if __name__ == "__main__":
    main()
