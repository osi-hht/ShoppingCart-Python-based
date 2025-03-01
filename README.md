# Shopping-Cart-Python-based
Shopping Cart - Object-Oriented Python Project

Overview

This is a Python-based Object-Oriented Programming (OOP) shopping cart system. It allows users to manage products, add items to a cart, remove items, calculate the total price, and check out. The project demonstrates key OOP principles such as encapsulation, inheritance, and polymorphism.

Features

Product Management: Add new products with name, price, and quantity.

Shopping Cart Functionality: Add, remove, and update product quantities in the cart.

Total Price Calculation: Automatically calculates the total price of items in the cart.

Discounts & Offers: Supports applying discounts on selected products.

User-Friendly Interface: Simple text-based interaction.

Technologies Used

Python 3.x

Object-Oriented Programming (OOP)

Classes and Structure

Product

Represents a product with attributes:

name (str)

price (float)

quantity (int)

ShoppingCart

Manages cart operations:

add_product(product, quantity): Adds a product to the cart.

remove_product(product_name): Removes a product from the cart.

update_quantity(product_name, quantity): Updates the quantity of a product in the cart.

calculate_total(): Returns the total price of items in the cart.

DiscountedProduct

A subclass of Product that applies a discount.

Future Enhancements

Add a graphical user interface (GUI) using Tkinter or PyQt.

Implement database integration for persistent storage.

Allow user authentication and multiple shopping carts.

Contributions

Contributions are welcome! Feel free to fork the repository, create a feature branch, and submit a pull request.

