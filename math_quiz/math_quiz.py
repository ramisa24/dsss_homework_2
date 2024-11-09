import random

def generate_random_number(min_value, max_value):
    """
    Generate a random number between minimum value and maximum value
    """
    return random.randint(min_value, max_value)

def find_random_operator():
    """
    Randomly select a mathematical operator from +, -, /, % and *.
    """
    return random.choice(['+', '-', '/', '%', '*'])

def create_problem_and_solution(value_1, value_2, operator):
    """
    Create a math problem with 2 values including operator and calculate the expected answer.

    Parameters:
        value_1 (int): First number.
        value_2 (int): Second number.
        operator (str): Mathematical operator.

    Returns:
        tuple: A string representation of the problem and the accurate answer.
    """
    problem = f"{value_1} {operator} {value_2}"
    if operator == '+':
        accurate_answer = value_1 + value_2
    elif operator == '-':
        accurate_answer = value_1 - value_2
    else:
        accurate_answer = value_1 * value_2
    return problem, accurate_answer

def math_quiz():
    "Initiate random mathmatical queries and evaluating the users input"
    score = 0 
    total_questions = 3  # total number of mathmatical queries

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the accurate answers.")

    for _ in range(total_questions):
        value_1 = generate_random_number(1, 10)
        value_2 = generate_random_number(1, 5)  
        operator = find_random_operator()

        problem, accurate_answer = create_problem_and_solution(value_1, value_2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
            if user_answer == accurate_answer:
                print("accurate! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {accurate_answer}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
