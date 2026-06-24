from datetime import datetime
import os

class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        try:
            entry = input("Enter your journal entry: ")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(self.filename, "a") as file:  
                file.write(f"\n[{timestamp}]\n")
                file.write(entry + "\n")

            print("Entry added successfully!")

        except Exception as e:
            print("Error:", e)

    def view_entry(self):
        try:
            with open(self.filename, "r") as file:  
                content = file.read()

                if content.strip():
                    print("\nYour Journal Entries:")
                    print("-" * 40)
                    print(content)
                else:
                    print("No journal entries found. Start by adding new entry!")

        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")

        except PermissionError:
            print("Permission denied while reading the file.")

    def search_entry(self):
        try:
            keyword = input("Enter a keyword or date to search: ")

            with open(self.filename, "r") as file:
                lines = file.readlines()

            found = False

            print("\nMatching Entries:")
            print("-" * 40)

            for line in lines:
                if keyword.lower() in line.lower():
                    print(line.strip())
                    found = True

            if not found:
                print(f"No entries were found for the keyword: {keyword}")

        except FileNotFoundError:
            print("Error: The journal file does not exist.")

        except PermissionError:
            print("Permission denied while searching the file.")

    def delete_entry(self):
        try:
            if os.path.exists(self.filename):
                confirm = input(
                    "Are you sure you want to delete all entries? (yes/no): "
                )

                if confirm.lower() == "yes":
                    os.remove(self.filename)
                    print("All journal entries have been deleted.")
                else:
                    print("Deletion cancelled.")
            else:
                print("No journal entries to delete.")

        except PermissionError:
            print("Permission denied while deleting the file.")

        except Exception as e:
            print("Error:", e)

    def create_file_exclusive(self):
        try:
            with open(self.filename, "x") as file: 
                file.write("Journal File Created Successfully!\n")

            print("Journal file created using 'x' mode.")

        except FileExistsError:
            print("File already exists.")


def main():
    journal = JournalManager()

    while True:
        print("\nWelcome to Personal Journal Manager!")
        print("Please select an option:")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            journal.add_entry()

        elif choice == "2":
            journal.view_entry()

        elif choice == "3":
            journal.search_entry()

        elif choice == "4":
            journal.delete_entry()

        elif choice == "5":
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break

        else:
            print("Invalid option. Please select a valid option from the menu.")


if __name__ == "__main__":
    main()