STR = "Whiskey Hotel Four Tango Dash Alpha Romeo Three Dash\
Yankee Oscar Uniform Dash Sierra One November Kilo India\
November Golf Dash Four Bravo Zero Uniform Seven"
DIC = {"Zero": "0", "One": "1",
       "Two": "2", "Three": "3",
       "Four": "4", "Five": "5",
       "Six": "6", "Seven": "7",
       "Eight": "8", "Nine": "9",
       "Ten": "10", "Dash": "-"}
L_STR = STR.split(" ")
L_STR_M = []
for i, j in enumerate(L_STR):
    if L_STR[i].capitalize() in DIC.keys():
        L_STR_M.append(DIC[j])
    else:
        L_STR_M.append(L_STR[i][0].capitalize())
STR_M = "".join(L_STR_M)
print(STR_M)
