# Objective: Build a coffee shop order system where customers can create and customize coffee orders
# - Create Coffee objects using a class (instantiation)
# - Add customizations using mutator methods (modify the order)
# - Get order details using accessor methods (read information)
# - Chain methods together for smooth customization



class Coffee:
    """
    A Coffee class representing a coffee order at a coffee shop.
    
    Base prices by size:
    - "small": $3.00
    - "medium": $4.00
    - "large": $5.00
    """
    
    def __init__(self, size, coffee_type):
        """
        Initialize a Coffee object.
        
        Args:
            size: Size of coffee ("small", "medium", or "large")
            coffee_type: Type of coffee (e.g., "latte", "cappuccino", "espresso")
        
        Hint: Store size and coffee_type as instance variables using self.
              Initialize empty lists for syrups and extras.
              Set base price based on size.
        """
        # TODO: Initialize instance variables
        # self.size = size
        # self.coffee_type = coffee_type
        # self.syrups = []  # List to store added syrups
        # self.milk_type = None  # No milk by default
        # self.has_whipped_cream = False
        # self.base_price = 3.0 if size == "small" else (4.0 if size == "medium" else 5.0)
        self.size = size
        self.coffee_type = coffee_type
        self.syrups = []
        self.milk_type = None
        self.has_whipped_cream = False
        if size == "small":
            self.base_price = 3.0
        elif size == "medium":
            self.base_price = 4.0
        elif size == "large":
            self.base_price = 5.0
        

    
    def add_syrup(self, syrup_flavor):
        """
        Add a syrup to the coffee (MUTATOR method - modifies the object).
        Each syrup adds $0.50 to the price.
        
        Args:
            syrup_flavor: Flavor of syrup to add (e.g., "vanilla", "caramel")
        
        Returns:
            self (to allow method chaining)
        
        Hint: Append syrup_flavor to self.syrups list, then return self
        """
        # TODO: Add syrup to the syrups list and return self
        self.syrups.append(syrup_flavor)
        return self
    
    def add_milk(self, milk_type):
        """
        Add milk to the coffee (MUTATOR method).
        Milk adds $0.50 to the price.
        
        Args:
            milk_type: Type of milk (e.g., "whole", "oat", "almond")
        
        Returns:
            self (to allow method chaining)
        
        Hint: Set self.milk_type to the milk_type, then return self
        """
        # TODO: Set milk type and return self
        if milk_type is not None:
            self.milk_type = milk_type
        return self
    
    def add_whipped_cream(self):
        """
        Add whipped cream to the coffee (MUTATOR method).
        Whipped cream adds $0.75 to the price.
        
        Returns:
            self (to allow method chaining)
        
        Hint: Set self.has_whipped_cream to True, then return self
        """
        # TODO: Add whipped cream and return self
        self.has_whipped_cream = True
        return self
    
    def get_price(self):
        """
        Calculate total price of the coffee (ACCESSOR method - doesn't modify).
        
        Returns:
            Total price as float
        
        Hint: Start with base_price, add $0.50 per syrup, $0.50 if milk added,
              $0.75 if whipped cream added
        """
        # TODO: Calculate and return total price
        total_price = self.base_price
        num_syrups = len(self.syrups)
        total_price += (0.5 * num_syrups)
        if self.milk_type is not None:
            total_price += 0.5
        if self.has_whipped_cream:
            total_price += 0.75
        return total_price
    
    def get_description(self):
        """
        Get full description of the coffee order (ACCESSOR method).
        
        Returns:
            Description string
        
        Hint: Build a string like "Large Latte with vanilla syrup, oat milk, whipped cream"
        """
        # TODO: Build and return description string
        description = f"{self.size} {self.coffee_type} with "
        for syrup in self.syrups:
            description += f"{syrup} syrup, "
        if self.milk_type is not None:
            description += f"{self.milk_type} milk, "
        if self.has_whipped_cream:
            description += f"whipped cream"
        else:
            description += f"no whipped cream"
        return description
    
    def get_size(self):
        """
        Get the size of the coffee (ACCESSOR method).
        
        Returns:
            Size string
        """
        # TODO: Return the size
        return self.size
    
    def get_type(self):
        """
        Get the type of coffee (ACCESSOR method).
        
        Returns:
            Coffee type string
        """
        # TODO: Return the coffee type
        return self.coffee_type


def create_simple_coffee(size, coffee_type):
    """
    Create a basic coffee with no customizations.
    This demonstrates instantiation - creating an object from a class.
    
    Args:
        size: Size of coffee
        coffee_type: Type of coffee
    
    Returns:
        Coffee object
    
    Hint: Call Coffee class like a function: Coffee(size, coffee_type)
    """
    # TODO: Create and return a Coffee object
    coffee = Coffee(size, coffee_type)
    return coffee


def create_customized_coffee(size, coffee_type, syrup, milk):
    """
    Create a coffee with syrup and milk customizations.
    
    Args:
        size: Size of coffee
        coffee_type: Type of coffee
        syrup: Syrup flavor to add
        milk: Milk type to add
    
    Returns:
        Customized Coffee object
    
    Hint: Create Coffee object, then call add_syrup() and add_milk() on it
    """
    # TODO: Create coffee and add customizations
    coffee = create_simple_coffee(size, coffee_type)
    coffee.add_syrup(syrup)
    coffee.add_milk(milk)
    return coffee



def create_deluxe_coffee_with_chaining(size, coffee_type, syrup1, syrup2, milk):
    """
    Create a deluxe coffee using method chaining.
    
    Args:
        size: Size of coffee
        coffee_type: Type of coffee
        syrup1: First syrup flavor
        syrup2: Second syrup flavor
        milk: Milk type
    
    Returns:
        Deluxe Coffee object
    
    Hint: Chain methods: coffee.add_syrup(syrup1).add_syrup(syrup2).add_milk(milk).add_whipped_cream()
    """
    # TODO: Create coffee and chain customization methods
    coffee = create_customized_coffee(size, coffee_type, syrup1, milk)
    coffee.add_syrup(syrup2)
    coffee.add_whipped_cream()
    return coffee



def compare_two_orders(coffee1, coffee2):
    """
    Compare prices of two coffee orders (using accessor methods).
    
    Args:
        coffee1: First Coffee object
        coffee2: Second Coffee object
    
    Returns:
        Tuple (price1, price2, more_expensive) where more_expensive is 1 if coffee1
        costs more, 2 if coffee2 costs more, or 0 if they cost the same
    
    Hint: Use get_price() accessor method on both objects to compare
    """
    # TODO: Get prices and compare them
    price1 = coffee1.get_price()
    price2 = coffee2.get_price()
    if price1 > price2:
        more_expensive = 1
    elif price2 > price1:
        more_expensive = 2
    else:
        more_expensive = 0
    return (price1, price2, more_expensive)

