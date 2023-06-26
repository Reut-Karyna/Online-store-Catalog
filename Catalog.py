def catalog(item1, item2, item3):
    item1_price = 200.0
    item2_price = 400.0
    item3_price = 600.0

    menu = "Output\n"
    menu += "Online Store\n"
    menu += "- - - - - - - - - - - - - - - - - - - - -\n"
    menu += f"Product(S)                         Price\n"

    if item1 == 1 and item2 == 1 and item3 == 1:
        gift_discount_price1 = (item1_price + item2_price + item3_price)
        gift_discount_price2 = gift_discount_price1 - (gift_discount_price1 * 0.25)
        menu += f"Combo 4(Item 1 + 2 + 3) -25%       {gift_discount_price2}\n"
    elif (item1 == 1 and item2 == 1):
        combo_discount_price1 = (item1_price + item2_price)
        combo_discount_price2 = combo_discount_price1 - (combo_discount_price1 * 0.1)
        menu += f"Combo 1(Item 1 + 2) -10%           {combo_discount_price2}\n"
    elif (item3 == 1 and item2 == 1):
        combo_discount_price1 = (item3_price + item2_price)
        combo_discount_price2 = combo_discount_price1 - (combo_discount_price1 * 0.1)
        menu += f"Combo 2(Item 2 + 3) -10%           {combo_discount_price2}\n"
    elif (item1 == 1 and item3 == 1):
        combo_discount_price1 = (item1_price + item3_price)
        combo_discount_price2 = combo_discount_price1 - (combo_discount_price1 * 0.1)
        menu += f"Combo 3(Item 1 + 3) -10%           {combo_discount_price2}\n"
    elif item1 == 1:
        menu += f"Item 1                             {item1 * item1_price}\n"
    elif item2 == 1:
        menu += f"Item 2                             {item2 * item2_price}\n"
    elif item3 == 1:
        menu += f"Item 3                             {item3 * item3_price}\n"
    else:
        menu += "You haven't purchased any item."
    menu += "_________________________________________\n"
    menu += "For delivery Contact: 98764678899"
    return menu

output = catalog(0, 0, 1)
print(output)
