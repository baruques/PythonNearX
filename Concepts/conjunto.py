set = {1, 2, 3, 4} # It's mutable but doesn't allow duplicates and is unordered (no indexing)
set.add(3)

print(set) # Won't add duplicate elements

set.add(25)

print(set) # Will add new element if it's not a duplicate

setcomprehension = {x for x in range(50) if x %2 == 0} # Can use comprehensions as well

print(setcomprehension)