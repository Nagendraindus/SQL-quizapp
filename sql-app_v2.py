import tkinter as tk
from tkinter import messagebox

# Define questions, options, and answers
quiz_questions = [
    {
        "question": "Q-1. Write an SQL query to fetch \"FIRST_NAME\" from Worker table using the alias name as <WORKER_NAME>.",
        "options": [
            "SELECT first_name FROM worker;",
            "SELECT first_name AS WORKER_NAME FROM worker;",
            "SELECT WORKER_NAME FROM worker;",
            "SELECT * FROM worker;"
        ],
        "answer": "SELECT first_name AS WORKER_NAME FROM worker;"
    },
    {
        "question": "Q-2. Write an SQL query to fetch \"FIRST_NAME\" from Worker table in upper case.",
        "options": [
            "SELECT first_name FROM worker;",
            "SELECT LOWER(first_name) FROM worker;",
            "SELECT UPPER(first_name) FROM worker;",
            "SELECT first_name AS UPPER FROM worker;"
        ],
        "answer": "SELECT UPPER(first_name) FROM worker;"
    },
    {
        "question": "Q-3. Write an SQL query to fetch unique values of DEPARTMENT from Worker table.",
        "options": [
            "SELECT DEPARTMENT FROM worker;",
            "SELECT UNIQUE(DEPARTMENT) FROM worker;",
            "SELECT distinct DEPARTMENT FROM worker;",
            "SELECT DEPARTMENT, COUNT(*) FROM worker GROUP BY DEPARTMENT;"
        ],
        "answer": "SELECT distinct DEPARTMENT FROM worker;"
    },
    {
        "question": "Q-4. Write an SQL query to print the first three characters of FIRST_NAME from Worker table.",
        "options": [
            "SELECT LEFT(first_name, 3) FROM worker;",
            "SELECT RIGHT(first_name, 3) FROM worker;",
            "SELECT MID(first_name, 3) FROM worker;",
            "SELECT SUBSTRING(first_name, 1, 3) FROM worker;"
        ],
        "answer": "SELECT SUBSTRING(first_name, 1, 3) FROM worker;"
    },
    {
        "question": "Q-5. Write an SQL query to find the position of the alphabet ('b') in the first name column 'Amitabh' from Worker table.",
        "options": [
            "SELECT POSITION('b' IN first_name) FROM worker WHERE first_name = 'Amitabh';",
            "SELECT LOCATE('b', first_name) FROM worker WHERE first_name = 'Amitabh';",
            "SELECT INSTR(first_name, 'b') FROM worker WHERE first_name = 'Amitabh';",
            "SELECT CHARINDEX('b', first_name) FROM worker WHERE first_name = 'Amitabh';"
        ],
        "answer": "SELECT INSTR(first_name, 'B') FROM worker WHERE first_name = 'Amitabh';"
    },
    {
        "question": "Q-6. Write an SQL query to print the FIRST_NAME from Worker table after removing white spaces from the right side.",
        "options": [
            "SELECT TRIM(first_name) FROM worker;",
            "SELECT LTRIM(first_name) FROM worker;",
            "SELECT RTRIM(first_name) FROM worker;",
            "SELECT REMOVE(first_name) FROM worker;"
        ],
        "answer": "SELECT RTRIM(first_name) FROM worker;"
    },
    {
        "question": "Q-7. Write an SQL query to print the DEPARTMENT from Worker table after removing white spaces from the left side.",
        "options": [
            "SELECT TRIM(department) FROM worker;",
            "SELECT LTRIM(department) FROM worker;",
            "SELECT RTRIM(department) FROM worker;",
            "SELECT REMOVE(department) FROM worker;"
        ],
        "answer": "SELECT LTRIM(first_name) FROM worker;"
    },
    {
        "question": "Q-8. Write an SQL query that fetches the unique values of DEPARTMENT from Worker table and prints its length.",
        "options": [
            "SELECT DEPARTMENT, LENGTH(DEPARTMENT) FROM worker;",
            "SELECT DISTINCT DEPARTMENT, LENGTH(DEPARTMENT) FROM worker;",
            "SELECT DEPARTMENT, DISTINCT LENGTH(DEPARTMENT) FROM worker;",
            "SELECT UNIQUE(DEPARTMENT), LENGTH(DEPARTMENT) FROM worker;"
        ],
        "answer": "SELECT DISTINCT DEPARTMENT, LENGTH(DEPARTMENT) FROM worker;"
    },
    {
        "question": "Q-9. Write an SQL query to print the FIRST_NAME from Worker table after replacing ‘a’ with ‘A’.",
        "options": [
            "SELECT REPLACE(first_name, 'A', 'a') FROM worker;",
            "SELECT REPLACE(first_name, 'a', 'A') FROM worker;",
            "SELECT SUBSTITUTE(first_name, 'a', 'A') FROM worker;",
            "SELECT TRANSLATE(first_name, 'a', 'A') FROM worker;"
        ],
        "answer": "SELECT REPLACE(first_name, 'a', 'A') FROM worker;"
    },
    {
        "question": "Q-10. Write an SQL query to print the FIRST_NAME and LAST_NAME from Worker table into a single column COMPLETE_NAME. A space char should separate them.",
        "options": [
            "SELECT CONCAT(FIRST_NAME, LAST_NAME) AS COMPLETE_NAME FROM worker;",
            "SELECT CONCAT(FIRST_NAME || ' ' || LAST_NAME) AS COMPLETE_NAME FROM worker;",
            "SELECT CONCAT(FIRST_NAME, ' ', LAST_NAME) AS COMPLETE_NAME FROM worker;",
            "SELECT CONCAT_WS(' ', FIRST_NAME, LAST_NAME) AS COMPLETE_NAME FROM worker;"
        ],
        "answer": "SELECT CONCAT(FIRST_NAME, ' ', LAST_NAME) AS COMPLETE_NAME FROM worker;"
    },
    {
        "question": "Q-11. Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME Ascending.",
        "options": [
            "SELECT * FROM worker ORDER BY FIRST_NAME ASC;",
            "SELECT * FROM worker ORDER BY FIRST_NAME;",
            "SELECT * FROM worker ORDER BY FIRST_NAME DESC;",
            "SELECT * FROM worker SORT BY FIRST_NAME;"
        ],
        "answer": "SELECT * FROM worker ORDER BY FIRST_NAME;"
    },
    {
        "question": "Q-12. Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME Ascending and DEPARTMENT Descending.",
        "options": [
            "SELECT * FROM worker ORDER BY FIRST_NAME ASC, DEPARTMENT DESC;",
            "SELECT * FROM worker ORDER BY FIRST_NAME, DEPARTMENT;",
            "SELECT * FROM worker ORDER BY DEPARTMENT DESC, FIRST_NAME ASC;",
            "SELECT * FROM worker ORDER BY FIRST_NAME ASC, DEPARTMENT ASC;"
        ],
        "answer": "SELECT * FROM worker ORDER BY FIRST_NAME, DEPARTMENT DESC;"
    },
    {
        "question": "Q-13. Write an SQL query to print details for Workers with the first name as “Vipul” and “Satish” from Worker table.",
        "options": [
            "SELECT * FROM worker WHERE FIRST_NAME = 'Vipul' OR FIRST_NAME = 'Satish';",
            "SELECT * FROM worker WHERE FIRST_NAME IN ('Vipul', 'Satish');",
            "SELECT * FROM worker WHERE FIRST_NAME = 'Vipul' AND FIRST_NAME = 'Satish';",
            "SELECT * FROM worker WHERE FIRST_NAME LIKE 'Vipul' AND FIRST_NAME LIKE 'Satish';"
        ],
        "answer": "SELECT * FROM worker WHERE FIRST_NAME IN ('Vipul', 'Satish');"
    },
    {
        "question": "Q-14. Write an SQL query to print details of workers excluding first names, “Vipul” and “Satish” from Worker table.",
        "options": [
            "SELECT * FROM worker WHERE FIRST_NAME NOT IN ('Vipul', 'Satish');",
            "SELECT * FROM worker WHERE FIRST_NAME <> 'Vipul' AND FIRST_NAME <> 'Satish';",
            "SELECT * FROM worker WHERE FIRST_NAME != 'Vipul' AND FIRST_NAME != 'Satish';",
            "SELECT * FROM worker WHERE FIRST_NAME IS NOT ('Vipul', 'Satish');"
        ],
        "answer": "SELECT * FROM worker WHERE FIRST_NAME NOT IN ('Vipul', 'Satish');"
    },
    {
        "question": "Q-15. Write an SQL query to print details of Workers with DEPARTMENT name as “Admin*”.",
        "options": [
            "SELECT * FROM worker WHERE DEPARTMENT = 'Admin*';",
            "SELECT * FROM worker WHERE DEPARTMENT LIKE 'Admin%';",
            "SELECT * FROM worker WHERE DEPARTMENT IN ('Admin');",
            "SELECT * FROM worker WHERE DEPARTMENT CONTAINS 'Admin';"
        ],
        "answer": "SELECT * FROM worker WHERE DEPARTMENT LIKE 'Admin%';"
    },
    {
        "question": "Q-16. Write an SQL query to print details of the Workers whose FIRST_NAME contains ‘a’.",
        "options": [
            "SELECT * FROM worker WHERE FIRST_NAME LIKE '%a%';",
            "SELECT * FROM worker WHERE FIRST_NAME LIKE '%a';",
            "SELECT * FROM worker WHERE FIRST_NAME LIKE 'a%';",
            "SELECT * FROM worker WHERE FIRST_NAME LIKE 'a';"
        ],
        "answer": "SELECT * FROM worker WHERE FIRST_NAME LIKE '%a%';"
    },
    {
        "question": "Q-17. Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘a’.",
        "options": [
            "SELECT * FROM worker WHERE FIRST_NAME LIKE '%a';",
            "SELECT * FROM worker WHERE FIRST_NAME LIKE 'a%';",
            "SELECT * FROM worker WHERE FIRST_NAME = 'a';",
            "SELECT * FROM worker WHERE FIRST_NAME CONTAINS 'a';"
        ],
        "answer": "SELECT * FROM worker WHERE FIRST_NAME LIKE '%a';"
    },
    {
        "question": "Q-18. Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘h’ and contains six alphabets.",
        "options": [
            "SELECT * FROM worker WHERE FIRST_NAME LIKE '_____h';",
            "SELECT * FROM worker WHERE FIRST_NAME LIKE 'h_____';",
            "SELECT * FROM worker WHERE FIRST_NAME LIKE '%h%';",
            "SELECT * FROM worker WHERE FIRST_NAME LIKE 'h%';"
        ],
        "answer": "SELECT * FROM worker WHERE FIRST_NAME LIKE '_____h';"
    },
    {
        "question": "Q-19. Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘a’ and contains five alphabets.",
        "options": [
            "SELECT * FROM worker WHERE FIRST_NAME LIKE '____a';",
            "SELECT * FROM worker WHERE FIRST_NAME LIKE 'a____';",
            "SELECT * FROM worker WHERE FIRST_NAME LIKE '%a%';",
            "SELECT * FROM worker WHERE FIRST_NAME LIKE 'a%';"
        ],
        "answer": "SELECT * FROM worker WHERE FIRST_NAME LIKE '____a';"
    },
    {
        "question": "Q-20. Write an SQL query to print details of the Workers whose SALARY lies between 100000 and 500000.",
        "options": [
            "SELECT * FROM worker WHERE SALARY BETWEEN 100000 AND 500000;",
            "SELECT * FROM worker WHERE SALARY >= 100000 AND SALARY <= 500000;",
            "SELECT * FROM worker WHERE SALARY > 100000 AND SALARY < 500000;",
            "SELECT * FROM worker WHERE SALARY NOT BETWEEN 100000 AND 500000;"
        ],
        "answer": "SELECT * FROM worker WHERE SALARY BETWEEN 100000 AND 500000;"
    },
    {
        "question": "Q-21. Write an SQL query to print details of the Workers whose SALARY lies between 50000 and 100000.",
        "options": [
            "SELECT * FROM worker WHERE SALARY BETWEEN 50000 AND 100000;",
            "SELECT * FROM worker WHERE SALARY >= 50000 AND SALARY <= 100000;",
            "SELECT * FROM worker WHERE SALARY > 50000 AND SALARY < 100000;",
            "SELECT * FROM worker WHERE SALARY NOT BETWEEN 50000 AND 100000;"
        ],
        "answer": "SELECT * FROM worker WHERE SALARY BETWEEN 50000 AND 100000;"
    },
    {
        "question": "Q-22. Write an SQL query to find the maximum, minimum, and average SALARY of the Workers.",
        "options": [
            "SELECT MAX(SALARY), MIN(SALARY), AVG(SALARY) FROM worker;",
            "SELECT MAX(SALARY), MIN(SALARY), SUM(SALARY) FROM worker;",
            "SELECT TOP 1 SALARY, MIN(SALARY), AVG(SALARY) FROM worker;",
            "SELECT MAXIMUM(SALARY), MINIMUM(SALARY), AVERAGE(SALARY) FROM worker;"
        ],
        "answer": "SELECT MAX(SALARY), MIN(SALARY), AVG(SALARY) FROM worker;"
    },
    {
        "question": "Q-23. Write an SQL query to find the maximum and minimum SALARY of the Workers by DEPARTMENT.",
        "options": [
            "SELECT DEPARTMENT, MAX(SALARY), MIN(SALARY) FROM worker;",
            "SELECT MAX(SALARY), MIN(SALARY) FROM worker GROUP BY DEPARTMENT;",
            "SELECT DEPARTMENT, SALARY FROM worker WHERE SALARY = MAX(SALARY) OR SALARY = MIN(SALARY);",
            "SELECT MAXIMUM(SALARY), MINIMUM(SALARY) FROM worker GROUP BY DEPARTMENT;"
        ],
        "answer": "SELECT DEPARTMENT, MAX(SALARY), MIN(SALARY) FROM worker GROUP BY DEPARTMENT;"
    },
    {
        "question": "Q-24. Write an SQL query to find the highest-paid employee from each DEPARTMENT.",
        "options": [
            "SELECT DEPARTMENT, FIRST_NAME, LAST_NAME, SALARY FROM worker GROUP BY DEPARTMENT ORDER BY SALARY DESC LIMIT 1;",
            "SELECT * FROM worker WHERE (DEPARTMENT, SALARY) IN (SELECT DEPARTMENT, MAX(SALARY) FROM worker GROUP BY DEPARTMENT);",
            "SELECT FIRST_NAME, LAST_NAME, DEPARTMENT, SALARY FROM worker ORDER BY DEPARTMENT, SALARY DESC;",
            "SELECT * FROM worker WHERE SALARY = MAX(SALARY) GROUP BY DEPARTMENT;"
        ],
        "answer": "SELECT * FROM worker WHERE (DEPARTMENT, SALARY) IN (SELECT DEPARTMENT, MAX(SALARY) FROM worker GROUP BY DEPARTMENT);"
    },
    {
        "question": "Q-25. Write an SQL query to find the highest-paid employee in the Worker table.",
        "options": [
            "SELECT FIRST_NAME, LAST_NAME, SALARY FROM worker ORDER BY SALARY DESC LIMIT 1;",
            "SELECT * FROM worker WHERE SALARY = MAX(SALARY);",
            "SELECT TOP 1 * FROM worker ORDER BY SALARY DESC;",
            "SELECT MAX(SALARY) FROM worker;"
        ],
        "answer": "SELECT FIRST_NAME, LAST_NAME, SALARY FROM worker ORDER BY SALARY DESC LIMIT 1;"
    },
    {
        "question": "Q-26. Write an SQL query to print the total number of workers with department Admin.",
        "options": [
            "SELECT COUNT(*) FROM worker WHERE DEPARTMENT = 'Admin';",
            "SELECT * FROM worker WHERE DEPARTMENT = 'Admin';",
            "SELECT TOTAL(DEPARTMENT) FROM worker WHERE DEPARTMENT = 'Admin';",
            "SELECT COUNT(DEPARTMENT) FROM worker WHERE DEPARTMENT = 'Admin';"
        ],
        "answer": "SELECT COUNT(*) FROM worker WHERE DEPARTMENT = 'Admin';"
    },
    {
        "question": "Q-27. Write an SQL query to print the departments along with the number of workers in each department.",
        "options": [
            "SELECT DEPARTMENT, COUNT(FIRST_NAME) FROM worker GROUP BY DEPARTMENT;",
            "SELECT DEPARTMENT, COUNT(*) FROM worker GROUP BY DEPARTMENT;",
            "SELECT DEPARTMENT, WORKER_COUNT(FIRST_NAME) FROM worker;",
            "SELECT DEPARTMENT, SUM(*) FROM worker GROUP BY DEPARTMENT;"
        ],
        "answer": "SELECT DEPARTMENT, COUNT(*) FROM worker GROUP BY DEPARTMENT;"
    },
    {
        "question": "Q-28. Write an SQL query to print the first name of workers along with the total of salaries in each department.",
        "options": [
            "SELECT FIRST_NAME, DEPARTMENT, SUM(SALARY) FROM worker GROUP BY FIRST_NAME;",
            "SELECT FIRST_NAME, SUM(SALARY) FROM worker GROUP BY FIRST_NAME, DEPARTMENT;",
            "SELECT FIRST_NAME, SUM(SALARY) AS TOTAL_SALARY FROM worker GROUP BY DEPARTMENT;",
            "SELECT DEPARTMENT, SUM(SALARY) FROM worker GROUP BY DEPARTMENT;"
        ],
        "answer": "SELECT FIRST_NAME, SUM(SALARY) FROM worker GROUP BY FIRST_NAME, DEPARTMENT;"
    },
    {
        "question": "Q-29. Write an SQL query to fetch duplicate records having matching data in some fields of a table.",
        "options": [
            "SELECT * FROM worker WHERE EXISTS (SELECT * FROM worker AS t2 WHERE worker.first_name = t2.first_name);",
            "SELECT * FROM worker WHERE EXISTS (SELECT * FROM worker AS t2 WHERE worker.first_name = t2.first_name AND worker.salary = t2.salary);",
            "SELECT first_name, COUNT(*) FROM worker GROUP BY first_name HAVING COUNT(*) > 1;",
            "SELECT * FROM worker WHERE COUNT(first_name) > 1;"
        ],
        "answer": "SELECT first_name, COUNT(*) FROM worker GROUP BY first_name HAVING COUNT(*) > 1;"
    },
    {
        "question": "Q-30. Write an SQL query to fetch the employees who are also managers.",
        "options": [
            "SELECT * FROM worker WHERE EXISTS (SELECT * FROM worker AS t2 WHERE worker.manager_id = t2.id);",
            "SELECT * FROM worker WHERE id IN (SELECT manager_id FROM worker);",
            "SELECT * FROM worker WHERE manager_id IS NOT NULL;",
            "SELECT * FROM worker WHERE id IN (SELECT id FROM worker);"
        ],
        "answer": "SELECT * FROM worker WHERE id IN (SELECT manager_id FROM worker);"
    },
    {
        "question": "Q-31. Write an SQL query to find the 3rd highest salary in the Worker table.",
        "options": [
            "SELECT SALARY FROM worker ORDER BY SALARY DESC LIMIT 2, 1;",
            "SELECT DISTINCT SALARY FROM worker ORDER BY SALARY DESC LIMIT 1 OFFSET 2;",
            "SELECT SALARY FROM worker ORDER BY SALARY DESC LIMIT 3;",
            "SELECT SALARY FROM worker WHERE ROWNUM = 3 ORDER BY SALARY DESC;"
        ],
        "answer": "SELECT DISTINCT SALARY FROM worker ORDER BY SALARY DESC LIMIT 1 OFFSET 2;"
    },
    {
        "question": "Q-32. Write an SQL query to find the Nth highest salary from a table.",
        "options": [
            "SELECT SALARY FROM worker ORDER BY SALARY DESC LIMIT N-1, 1;",
            "SELECT DISTINCT SALARY FROM worker ORDER BY SALARY DESC LIMIT N;",
            "SELECT * FROM (SELECT SALARY, DENSE_RANK() OVER (ORDER BY SALARY DESC) rank FROM worker) t WHERE t.rank = N;",
            "SELECT TOP 1 SALARY FROM worker WHERE SALARY NOT IN (SELECT TOP (N-1) SALARY FROM worker ORDER BY SALARY DESC);"
        ],
        "answer": "SELECT * FROM (SELECT SALARY, DENSE_RANK() OVER (ORDER BY SALARY DESC) rank FROM worker) t WHERE t.rank = N;"
    },
    {
        "question": "Q-33. Write an SQL query to find the 2nd highest salary in the Worker table.",
        "options": [
            "SELECT SALARY FROM worker ORDER BY SALARY DESC LIMIT 1 OFFSET 1;",
            "SELECT DISTINCT SALARY FROM worker ORDER BY SALARY DESC LIMIT 1 OFFSET 1;",
            "SELECT TOP 1 SALARY FROM worker WHERE SALARY NOT IN (SELECT MAX(SALARY) FROM worker);",
            "SELECT MAX(SALARY) FROM worker WHERE SALARY NOT IN (SELECT MAX(SALARY) FROM worker);"
        ],
        "answer": "SELECT DISTINCT SALARY FROM worker ORDER BY SALARY DESC LIMIT 1 OFFSET 1;"
    },
    {
        "question": "Q-34. Write an SQL query to fetch the list of employees with the same salary.",
        "options": [
            "SELECT * FROM worker WHERE SALARY IN (SELECT SALARY FROM worker GROUP BY SALARY HAVING COUNT(*) > 1);",
            "SELECT * FROM worker GROUP BY SALARY HAVING COUNT(*) > 1;",
            "SELECT SALARY, COUNT(*) FROM worker GROUP BY SALARY HAVING COUNT(*) > 1;",
            "SELECT * FROM worker WHERE SALARY IS NOT NULL GROUP BY SALARY;"
        ],
        "answer": "SELECT SALARY, COUNT(*) FROM worker GROUP BY SALARY HAVING COUNT(*) > 1;"
    },
    {
        "question": "Q-35. Write an SQL query to fetch all the employees working in the Admin department.",
        "options": [
            "SELECT * FROM worker WHERE DEPARTMENT = 'Admin';",
            "SELECT * FROM worker WHERE DEPARTMENT LIKE 'Admin%';",
            "SELECT * FROM worker WHERE DEPARTMENT IN ('Admin');",
            "SELECT * FROM worker WHERE DEPARTMENT = 'Administration';"
        ],
        "answer": "SELECT * FROM worker WHERE DEPARTMENT = 'Admin';"
    },
    {
        "question": "Q-36. Write an SQL query to fetch all the employees from the Worker table in ascending order of their FIRST_NAME.",
        "options": [
            "SELECT * FROM worker ORDER BY FIRST_NAME ASC;",
            "SELECT * FROM worker ORDER BY FIRST_NAME;",
            "SELECT * FROM worker ORDER BY FIRST_NAME DESC;",
            "SELECT * FROM worker SORT BY FIRST_NAME;"
        ],
        "answer": "SELECT * FROM worker ORDER BY FIRST_NAME ASC;"
    },
    {
        "question": "Q-37. Write an SQL query to fetch the departments with the highest and lowest salary in the Worker table.",
        "options": [
            "SELECT DEPARTMENT, MAX(SALARY), MIN(SALARY) FROM worker;",
            "SELECT DEPARTMENT, MAX(SALARY), MIN(SALARY) FROM worker GROUP BY DEPARTMENT;",
            "SELECT DEPARTMENT, FIRST_NAME, LAST_NAME, SALARY FROM worker ORDER BY SALARY DESC LIMIT 1;",
            "SELECT DEPARTMENT, FIRST_NAME, LAST_NAME, SALARY FROM worker ORDER BY SALARY ASC LIMIT 1;"
        ],
        "answer": "SELECT DEPARTMENT, MAX(SALARY), MIN(SALARY) FROM worker GROUP BY DEPARTMENT;"
    },
    {
        "question": "Q-38. Write an SQL query to fetch all the employees whose FIRST_NAME starts with the alphabet ‘A’.",
        "options": [
            "SELECT * FROM worker WHERE FIRST_NAME LIKE 'A%';",
            "SELECT * FROM worker WHERE FIRST_NAME LIKE '%A';",
            "SELECT * FROM worker WHERE FIRST_NAME LIKE '%A%';",
            "SELECT * FROM worker WHERE FIRST_NAME LIKE 'A';"
        ],
        "answer": "SELECT * FROM worker WHERE FIRST_NAME LIKE 'A%';"
    },
    {
        "question": "Q-39. Write an SQL query to fetch all the employees whose FIRST_NAME starts with ‘A’ and ends with ‘a’.",
        "options": [
            "SELECT * FROM worker WHERE FIRST_NAME LIKE 'A%a';",
            "SELECT * FROM worker WHERE FIRST_NAME LIKE '%A%';",
            "SELECT * FROM worker WHERE FIRST_NAME LIKE 'A%';",
            "SELECT * FROM worker WHERE FIRST_NAME LIKE '%a';"
        ],
        "answer": "SELECT * FROM worker WHERE FIRST_NAME LIKE 'A%a';"
    },
    {
        "question": "Q-40. Write an SQL query to fetch all the employees who have the same department and salary.",
        "options": [
            "SELECT * FROM worker WHERE DEPARTMENT = SALARY;",
            "SELECT * FROM worker WHERE DEPARTMENT IN (SELECT DEPARTMENT FROM worker GROUP BY DEPARTMENT HAVING COUNT(*) > 1);",
            "SELECT DEPARTMENT, SALARY, COUNT(*) FROM worker GROUP BY DEPARTMENT, SALARY HAVING COUNT(*) > 1;",
            "SELECT * FROM worker WHERE DEPARTMENT IN (SELECT DEPARTMENT FROM worker);"
        ],
        "answer": "SELECT DEPARTMENT, SALARY, COUNT(*) FROM worker GROUP BY DEPARTMENT, SALARY HAVING COUNT(*) > 1;"
    },
    {
        "question": "Q-41. Write an SQL query to fetch the employee count working in each department.",
        "options": [
            "SELECT DEPARTMENT, COUNT(*) FROM worker GROUP BY DEPARTMENT;",
            "SELECT DEPARTMENT, COUNT(DEPARTMENT) FROM worker;",
            "SELECT COUNT(*), DEPARTMENT FROM worker GROUP BY DEPARTMENT;",
            "SELECT DEPARTMENT, EMPLOYEE_COUNT(FIRST_NAME) FROM worker;"
        ],
        "answer": "SELECT DEPARTMENT, COUNT(*) FROM worker GROUP BY DEPARTMENT;"
    },
    {
        "question": "Q-42. Write an SQL query to fetch all the employees whose salary is between 100000 and 150000.",
        "options": [
            "SELECT * FROM worker WHERE SALARY BETWEEN 100000 AND 150000;",
            "SELECT * FROM worker WHERE SALARY >= 100000 AND SALARY <= 150000;",
            "SELECT * FROM worker WHERE SALARY > 100000 AND SALARY < 150000;",
            "SELECT * FROM worker WHERE SALARY NOT BETWEEN 100000 AND 150000;"
        ],
        "answer": "SELECT * FROM worker WHERE SALARY BETWEEN 100000 AND 150000;"
    },
    {
        "question": "Q-43. Write an SQL query to fetch the details of workers with the highest salary in each department.",
        "options": [
            "SELECT DEPARTMENT, FIRST_NAME, LAST_NAME, MAX(SALARY) FROM worker GROUP BY DEPARTMENT;",
            "SELECT * FROM worker WHERE (DEPARTMENT, SALARY) IN (SELECT DEPARTMENT, MAX(SALARY) FROM worker GROUP BY DEPARTMENT);",
            "SELECT * FROM worker WHERE SALARY = (SELECT MAX(SALARY) FROM worker);",
            "SELECT DEPARTMENT, FIRST_NAME, LAST_NAME, SALARY FROM worker ORDER BY DEPARTMENT, SALARY DESC LIMIT 1;"
        ],
        "answer": "SELECT * FROM worker WHERE (DEPARTMENT, SALARY) IN (SELECT DEPARTMENT, MAX(SALARY) FROM worker GROUP BY DEPARTMENT);"
    },
    {
        "question": "Q-44. Write an SQL query to fetch the worker details who earn the highest salary.",
        "options": [
            "SELECT FIRST_NAME, LAST_NAME, SALARY FROM worker ORDER BY SALARY DESC LIMIT 1;",
            "SELECT * FROM worker WHERE SALARY = (SELECT MAX(SALARY) FROM worker);",
            "SELECT TOP 1 * FROM worker ORDER BY SALARY DESC;",
            "SELECT FIRST_NAME, LAST_NAME, SALARY FROM worker WHERE SALARY NOT IN (SELECT MAX(SALARY) FROM worker);"
        ],
        "answer": "SELECT * FROM worker WHERE SALARY = (SELECT MAX(SALARY) FROM worker);"
    },
    {
        "question": "Q-45. Write an SQL query to fetch the department-wise details of the workers with the highest salary.",
        "options": [
            "SELECT DEPARTMENT, MAX(SALARY) FROM worker GROUP BY DEPARTMENT;",
            "SELECT DEPARTMENT, FIRST_NAME, LAST_NAME, SALARY FROM worker WHERE SALARY IN (SELECT MAX(SALARY) FROM worker GROUP BY DEPARTMENT);",
            "SELECT * FROM worker WHERE SALARY = (SELECT MAX(SALARY) FROM worker);",
            "SELECT DEPARTMENT, FIRST_NAME, LAST_NAME, SALARY FROM worker ORDER BY DEPARTMENT, SALARY DESC LIMIT 1;"
        ],
        "answer": "SELECT DEPARTMENT, FIRST_NAME, LAST_NAME, SALARY FROM worker WHERE SALARY IN (SELECT MAX(SALARY) FROM worker GROUP BY DEPARTMENT);"
    }
]

# Define color scheme
COLOR_SCHEME = {
    "sapphire": "#4059ad",
    "blue_gray": "#6b9ac4",
    "tiffany_blue": "#97d8c4",
    "antiflash_white": "#eff2f1",
    "xanthous": "#f4b942",
    "option_bg": "#ffffff",
    "correct": "#28a745",
    "incorrect": "#dc3545",
    "button_hover": "#5a73e5",
    "button_active": "#283e6e"
}

# Define font styles
font_family = "Segoe UI"
question_font = (font_family, 16, "bold")
option_font = (font_family, 14)
button_font = (font_family, 14)
score_font = (font_family, 14, "italic")


class CustomWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.overrideredirect(True)  # Remove the native window border
        self.configure(bg=COLOR_SCHEME["antiflash_white"])

         # Use forward slashes

        # Custom Title Bar
        self.title_bar = tk.Frame(self, bg=COLOR_SCHEME["sapphire"], relief="raised", bd=2)
        self.title_bar.pack(fill=tk.X)

        # Title
        self.title_label = tk.Label(
            self.title_bar, text="SQL Quiz Game", bg=COLOR_SCHEME["sapphire"], fg="white", font=question_font
        )
        self.title_label.pack(side=tk.LEFT, padx=10)

        # Close Button
        self.close_button = tk.Button(
            self.title_bar, text="X", bg=COLOR_SCHEME["xanthous"], fg="black", command=self.destroy, relief="flat",
            font=button_font
        )
        self.close_button.pack(side=tk.RIGHT, padx=10)

        # Dragging the Window
        self.title_bar.bind("<ButtonPress-1>", self.start_move)
        self.title_bar.bind("<B1-Motion>", self.do_move)

        # Initialize the quiz game
        self.quiz_game = QuizGame(self)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")


class QuizGame:
    def __init__(self, root):
        self.root = root
        self.score = 0
        self.question_index = 0

        # Create label for question
        self.question_label = tk.Label(
            root, text="", font=question_font, wraplength=600, fg=COLOR_SCHEME["sapphire"],
            bg=COLOR_SCHEME["antiflash_white"]
        )
        self.question_label.pack(pady=20)

        # Create frame for options
        self.options_frame = tk.Frame(root, bg=COLOR_SCHEME["antiflash_white"])
        self.options_frame.pack(pady=10)

        # Create labels for options using frames
        self.option_frames = []
        for i in range(4):
            frame = tk.Frame(self.options_frame, bg=COLOR_SCHEME["option_bg"], relief="raised", bd=1)
            frame.pack(fill=tk.X, pady=5)

            label = tk.Label(
                frame, text="", bg=COLOR_SCHEME["option_bg"], fg=COLOR_SCHEME["sapphire"], font=option_font,
                anchor="w", padx=10, pady=5
            )
            label.pack(fill=tk.X)
            label.bind("<Button-1>", lambda event, opt=i: self.select_option(opt))

            self.option_frames.append((frame, label))

        # Create check answer button
        self.check_button = tk.Button(
            root, text="Check Answer", font=button_font, bg=COLOR_SCHEME["blue_gray"], fg="white",
            command=self.check_answer, activebackground=COLOR_SCHEME["button_active"]
        )
        self.check_button.pack(pady=10)

        # Create submit button
        self.submit_button = tk.Button(
            root, text="Submit Test", font=button_font, bg=COLOR_SCHEME["xanthous"], fg="black",
            command=self.submit_test, activebackground=COLOR_SCHEME["button_active"]
        )
        self.submit_button.pack(pady=10)

        # Create label for score
        self.score_label = tk.Label(
            root, text="Score: 0", font=score_font, fg=COLOR_SCHEME["sapphire"], bg=COLOR_SCHEME["antiflash_white"]
        )
        self.score_label.pack(pady=10)

        # Variable to track selected option
        self.selected_option = -1

        # Show the first question
        self.next_question()

    def next_question(self):
        # Reset the color of the labels
        for frame, label in self.option_frames:
            frame.config(bg=COLOR_SCHEME["option_bg"])
            label.config(bg=COLOR_SCHEME["option_bg"], fg=COLOR_SCHEME["sapphire"])
            label.config(text="")

        # Reset the selected option
        self.selected_option = -1

        # Check if there are more questions
        if self.question_index < len(quiz_questions):
            # Load the question and options
            question_data = quiz_questions[self.question_index]
            self.question_label.config(text=question_data["question"])

            for i, option in enumerate(question_data["options"]):
                self.option_frames[i][1].config(text=option)
        else:
            # Show the final score
            messagebox.showinfo("Quiz Completed", f"Quiz Completed! Your final score is: {self.score}")
            self.root.destroy()

    def select_option(self, selected_option):
        # Reset the color of all option frames
        for frame, label in self.option_frames:
            frame.config(bg=COLOR_SCHEME["option_bg"])
            label.config(bg=COLOR_SCHEME["option_bg"], fg=COLOR_SCHEME["sapphire"])

        # Highlight the selected option
        self.selected_option = selected_option
        selected_frame, selected_label = self.option_frames[selected_option]
        selected_frame.config(bg=COLOR_SCHEME["button_hover"])
        selected_label.config(bg=COLOR_SCHEME["button_hover"], fg="white")

    def check_answer(self):
        if self.selected_option != -1:
            correct_answer = quiz_questions[self.question_index]["answer"]
            selected_text = self.option_frames[self.selected_option][1].cget("text")

            # Color the correct and wrong labels
            for i, (frame, label) in enumerate(self.option_frames):
                if label.cget("text") == correct_answer:
                    frame.config(bg=COLOR_SCHEME["correct"])
                    label.config(bg=COLOR_SCHEME["correct"], fg="white")
                elif i == self.selected_option:
                    frame.config(bg=COLOR_SCHEME["incorrect"])
                    label.config(bg=COLOR_SCHEME["incorrect"], fg="white")

            # Update the score if the selected answer is correct
            if selected_text == correct_answer:
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")

            # Move to the next question after a short delay
            self.root.after(1000, self.increment_question)
        else:
            messagebox.showwarning("No Selection", "Please select an answer.")

    def increment_question(self):
        self.question_index += 1
        self.next_question()

    def submit_test(self):
        messagebox.showinfo("Submit Test", f"You have submitted the test. Your final score is: {self.score}")
        self.root.destroy()


# Run the quiz game
app = CustomWindow()
app.mainloop()