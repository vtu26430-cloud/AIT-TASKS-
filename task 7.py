# Robot Traversal to Fetch a Tool
# Warehouse / Workshop simulation using AI planni

class Robot:
    def __init__(self, location):
        self.location = location
        self.on_ladder = False
        self.has_tool = False

class Ladder:
    def __init__(self, location):
        self.location = location

class Tool:
    def __init__(self, location):
        self.location = location

# Actions
def move(robot, target_location):
    print(f"Robot moves from {robot.location} to {target_location}")
    robot.location = target_location

def push_ladder(robot, ladder, target_location):
    if robot.location != ladder.location:
        print("Robot cannot push ladder: not at ladder location")
        return
    print(f"Robot pushes ladder from {ladder.location} to {target_location}")
    ladder.location = target_location
    robot.location = target_location  # Robot moves with ladder

def climb_ladder(robot, ladder):
    if robot.location != ladder.location:
        print("Robot cannot climb ladder: not at ladder location")
        return
    print("Robot climbs ladder")
    robot.on_ladder = True

def descend_ladder(robot):
    if not robot.on_ladder:
        print("Robot is not on ladder")
        return
    print("Robot descends ladder")
    robot.on_ladder = False

def pick_tool(robot, ladder, tool):
    if robot.location == ladder.location == tool.location and robot.on_ladder:
        print("Robot picks up the tool")
        robot.has_tool = True
    else:
        print("Robot cannot pick tool: conditions not met")

# Planning sequence
def fetch_tool_plan():
    # Initialize objects
    robot = Robot(location='A')
    ladder = Ladder(location='B')
    tool = Tool(location='C')

    print("\n--- Initial State ---")
    print(f"Robot at {robot.location}, Ladder at {ladder.location}, Tool at {tool.location}")
    print(f"Robot on ladder? {robot.on_ladder}, Robot has tool? {robot.has_tool}\n")

    # Step 1: Move to ladder
    move(robot, ladder.location)

    
    push_ladder(robot, ladder, tool.location)

    
    climb_ladder(robot, ladder)


    pick_tool(robot, ladder, tool)

    
    descend_ladder(robot)

    print("\n--- Final State ---")
    print(f"Robot at {robot.location}, Ladder at {ladder.location}, Tool at {tool.location}")
    print(f"Robot on ladder? {robot.on_ladder}, Robot has tool? {robot.has_tool}")

    return robot.has_tool

# Run the plan
if __name__ == "__main__":
    goal_achieved = fetch_tool_plan()
    print("\nGoal achieved:", goal_achieved)
