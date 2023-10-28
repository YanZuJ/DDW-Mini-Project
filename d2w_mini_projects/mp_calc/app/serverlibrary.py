import re

#Each merge function has a byfunc parameter
def merge(array, p, q, r, byfunc=None):
    nleft = q - p + 1
    nright = r - q
    left_array = []
    right_array = []
    for idx in range(p,q+1):
        left_array.append(array[idx])
    for idx2 in range(q+1,r+1):
        right_array.append(array[idx2])
    left = 0
    right = 0
    dest = p
    while left < nleft and right < nright :
        # Implement byfunc function on elements in array if byfunc exists
        if (byfunc is None and left_array[left] <= right_array[right]) or (byfunc is not None and byfunc(left_array[left]) <= byfunc(right_array[right])):
            array[dest] = left_array[left]
            left += 1
        else:
            array[dest] = right_array[right]
            right += 1
        dest += 1
    while left < nleft:
        array[dest] = left_array[left]
        left += 1
        dest += 1
    while right < nright:
        array[dest] = right_array[right]
        right += 1
        dest += 1

def mergesort_recursive(array, p, r, byfunc=None):
    if r - p > 0:
        q = int((p + r)/2)
        mergesort_recursive(array, p, q, byfunc)
        mergesort_recursive(array, q+1, r, byfunc)
        merge(array, p, q, r, byfunc)

def mergesort(array, byfunc=None):
    p = 0
    r = len(array)-1
    mergesort_recursive(array,p,r,byfunc)

class Stack:
    def __init__(self):
        self.__items = [] #protected attribute
        
    def push(self, item):
        self.__items.append(item) #include self as this is under a method, points to object instance
 

    def pop(self):
        if len(self.__items) == 0:
            return None
        else:
            return self.__items.pop()


    def peek(self):
        if len(self.__items) == 0:
            return None
            
        else:
            return self.__items[-1]


    @property
    def is_empty(self):
        return len(self.__items) == 0 # alternatively, can use return self.__items == [] 


    @property
    def size(self):
        return len(self.__items)

class EvaluateExpression:
  valid_char = '0123456789+-*/() '
  def __init__(self, expr=""):
    self._expr = ""
    if self.is_valid_expression(expr):
      self.expression = expr

  @property
  def expression(self):
    return self._expr 

  @expression.setter
  def expression(self, new_expr):
    if self.is_valid_expression(new_expr):
      self._expr = new_expr 
    else:
      self._expr = ""

  def is_valid_expression(self, expr):
    return all([char in self.valid_char for char in expr])

  def insert_space(self):
    modified_expr = ""
    for char in self._expr:
      if char in "+-*/()":
        modified_expr += f" {char} "
      else:
        modified_expr += char
    return modified_expr

  def process_operator(self, operand_stack, operator_stack):
    if not operator_stack.is_empty and operator_stack.peek() in "+-*/":
      operator = operator_stack.pop()
      operand2 = operand_stack.pop()
      operand1 = operand_stack.pop()
      if operator == "*":
        result = operand1 * operand2
      elif operator == "/":
        result = operand1 // operand2  # integer division      
      elif operator == "+":
        result = operand1 + operand2
      elif operator == "-":
        result = operand1 - operand2
      operand_stack.push(result)

  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()
    for token in tokens:
        if token.isnumeric():
            operand_stack.push(int(token))
        elif token in "+-":
            if operator_stack.peek() == "*" or operator_stack.peek() == "/":
              self.process_operator(operand_stack, operator_stack)
            operator_stack.push(token)
        elif token in "*/":
            if operator_stack.peek() == "*" or operator_stack.peek() == "/":
              self.process_operator(operand_stack, operator_stack)
            operator_stack.push(token)
        elif token == "(":
            operator_stack.push(token)
        elif token == ")":
            if operator_stack.peek() == "*" or operator_stack.peek() == "/":
              self.process_operator(operand_stack, operator_stack)
            while operator_stack.peek() != "(":
                self.process_operator(operand_stack, operator_stack)
            operator_stack.pop()  # Pop the "("
    while not operator_stack.is_empty:
      self.process_operator(operand_stack, operator_stack)
    return operand_stack.pop()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





