from robot import Robot

rob = Robot()


for i in range(2):
    rob.GoRight()
    print(f"X POS: {list(rob.GetPosition())[0]}")
    print(f"Y POS: {list(rob.GetPosition())[1]}")
