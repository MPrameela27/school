from datetime import date


def calculate_age(birth_date: date) -> int:
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age


def parse_birth_date(input_text: str) -> date:
    year_str, month_str, day_str = input_text.split("-")
    year = int(year_str)
    month = int(month_str)
    day = int(day_str)
    return date(year, month, day)


def main() -> None:
    print("Age Calculator")
    print("Enter your date of birth in YYYY-MM-DD format:")

    while True:
        raw_input = input("Date of birth: ")
        try:
            birth_date = parse_birth_date(raw_input.strip())
            if birth_date > date.today():
                print("The birth date cannot be in the future. Try again.")
                continue
            age = calculate_age(birth_date)
            print(f"You are {age} years old.")
            break
        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format.")


if __name__ == "__main__":
    main()
