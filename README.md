# Online-store-Catalog

The provided code is a Python function named catalog that generates an online store catalog based on the items purchased. Here's a description of the code:

The function catalog takes three arguments: item1, item2, and item3, representing the purchase status of each item (0 indicates not purchased, 1 indicates purchased).
It initializes the prices for each item (item1_price, item2_price, item3_price).
It creates a string variable named menu to store the catalog output and initializes it with the header and initial lines.
The function uses conditional statements to determine the purchased items and add them to the catalog:
If all three items are purchased (item1 == 1 and item2 == 1 and item3 == 1), it calculates the discounted price by subtracting 25% from the sum of item prices (gift_discount_price1). Then, it adds a line to the menu string indicating the combo pack with the discounted price (gift_discount_price2).
If items 1 and 2 are purchased (item1 == 1 and item2 == 1), it calculates the discounted price by subtracting 10% from the sum of item prices (combo_discount_price1). Then, it adds a line to the menu string indicating the combo pack with the discounted price (combo_discount_price2).
If items 2 and 3 are purchased (item3 == 1 and item2 == 1), it follows a similar process as above to add a line to the menu string for the combo pack.
If items 1 and 3 are purchased (item1 == 1 and item3 == 1), it follows a similar process as above to add a line to the menu string for the combo pack.
If only item 1 is purchased (item1 == 1), it adds a line to the menu string indicating the purchase of item 1 and its price.
If only item 2 is purchased (item2 == 1), it adds a line to the menu string indicating the purchase of item 2 and its price.
If only item 3 is purchased (item3 == 1), it adds a line to the menu string indicating the purchase of item 3 and its price.
If no item is purchased, it adds a line to the menu string indicating that no items have been purchased.
Finally, it adds the closing lines for delivery contact information to the menu string.
The function returns the menu string.
The code calls the catalog function with specific arguments (0, 0, 1) to simulate a purchase and prints the generated catalog output.
This code can be used to display an online store catalog with item prices and combo pack discounts based on the purchased items. It can be adapted and expanded upon to suit specific requirements for an online store.
