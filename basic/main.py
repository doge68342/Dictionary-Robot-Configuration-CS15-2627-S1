robot = {
    "name": "Atlas",
    "model": "RX-7",
    "battery": 85,
    "speed": 6,
    "mode": "exploration"
}

print(f"Name: {robot["name"]}")
print(f"Model: {robot["model"]}")
robot["battery"] = 100
robot["color"] = "red"
robot.pop("mode")
print(f"{len(robot)} key value pairs in robot")

for key in robot:
    print(f"{key}: {robot[key]}")