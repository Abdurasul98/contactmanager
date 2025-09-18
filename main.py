from apps.admin.query import ContactQueries
from core.utils import main_menu, execute_tables, get_user_option


class Menu:
    def main_menu(self):
        while True:
            option = get_user_option(menu=main_menu, max_option=5)

            if option == "1":
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                ContactQueries.add_contact((name, phone))

            elif option == "2":
                rows = ContactQueries.read_contact()
                for row in rows:
                    print(row)

            elif option == "3":
                phone = input("Enter phone to update: ")
                new_name = input("Enter new name: ")
                ContactQueries.update_contact(new_name, phone)

            elif option == "4":
                phone = input("Enter phone to delete: ")
                ContactQueries.delete_contact(phone)

            elif option == "5":
                print("Goodbye!")
                break


if __name__ == "__main__":
    # execute_tables()
    Menu().main_menu()
