# import sys

# print(sys.argv)

# print(sys.argv[2])

# for arg in sys.argv:
#     print(arg)


# ['.\\p31_sys_args.py', 'mehdi', '12', '14.56', 'True', 'ali']




# import sys

# if len(sys.argv)==3:
#     name=sys.argv[1]
#     age=int(sys.argv[2])
#     print(f"Name : {name}\t\tAge : {age}")
# else:
#     print("Usage : py p31_sys_args.py <name,age>")





# py p31_sys_args.py mehdi 12 
# py p31_sys_args.py mehdi 12 --avg 13.45

# import argparse
# parser=argparse.ArgumentParser()
# parser.add_argument('name')
# parser.add_argument('age')
# parser.add_argument('--avg',required=True)

# args=parser.parse_args()
# print(args.name)
# print(args.age)
# print(args.avg)







# import argparse
# parser=argparse.ArgumentParser()
# parser.add_argument('name')
# parser.add_argument('--age',type=int)


# args=parser.parse_args()
# print(args.name)
# print(args.age+100)



# import argparse
# parser=argparse.ArgumentParser()

# parser.add_argument('name')
# parser.add_argument('-a','--age',type=int,help="Usage : python p31_sys_args.py <name> , [--age]")


# args=parser.parse_args()

# print(args.name)
# print(args.age)






# import argparse
# parser=argparse.ArgumentParser(description="A simple CLI program")

# parser.add_argument('name')
# parser.add_argument('-a','--age',type=int)
# parser.add_argument('--avg',type=float,default=12.00)

# args=parser.parse_args()

# print(args.name)
# print(args.age)
# print(args.avg)






#               py .\p31_sys_args.py  Sum 12 23
#               py .\p31_sys_args.py  Mul 12 23


import argparse
parser=argparse.ArgumentParser()

subparses=parser.add_subparsers(dest="command",required=True)

sum_parser=subparses.add_parser("sum")
sum_parser.add_argument("num1",type=int)
sum_parser.add_argument("num2",type=int)

mul_parser=subparses.add_parser("mul")
mul_parser.add_argument("num1",type=int)
mul_parser.add_argument("num2",type=int)



args=parser.parse_args()
if args.command=="sum":
    print(args.num1+args.num2)
elif args.command=="mul":
    print(args.num1*args.num2)



# parser 
    # sub_parser
        # parser -> argument