from modules.stack import Stack

ops = Stack()

ord_of_precedence = {
    "^": 3,
    "*": 2,
    "/": 2,
    "+": 1,
    "-": 1
}

def convert(input):
    output = ""

    for element in input.replace(" ", ""):
        if element not in ord_of_precedence and element not in ("(", ")"):
            output += element
        elif element in ("(", ")"):
            if element == "(":
                ops.push(element)
            elif element == ")":
                while ops.peek() != "(":
                    output += ops.pop()
                ops.pop()
        elif element in ord_of_precedence:
            while ops.peek() in ord_of_precedence and ord_of_precedence[ops.peek()] >= ord_of_precedence[element]:
                output += ops.pop()
            ops.push(element)

    while ops.peek() != None:
        output += ops.pop()
        
    return output

result = convert("A*(B+C)/D")
print(result)