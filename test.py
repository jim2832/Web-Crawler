from colorama import init, Fore, Back

init(autoreset=True)
print("This is a test...")
print(Fore.RED + "Hello")
print(Fore.YELLOW + "World!")
print(Fore.BLACK + Back.WHITE + "Good day!")

str = "HELLO"
if("H" in str):
    print(1)