from decimal import Decimal

# Class to represent a sales person
class SalesPerson:
    # Constructor for initializing the sales person
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.sales = []  # List to store sales figures

    # Method to add a new sale to the list
    def add_sale(self, amount):
        self.sales.append(amount)

    # Generator to iterate over the sales figures; the iter_sales method is a generator function using yield
    # Considered more Pythonic and efficient than manually creating an iterator object   
    def iter_sales(self):
        for sale in self.sales:
            yield sale  # Yield each sale value one at a time

# Function to generate a sales report
def create_report(sales_people):
    company_total = Decimal(0.0)  # Initialize company total

    # Iterate over each sales person
    for person in sales_people:
        total = Decimal(0.0)
        min_sale = Decimal('Infinity')  # Set initial minimum to infinity
        max_sale = Decimal(0.0)

        # Iterate over each sale for the current person
        for sale in person.iter_sales():
            total += Decimal(sale)  # Calculates the total sales
            min_sale = min(min_sale, Decimal(sale))  # Finds the minimum sale
            max_sale = max(max_sale, Decimal(sale))  # Finds the maximum sale

        average = total / len(person.sales) if person.sales else 0  # Calculate average sale

        # Print the report for the current sales person
        print(f"Sales person: {person.name} ({person.title})")
        print(f"Total Sales: ${total:.2f}")  # Format the output with 2 decimal places
        print(f"Min Sales: ${min_sale:.2f}")
        print(f"Max Sales: ${max_sale:.2f}")
        print(f"Average Sales: ${average:.2f}")
        print("-" * 20)  # Print a separator!

        company_total += total  # Add to company total

    # Print the total sales for the entire company
    print(f"Company total sales: ${company_total:.2f}")

# Main function to start the program
def main():
    sales_people = []  # List to store sales people
    
    # Get input for 3 sales people
    for i in range(3):
        name = input("Please enter sales person name: ")
        title = input("Please enter your sales person title: ")
        num_sales = int(input("How many sales values will you enter for this sales person? "))
        person = SalesPerson(name, title)

        # Get sales figures for each person
        for j in range(num_sales):
            sale = float(input(f"Please enter sales figure for {name}: "))
            person.add_sale(sale)

        sales_people.append(person)  # Add the sales person to the list

    # Create and print the report
    create_report(sales_people)

# Check if the script is run as the main program
if __name__ == "__main__":
    main()
