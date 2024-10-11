import random
import time
import os
import sys  # Import sys module for sys.stdout.write

# ANSI escape sequences for colors
RESET = "\033[0m"
GREEN_46 = "\033[38;5;46m"
RED = "\033[38;5;196m"
YELLOW = "\033[38;5;226m"
BLUE = "\033[38;5;33m"
CYAN ="\033[36m"
BRIGHT_YELLOW = "\033[93m"
CYAN ="\033[36m"
BRIGHT_YELLOW = "\033[93m"
MAGENTA ="\033[35m"
BG_DARK_TURQUOISE = "\033[48;5;37m"
BG_TURQUOISE = "\033[48;5;51m"
X ="\033[48;5;223m"
MINT = "\033[38;5;43m"
AQUA ="\033[36m"
def clear():
    os.system('clear')  # Clears the terminal

def show_banner():
    banner = f"""
{GREEN_46}╔════════════════════════╗
{GREEN_46}║ {RED}BBBBB   CCCCC   AAAAAA{RESET} {GREEN_46}║
{GREEN_46}║ {RED}B    B  C       A    A{RESET} {GREEN_46}║
{GREEN_46}║ {RED}BBBBB   C       AAAAAA{RESET} {GREEN_46}║
{GREEN_46}║ {RED}B    B  C       A    A{RESET} {GREEN_46}║
{GREEN_46}║ {RED}BBBBB   CCCCC   A    A{RESET} {GREEN_46}║
{GREEN_46}╚════════════════════════╝

{RESET}{AQUA}💝A tool for BANGLADESH CYBER ARMY TEAM💝{RESET}

{GREEN_46}╔═════════════╗  ࿇⃝🌹⃢A🌹⃝࿇  {GREEN_46}╔══════════════════════════════╗
{GREEN_46}║[🤎]{GREEN_46}𝐂𝐨𝐝𝐞 𝐛𝐲  ║  ࿇⃝🌹⃢D🌹⃝࿇  {GREEN_46}║{GREEN_46}𝐀𝐃𝐈𝐑𝐓𝐓𝐀                       ║
{GREEN_46}║[💛]{GREEN_46}𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 ║  ࿇⃝🌹⃢I🌹⃝࿇  {GREEN_46}║{GREEN_46}𝐒𝐇𝐈𝐍𝐂𝐇𝐎𝐘𝐎𝐍 𝐁𝐀𝐑𝐔𝐀 𝐀𝐃𝐈𝐑𝐓𝐓𝐀      ║
{GREEN_46}║[🧡]{GREEN_46}𝐆𝐈𝐓𝐇𝐔𝐁   ║  ࿇⃝🌹⃢R🌹⃝࿇  {GREEN_46}║{GREEN_46}𝐀𝐃𝐈𝐑𝐓𝐓𝐀                       ║
{GREEN_46}║[💚]{GREEN_46}𝐀𝐆𝐄      ║  ࿇⃝🌹⃢T🌹⃝࿇  {GREEN_46}║{GREEN_46}𝐉𝐔𝐒𝐓 𝟏𝟔                       ║
{GREEN_46}║[💜]{GREEN_46}𝐅𝐑𝐎𝐌     ║  ࿇⃝🌹⃢T🌹⃝࿇  {GREEN_46}║{GREEN_46}𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇                    ║
{GREEN_46}╚═════════════╝  ࿇⃝🌹⃢A🌹⃝࿇{RESET}  {GREEN_46}╚══════════════════════════════╝
    """
    print(banner)

def loading_animation():
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]",
                 "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]",
                 "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        sys.stdout.write(f'\r{BLUE}Loading {animation[i]}{RESET}')
        sys.stdout.flush()
        time.sleep(0.4)  # Adjust the speed of the animation as needed

def generate_password():
    # Predefined list of passwords
    predefined_passwords = [
        "12345",
        "123456",
        "1234567",
        "12345678",
        "123456789",
        "1234567890",
        "0123456789"
    ]
    return random.choice(predefined_passwords)

def generate_data(num_entries, id_type):
    entries = []
    ok_count = 0  # Counter for successful IDs (OK)
    cp_count = 0  # Counter for failed IDs (CP)

    for loop in range(1, num_entries + 1):
        if id_type == '1':  # Old ID
            number = random.randint(100001000000000, 100001999999999)
        else:  # Random ID
            number = random.randint(200001000000000, 200001999999999)

        password = generate_password()
        entry = f"{number}|{password}"

        # Simulate 40-50% success (OK)
        if random.random() < 0.55:  # 45% chance of OK
            status = 'OK'
            ok_count += 1
            entries.append(entry)  # Save OK entries
        else:
            status = 'CP'
            cp_count += 1  # Increment CP counter

        # Show created ID and password with proper formatting for OK entries
        if status == 'OK':
            formatted_entry = f"{entry: <25} | Status: {status}"
            print(formatted_entry)

        # Show progress
        sys.stdout.write(f'\r {MINT}[ ᗷ.ᑕ.ᗩ. ] {loop}/{num_entries} • OK:{ok_count} • CP:{cp_count} | ')
        sys.stdout.flush()

        time.sleep(1)  # Wait for 1 second before generating the next entry

    return entries

def save_to_file(filename, data):
    # Check if the file already exists and remove it
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{GREEN_46}Existing file '{filename}' removed.{RESET}")

    with open(filename, 'w') as file:
        for entry in data:
            file.write(entry + '\n')

def get_user_choice():
    print(f"\n{GREEN_46}(1) Generate 900 𝙸𝙳'𝚜{RESET}")
    print(f"{GREEN_46}(2) Generate 500 𝙸𝙳'𝚜{RESET}")
    print(f"{GREEN_46}(3) Generate 200 𝙸𝙳'𝚜{RESET}")
    print(f"{BG_DARK_TURQUOISE}(4) Enter custom number of 𝙸𝙳'𝚜{RESET}")

    choice = input(f"\n{RED}Enter your choice (1-4): {RESET}")

    if choice == '1':
        return 900
    elif choice == '2':
        return 500
    elif choice == '3':
        return 200
    elif choice == '4':
        custom_choice = int(input(f"{YELLOW}Enter the number of entries to generate:{RESET} "))
        return custom_choice
    else:
        print(f"{GREEN_46}Invalid choice, defaulting to 10 entries.{RESET}")
        return 10

def get_id_choice():
    print(f"\n{GREEN_46}(1) Old ID{RESET}")
    print(f"{GREEN_46}(2) Random ID{RESET}")
    print(f"{BG_DARK_TURQUOISE}(3) My other tools{RESET}")  # New option for "My other tools"

    id_choice = input(f"{YELLOW}Choose ID type (1-3): {RESET}")

    if id_choice == '3':  # Open GitHub if "My other tools" is selected
        os.system('xdg-open https://github.com/ADIRTTA')
        sys.exit()  # Exit the script after opening the GitHub page

    if id_choice not in ['1', '2']:
        print(f"{GREEN_46}Invalid choice, defaulting to Random ID.{RESET}")
        return '2'  # Default to Random ID
    return id_choice

# Clear the screen
clear()

# Show the banner
show_banner()

# Show loading animation before getting the ID choice
loading_animation()

# Get user choice for ID type (Old ID, Random ID, or My other tools)
id_type = get_id_choice()

# Clear the screen again after ID choice
clear()

# Show the banner again after clearing the screen
show_banner()

# Show loading animation before getting the number of entries
loading_animation()

# Get user choice for the number of entries to generate
num_entries = get_user_choice()

# Show loading animation before generating data
loading_animation()

# Generate the chosen number of entries with the selected ID type
data = generate_data(num_entries, id_type)

# Save the data to a file in Termux
filename = 'ᗷ.ᑕ.ᗩ.txt'
save_to_file(filename, data)

print(f"{BRIGHT_YELLOW}\nData saved to {filename}{RESET}")
