def arithmetic_arranger(problems, show_answers=False):
    # Initialize the formatted problem string
    formatted_problem = ''
    # Check if there are too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # List to store parsed problems
    arranged_problems = []
    
    # Iterate through each problem
    for problem in problems:
        # Split the problem based on operator
        if '+' in problem:
            num1, num2 = problem.split('+')
            operator = '+'
        elif '-' in problem:
            num1, num2 = problem.split('-')
            operator = '-'
        else:
            return "Error: Operator must be '+' or '-'."
        
        # Strip whitespace and check if numbers are digits
        num1 = num1.strip()
        num2 = num2.strip()
        if not (num1.isnumeric() and num2.isnumeric()):
            return "Error: Numbers must only contain digits."
        if len(num1)>4 or  len(num2)>4:
            return "Error: Numbers cannot be more than four digits."
        
        # Convert numbers to integers
        num1_int = int(num1)
        num2_int = int(num2)
        
        # Calculate the length of the longest number for formatting
        max_length = max(len(num1), len(num2)) + 2  # Add 2 for the operator and padding
        
        # Append formatted problem to the list
        arranged_problems.append({
            'num1': num1,
            'num2': num2,
            'operator': operator,
            'max_length': max_length
        })
    
    # Prepare the arranged strings for output
    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''
    
    for problem in arranged_problems:
        first_line += problem['num1'].rjust(problem['max_length']) + '    '
        second_line += problem['operator'] + ' ' + problem['num2'].rjust(problem['max_length'] - 2) + '    '
        third_line += '-' * problem['max_length'] + '    '
        if show_answers:
            if problem['operator'] == '+':
                answer = str(int(problem['num1']) + int(problem['num2']))
            elif problem['operator'] == '-':
                answer = str(int(problem['num1']) - int(problem['num2']))
            fourth_line += answer.rjust(problem['max_length']) + '    '
    
    # Combine all lines into the final formatted string
    formatted_problem = '\n'.join([first_line.rstrip(),
                                   second_line.rstrip(),
                                   third_line.rstrip()])
    
    if show_answers:
        formatted_problem += '\n' + fourth_line.rstrip()
    
    return formatted_problem

# Example usage:
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))