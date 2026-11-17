robot = {
    "name": "Atlas",
    "model": "RX-7",
    "battery": 85,
    "speed": 6,
    "mode": "exploration"
}

def get_user_input(prompt, data_type, max):
    if data_type == "string":
        return input(prompt)
    elif data_type == "int":
        try:
            output = int(input(prompt))
            if output <= max and output > 0:
                return output
            else:
                print(f"Please input an integer between 1 and {max}")
                return get_user_input(prompt, data_type, max)
        except ValueError:
            print("Please input integer and try again")
            return (get_user_input(prompt, data_type, max))

while True:
    print("What would you like to do to robot?")
    print("1: View all settings")
    print("2: Look up a setting")
    print("3: Change a setting")
    print("4: Add a setting")
    print("5: Exit")
    print()
    choice = get_user_input("Choice - ", "int", 5)

    if choice == 1:
        for key in robot:
            print(f"{key}: {robot[key]}")

    if choice == 2:
        setting = get_user_input("Setting to look up - ", "string", None)
        value = robot.get(setting)
        if value != None:
            print(f"{setting}: {value}")
        else:
            print("Robot does not contain this setting")

    if choice == 3:
        setting = get_user_input("Setting to change - ", "string", None)
        if setting in robot:
            value = get_user_input("Change setting to - ", "string", None)
            robot[setting] = value
        else:
            print(f"Robot does not contain setting {setting}")

    if choice == 4:
        setting = get_user_input("Setting to add - ", "string", None)
        value = get_user_input("Setting value - ", "string", None)
        robot[setting] = value

    if choice == 5:
        print("Exiting")
        break
        
