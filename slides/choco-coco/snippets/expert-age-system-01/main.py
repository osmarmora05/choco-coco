from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator


# Hechos
def run() -> tuple[str, int]:
    name = inquirer.text(
        message="¿Cuál es tu nombre?", validate=EmptyInputValidator()
    ).execute()
    age = inquirer.number(
        "¿Cuántos años tienes?",
        min_allowed=0,
        max_allowed=110,
        validate=EmptyInputValidator(),
    ).execute()

    return name, int(age)


# Reglas + Motor de inferencia
def classify_age(age: int) -> str:
    match age:
        case age if age <= 2:
            return "Eres un bebé"
        case age if age <= 12:
            return "Eres un niño"
        case age if age <= 17:
            return "Eres un adolescente"
        case age if age <= 64:
            return "Eres un adulto"
        case _:
            return "Eres super saiyajin"


def main():
    (name, age) = run()

    age_classification = classify_age(age)

    print(f"{name}. {age_classification}")


if __name__ == "__main__":
    main()
