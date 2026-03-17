import unittest
from .utils import *

PREFIX_DIR = "grade_func"

def change_prefix_dir(prefix):
    global PREFIX_DIR
    PREFIX_DIR = prefix

# Custom TestCase that accepts a function and input/output dynamically
class TestFunction(unittest.TestCase):
    
    def __init__(self, methodName, func, input_value, expected_value, test_index):
        super().__init__(methodName)
        self.func = func
        self.input_value = input_value
        self.expected_value = expected_value
        self.test_index = test_index

    # Test case method with a 1-second timeout
    def runTest(self):
        with self.subTest(i=self.test_index):
            self.assertEqual(self.func(*self.input_value), self.expected_value)

class ApproximationTest(unittest.TestCase):
    def __init__(self, methodName, func, input_value, expected_value, test_index, delta = 0.001):
        super().__init__(methodName)
        self.func = func
        self.input_value = input_value
        self.expected_value = expected_value
        self.test_index = test_index
        self.delta = delta

    # Test case method with a 1-second timeout
    def runTest(self):
        with self.subTest(i=self.test_index):
            self.assertAlmostEqual(self.func(*self.input_value), self.expected_value, delta=self.delta)


# Custom Test Runner with Grading Logic
def grade_tests(suite, max_grade=1.0):
    # Create a result object to track the test outcomes
    result = unittest.TestResult()
    
    # Run the tests
    suite.run(result)

    # Calculate the score based on number of passed test cases
    total_tests = result.testsRun
    passed_tests = total_tests - len(result.failures) - len(result.errors)
    
    # Grading from 0 to 1
    grade = passed_tests / total_tests if total_tests > 0 else 0 * max_grade
    
    # Print the result
    print(f"Total tests: {total_tests}")
    print(f"Passed tests: {passed_tests}")
    return grade * max_grade

# Example Usage
def question_1(func_to_test):
    suite = unittest.TestSuite()
    test_data = [(i, (func_to_test(i)//2)*2) for i in range(1, 10001)]  # Generate 10,000 test cases
    for i, (input_value, expected_value) in enumerate(test_data):
        # Add each test case to the suite
        suite.addTest(TestFunction('runTest', func_to_test, input_value, expected_value, i))
    return grade_tests(suite, 1.0)

def hw8_q4_1_1(func_to_test):
    suite = unittest.TestSuite()
    input_data = read_mixed_lists_from_file('grade_func/input/hw8_q4_1_1.txt')
    output_data = read_single_from_file('grade_func/output/hw8_q4_1_1.txt')
    
    assert len(input_data) == len(output_data), "Input and output data sizes do not match"
    
    test_data = [(*input_data[i], output_data[i]) for i in range(len(input_data))]
    
    for i, (input_value, expected_value) in enumerate(test_data):
        # Add each test case to the suite
        suite.addTest(TestFunction('runTest', func_to_test, input_value, expected_value, i))
    return grade_tests(suite, 0.4)

def test_func_from_file(func_to_test, input_file, output_file = None, output_type = 'single', max_grade=1.0, delta=0, plain_text_input=False, plain_text_output=False):
    suite = unittest.TestSuite()
    if output_file is None:
        if plain_text_input:
            input_data = read_plain_text_from_file(f"{PREFIX_DIR}/input/{input_file}")
        else:
            input_data = read_mixed_lists_from_file(f"{PREFIX_DIR}/input/{input_file}")
        
        if plain_text_output:
            output_data = read_plain_text_from_file(f"{PREFIX_DIR}/output/{input_file}")
        elif output_type == 'single':
            output_data = read_single_from_file(f"{PREFIX_DIR}/output/{input_file}")
        else:
            output_data = read_mixed_lists_from_file(f"{PREFIX_DIR}/output/{input_file}")
    else:
        if plain_text_input:
            input_data = read_mixed_lists_from_file(input_file)
        else:
            input_data = read_mixed_lists_from_file(input_file)
        
        if plain_text_output:
            output_data = read_plain_text_from_file(output_file)
        elif output_type == 'single':
            output_data = read_single_from_file(output_file)
        else:
            output_data = read_mixed_lists_from_file(output_file)
    
    
    assert len(input_data) == len(output_data), "Input and output data sizes do not match"
    
    test_data = [(input_data[i], output_data[i]) for i in range(len(input_data))]
    for i, (input_value, expected_value) in enumerate(test_data):
        # Add each test case to the suite
        if delta > 0:
            suite.addTest(ApproximationTest('runTest', func_to_test, input_value, expected_value, i, delta))
        else:
            suite.addTest(TestFunction('runTest', func_to_test, input_value, expected_value, i))
        
    return grade_tests(suite, max_grade)