import periodictable

Atomic_no=int(input("Enter Atomic No.:"))

def get_family(Atomic_no):
    if Atomic_no in (3,11,19,37,55,87):
        return "Alkali metals"
    elif Atomic_no in (4,12,20,38,56,88):
        return "Alkaline earth metals"
    elif 57 >= Atomic_no <=71:
        return "Lanthanides"
    elif 89 <= Atomic_no <=103:
        return "Actinides"
    elif (
        (21 <= Atomic_no <= 30)
        or (39 <= Atomic_no <= 48)
        or (72 <= Atomic_no <= 80)
        or (104 <= Atomic_no <= 112)):
        return "Transition metals"
    elif 113 <= Atomic_no <= 118:
        return "Unknown properties"
    elif Atomic_no in (13,31,49,50,81,82,83,84):
        return "Post-transition metals"
    elif Atomic_no in (5,14,32,33,51,52):
        return "Metalloids"
    elif Atomic_no in (1,6,7,8,15,16,34):
        return "Other nonmetals"
    elif Atomic_no in (9,17,35,53,85):
        return "Halogens"
    elif Atomic_no in (2,10,18,36,54,86):
        return "Noble gases"
    else:
        return "Invalid or unknown atomic number"
    

element=periodictable.elements[Atomic_no]
print('Name:', element.name)
print('Symbol:', element.symbol)
print('Atomic mass:', element.mass)
print('Density:', element.density)
print('Element family:', get_family(Atomic_no))
