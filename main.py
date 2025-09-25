from apps.contact.query import ContactQueries
from apps.message.query import MessageQueries
from core.utils import main_menu, contact_manager, sms_manager, execute_tables, get_user_option



class Menu:
    def main(self):
        while True:
            option = get_user_option(menu=main_menu,max_option=3)
            if option == "1":
                self.contact()

            elif option == "2":
                self.message()

            elif option == "3":
                print("Bye")
                break

    def message(self):
        while True:
            option = get_user_option(menu=sms_manager,max_option=4)

            if option == "1":
                phone_number = input("Enter phone: ")
                message = input("Enter message: ")
                MessageQueries.send_message((phone_number,message,phone_number))

            elif option == "2":
                MessageQueries.show_all_messages()
                message_id = input("Enter message_id: ")
                MessageQueries.delete_message(message_id)

            elif option == "3":
                MessageQueries.show_all_messages()
            else:
                print("Goodbye!")
                break

    def contact(self):
        while True:
            option = get_user_option(menu=contact_manager, max_option=5)

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
    Menu().main()
