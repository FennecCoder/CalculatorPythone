#!/usr/bin/python3
"""
Sami Remili Pythonist
DZ
"""
import sys
print("### Fennec Calculator ###\n\n\tSami_Fennec_Deve\n")
def main():
    while True:
        
        menu = input("[A]-Addition [+]\n[B]-Substration [-]\n[C]-Multiplication [*]\n[D]-Division [/]\n[E]-Exponent [**]\n[#]-Exit\n[F]-Choose One Operation: ").upper()
        
        if menu == "#":
            print("\nThank You for Using My App!")
            sys.exit()
        
        
        #Variables for take two number
        number_1 = float((input("Enter your first Number: ")))
        number_2 = float((input("Enter your Second Number: ")))
    
        if menu == "A":
            # Def for  Addition only
            def Add():
                result = number_1 + number_2
                return print(f"The Result is: {result}\n")
            Add()
        
        if menu == "B":
            # Def for  Substration only
            def Sub():
                result = number_1 - number_2
                return print(f"The Result is: {result}\n")
            Sub()
            
        if menu == "C":
            # Def for  Multiplication  only
            def Multi():
                result = number_1 * number_2
                return print(f"The Result is: {result}\n")
            Multi()
            
        
        if menu == "D":
            # Def for  Devision only
            def Divi():
                result = number_1 / number_2
                return print(f"The Result is: {result}\n")
            Divi()
        
        
        if menu == "E":
            # Def for  Exponent only
            def Expo():
                result = number_1 ** number_2
                return print(f"The Result is: {result}\n")
            Expo()
                
main()

