import os                                                                        #os module for access to clear screen command
import random                                                                  #module for clock and timer settings

def cls():                                                                        #function for clearing terminal window
    os.system('cls')
                                                                                  #These dictionaries are used to convert numbers and letters
text2num = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
num2text = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z"}


def consoleprint(text_in1,text_in2,text_in3):                                            #print function that generates a shitty ascii UI
    blank = " "
    launch_time = random.randint(10000,99999)
    date_time = "13-Dec-72"
    box_width = 64                                                                #for proper formatting, box_width must be between 37 and 74.
    border_width = box_width + 5
    line1 = ["-",text_in1,((box_width-len(text_in1))*blank),"-"]
    line2 = ["-",text_in2,((box_width-len(text_in2))*blank),"-"]
    line3 = ["-",text_in3,((box_width-len(text_in3))*blank),"-"]
    blank_line = ["-",(border_width-4)*" ","-"]
    cls()
    print ("-" * border_width)
    print ("- Silo 1138",blank*(border_width-42),"Command and Control Console -")
    print ("-" * border_width)
    print (blank_line[0],blank_line[1],blank_line[2])
    print (blank_line[0],blank_line[1],blank_line[2])
    print (line1[0],line1[1],line1[2],line1[3])
    print (line2[0],line2[1],line2[2],line2[3])
    print (line3[0],line3[1],line3[2],line3[3])
    print (blank_line[0],blank_line[1],blank_line[2])
    print (blank_line[0],blank_line[1],blank_line[2])
    print ("-" * border_width)
    print ("-",date_time,blank*(border_width-37),"Time To Launch :",launch_time,"-")
    print ("-" * border_width)


def cleaninput(check_this):                                                        #function that collects and sanitizes user input plaintext
    check_var = False   
    while check_var == False:
        check_this = input ("Enter a ten digit plaintext: ")    
        check_user = check_this.replace(' ','')
        if len(check_user) < len(check_this):
            print ("No spaces")            
        elif check_this.isalpha() == False:
            print ("Letters only.")            
        elif len(check_this) < 10:
            print ("Too short, exactly ten digits only.")            
        elif len(check_this) > 10:
            print ("Too long, exactly ten digits only.")            
        else:            
            break
        
    return check_this
    
def codeinput(check_this):                                                        #function that collects and sanitizes user input codekey
    check_var = False   
    while check_var == False:
        check_this = input ("Enter a ten digit codekey: ")    
        check_user = check_this.replace(' ','')
        if len(check_user) < len(check_this):
            print ("No spaces")            
        elif check_this.isalpha() == False:
            print ("Letters only.")            
        elif len(check_this) < 10:
            print ("Too short, exactly ten digits only.")            
        elif len(check_this) > 10:
            print ("Too long, exactly ten digits only.")            
        else:            
            break
        
    return check_this    

def encode(user_input,code_input):                                                #takes plaintext and code key and returns encoded cypher text

    calc_list = []                                                                #blank list to do math with
    code_list = []                                                                #blank list to do math with
    output_list = []                                                            #blank list for results to go into
    
    for each_char in user_input:                                                #for loop that converts each letter of user_input to a corresponding number as a list in calc_list
        calc_list.append(text2num[each_char])

    for each_char in code_input:                                                #for loop that converts each letter of code_input to a corresponding number as a list in code_list
        code_list.append(text2num[each_char])

    for list_index, null_var in enumerate(calc_list):                            #for loop that adds each corresponding list index in code_list and calc_list
        calc_list[list_index] = calc_list[list_index] + code_list[list_index]
        if calc_list[list_index] > 25:                                            #if condition that keeps numbers between 0 - 26
            calc_list[list_index] = calc_list[list_index] - 26

    for each_char in calc_list:                                                    #for loop that converts each number of calc_list back into a letter
        output_list.append(num2text[each_char])

    output_code = ''.join(output_list)                                            #convert encrypted code list to string
    print_input1 = ("plaintext message:    " + user_input)
    print_input2 = ("one-time cypher code: " + code_input)
    print_input3 = ("cypher text:          " + output_code)
    consoleprint(print_input1,print_input2,print_input3)                        #display results
    

def decode(user_input,code_input):                                                #takes cypher text and code key and returns decoded plaintext

    calc_list = []                                                                #blank list to do math with
    code_list = []                                                                #blank list to do math with
    output_list = []                                                            #blank list for results to go into

    for each_char in user_input:                                                #for loop that converts each letter of user_input to a corresponding number as a list in calc_list
        calc_list.append(text2num[each_char])

    for each_char in code_input:                                                #for loop that converts each letter of code_input to a corresponding number as a list in code_list
        code_list.append(text2num[each_char])

    for list_index, null_var in enumerate(calc_list):                            #for loop that subtracts each corresponding list index from calc_list and code_list
        calc_list[list_index] = calc_list[list_index] - code_list[list_index]
        if calc_list[list_index] < 0:                                            #if condition that keeps numbers between 0 - 26
            calc_list[list_index] = calc_list[list_index] + 26

    for each_char in calc_list:                                                    #for loop that converts each number of calc_list back into a letter
        output_list.append(num2text[each_char])

    output_code = ''.join(output_list)                                            #convert encrypted code list to string
    print_input1 = ("cypher text:          " + user_input)
    print_input2 = ("one-time cypher code: " + code_input)
    print_input3 = ("plaintext message:    " + output_code)
    consoleprint(print_input1,print_input2,print_input3)


                                                                                #program starts here


consoleprint("","","")
ans=True
while ans:
    print("""
       1 - Encode a one-time cypher
       2 - Decode a one-time cypher""")
    print()
    ans=input("Enter selection: ") 
    if ans=="1":
        consoleprint("","","")
        user_input = cleaninput("text")                                                 #sanitizes user input so that only ten letters are used
        user_input = user_input.lower()                                                    #changes user input string to lowercase
        print_input1 = ("plaintext message:    " + user_input)
        consoleprint(print_input1,"","")
        code_input = codeinput("text")                                                    #sanitizes user passcode input so that only ten letters are used
        code_input = code_input.lower()
        encode(user_input,code_input)
    elif ans=="2":
        consoleprint("","","")
        user_input = codeinput("text")                                                 #sanitizes user input so that only ten letters are used
        user_input = user_input.lower()                                                    #changes user input string to lowercase
        print_input1 = ("cypher text:          " + user_input)
        consoleprint(print_input1,"","")
        code_input = codeinput("text")                                                    #sanitizes user passcode input so that only ten letters are used
        code_input = code_input.lower()
        decode(user_input,code_input)
    elif ans=="3":
        consoleprint("Student Record Not Found","","")
    elif ans=="4":
        consoleprint("","","")
        break 
    elif ans !="":
      consoleprint ("","","",)
      print("\n Not Valid Choice Try again") 



	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
