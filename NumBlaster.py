import os,random
import string
import webbrowser
import time, pyfiglet
from colorama import Fore

def banner():
    banner = pyfiglet.figlet_format("BRUTAL NUMBER", font="doom")
    print(Fore.WHITE+banner)
    print(f"| {Fore.RED}YouTube: {Fore.WHITE}TR CYBER LAB | {Fore.BLUE}Github: {Fore.WHITE}trfahim | \n")
def home():
    banner()
    print(f"\n{Fore.WHITE}[{Fore.LIGHTYELLOW_EX}1{Fore.WHITE}] {Fore.YELLOW}Brutal Mobile Number (Country)")
    print(f"\n{Fore.WHITE}[{Fore.BLUE}2{Fore.WHITE}] {Fore.BLUE}Customize Phone Number")
    print(f"\n{Fore.WHITE}[{Fore.CYAN}00{Fore.WHITE}] {Fore.CYAN}Exit")
def cl():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def banner2():
    print(f"\n{Fore.BLUE}[+] Wait sometimes. It depends on your device capability\n")  
def back():
    back_in = input(f"\n{Fore.WHITE}[{Fore.GREEN}B{Fore.WHITE}]{Fore.GREEN}ack Home {Fore.WHITE}[{Fore.RED}E{Fore.WHITE}]{Fore.RED}xit {Fore.CYAN}>> ").lower()
    if back_in == "e":
        print(Fore.RED+ "\nExit Sucessful\n")
        os._exit(0)
    else:
        main()
        
def bd_number_home():
    print(Fore.CYAN + "\n[A] Airtel")
    print(Fore.CYAN + "\n[B] Banglalink")
    print(Fore.CYAN + "\n[G] Grameenphone")
    print(Fore.CYAN + "\n[R] Robi")
    print(Fore.CYAN + "\n[T] Teletalk")
    print(Fore.RED + "\n[0] Exit")
def india_num_home():
    print(Fore.CYAN + "\n[A] Airtel")
    print(Fore.CYAN + "\n[B] Bsnl")
    print(Fore.CYAN + "\n[I] Idea")
    print(Fore.CYAN + "\n[V] Vodafone")
    print(Fore.RED + "\n[0] Exit")
def pak_num_home():
    print(Fore.CYAN + "\n[T] Telenor")
    print(Fore.CYAN + "\n[J] Jazz")
    print(Fore.CYAN + "\n[U] Ufone")
    print(Fore.CYAN + "\n[W] Warid")
    print(Fore.RED + "\n[0] Exit")
def us_num_home():
    print(Fore.CYAN + "\n[N] New York City")
    print(Fore.CYAN + "\n[S] San Francisco")
    print(Fore.CYAN + "\n[M] Miami")
    print(Fore.CYAN + "\n[L] Los Angeles")
    print(Fore.CYAN + "\n[W] Washington")
    print(Fore.RED + "\n[0] Exit")
def canada_num_home():
    print(Fore.CYAN + "\n[T] Toronto")
    print(Fore.CYAN + "\n[V] Vancouver")
    print(Fore.CYAN + "\n[M] Montreal")
    print(Fore.RED + "\n[0] Exit")  
def brutal_mobile_number():
    print(Fore.CYAN + "\n[10] Austrila")
    print(Fore.CYAN + "\n[11] Bangladesh")
    print(Fore.CYAN + "\n[12] India")
    print(Fore.CYAN + "\n[13] Pakistan")
    print(Fore.CYAN + "\n[14] USA")
    print(Fore.CYAN + "\n[15] Canada")
    print(Fore.RED + "\n[00] Exit")

    print(Fore.GREEN + "\nSelect Country to Generate Brutal Mobile Number >> " + Fore.RESET, end="")
    select = input()
    code = ""

    if select == "10":
        code = "04"
        country = "Austrila"
        start = 9999999
        end = 99999999
    elif select == "11":
        cl()
        banner()
        bd_number_home()
        start = 9999999
        end = 99999999
        print(Fore.GREEN + "\nSelect a Oparetor to Generate Brutal Number >> " + Fore.RESET, end="")
        user_in = input().upper()
        if user_in == "A":
            code = "016"
            country = "BD_Airtel"
        elif user_in == "B":
            code = "019"
            country = "BD_Banglalink"
        elif user_in == "G":
            code = "017"
            country = "BD_Grameenphone"
        elif user_in == "R":
            code = "018"
            country = "BD_Robi"
        elif user_in == "T":
            code = "015"
            country = "BD_Teletalk"
        else:
            back()
    elif select == "12":
        cl()
        banner()
        india_num_home()
        start = 9999999
        end = 99999999
        print(Fore.GREEN + "\nSelect a Oparetor to Generate Brutal Number >> " + Fore.RESET, end="")
        user_in = input().upper()
        if user_in == "A":
            code = "98"
            country = "IND_Airtel"
        elif user_in == "B":
            code = "94"
            country = "IND_Bsl"
        elif user_in == "I":
            code = "93"
            country = "IND_Idea"
        elif user_in == "V":
            code = "88"
            country = "IND_Vodafone"
        else:
            back()
    elif select == "13":
        cl()
        banner()
        pak_num_home()
        start = 999999
        end = 9999999
        print(Fore.GREEN + "\nSelect a Oparetor to Generate Brutal Number >> " + Fore.RESET, end="")
        user_input = input().upper()
        if user_input == "T":
            code = "307"
            country = "PAK_Telenor"
        elif user_input == "J":
            code = "300"
            country = "PAK_Jazz"
        elif user_input == "U":
            code = "330"
            country = "PAK_Ufone"
        elif user_input == "W":
            code = "320"
            country = "PAK_Warid"
        else:
            back()
    elif select == "14":
        cl()
        banner()
        us_num_home()
        start =  999999
        end = 9999999
        print(Fore.GREEN + "\nSelect Region to Generate Brutal Number >> " + Fore.RESET, end="")
        user_in = input().upper()
        if user_in == "N":
            code = "212"
            country = "USA_New_York"
        elif user_in == "S":
            code = "415"
            country = "USA_San_Francisco"
        elif user_in == "M":
            code = "305"
            country = "USA_Miami"
        elif user_in == "L":
            code = "213"
            country = "USA_Los_Angeles"
        elif user_in == "W":
            code = "202"
            country = "USA_Washington"
        else:
            back()
    elif select == "15":
        cl()
        banner()
        canada_num_home()
        start = 999999
        end = 9999999
        print(Fore.GREEN + "\nSelect Region to Generate Brutal Number >> " + Fore.RESET, end="")
        user_in = input().upper()
        if user_in == "T":
            code = "416"
            country = "CANADA_Toronto"
        elif user_in == "V":
            code = "604"
            country = "CANADA_Vancouver"
        elif user_in == "M":
            code = "514"
            country = "CANADA_Montreal"
        else:
            back()
    elif select == "00":
        main()
    else:
        print(f"{Fore.RED}Wrong Input!!")
        back()
    cl()
    banner()
    banner2()
    total = end
    start_tm = time.time()
    file_nm = (f"{country}_Brutal_Mobile_Number.txt")
    print(f"Time: {start_tm}")
    with open(file_nm, "w") as file:
        for passwords in range(start, end):
            file.write(f"{code}{passwords}\n")
            parcent = (passwords / total)*100
            print(f"{Fore.GREEN}Progress: {Fore.LIGHTCYAN_EX}{round(parcent, 2)}%", end="\r")  
        end_tm = time.time()
        count = end_tm - start_tm    
        print(f"{Fore.BLUE}Time Spend: {Fore.WHITE}{round(count, 2)} Seconds", end="\r")  
        print("\n")
        print(Fore.BLUE+"-"*50)
        print(f"{Fore.LIGHTMAGENTA_EX}File Save as '{Fore.YELLOW}{country}_Brutal_Mobile_Number.txt'")
        print(Fore.BLUE+"-"*50)
        back()

def customize_phone_num():
    print(Fore.CYAN + "\n[A] 1 digit Oprator")
    print(Fore.CYAN + "[B] 2 digit Oprator ")
    print(Fore.CYAN + "[C] 3 digit Oprator")
    print(Fore.CYAN + "[D] 4 digit Oprator")
    print(Fore.CYAN + "[H] Home")
    print(Fore.GREEN + "\n>>>> " + Fore.RESET, end="")
    choose_oprator = input().upper()
    if choose_oprator == "A":
        print(Fore.GREEN + "\nEnter 1 digit oprator >>> " + Fore.RESET, end="")
        digit = input()
        if digit.isdigit and len(digit) == 1:
            user_digit = digit
            op_digit = 1
        else:
            print(Fore.RED + "\nWrong Input!! Enter digit and try again")
            back()
    elif choose_oprator == "B":
        print(Fore.GREEN + "\nEnter 2 digit oprator >>> " + Fore.RESET, end="")
        digit = input()
        if digit.isdigit and len(digit) == 2:
            user_digit = digit
            op_digit = 2
        else:
            print(Fore.RED + "\nWrong Input!! Enter digit and try again")
            back()
    elif choose_oprator == "C":
        print(Fore.GREEN + "\nEnter 3 digt oprator >>> " + Fore.RESET, end="")
        digit = input()
        if digit.isdigit and len(digit) == 3:
            user_digit = digit
            op_digit = 3
        else:
            print(Fore.RED + "\nWrong Input!! Enter digit and try again")
            back()
    elif choose_oprator == "D":
        print(Fore.GREEN + "\nEnter 4 digt oprator >>> " + Fore.RESET, end="")
        digit = input()
        if digit.isdigit and len(digit) == 4:
            user_digit = digit
            op_digit = 4
        else:
            print(Fore.RED + "\nWrong Input!! Enter digit and try again")
            back()
    else:
        back()            
            
    case1 = random.choice(string.ascii_letters)
    case2 = random.choice(string.digits)
    case3 = random.choice(string.ascii_lowercase)
    random_num = (f"{case1}{case2}{case3}")
    print(Fore.CYAN + "\n[1] 7 Digit")
    print(Fore.CYAN + "[2] 8 Digit")
    print(Fore.CYAN + "[3] 9 Digit")
    print(Fore.CYAN + "[4] 10 Digit")
    print(Fore.CYAN + "[5] 11 Digit")
    print(Fore.GREEN + "\n>>>> " + Fore.RESET, end="")
    user_num_input = input()
    if user_num_input == "1":
        cal_st = (7-(int(op_digit)))
        cal_st_num = (cal_st-1)
        cal_end_num = (cal_st_num+1)
        start_num = (cal_st_num*"9")
        end_num = (cal_end_num*"9")
        file_nm = f"7_Digit_{user_digit}_Mobile_Num_{random_num}.txt"
    elif user_num_input == "2":
        cal_st = (8-(int(op_digit)))
        cal_st_num = (cal_st-1)
        cal_end_num = (cal_st_num+1)
        start_num = (cal_st_num*"9")
        end_num = (cal_end_num*"9")
        file_nm = f"8_Digit_{user_digit}_Mobile_Num_{random_num}.txt"
    elif user_num_input == "3":
        cal_st = (9-(int(op_digit)))
        cal_st_num = (cal_st-1)
        cal_end_num = (cal_st_num+1)
        start_num = (cal_st_num*"9")
        end_num = (cal_end_num*"9")
        file_nm = f"9_Digit_{user_digit}_Mobile_Num_{random_num}.txt"
    elif user_num_input == "4":
        cal_st = (10-(int(op_digit)))
        cal_st_num = (cal_st-1)
        cal_end_num = (cal_st_num+1)
        start_num = (cal_st_num*"9")
        end_num = (cal_end_num*"9")
        file_nm = f"10_Digit_{user_digit}_Mobile_Num_{random_num}.txt"
    elif user_num_input == "5":
        cal_st = (11-(int(op_digit)))
        cal_st_num = (cal_st-1)
        cal_end_num = (cal_st_num+1)
        start_num = (cal_st_num*"9")
        end_num = (cal_end_num*"9")
        file_nm = f"11_Digit_{user_digit}_Mobile_Num_{random_num}.txt"
    else:
        back()
    st_time = time.time() 
    total = int(end_num)
    with open(file_nm, "w") as file:
        for passwords in range(int(start_num), int(end_num)):
            file.write(f"{user_digit}{passwords}\n")
            progress = (int(passwords) / total)*100
            print(f"{Fore.GREEN}Progress: {Fore.LIGHTCYAN_EX}{round(progress, 2)}%", end="\r")
        end_time = time.time()
        count = end_time - st_time
        print(f"{Fore.BLUE}Time Spend: {Fore.WHITE}{round(count, 2)} Seconds", end="\r")     
        print("\n")
        print(Fore.BLUE+"-"*50)
        print(f"{Fore.LIGHTMAGENTA_EX}File Save as '{Fore.YELLOW}{file_nm}'")
        print(Fore.BLUE+"-"*50)
        back()
        
def main():
    webbrowser.open("https://www.youtube.com/@tr_cyberlab")
    time.sleep(5)
    cl()
    home()
    print(Fore.WHITE + "\n>>>> " + Fore.GREEN, end="")
    user_input = input()
    if user_input == "1":
        cl()
        banner()
        time.sleep(3)
        brutal_mobile_number()
    elif user_input == "2":
        cl()
        banner()
        time.sleep(3)
        customize_phone_num()
    else:
        main()

if __name__ == "__main__":
    main()
