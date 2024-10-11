class Customer:
    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

    # Accessor methods
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone_number

    # Mutator methods
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def __str__(self):
        return f"Customer Name: {self.__name}\nAddress: {self.__address}\nPhone Number: {self.__phone_number}"


class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    # Accessor methods
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    # Mutator methods
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def __str__(self):
        return f"Car Make: {self.__make}, Model: {self.__model}, Year: {self.__year}"


class ServiceQuote:
    def __init__(self, parts_charges, labor_charges):
        self.__parts_charges = parts_charges
        self.__labor_charges = labor_charges
        self.__sales_tax_rate = 0.07  # 7% sales tax

    # Accessor methods
    def get_parts_charges(self):
        return self.__parts_charges

    def get_labor_charges(self):
        return self.__labor_charges

    def get_sales_tax(self):
        return (self.__parts_charges + self.__labor_charges) * self.__sales_tax_rate

    def get_total_charges(self):
        return self.__parts_charges + self.__labor_charges + self.get_sales_tax()

    # Mutator methods
    def set_parts_charges(self, parts_charges):
        self.__parts_charges = parts_charges

    def set_labor_charges(self, labor_charges):
        self.__labor_charges = labor_charges

    def __str__(self):
        return (f"Parts Charges: ${self.__parts_charges:.2f}\n"
                f"Labor Charges: ${self.__labor_charges:.2f}\n"
                f"Sales Tax: ${self.get_sales_tax():.2f}\n"
                f"Total Charges: ${self.get_total_charges():.2f}")


# Main function to demonstrate the program
def main():
    # Create a customer
    customer = Customer("Dwayne Johnson", "123 Main St, Waco", "254-1234")

    # Create a car
    car = Car("BMW", "X5", 2020)

    # Create a service quote
    service_quote = ServiceQuote(300, 150)

    # Display customer, car, and service quote information
    print(customer)
    print(car)
    print(service_quote)


if __name__ == "__main__":
    main()
