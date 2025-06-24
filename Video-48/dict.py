# Python Dictionaries - Complete Examples
# =====================================

print("🐍 Python Dictionaries Examples")
print("=" * 40)

# 1. CREATING DICTIONARIES
print("\n1. Creating Dictionaries:")
print("-" * 25)

# Empty dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")

# Dictionary with initial values
student = {
    "name": "Alice Johnson",
    "age": 22,
    "grade": "A",
    "subjects": ["Math", "Physics", "Chemistry"],
    "gpa": 3.8,
    "is_graduated": False
}
print(f"Student info: {student}")

# Using dict() constructor
person = dict(
    name="Bob Smith",
    age=25,
    city="New York",
    occupation="Software Engineer"
)
print(f"Person info: {person}")

# From list of tuples
items = [("brand", "Apple"), ("model", "iPhone"), ("year", 2024)]
phone = dict(items)
print(f"Phone info: {phone}")

# 2. ACCESSING DICTIONARY ELEMENTS
print("\n2. Accessing Elements:")
print("-" * 22)

# Using square brackets
print(f"Student name: {student['name']}")
print(f"First subject: {student['subjects'][0]}")

# Using get() method (safer)
print(f"Student age: {student.get('age')}")
print(f"Student phone: {student.get('phone', 'Not available')}")

# Check if key exists
if 'grade' in student:
    print(f"Student grade: {student['grade']}")

# 3. MODIFYING DICTIONARIES
print("\n3. Modifying Dictionaries:")
print("-" * 26)

# Adding new items
student["email"] = "alice@university.edu"
student["phone"] = "+1-555-0123"

# Updating existing items
student["age"] = 23
student["subjects"].append("Biology")

print(f"Updated student: {student}")

# Using update() method
additional_info = {"scholarship": True, "year": "Senior"}
student.update(additional_info)
print(f"After update(): {student}")

# 4. REMOVING ITEMS
print("\n4. Removing Items:")
print("-" * 18)

sample_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
print(f"Original: {sample_dict}")

# Using del
del sample_dict["a"]
print(f"After del: {sample_dict}")

# Using pop() - returns the value
removed_value = sample_dict.pop("b")
print(f"Removed value: {removed_value}, Dict: {sample_dict}")

# Using popitem() - removes last item
last_item = sample_dict.popitem()
print(f"Last item removed: {last_item}, Dict: {sample_dict}")

# 5. DICTIONARY METHODS
print("\n5. Dictionary Methods:")
print("-" * 21)

colors = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF", "yellow": "#FFFF00"}

print(f"Keys: {list(colors.keys())}")
print(f"Values: {list(colors.values())}")
print(f"Items: {list(colors.items())}")

# Copy dictionary
colors_copy = colors.copy()
print(f"Copy: {colors_copy}")

# 6. ITERATING THROUGH DICTIONARIES
print("\n6. Iterating Through Dictionaries:")
print("-" * 33)

grades = {"Math": 95, "Physics": 88, "Chemistry": 92, "Biology": 89}

print("Iterating through keys:")
for subject in grades:
    print(f"  {subject}")

print("\nIterating through values:")
for score in grades.values():
    print(f"  {score}")

print("\nIterating through key-value pairs:")
for subject, score in grades.items():
    print(f"  {subject}: {score}")

# 7. DICTIONARY COMPREHENSIONS
print("\n7. Dictionary Comprehensions:")
print("-" * 27)

# Square numbers
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print(f"Even squares: {even_squares}")

# String manipulation
words = ["hello", "world", "python", "dictionaries"]
word_lengths = {word: len(word) for word in words}
print(f"Word lengths: {word_lengths}")

# Temperature conversion
celsius_temps = {"morning": 20, "afternoon": 25, "evening": 18}
fahrenheit_temps = {time: (temp * 9/5) + 32 for time, temp in celsius_temps.items()}
print(f"Fahrenheit temperatures: {fahrenheit_temps}")

# 8. NESTED DICTIONARIES
print("\n8. Nested Dictionaries:")
print("-" * 23)

company = {
    "employees": {
        "emp001": {
            "name": "Alice Johnson",
            "position": "Software Engineer",
            "salary": 75000,
            "skills": ["Python", "JavaScript", "SQL"],
            "department": "Engineering"
        },
        "emp002": {
            "name": "Bob Smith",
            "position": "Data Scientist",
            "salary": 80000,
            "skills": ["Python", "R", "Machine Learning"],
            "department": "Analytics"
        },
        "emp003": {
            "name": "Carol Davis",
            "position": "Product Manager",
            "salary": 85000,
            "skills": ["Strategy", "Communication", "Analytics"],
            "department": "Product"
        }
    },
    "company_info": {
        "name": "Tech Solutions Inc.",
        "founded": 2010,
        "location": "San Francisco",
        "employees_count": 150
    }
}

# Accessing nested data
print(f"Employee name: {company['employees']['emp001']['name']}")
print(f"Company name: {company['company_info']['name']}")
print(f"Alice's skills: {company['employees']['emp001']['skills']}")

# 9. PRACTICAL EXAMPLES
print("\n9. Practical Examples:")
print("-" * 22)

# Example 1: Word Frequency Counter
def count_words(text):
    """Count the frequency of each word in a text."""
    words = text.lower().split()
    word_count = {}
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

text = "python is great python is powerful python is versatile and python is fun"
word_frequency = count_words(text)
print(f"Word frequency: {word_frequency}")

# Example 2: Student Grade Manager
class GradeManager:
    def __init__(self):
        self.students = {}
    
    def add_student(self, name, grades):
        self.students[name] = grades
    
    def get_average(self, name):
        if name in self.students:
            grades = self.students[name]
            return sum(grades) / len(grades)
        return None
    
    def get_top_student(self):
        if not self.students:
            return None
        
        top_student = max(self.students.items(), 
                         key=lambda x: sum(x[1]) / len(x[1]))
        return top_student[0]
    
    def get_class_average(self):
        if not self.students:
            return None
        
        all_grades = []
        for grades in self.students.values():
            all_grades.extend(grades)
        
        return sum(all_grades) / len(all_grades)

# Using the GradeManager
print("\nGrade Manager Example:")
gm = GradeManager()
gm.add_student("Alice", [85, 92, 78, 96, 88])
gm.add_student("Bob", [76, 88, 92, 85, 90])
gm.add_student("Carol", [95, 89, 94, 91, 93])

print(f"Alice's average: {gm.get_average('Alice'):.2f}")
print(f"Top student: {gm.get_top_student()}")
print(f"Class average: {gm.get_class_average():.2f}")

# Example 3: Inventory Management
inventory = {
    "laptops": {"quantity": 50, "price": 999.99, "category": "Electronics"},
    "keyboards": {"quantity": 120, "price": 79.99, "category": "Accessories"},
    "mice": {"quantity": 200, "price": 29.99, "category": "Accessories"},
    "monitors": {"quantity": 30, "price": 299.99, "category": "Electronics"}
}

print("\nInventory Management:")
print(f"Total items: {len(inventory)}")

# Calculate total inventory value
total_value = sum(item["quantity"] * item["price"] for item in inventory.values())
print(f"Total inventory value: ${total_value:,.2f}")

# Find items with low stock (less than 50)
low_stock = {item: details for item, details in inventory.items() 
             if details["quantity"] < 50}
print(f"Low stock items: {list(low_stock.keys())}")

# Example 4: Contact Book
contacts = {
    "alice": {
        "phone": "+1-555-0123",
        "email": "alice@email.com",
        "address": "123 Main St, Boston, MA"
    },
    "bob": {
        "phone": "+1-555-0456",
        "email": "bob@email.com", 
        "address": "456 Oak Ave, New York, NY"
    }
}

def add_contact(name, phone, email, address=""):
    contacts[name.lower()] = {
        "phone": phone,
        "email": email,
        "address": address
    }

def find_contact(name):
    return contacts.get(name.lower(), "Contact not found")

print("\nContact Book Example:")
add_contact("Carol", "+1-555-0789", "carol@email.com", "789 Pine St, Chicago, IL")
print(f"Carol's info: {find_contact('carol')}")

# 10. ADVANCED DICTIONARY OPERATIONS
print("\n10. Advanced Operations:")
print("-" * 24)

# Merging dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2  # Union operator
print(f"Merged dictionaries: {merged}")

# Alternative merging methods
merged_alt = {**dict1, **dict2}  # Unpacking
print(f"Merged (unpacking): {merged_alt}")

# Dictionary with default values using get()
settings = {"theme": "dark", "language": "en"}
theme = settings.get("theme", "light")
font_size = settings.get("font_size", 14)
print(f"Theme: {theme}, Font size: {font_size}")

# Sorting dictionary by keys or values
scores = {"Alice": 95, "Bob": 87, "Carol": 92, "David": 88}

# Sort by keys
sorted_by_keys = dict(sorted(scores.items()))
print(f"Sorted by keys: {sorted_by_keys}")

# Sort by values
sorted_by_values = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print(f"Sorted by values: {sorted_by_values}")

# Filter dictionary
high_scores = {name: score for name, score in scores.items() if score >= 90}
print(f"High scores (>=90): {high_scores}")

print("\n" + "=" * 40)
print("🎉 Dictionary examples completed!")
