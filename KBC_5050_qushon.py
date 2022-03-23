question_list=["1.How many continents are there ?","2.What is the capital of India ?",
"3.NG mei kaun se course padhaya jaata hai ? "]
options_list=[["Four","Nine","Seven","Eight"],
["Chandigarh","Bhopal","Chennai","Delhi"],
["Software Engineering","Counseling","Tourism","Agriculture"]]
life_line_5050=[["Seven","Eight"],["Bhopal","Delhi"],["SoftwareEngineering","Counseling"]]
solution_lifeline=[1,2,1]
solution_list=[3,4,1]

i=0
count=0
while i<len(question_list):          
    print(question_list[i])
    j=0
    while j<len(options_list[i]):
        print(j+1,options_list[i][j])
        j=j+1
    user=int(input("Enter the anynumber: ya used lifeline 5050:-"))
    if user==solution_list[i]:
        print("congrates your answer is correct")
    elif user==5050:          
        if count==0:
            k=0
            while k<len(life_line_5050[i]):
                print(k+1,life_line_5050[i][k])
                k=k+1
            count+=1
            user2=int(input("enter any number. "))
            if user2==solution_lifeline[i]:
                print("Congrats!")
            else:
                print("Sadly:") 
                break
   
        else:
            print("you already used the 5050 ")
            num=int(input("enter any number: "))
            if num==solution_list[i]:
                print("Congrats!")
            else:
                print("Sadly")
                break
    else:
        print("Your answer is wrong")
        break        
    i=i+1       
        

