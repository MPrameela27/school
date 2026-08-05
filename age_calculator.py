from datetime import date
import calendar


def calculate_age_components(birth_date: date) -> tuple[int, int, int]:
    today = date.today()
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        months -= 1
        prev_month = today.month - 1 or 12
        prev_year = today.year if today.month != 1 else today.year - 1
        days_in_prev_month = calendar.monthrange(prev_year, prev_month)[1]
        days += days_in_prev_month

    if months < 0:
        years -= 1
        months += 12

    return years, months, days


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
            years, months, days = calculate_age_components(birth_date)
            print(f"You are {years} years, {months} months, and {days} days old.")
            break
        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format.")


if __name__ == "__main__":
    main()
