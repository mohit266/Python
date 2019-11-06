# Store calculator 
class Calculator:
    def __init__(self):
        self.item_purchase = {}

    def add_item(self):
        sum_ = 0
        while True:
            item_name = input("\nEnter name of item or press 'q' for exit : ").lower()
            if item_name != 'q':
                item_price = input("Enter item price : Rs ")
                sum_ = sum_ + int(item_price)
                # print(f"Item total so far {sum_}")
                self.item_purchase.update({item_name: int(item_price)})
            else:
                break

    def purchase_list(self):
        print(self.item_purchase)

    def delete_item(self, item_name):
        if item_name.lower() not in self.item_purchase.keys():
            print("Item is not found.")
        else:
            del self.item_purchase[item_name]

    def check_out(self):
        total_bill = 0
        for key in self.item_purchase.keys():
            item_value = self.item_purchase.get(key)
            total_bill = total_bill + item_value
        print(f"Total amount (including GST) is: Rs {total_bill}. Thanks for shopping with us.")

if __name__ == '__main__':
    Programmer = Calculator()
    while True:
        print("\nEnter: \n"
              " 1.To add item in cart. \n"
              " 2.To remove item from the list. \n"
              " 3.To check the total item in the cart. \n"
              " 4.Proceed to checkout. \n"
              " 5.Exit.")

        user_choice = input("Enter your choice:")

        if user_choice not in ['1', '2', '3', '4', '5']:
            print("Please enter a valid option.")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            Programmer.add_item()

        elif user_choice == 2:
            item_name = input("Enter item name :").lower()
            Programmer.delete_item(item_name)

        elif user_choice == 3:
            print("\nList of items are:")
            Programmer.purchase_list()

        elif user_choice == 4:
            Programmer.check_out()

        elif user_choice == 5:
            exit()

        else:
            print("\nInvalid choice...Please try again.")