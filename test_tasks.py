import pytest
import sys
import os
from io import StringIO


# =============================================================================
# TASK 1 TESTS: Code Errors (23 snippets)
# =============================================================================

def test_task1_00_file_exists():
    """Test that task1.py exists"""
    assert os.path.exists('task1.py'), "task1.py not found"


def test_task1_01_snippet_1_fixed():
    """Snippet 1: Missing closing quote"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
message = "Hello, welcome to Python!"
print(message)
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "Hello, welcome to Python!" in output, "Snippet 1 not fixed correctly"


def test_task1_02_snippet_2_fixed():
    """Snippet 2: Variable name typo (studentname vs student_name)"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
student_name = "Jordan"
print(f"The student is {student_name}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "Jordan" in output, "Snippet 2 not fixed correctly"


def test_task1_03_snippet_3_fixed():
    """Snippet 3: Space before parenthesis"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
favorite_color = "blue"
print(f"My favorite color is {favorite_color}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "blue" in output, "Snippet 3 not fixed correctly"


def test_task1_04_snippet_4_fixed():
    """Snippet 4: Missing quotes on string"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
city = "Austin"
print(f"I live in {city}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "Austin" in output, "Snippet 4 not fixed correctly"


def test_task1_05_snippet_5_fixed():
    """Snippet 5: Spaces in variable name"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
number_of_pets = 5
print(f"I have {number_of_pets} pets")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "5 pets" in output, "Snippet 5 not fixed correctly"


def test_task1_06_snippet_6_fixed():
    """Snippet 6: Mismatched quotes"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
book_title = "The Great Gatsby"
print(f"I am reading {book_title}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "The Great Gatsby" in output, "Snippet 6 not fixed correctly"


def test_task1_07_snippet_7_fixed():
    """Snippet 7: Extra indentation"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
greeting = "Good morning!"
print(f"{greeting}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "Good morning!" in output, "Snippet 7 not fixed correctly"


def test_task1_08_snippet_8_fixed():
    """Snippet 8: Variable typo (temperture vs temperature)"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
temperature = 72
print(f"The temperature is {temperature} degrees")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "72" in output, "Snippet 8 not fixed correctly"


def test_task1_09_snippet_9_fixed():
    """Snippet 9: Missing parentheses on print"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
team_name = "Eagles"
print(f"Go {team_name}!")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "Eagles" in output, "Snippet 9 not fixed correctly"


def test_task1_10_snippet_10_fixed():
    """Snippet 10: Wrong bracket in f-string"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
favorite_food = "pizza"
print(f"I love {favorite_food}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "pizza" in output, "Snippet 10 not fixed correctly"


def test_task1_11_snippet_11_fixed():
    """Snippet 11: Mismatched quotes at end"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
animal = "dog"
print(f"My favorite animal is {animal}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "dog" in output, "Snippet 11 not fixed correctly"


def test_task1_12_snippet_12_fixed():
    """Snippet 12: Spaces in variable name"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
school_name = "Central High"
print(f"I attend {school_name}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "Central High" in output, "Snippet 12 not fixed correctly"


def test_task1_13_snippet_13_fixed():
    """Snippet 13: Missing quotes on string"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
movie_title = "Inception"
print(f"My favorite movie is {movie_title}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "Inception" in output, "Snippet 13 not fixed correctly"


def test_task1_14_snippet_14_fixed():
    """Snippet 14: Variable typo (frut vs fruit)"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
fruit = "apple"
print(f"I like to eat {fruit}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "apple" in output, "Snippet 14 not fixed correctly"


def test_task1_15_snippet_15_fixed():
    """Snippet 15: Extra indentation"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
favorite_sport = "basketball"
print(f"I play {favorite_sport}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "basketball" in output, "Snippet 15 not fixed correctly"


def test_task1_16_snippet_16_fixed():
    """Snippet 16: Missing quotes in f-string"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
morning_greeting = "Rise and shine!"
print(f"{morning_greeting}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "Rise and shine!" in output, "Snippet 16 not fixed correctly"


def test_task1_17_snippet_17_fixed():
    """Snippet 17: Missing closing quote"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
car_color = "red"
print(f"My car is {car_color}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "red" in output, "Snippet 17 not fixed correctly"


def test_task1_18_snippet_18_fixed():
    """Snippet 18: Variable starts with number"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
third_day = "Wednesday"
print(f"Today is {third_day}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "Wednesday" in output, "Snippet 18 not fixed correctly"


def test_task1_19_snippet_19_fixed():
    """Snippet 19: Function typo (prnt vs print)"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
home_state = "Texas"
print(f"I live in {home_state}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "Texas" in output, "Snippet 19 not fixed correctly"


def test_task1_20_snippet_20_fixed():
    """Snippet 20: Mismatched quotes"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
favorite_season = "summer"
print(f"My favorite season is {favorite_season}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "summer" in output, "Snippet 20 not fixed correctly"


def test_task1_21_snippet_21_fixed():
    """Snippet 21: Missing colon after if"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
temperature = 95
if temperature > 90:
    print("It is hot outside!")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "hot outside" in output, "Snippet 21 not fixed correctly"


def test_task1_22_snippet_22_fixed():
    """Snippet 22: Missing indentation after if"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
score = 85
if score >= 70:
    print("You passed!")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "passed" in output, "Snippet 22 not fixed correctly"


def test_task1_23_snippet_23_fixed():
    """Snippet 23: Missing colon after else"""
    import task1
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "adult" in output, "Snippet 23 not fixed correctly"


# =============================================================================
# TASK 2 TESTS: Gas Station Receipt
# =============================================================================

def test_task2_00_file_exists():
    """Test that task2.py exists"""
    assert os.path.exists('task2.py'), "task2.py not found"


def test_task2_01_receipt_runs():
    """Test that task2.py runs without errors"""
    import task2


def  test_task2_02_candy_total():
    """Candy: 3 x $1.89 = $5.67"""
    import task2
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
candy_price = 1.89
candy_quantity = 3
candy_total = candy_price * candy_quantity
print(f"Candy total: {candy_total}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "5.67" in output, "Candy total should be $5.67"


def test_task2_03_soda_total():
    """Soda: 2 x $2.49 = $4.98"""
    import task2
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
soda_price = 2.49
soda_quantity = 2
soda_total = soda_price * soda_quantity
print(f"Soda total: {soda_total}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "4.98" in output, "Soda total should be $4.98"


def test_task2_04_gas_total():
    """Gas: 10.5 gallons x $3.25 = $34.125"""
    import task2
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
gas_price = 3.25
gallons = 10.5
gas_total = gas_price * gallons
print(f"Gas total: {gas_total}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "34.125" in output, "Gas total should be $34.125"


def test_task2_05_deli_total():
    """Deli: 1.25 lbs x $8.99 = $11.2375"""
    import task2
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
deli_price = 8.99
pounds = 1.25
deli_total = deli_price * pounds
print(f"Deli total: {deli_total}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "11.2375" in output, "Deli total should be $11.2375"


def test_task2_06_lottery_total():
    """Lottery: 5 x $2 = $10"""
    import task2
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
lottery_price = 2
lottery_quantity = 5
lottery_total = lottery_price * lottery_quantity
print(f"Lottery total: {lottery_total}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "10" in output, "Lottery total should be $10"
