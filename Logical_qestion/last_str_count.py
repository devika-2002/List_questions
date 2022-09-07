s= "coding is fun"
length = 0
new_str = s.strip()
for i in range(len(new_str)):
    if new_str[i] == " ":
        length = 0
    else:
        length +=1
print(length)


        # function_question
# def string(s):
#     length = 0   
#     new_str = s.strip()   
#     for i in range(len(new_str)):
#         if new_str[i] == " ":
#             length = 0
#         else:
#             length +=1
#     print(length)
# string("coding is fun" )





