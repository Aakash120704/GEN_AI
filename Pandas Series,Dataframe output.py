Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
==================== RESTART: C:/Python314/Pandas Series.py ====================
Tech Gadgets Inventory
----------------------
0          Smartphone
1              Laptop
2          Smartwatch
3    Wireless Earbuds
4              Tablet
dtype: object
Original data type: <class 'list'>

--- Slicing & Retrieval (Default Index) ---
Item at index 1: Laptop
Item at index 4: Tablet

Slicing from index 2 onwards:
2          Smartwatch
3    Wireless Earbuds
4              Tablet
dtype: object

Slicing with a step of 2 (index 0 to 3):
0    Smartphone
2    Smartwatch
dtype: object

========================================

Gadgets organized by Brand
--------------------------
Apple            Smartphone
Dell                 Laptop
Apple            Smartwatch
Sony       Wireless Earbuds
Samsung              Tablet
dtype: object

--- Retrieval using Custom Labels & iloc ---
Retrieving all 'Apple' products:
Apple    Smartphone
Apple    Smartwatch
dtype: object

Retrieving item at position 3 using .iloc:
Wireless Earbuds

========================================

Gadget Prices (Created from Dictionary)
---------------------------------------
iPhone 15          799
MacBook Air        999
Galaxy S24         799
Sony WH-1000XM5    399
dtype: int64
Original data type: <class 'dict'>

--- Dictionary Series Retrieval ---
Price of iPhone 15: 799
Price of Sony headphones (using .loc): 399
Price of the 3rd item in the list (using .iloc): 799

============================================================= RESTART: D:/GEN AI/Pandas Dataframe 1.py ============================================================
--- Showing the whole data table ---
   Emp_ID     Name  Experience_Yrs Department  Performance_Score
0     501    Alice               3         HR                 88
1     502      Bob               7         IT                 95
2     503  Charlie               2      Sales                 72
3     504    Alice               5         IT                 91
4     505    David               8  Marketing                 84

Total number of rows and columns: (5, 5)
----------------------------------------

Showing just the first 3 rows:
   Emp_ID     Name  Experience_Yrs Department  Performance_Score
0     501    Alice               3         HR                 88
1     502      Bob               7         IT                 95
2     503  Charlie               2      Sales                 72

Showing just the last 2 rows:
   Emp_ID   Name  Experience_Yrs Department  Performance_Score
3     504  Alice               5         IT                 91
4     505  David               8  Marketing                 84

Showing math summary like count, average, min, and max:
           Emp_ID  Experience_Yrs  Performance_Score
count    5.000000         5.00000           5.000000
mean   503.000000         5.00000          86.000000
std      1.581139         2.54951           8.803408
min    501.000000         2.00000          72.000000
25%    502.000000         3.00000          84.000000
50%    503.000000         5.00000          88.000000
75%    504.000000         7.00000          91.000000
max    505.000000         8.00000          95.000000
----------------------------------------

Showing the list of names in reverse order:
4      David
3      Alice
2    Charlie
1        Bob
0      Alice
Name: Name, dtype: object

Showing only Name and Department for the first 2 rows:
    Name Department
0  Alice         HR
1    Bob         IT

Showing only the first 2 rows of the table:
   Emp_ID   Name  Experience_Yrs Department  Performance_Score
0     501  Alice               3         HR                 88
1     502    Bob               7         IT                 95
----------------------------------------

Showing the department of the very first employee (Row 0, Column 3):
HR

Showing all details of the 3rd employee:
Emp_ID                   503
Name                 Charlie
Experience_Yrs             2
Department             Sales
Performance_Score         72
Name: 2, dtype: object

Showing rows from label A to label D:
   Emp_ID     Name  Experience_Yrs Department  Performance_Score
A     501    Alice               3         HR                 88
B     502      Bob               7         IT                 95
C     503  Charlie               2      Sales                 72
D     504    Alice               5         IT                 91
----------------------------------------

Showing only employees whose name is Alice:
   Emp_ID   Name  Experience_Yrs Department  Performance_Score
0     501  Alice               3         HR                 88
3     504  Alice               5         IT                 91

Showing only employees with a performance score above 90:
   Emp_ID   Name  Experience_Yrs Department  Performance_Score
1     502    Bob               7         IT                 95
3     504  Alice               5         IT                 91

Sorting table: Experience from low-to-high, Name from Z-to-A:
   Emp_ID     Name  Experience_Yrs Department  Performance_Score
2     503  Charlie               2      Sales                 72
0     501    Alice               3         HR                 88
3     504    Alice               5         IT                 91
1     502      Bob               7         IT                 95
4     505    David               8  Marketing                 84
----------------------------------------

Calculating math stats for Experience Years:
Average Experience: 5.0
Middle (Median) Experience: 5.0
Lowest Experience: 2
Highest Experience: 8
Standard Deviation of Experience: 2.5495097567963922
Total Sum of all Experience Years: 25
----------------------------------------

Adding a new column for Base Salary:
   Emp_ID     Name  Experience_Yrs Department  Performance_Score  base_salary
0     501    Alice               3         HR                 88        50000
1     502      Bob               7         IT                 95        85000
2     503  Charlie               2      Sales                 72        45000
3     504    Alice               5         IT                 91        70000
4     505    David               8  Marketing                 84        90000

Converting the salary into thousands (dividing by 1000):
   Emp_ID     Name  Experience_Yrs  ... Performance_Score  base_salary  salary_in_k
0     501    Alice               3  ...                88        50000         50.0
1     502      Bob               7  ...                95        85000         85.0
2     503  Charlie               2  ...                72        45000         45.0
3     504    Alice               5  ...                91        70000         70.0
4     505    David               8  ...                84        90000         90.0

[5 rows x 7 columns]
----------------------------------------

Adding a bonus column based on which department they work in:
   Emp_ID     Name  Experience_Yrs  ... base_salary  salary_in_k  bonus
0     501    Alice               3  ...       50000         50.0   2000
1     502      Bob               7  ...       85000         85.0   7500
2     503  Charlie               2  ...       45000         45.0   5000
3     504    Alice               5  ...       70000         70.0   7500
4     505    David               8  ...       90000         90.0   6000

[5 rows x 8 columns]
