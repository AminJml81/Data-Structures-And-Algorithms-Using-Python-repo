from liststack import Stack


def convert_infix_to_postfix(expression):
    """
    converts given infix expression to it postfix form
    Algorithm Description:
                      preconditions are
                            a stack for holding operators and
                            a given infix expression and
                            an empty postfix expression at the beginning of the scanning.
                            operands single digit or single character
                      1) scan the the expression character by character.
                      1-1) if the current character is an operand add it to to postfix expression.
                      # Note : if the operands are numbers, it must scan further characters
                               until it reaches a whitespace or an operator.(checking for multi digit numbers )
                      1-2) if the current character is an operator:
                                1-2-1) if the stack is empty push the operator to the stack.
                                1-2-2) if the precedence of the scanned operator is higher than the
                                       stack peek operator : push the operator to the stack.
                                1-2-3) if the precedence of the operator is equal to the stack peek
                                          pop the operator(s)
                                          until: the precedence of the stack peek is lower than the scanned
                                          operator
                                       then push the scanned operator to the stack.
                                1-2-4) if the precedence of the operator is lower than the stack peek operator
                                       pop the stack and add it to the postfix expression
                                       until: the precedence of the stack peek is lower than the scanned operator
                                       then push the scanned operator to the stack.
                                1-2-5) if the scanned character is '(', push it to the stack.
                                1-2-6) if the scanned character is ')', pop the stack and add the operator(s)
                                          to the postfix expression
                                          until: the stack peek is '('
                                          # Note: there shouldn't be any parenthesis in the postfix expression.
                      1-3) if all the characters of the given expression were scanned and the stack is not empty
                              pop the element(s) from the stack and add to postfix expression.
                              until : the stack is empty

    parameters:
    -----------
               expression: infix expression
    returns it's equivalence postfix expression.
    """
    assert expression is not None, 'expression parameter is not provided'
    stack = Stack()
    postfix_expression = ''
    operators = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }
    index, max_index = 0, len(expression)
    while index < max_index:
        current_character = expression[index]
        # operands are variables
        if current_character == ' ':
            index += 1
            continue

        if current_character == '(':
            stack.push(current_character)
            index += 1
            continue

        if current_character == ')':
            # 1-2-6
            while stack.peek() != '(':
                postfix_expression += stack.pop()

            stack.pop()
            # popping '(' from the stack
            index += 1
            continue

        if current_character not in operators:
            # 1-1 (scanned character is operand)
            postfix_expression += current_character
            index += 1
            continue

        else:
            current_operator_precedence = operators[current_character]
            while True:
                if stack.is_empty():
                    # 1-2-1
                    stack.push(current_character)
                    index += 1
                    break

                stack_operator_precedence = operators[stack.peek()]

                if current_operator_precedence > stack_operator_precedence:
                    # 1-2-2
                    stack.push(current_character)
                    index += 1
                    break

                elif current_operator_precedence == stack_operator_precedence:
                    if current_operator_precedence == 3:
                        # 1-2-3-1
                        stack.push(current_character)
                        index += 1
                        break
                    else:
                        # 1-2-3-2
                        postfix_expression += stack.pop()

                elif current_operator_precedence < stack_operator_precedence:
                    # 1-2-4
                    postfix_expression += stack.pop()

    while not stack.is_empty():
        postfix_expression += stack.pop()

    return postfix_expression


def evaluate_postfix(postfix_expression, operands_values):
    """
    calculates the operations of the given expression.
    Algorithm description:
                         1) scans the expression character by character.
                         2) if the character is an operand, push it's value to the stack.
                         3) if the character is an operator:
                         3-1) pop two operands from the stack
                         3-2) do the operation
                              Note: the top most element is the second operator and
                                    the previous one is the first operator
                         3-3) push the result into the stack

    parameters:
    ----------
    postfix_expression: string
                       postfix string
    operand_values: dictionary
                    a dictionary contains operands and their values.
    returns results of the expression
    """

    index, max_index = 0, len(postfix_expression)
    stack = Stack()
    operators = ['+', '-', '*', '/']
    while index < max_index:
        current_character = postfix_expression[index]
        if current_character in operands_values:
            # 2
            stack.push(current_character)
        elif current_character in operators:
            second_operand = stack.pop()
            first_operand = stack.pop()
            try:
                second_operand = operands_values[second_operand]
            except KeyError:
                second_operand = int(second_operand)
            try:
                first_operand = operands_values[first_operand]
            except KeyError:
                first_operand = int(first_operand)
            # if the operand was calculated from previous operations, it will not be in the dictionary
            # so if it tries to get it's value exception occurs.
            math_expression = f'{first_operand} {current_character} {second_operand}'
            result = eval(math_expression)
            stack.push(result)

        index += 1
    calculated_result = int(stack.pop())
    if stack.is_empty():
        # there should be just one item which is the total result otherwise the expression was incorrect.
        return calculated_result
    return 'Invalid postfix expression'


if __name__ == '__main__':
    postfix1 = convert_infix_to_postfix('A * B + C')
    print(postfix1)
    try:
        result1 = evaluate_postfix(postfix1, {'A': 8, 'B': 2, 'C': 3, 'D': 4})
        print(result1)
    except AssertionError:
        print('Invalid prefix expression')