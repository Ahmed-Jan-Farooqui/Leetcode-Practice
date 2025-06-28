'''
Valid Parentheses

You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.
'''


def validParens(string: str):
    stack = []
    symbols = {")": "(", "]": "[", "}": "{"}
    for char in string:
        # Check if key symbol
        if symbols.get(char):
            if len(stack) == 0:
                return False
            if stack[-1] != symbols[char]:
                return False
            else:
                stack.pop()
        else:
            stack.append(char)
    if len(stack) == 0:
        return True
    return False


'''
    Minimum Stack

    Design a stack class that supports the push, pop, top, and getMin operations.

        MinStack() initializes the stack object.
        void push(int val) pushes the element val onto the stack.
        void pop() removes the element on the top of the stack.
        int top() gets the top element of the stack.
        int getMin() retrieves the minimum element in the stack.

    Each function should run in O(1)O(1) time.
'''

'''
    Here, I keep track of the minimum value for each position. 
'''


class MinStack:

    def __init__(self):
        self.val_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.val_stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        elif self.min_stack[-1] > val:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.val_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.val_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


'''
    Evaluate Reverse Polish Notation

    You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

    Return the integer that represents the evaluation of the expression.

        The operands may be integers or the results of other operations.
        The operators include '+', '-', '*', and '/'.
        Assume that division between integers always truncates toward zero.

'''

'''
    Step through token list. Push each number on top of stack. If I encounter an operator, pop two
    numbers from the stack, and then evaluate the result. Push back onto stack. Continue until end of 
    list. Return top value of stack.
'''


def evalRPN(tokens: list[str]):
    import math
    stack = []
    operators = set(["*", "/", "+", "-"])
    for token in tokens:
        if token in operators:
            assert len(stack) >= 2
            operand_two = int(stack.pop())
            operand_one = int(stack.pop())
            result = 0
            if token == "*":
                result = operand_one * operand_two
            if token == "/":
                result = operand_one / operand_two
                if result > 0:
                    result = math.floor(result)
                else:
                    result = math.ceil(result)
            if token == "+":
                result = operand_one + operand_two
            if token == "-":
                result = operand_one - operand_two
            stack.append(result)
        else:
            stack.append(token)
    assert len(stack) == 1
    return int(stack[-1])


print(evalRPN(["18"]))


'''
Daily Temperatures

You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. 
If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.
'''

'''
    Iterate through list, appending the indices of the elements one by one.
    For each element, if the current element is > than the top, pop it and update the index value.
'''


def dailyTemps(temperatures: list[int]):
    stack = []
    final = [0 for idx in range(len(temperatures))]
    for idx in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[idx]:
            idx_to_modify = stack.pop()
            final[idx_to_modify] = idx - idx_to_modify
        stack.append(idx)
    return final


print(dailyTemps([1, 1, 1, 1, 1, 199]))


'''
    Car Fleet

    There are n cars traveling to the same destination on a one-lane highway.

    You are given two arrays of integers position and speed, both of length n.

        position[i] is the position of the ith car (in miles)
        speed[i] is the speed of the ith car (in miles per hour)

    The destination is at position target miles.

    A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

    A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

    If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

    Return the number of different car fleets that will arrive at the destination.
'''


def carFleets(target: int, position: list[int], speed: list[int]):
    '''
        Here, I will find out the following:
        1. If a given car will take less time to get to the destination than the fleet ahead of it,
            then it will become a part of the fleet ahead of it.
        2. If a given car will take more time to get to the destination than the fleet ahead of it, 
            then it will arrive after the fleet ahead of it already has. Therefore, it is another fleet.
    '''
    # Define pairs
    pairs = [(position[idx], speed[idx]) for idx in range(len(position))]
    speed_of_fleet_ahead_time = -1
    fleets = 0
    for pos, velo in sorted(pairs, reverse=True):
        dest_time = (target - pos) / velo
        # If you will reach destination after the fleet ahead of you, then you are another fleet.
        if speed_of_fleet_ahead_time < dest_time:
            fleets += 1
            speed_of_fleet_ahead_time = dest_time
    return fleets


print(carFleets(target=10,
                position=[0, 4, 2],
                speed=[2, 1, 3]))
