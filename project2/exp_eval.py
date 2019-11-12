""" Contains expression evaluation implementation functions
Name: Sullivan Xiong
CPE202 Section 03
Spring 2019
"""


class StackArray:
    """ A stack data structure implemented with the built in list data type.

    Attributes:
        capacity(int): The size limiter of the stack.
        items(list): A list containing the data of the items and None.
        num_items(int): The number of items in the stack.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.num_items = 0

    def __repr__(self):
        return "StackArray({}, {}, {})".format(self.capacity, self.items, self.num_items)

    def __eq__(self, other):
        return (isinstance(self, StackArray) ==
                isinstance(other, StackArray) and
                self.capacity == other.capacity and
                self.items == other.items and
                self.num_items == other.num_items)

    def is_empty(self):
        """ Checks if the stack is empty.
        Returns:
            boolean: True if the stack is empty, else false.
        """
        return self.num_items == 0

    def is_full(self):
        """ Checks if the stack is full.
        Returns:
            boolean: True if the stack is full, else false.
        """
        return self.num_items == self.capacity

    def push(self, item):
        """ Add an item to the stack. If the stack is full return Error.
        Args:
            item(Any): The data that is going to be pushed to the stack
        Returns:
            None: Does not return anything
        """
        if self.is_full():
            raise IndexError
        self.items[self.num_items] = item
        self.num_items += 1

    def pop(self):
        """ Removes an item from the top of the stack. If the stack is empty
        return None.
        Returns:
            Any: The data that was removed from the top of the stack.
        """
        if self.is_empty():
            raise IndexError
        item = self.items[self.num_items-1]
        self.items[self.num_items-1] = None
        self.num_items -= 1
        return item

    def peek(self):
        """ The item at the top of the Stack.
        Returns:
            *: The data at the top of the Stack.
        """
        return self.items[self.num_items-1]

    def size(self):
        """ The size of the StackArray.
        Returns:
            int: Number of items in the Stack.
        """
        return self.num_items


def infix_to_postfix(infix_expr):
    """ Translate an infix expression into a postfix expression.
    Args:
        infix_expr(str): A string representing our infix expression, separated
                         by a blank space for operands and operators.
    Returns:
        str: The postfix expression version of the string.
    """
    infix_expr = infix_expr.split()
    postfix_expr = ""
    operator_stack = StackArray(30)
    for i in range(len(infix_expr)):
        try:
            float(infix_expr[i])
            postfix_expr += infix_expr[i] + " "
            if operator_stack.peek() == "^"\
                and i+1 < len(infix_expr)\
                and infix_expr[i+1] != "^":
                postfix_expr += operator_stack.pop() + " "
                while operator_stack.peek() == "^":
                    postfix_expr += operator_stack.pop() + " "
        except ValueError:
            if operator_stack.is_empty():
                operator_stack.push(infix_expr[i])
            elif infix_expr[i] == "(":
                operator_stack.push(infix_expr[i])
            elif infix_expr[i] == ")":
                while operator_stack.peek() != "(":
                    postfix_expr += operator_stack.pop() + " "
                operator_stack.pop()
            elif infix_expr[i] in ["+", "-"]:
                if operator_stack.peek() in ["+", "-", "("]:
                    operator_stack.push(infix_expr[i])
                else:
                    while not operator_stack.is_empty() and operator_stack.peek() != "(":
                        postfix_expr += operator_stack.pop() + " "
                    operator_stack.push(infix_expr[i])
            elif infix_expr[i] in ["*", "/"]:
                if operator_stack.peek() in ["+", "-", "*", "/", "("]:
                    operator_stack.push(infix_expr[i])
                else:
                    while not operator_stack.is_empty() and operator_stack.peek() != "(":
                        postfix_expr += operator_stack.pop() + " "
                    operator_stack.push(infix_expr[i])
            elif infix_expr[i] in ["^", "~"]:
                operator_stack.push(infix_expr[i])
    while not operator_stack.is_empty():
        postfix_expr += operator_stack.pop() + " "
    return postfix_expr[:len(postfix_expr) - 1]

def postfix_eval(postfix_expr):
    """ Evaluates a postfix expression and returns the resulting value.
    Args:
        postfix_expr(str): The postfix expression to be computed.
    Returns:
        int: The resulting value from the expression.
    """
    operand_stack = StackArray(30)
    if not postfix_valid(postfix_expr):
        raise SyntaxError
    postfix_expr = postfix_expr.split()
    for i in postfix_expr:
        try:
            float(i)
            operand_stack.push(i)
        except ValueError:
            if i in ["+", "-", "*", "/", "^"]:
                operand1 = operand_stack.pop()
                operand2 = operand_stack.pop()
                operand_stack.push(str(operate(operand1, operand2, i)))
            elif i == "~":
                curr = operand_stack.pop()
                if curr[0] == "-":
                    curr = curr[1:]
                else:
                    curr = "-" + curr
                operand_stack.push(curr)
    return float(operand_stack.pop())

def operate(op1, op2, operator):
    """ Performs a math operation and returns the result.
    Args:
        op1(string): String containing the first operand.
        op2(string): String containing the second operand.
        operator(string): String containing the operator.
    Returns:
        int: The resulting value, could be a float if division was performed.
    """
    if operator == "+":
        return float(op2) + float(op1)
    elif operator == "-":
        return float(op2) - float(op1)
    elif operator == "*":
        return float(op2) * float(op1)
    elif operator == "/":
        try:
            return float(op2) / float(op1)
        except ZeroDivisionError:
            raise ZeroDivisionError
    elif operator == "^":
        return float(op2) ** float(op1)

def postfix_valid(postfix_expr):
    """ Checks to see if the postfix expression is a balanced expression where
    if we have n operands then we will have n - 1 operators.
    Args:
        postfix_expr(str): The postfix expression.
    Returns:
        boolean: True if the expression is valid, else False if invalid.
    """
    postfix_expr = postfix_expr.split()
    expr_stack = StackArray(30)
    operand = 0
    operator = 0
    for i in postfix_expr:
        try:
            int(i)
            expr_stack.push(i)
            operand += 1
        except ValueError:
            if i in ["+", "-", "*", "/", "^"]:
                operator += 1
                if expr_stack.size() >= 2:
                    expr_stack.pop()
                    expr_stack.pop()
                    expr_stack.push('1')
                else:
                    return False
            elif i == "~":
                continue
            else:
                return False
    return operand == operator + 1 and expr_stack.size() == 1
