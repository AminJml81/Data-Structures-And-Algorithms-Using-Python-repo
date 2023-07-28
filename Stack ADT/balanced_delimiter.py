from liststack import Stack


def check_delimiters(file=None, expression=None):
    """
    checking if the delimiters in the given file or expression are correct or not.

    for determining if the delimiters are valid two conditions must be satisfied.
    1) stack must be empty at the end of reading characters.
    2) each time it scans closing delimiter, it's corresponding opening delimiter must be the top of stack.

    parameters:
    -----------
               file: programming script file
               expression: mathematical expression in string format
    return True if they are correct and balanced, Otherwise it will return False.
    """
    try:
        if file:
            return check_file_delimiters(file)
        elif expression and type(expression) == str:

            return check_expression_delimiters(expression)
        return "Incorrect Input"

    except AssertionError:
        # this occurs when it pops from an empty stack.
        # actually when it sees closing delimiter first.
        return False


def check_file_delimiters(file):
    stack = Stack()
    with open(file, 'r') as fin:
        line = fin.readline()
        while line:
            for token in line:
                if token == '#':
                    # moving to the next line if the current line is comment.
                    break

                elif token in '({[':
                    # checking opening delimiter
                    stack.push(token)

                elif token in ')}]':
                    close_delimiter = token
                    open_delimiter = stack.pop()
                    if (open_delimiter == '(' and close_delimiter != ')')\
                        or (open_delimiter == '{' and close_delimiter != '}')\
                            or (open_delimiter == '[' and close_delimiter != ']'):
                        # if they don't match return False
                        return False

            # reading next line
            line = fin.readline()
    # stack must be empty at the end of scanning if the delimiters are balanced.
    return stack.is_empty()


def check_expression_delimiters(expression):
    """
    checking delimiters(parenthesis) of mathematical expression.
    parameters:
    -----------
                expression: string
                          mathematical expression
    returns True if the delimiters are balanced and false otherwise.
    """
    stack = Stack()
    for character in expression:
        if character in '(':
            # checking opening delimiter
            stack.push(character)
        elif character in ')':
            close_delimiter = character
            open_delimiter = stack.pop()
            if open_delimiter == '(' and close_delimiter != ')':
                # if they don't match return False
                return False
    # stack must be empty at the end of scanning if the delimiters are balanced.
    return stack.is_empty()

