import sqlite3

# Connect to the database
conn = sqlite3.connect('database.sql.db')
c = conn.cursor()

# Create tables for each category
c.execute('''CREATE TABLE IF NOT EXISTS geography
             (id INTEGER PRIMARY KEY, question TEXT, choice1 TEXT, choice2 TEXT, choice3 TEXT, choice4 TEXT, answer TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS history
             (id INTEGER PRIMARY KEY, question TEXT, choice1 TEXT, choice2 TEXT, choice3 TEXT, choice4 TEXT, answer TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS accounting
             (id INTEGER PRIMARY KEY, question TEXT, choice1 TEXT, choice2 TEXT, choice3 TEXT, choice4 TEXT, answer TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS math
             (id INTEGER PRIMARY KEY, question TEXT, choice1 TEXT, choice2 TEXT, choice3 TEXT, choice4 TEXT, answer TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS programming
             (id INTEGER PRIMARY KEY, question TEXT, choice1 TEXT, choice2 TEXT, choice3 TEXT, choice4 TEXT, answer TEXT)''')

# Insert 10 questions for geography
geography_questions = [
    ("What is the capital of France?", "London", "Berlin", "Paris", "Rome", "Paris"),
    ("Which is the largest desert in the world?", "Sahara", "Gobi", "Arabian", "Kalahari", "Sahara"),
    ("Which river passes through the city of Cairo?", "Amazon", "Nile", "Danube", "Yangtze", "Nile"),
    ("In which country is the Great Barrier Reef located?", "Brazil", "India", "Canada", "Australia", "Australia"),
    ("What is the highest mountain in Africa?", "Kilimanjaro", "Everest", "K2", "Aconcagua", "Kilimanjaro"),
    ("Which is the smallest continent by land area?", "Australia", "Europe", "Africa", "Asia", "Australia"),
    ("Which country is known as the Land of the Rising Sun?", "China", "India", "Japan", "Korea", "Japan"),
    ("What is the longest river in South America?", "Nile", "Mississippi", "Yangtze", "Amazon", "Amazon"),
    ("Which city is known as the City of Love?", "Venice", "Paris", "Rome", "Barcelona", "Paris"),
    ("Which country has the most islands in the world?", "Sweden", "Indonesia", "Australia", "Philippines", "Sweden")
]

for i, question in enumerate(geography_questions):
    c.execute("INSERT INTO geography (id, question, choice1, choice2, choice3, choice4, answer) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (i+1, question[0], question[1], question[2], question[3], question[4], question[5]))

# Insert 10 questions for history
history_questions = [
    ("In which year did World War I begin?", "1918", "1914", "1939", "1945", "1914"),
    ("Who was the first President of the United States?", "Thomas Jefferson", "John Adams", "George Washington", "James Madison", "George Washington"),
    ("Who painted the Mona Lisa?", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", "Michelangelo", "Leonardo da Vinci"),
    ("Which ancient wonder was located in Alexandria, Egypt?", "Pharos Lighthouse", "Great Pyramid of Giza", "Hanging Gardens of Babylon", "Colossus of Rhodes", "Pharos Lighthouse"),
    ("Who was the first female Prime Minister of the United Kingdom?", "Margaret Thatcher", "Theresa May", "Indira Gandhi", "Angela Merkel", "Margaret Thatcher"),
    ("Which war was known as the 'Great War for Civilization'?", "World War II", "Vietnam War", "Korean War", "World War I", "World War I"),
    ("Which country was the first to reach the moon?", "United States", "Russia", "China", "India", "United States"),
    ("Who wrote the play 'Romeo and Juliet'?", "George Bernard Shaw", "Arthur Miller", "William Shakespeare", "Samuel Beckett", "William Shakespeare"),
    ("Which city was the capital of the Roman Empire?", "Athens", "Alexandria", "Constantinople", "Rome", "Rome"),
    ("Who was the first emperor of unified China?", "Han Wudi", "Qin Shi Huang", "Genghis Khan", "Mao Zedong", "Qin Shi Huang")
]
for i, question in enumerate(history_questions):
    c.execute("INSERT INTO history (id, question, choice1, choice2, choice3, choice4, answer) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (i+1, question[0], question[1], question[2], question[3], question[4], question[5]))

accounting_questions = [
    ("What is the accounting equation?", "Assets + Liabilities = Equity", "Equity = Assets - Liabilities", "Assets = Liabilities + Equity", "Equity = Assets + Liabilities", "Assets = Liabilities + Equity"),
    ("What is depreciation?", "A decrease in the value of an asset over time", "An increase in the value of an asset over time", "The cost of an asset", "The residual value of an asset", "A decrease in the value of an asset over time"),
    ("What is the purpose of a balance sheet?", "To show the revenue and expenses of a company over a period of time", "To show the cash flows of a company over a period of time", "To show the financial position of a company at a specific point in time", "To show the profitability of a company over a period of time", "To show the financial position of a company at a specific point in time"),
    ("What is an income statement?", "A financial statement that shows the revenue and expenses of a company over a period of time", "A financial statement that shows the financial position of a company at a specific point in time", "A financial statement that shows the cash flows of a company over a period of time", "A financial statement that shows the profitability of a company over a period of time", "A financial statement that shows the revenue and expenses of a company over a period of time"),
    ("What is the purpose of a trial balance?", "To ensure that debits equal credits in the accounting records", "To show the financial position of a company at a specific point in time", "To show the revenue and expenses of a company over a period of time", "To show the cash flows of a company over a period of time", "To ensure that debits equal credits in the accounting records"),
    ("What is the accounting cycle?", "The process of preparing financial statements", "The process of recording, summarizing, and analyzing financial transactions", "The process of analyzing financial statements", "The process of auditing financial statements", "The process of recording, summarizing, and analyzing financial transactions"),
    ("What is the difference between cash basis and accrual basis accounting?", "Cash basis recognizes revenue and expenses when cash is received or paid, while accrual basis recognizes revenue and expenses when they are earned or incurred", "Cash basis recognizes revenue and expenses when they are earned or incurred, while accrual basis recognizes revenue and expenses when cash is received or paid", "Cash basis is used by small businesses, while accrual basis is used by large businesses", "Cash basis is more accurate than accrual basis", "Cash basis recognizes revenue and expenses when cash is received or paid, while accrual basis recognizes revenue and expenses when they are earned or incurred"),
    ("What is a journal entry?", "A list of all accounts used by a company", "A summary of all financial transactions of a company", "The recording of a financial transaction in a journal", "The financial statement that shows the financial position of a company at a specific point in time", "The recording of a financial transaction in a journal"),
    ("What is the difference between an asset and a liability?", "An asset is something of value owned by a company, while a liability is a company's obligations or debts", "An asset is a company's obligations or debts, while a liability is something of value owned by a company", "An asset is a company's revenue, while a liability is a company's expenses", "An asset is a company's expenses, while a liability is a company's revenue", "An asset is something of value owned by a company, while a liability is a company's obligations or debts"),
    ("What is the purpose of an audit?", "To ensure that financial statements are accurate and comply with laws and regulations", "To prepare financial statements for a company", "To analyze financial statements", "To summarize financial transactions of a company", "To ensure that financial statements are accurate and comply with laws and regulations")
]

for i, question in enumerate(accounting_questions):
    c.execute("INSERT INTO accounting (id, question, choice1, choice2, choice3, choice4, answer) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (i+1, question[0], question[1], question[2], question[3], question[4], question[5]))

# Insert 10 questions for math
math_questions = [
    ("What is the value of pi (π)?", "3.142", "3.14", "3.141", "3.14159", "3.14159"),
    ("What is the square root of 64?", "6", "4", "8", "10", "8"),
    ("What is the area of a circle with radius 5 units?", "31.42 square units", "25 square units", "15.7 square units", "78.54 square units", "78.54 square units"),
    ("What is the sum of angles in a triangle?", "180 degrees", "90 degrees", "270 degrees", "360 degrees", "180 degrees"),
    ("What is the volume of a cube with side length 3 units?", "9 cubic units", "27 cubic units", "6 cubic units", "3 cubic units", "27 cubic units"),
    ("What is the formula for the area of a rectangle?", "2 × (Length + Width)", "Length × Width", "Length + Width", "Length ÷ Width", "Length × Width"),
    ("What is the value of 5 factorial (5!)?", "25", "10", "5", "120", "120"),
    ("What is the slope-intercept form of a linear equation?", "y = mx + b", "y = ax^2 + bx + c", "y = a(x - h)^2 + k", "y = a/x + b", "y = mx + b"),
    ("What is the quadratic formula?", "x = -b ± √(b² + 4ac) / 2a", "x = -b ± √(b² - 4ac) / a", "x = (-b ± √(b² - 4ac)) / 2a", "x = -b ± √(b² + 4ac) / a", "x = (-b ± √(b² - 4ac)) / 2a"),
    ("What is the value of sin(90 degrees)?", "1", "0", "-1", "undefined", "1")
]

for i, question in enumerate(math_questions):
    c.execute("INSERT INTO math (id, question, choice1, choice2, choice3, choice4, answer) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (i+1, question[0], question[1], question[2], question[3], question[4], question[5]))

# Insert 10 questions for programming
programming_questions = [
    ("What does HTML stand for?", "Hyper Text Markup Language", "Home Tool Markup Language", "Hyperlinks and Text Markup Language", "Hypertext Markup Language", "Hypertext Markup Language"),
    ("Who is the father of Python programming language?", "Dennis Ritchie", "Guido van Rossum", "Bjarne Stroustrup", "James Gosling", "Guido van Rossum"),
    ("What is the output of the following code? print(2+2*2)", "6", "8", "4", "2", "6"),
    ("What is the file extension of a Python source code file?", ".py", ".python", ".pyth", ".pt", ".py"),
    ("Which data structure uses LIFO order?", "Queue", "Heap", "Stack", "Linked List", "Stack"),
    ("What is the output of the following code? print('hello'[::-1])", "hello", "h", "olleh", "o", "olleh"),
    ("Which of the following is not a programming language?", "HTML", "Java", "Python", "C++", "HTML"),
    ("What does CPU stand for?", "Computer Personal Unit", "Central Processing Unit", "Central Process Unit", "Central Processor Unit", "Central Processing Unit"),
    ("Which programming language is known as the 'language of the web'?", "JavaScript", "Java", "Python", "C++", "JavaScript"),
    ("What is the output of the following code? print(10 == '10')", "True", "Error", "None", "False", "False")
]

for i, question in enumerate(programming_questions):
    c.execute("INSERT INTO programming (id, question, choice1, choice2, choice3, choice4, answer) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (i+1, question[0], question[1], question[2], question[3], question[4], question[5]))

# Commit changes and close the connection
conn.commit()
conn.close()