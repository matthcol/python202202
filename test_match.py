# match ... case en python 3.10

# ville = "Toulouse"
# ville = "Pau"
# ville = "Paris"
ville = "Barcelona"
match ville:
    case "Pau" | "Paris":
        print("begin by P:", ville)
    case "Toulouse":
        print("found Toulouse")
    case _:
        print ("default")
    