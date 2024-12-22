from datetime import datetime


class Person:
    def __init__(self, first_name, last_name=None, middle_name=None, birth_date=None, death_date=None, gender=None):
        if not first_name:
            raise ValueError("Ім'я є обов'язковим полем!")
        if not birth_date:
            raise ValueError("Дата народження є обов'язковим полем!")

        self.first_name = first_name.strip().capitalize() if first_name else ""
        self.last_name = last_name.strip().capitalize() if last_name else None
        self.middle_name = middle_name.strip().capitalize() if middle_name else None
        self.birth_date = self._validate_date(birth_date)
        self.death_date = self._validate_date(death_date) if death_date else None
        self.gender = gender.lower() if gender and gender.lower() in ['m', 'f'] else None

    def _validate_date(self, date_str):
        if isinstance(date_str, datetime):
            return date_str

        formats = ["%d.%m.%Y", "%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d"]
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        raise ValueError(f"Неправильний формат дати: {date_str}")

    def calculate_age(self):
        if not self.birth_date:
            return 0
        end_date = self.death_date if self.death_date else datetime.now()
        age = end_date.year - self.birth_date.year
        if end_date.month < self.birth_date.month or (
                end_date.month == self.birth_date.month and end_date.day < self.birth_date.day
        ):
            age -= 1
        return age

    def _age_with_suffix(self, age):
        last_digit = age % 10
        last_two_digits = age % 100

        if 11 <= last_two_digits <= 14:
            return f"{age} років"
        elif last_digit == 1:
            return f"{age} рік"
        elif 2 <= last_digit <= 4:
            return f"{age} роки"
        else:
            return f"{age} років"

    def __str__(self):
        name_parts = [part for part in [self.first_name, self.last_name, self.middle_name] if part]
        full_name = " ".join(name_parts)

        age = self._age_with_suffix(self.calculate_age())
        result = f"{full_name}, {age}"

        if self.gender:
            gender_str = "чоловік" if self.gender == "m" else "жінка"
            result += f", {gender_str}"

        if self.birth_date:
            birth_phrase = "Народився" if self.gender == "m" else "Народилася" if self.gender == "f" else "Народився(лася)"
            birth_date_str = self.birth_date.strftime("%d.%m.%Y")
            result += f". {birth_phrase}: {birth_date_str}"

        if self.death_date:
            death_phrase = "Помер" if self.gender == "m" else "Померла" if self.gender == "f" else "Помер(ла)"
            death_date_str = self.death_date.strftime("%d.%m.%Y")
            result += f". {death_phrase}: {death_date_str}"

        result += "."
        return result


