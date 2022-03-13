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


#function to print my name
def creator():
    print("""
██╗░░██╗░██╗░░░░░░░██╗░░░░░██╗
██║░░██║░██║░░██╗░░██║░░░░░██║
███████║░╚██╗████╗██╔╝░░░░░██║
██╔══██║░░████╔═████║░██╗░░██║
██║░░██║░░╚██╔╝░╚██╔╝░╚█████╔╝
╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░╚════╝░""")

#function to print the pp
def print_pp():
    print(prefix + length + suffix)

#here we call the functions
if __name__ == "__main__":
    creator()
    print_pp()