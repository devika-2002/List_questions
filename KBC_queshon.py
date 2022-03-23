question_list = [
"1 How many continents are there?",
"2 What is the capital of India?",
"3 NG mei kaun se course padhaya jaata hai?"
]
options_list  = [
["Four", "Nine", "Seven", "Eight"],
["Chandigarh", "Bhopal", "Chennai", "Delhi"],

["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution_list = [3, 4, 1]
i=0
while i<len(question_list):
    print(question_list[i])
    a=0
    while a<=len(options_list):
        print(a+1,options_list[i][a])
        a=a+1
    n=int(input("enter the number"))
    if n==solution_list [i]:
        print("Congrats!") 
    else:
        print("Sadly")
        break  
    i=i+1