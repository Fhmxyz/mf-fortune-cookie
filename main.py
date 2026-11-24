import os

# Fortune Cookie Wisdom for Developers — one original fortune-cookie
# line, at most 120 characters, in the cookie's prophetic register.
LINE = (
    "One day you will be the legacy code you curse \u2014 feared by strangers, "
    "understood by no one, not even by you."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
