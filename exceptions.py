
itemsInCart = 0
# 2 items will be added to cart

if itemsInCart != 2:
    # raise Exception("Products cart count not matching") -- this will throw an error when its not = 2
    pass

# if this was == 0 it would work fine
assert(itemsInCart == 2) # this only works if it is true

