import random


#array list for pp's body
pp_body = ["=", "==", "===", "====", "====="]
#array list for pp's suffix/tip
suffix_list = [">", ")", "D"]


#randomly selects the the pp's body
length = random.choice(pp_body)
#sets the pp's prefix
prefix = "8"
#randomly selects the pp's suffix
suffix = random.choice(suffix_list)


#prints the whole thing
print(prefix + length + suffix)