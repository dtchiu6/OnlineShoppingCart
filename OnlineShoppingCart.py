class ItemToPurchase:

    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description = 'none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        string = '{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, (self.item_quantity * self.item_price))
        cost = self.item_quantity * self.item_price
        return string, cost

    def print_item_description(self):
        string = '{}: {}'.format(self.item_name, self.item_description)
        print(string, end='\n')
        return string


class ShoppingCart:

    def __init__(self, customer_name = 'none', current_date = 'January 1, 2016', cart_items = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
    
    def add_item(self, string):
        print('ADD ITEM TO CART', end = '\n')
        item_name = str(input('Enter the item name:\n'))
        item_description = str(input('Enter the item description:\n'))
        item_price = int(input('Enter the item price:\n'))
        item_quantity = int(input('Enter the item quantity:\n'))
        self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))
    
    def remove_item(self):
        total_cost = self.get_cost_of_cart()
        if (total_cost == 0):
            print('SHOPPING CART IS EMPTY')
        else:
            print('REMOVE ITEM FROM CART', end='\n')
            string = str(input('Enter name of item to remove:\n'))
            for item in self.cart_items:
                if(item.item_name == string):
                    index = self.cart_items.index(item)
                    del self.cart_items[index]
                    flag=True
                    break
                else:
                    flag=False
            if(flag==False):
                print('Item not found in cart. Nothing removed.')
    
    def modify_item(self):
        total_cost = self.get_cost_of_cart()
        if(total_cost == 0):
            print('SHOPPING CART IS EMPTY')
        else:
            print('\nCHANGE ITEM QUANTITY', end = '\n')
            name = str(input('Enter the item name:'))
        
            for item in self.cart_items:
                if(item.item_name == name):
                    quantity = int(input('Enter the new quantity:'))
                    item.item_quantity = quantity
                    flag=True
                    break
                else:
                    flag=False
            if(flag == False):
                print('Item not found in cart. Nothing modified.')
    
    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items = num_items + item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost = 0
        cost = 0
        for item in self.cart_items:
            cost = (item.item_quantity * item.item_price)
            total_cost += cost
        return total_cost

    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if (total_cost == 0):
            print('SHOPPING CART IS EMPTY')
        else:
            self.output_cart()

    def print_descriptions(self):
        total_cost = self.get_cost_of_cart()
        if(total_cost == 0):
            print('SHOPPING CART IS EMPTY')
        else:
            print('\nOUTPUT ITEMS\' DESCRIPTIONS')
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date),end='\n')
            print('\nItem Descriptions', end = '\n')
            for item in self.cart_items:
                print('{}: {}'.format(item.item_name, item.item_description), end = '\n')

    def output_cart(self):
        total_cost = self.get_cost_of_cart()
        print('OUTPUT SHOPPING CART', end='\n')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date), end='\n')
        print('Number of Items:', self.get_num_items_in_cart(), end='\n\n')
        tc = 0
        for item in self.cart_items:
            print('{} {} @ ${} = ${}'.format(item.item_name, item.item_quantity, item.item_price, (item.item_quantity * item.item_price)), end='\n')
            tc += (item.item_quantity * item.item_price)
        if(total_cost == 0):
            print('SHOPPING CART IS EMPTY')
        print('\nTotal: ${}'.format(tc), end='\n')
        
def print_menu(ShoppingCart):
    customer_Cart = ShoppingCart
    string = ''
    menu = ('\nMENU\n'
    'a - Add item to cart\n'
    'r - Remove item from cart\n'
    'c - Change item quantity\n'
    'i - Output items\' descriptions\n'
    'o - Output shopping cart\n'
    'q - Quit\n')
        
    command = ''
        
    while (command != 'q'):
        string = ''
        print(menu, end='\n')
        command = input('Choose an option:\n')
        while (command != 'a' and command != 'o' and command != 'i' and command != 'r' and command != 'c' and command != 'q'):
            command = input('Choose an option:\n')
                
        #-----Commands------
        if(command == 'a'):
            customer_Cart.add_item(string)
        if(command == 'o'):
            customer_Cart.output_cart()
        if(command == 'i'):
            customer_Cart.print_descriptions()
        if(command == 'r'):
            customer_Cart.remove_item()
        if(command == 'c'):
            customer_Cart.modify_item()

def main():
    if __name__ == "__main__":
        # Type main section of code here
        
        customer_name = str(input('Enter customer\'s name:'))
        current_date = str(input('\nEnter today\'s date:\n'))
        print('\nCustomer name:', customer_name, end='\n')
        print('Today\'s date:', current_date, end='\n')
        new_Cart = ShoppingCart(customer_name, current_date)
        print_menu(new_Cart)
main()

