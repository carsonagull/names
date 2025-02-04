def process_names():
    names_input = input("Enter the names: ").strip()

    if not names_input:
        print("No names entered. Please try again.")
        return

    names = [name.strip() for name in names_input.split(",")]
    sorted_names = sorted(names)

    print("\nNames in Ascending Order:")
    for name in sorted_names:
        print(f"- {name}")

    print(f"\nTotal number of names entered: {len(names)}")

process_names()
