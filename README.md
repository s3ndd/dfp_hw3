# Data Focused Python
## Homework 3
- Mini 2 2022
-  Due at 11:59 pm on Monday, Nov. 14
- You will lose 10 points per hour after that time
* * *
### 1. (30 points) Lists, Tuples, Sets, Dicts, and Comprehensions
```
expenses.txt is a small text file describing business expenses. Each line (after the header) gives the money amount, category, date, and description of an expense.
```
- a. Create a Python script file named **hw3.1.py**. In this script, define an empty list named **records** , then read the lines from **expenses.txt** and **append** each line (_excluding_ its terminating newline character) to the **records** list. Add this code to display the lines from **records** :
```python
for line in records:
	print(line)
```

Confirm that the output is not double-spaced; that is, confirm that each line (string) in the **records** list does not include a terminating newline.

- b. Close the open **expenses.txt** file, then open **expenses.txt** again. Use _ **list** _ _comprehension_ notation to create and initialize a new list, **records2** , from the lines in the **expenses.txt** file, excluding the terminating newline characters. Confirm that you have done this correctly, by adding this code at the end of the script:
```python
print("\nrecords == records2:",
	records == records2, '\n')
```
This should display **records == records2: True**.

- c. Close the open **expenses.txt** file, and open **expenses.txt** again. Learn about the **str** class's **split** function. Fields in the **expenses.txt** file are separated with colon characters, **':'** , since expense descriptions often contain commas. Use _nested_ _ **tuple** _ _conversion_ notation to create and initialize a new _tuple__of tuples_, **records3** , in which each "inner" tuple has the form **(**_amount_ **,** _category_ **,** _date_ **,** _description_**)**, and the "outer" tuple contains one "inner" tuple for each line of input. We use a tuple of tuples because tuples are _immutable_, and we want to protect the input data from accidental change.

Add this code to display the tuple of tuples **records3** :

```python
for tup in records3:
	print(tup)
```

The output from this loop should look like: 
```python
('Amount', 'Category', 'Date', 'Description')
('5.25', 'supply', '20170222', 'box of staples')
...
('8.98', 'supply', '20170325', 'Flair pens')
```

- d.  A function is a mapping from arguments to values. A sequence or map ( **dict** ) can also be thought of as a mapping from arguments to values. Creation of sequences/maps from data can simplify function definitions, or even eliminate the need for some of them. A **list** or **tuple** is a mapping from an integer subscript to a value; a **set** is a mapping from a value to **in == True** or **in == False** ; and a **dict** is a mapping from a key to a value.

Using _ **set** _ _comprehension_ notation with **records3** , define: **cat\_set** , the set of categories (do not include the string **'Category'** ) in the expense records; and, **date\_set** , the set of dates (again, do not include the string **'Date'** ) in the expense records. Add this code to display these two sets:
```python
print('Categories:', cat_set, '\n')
		print('Dates:     ', date_set, '\n')
```

Since **set** s are unordered, your exact output may differ, but the output should look something like:
```pyhthon
Categories: {'supply', 'meal', 'travel', 'util'}
Dates:      {'20170222', '20170223', …, '20170325'}
```

- e. Using _ **dict** _ _comprehension_ notation with **records3** , define a **dict** named **rec\_num\_to\_record** in which each entry's _key_ is the record (line) number, and each entry's _value_ is the tuple representing the data. _Hint_: use a combination of **range()** and **zip** () along with **records3**. In **rec\_num\_to\_record** , store the field names as record number **0**.

Add this code to display **rec\_num\_to\_record** :
```python
for rn in range(len(rec_num_to_record)):
	print('{:3d}:{}'.format(rn,rec_num_to_record[rn]))

```

The output from this loop should look like:

```python
0: ('Amount', 'Category', 'Date', 'Description')
  1: ('5.25', 'supply', '20170222', 'box of staples')
...
 22: ('212.06', 'util', '20170308', 'Duquesne Light')
```

Add this code, using the **items()** iterable, to display **rec\_num\_to\_record** :
```python
for i in rec_num_to_record.items():
	print('{:3d}: {}'.format(i[0], i[1]))
```

Alternatively, using _tuple unpacking_ into two loop variables, you can use (for example):
```python
for k, v in rec_num_to_record.items():
	print('{:3d}: {}'.format(k, v))
```
* * *
### 2. **(30 points) Variadic Functions**

You will need to modify the file **mystats.py** for this part of the homework, since we will use **mystats.py** as a module to **import** in part 3 of the homework. Your **mystats.py** file must be included in the **.zip** archive that you upload when you have completed this homework.

 **HINT:** It is cheating to implement your **mean** function by calling the **mean** function from some other library/module. Write your own code! Check Wikipedia, Wolfram, or elsewhere to make sure you have the correct formulas.

- a. Open the **mystats.py** file (uploaded to Canvas as part of this homework) for editing and running with Python. You will see that **mystats.py** mostly consists of comments describing functions that you will need to write, with a single uncommented **print()** function call that displays the name of the module itself.

```python
print('The current module is:', __name__)
```

Run the module, and add a comment after the **print()** function call describing the output when **mystats.py** is the main module, that is, the module that you are currently editing and testing.

- b. Define the function **mean()** below the relevant comment. The **mean()** function should take _one or more_ positional parameters, and return the arithmetic mean of its arguments when called. Uncomment these test statements in **mystats.py** to test that your **mean()** function is working correctly:

```python
print('mean(1) should be 1.0, and is:', mean(1))
print('mean(1,2,3,4) should be 2.5, and is:',
                                    mean(1,2,3,4))
print('mean(2.4,3.1) should be 2.75, and is:',
                                    mean(2.4,3.1))
print('mean() should FAIL:', mean())

```

Run the module and confirm success. (Comment out the last of these four **print()** calls after you have confirmed that calling **mean()** with no argument fails.)

- c. Improve your **mean()** function so that it accepts numeric _iterables_ as well as individual numeric values as arguments. To test whether a variable refers to an _iterable_, you can call the **iter()** function. **iter()** will fail and _raise an exception_ if its argument is not iterable. Here is a function that uses **try** / **except** to test whether an object is iterable without crashing your program. (You can copy this function code into your own program.)
```python
def is_iter(v):
    v_is_iter = True
    try:
        iter(v)
    except:
        v_is_iter = False
    return v_is_iter

v1 = {1, 2, 3}     # a set is iterable
print(v1, "is iterable:", is_iter(v1))
v2 = 123
print(v2, "is iterable:", is_iter(v2))

```

_Hint_: If **v** refers to an iterable, then **sum(v)** is the sum of the values in the iterable, and **len(v)** is the length of the iterable. You can use these to help with your implementation of your improved **mean()** function.

Uncomment these test statements in **mystats.py** to test that your improved **mean()** function is working correctly. (The test **print()** functions from part (b) should also continue to work, except of course for the call of **main()** with no argument, which should be commented out.)
```python
print('mean([1,1,1,2]) should be 1.25, and is:',
                               mean([1,1,1,2]))
print('mean((1,), 2, 3, [4,6]) should be 3.2,' +
      'and is:', mean((1,), 2, 3, [4,6]))
```

Run the module and confirm success.

- d. At the top of your **mystats.py** file, insert the line:

```python
import numpy as np*
```

so that we can use NumPy's random number generator functions. (We will do more with NumPy in part (3) below.)

**np.random.randn()** with no argument will return a single random draw from the standard Normal distribution (mean 0.0, standard deviation 1.0, often represented in writing as **Norm(0,1)**). Add this code to the end of your program to display ten draws from Norm(0,1):

```python
for i in range(10):
	print("Draw", i, "from Norm(0,1):", np.random.randn())

```

At the end of your program, use **list** comprehension to create a **list** of 50 draws from Norm(0,1). Then, test your **mean()** function on this **list** , like this:

```python
ls50 = ... list comprehension ...
print("Mean of", len(ls50), "values from Norm(0,1):",mean(ls50))
```

The displayed mean should be "close to" 0.0. If the random number generator is "truly random" then the mean should tend closer to 0.0 as the number of draws in the sample increases. Perform another test using 10,000 draws, like this:
```python
ls10000 = ... list comprehension ...
print("Mean of", len(ls10000), "values from " +
           "Norm(0,1):", mean(ls10000))

```

Is the displayed mean "closer to" 0.0 than before? Of course, this is a casual test, not a rigorous test.

- e. We can set the _seed_ value for the random number generator with:
```python
np.random.seed(seed)
```

Set the seed to **0** , then create an **ndarray** of 10 random draws from Norm(0,1) as we illustrated in lecture. Add this code at the end of your program; run the module and confirm success.
```python
a1 = np.random.randn(10)
print("a1:", a1)    # should display an ndarray of 10 values

```

An **ndarray** object is iterable, so your **mean()** functions should process **a1** just fine.
Add this code at the end of your program, then run the module.
```python
print("the mean of a1 is:", mean(a1))
```
Since you set the seed to 0.0 prior to this, you should get the same value that I do:
**0.7380231707288347**
- f. Define the **stddev()** function to compute the _sample standard deviation_ of its arguments, where the arguments can be the same as those passed to the **mean()** function. Add this code at the end of your program, then run the module.
```phyton
print("the stddev of a1 is:", stddev(a1))
```

If you have defined **stddev()** correctly, you should get the same value that I do:
**1.0193909949356386**

- g. Define the **median()** function to compute the _median_ of its arguments, where the arguments can be the same as those passed to the **mean()** function. Add this code at the end of your program, then run the module.
```
print("the median of a1 is:", median(a1))
```

If you have defined **median()** correctly, you should get the same value that I do:
**0.6803434597319808**

Then, add this code at the end of your program, and run the module.

```python
print("median(3, 1, 5, 9, 2):", median(3, 1, 5, 9, 2))
```
If you have defined **median()** correctly, you should get **3**.

- h. Define the **mode()** function to compute the _mode_ of its arguments, where the arguments can be the same as those passed to the **mean()** function. The mode is usually used with integer counts, rather than floating point values. Since a data set can be _multimodal_ (that is, have two or more values that each occur "most often"), your **mode()** function should return a **tuple** of modal values. _Hint:_ You may find a **dict** useful for keeping track of how often each value occurs. You can use _v_ **in** _d_ to test whether _v_ is a key in dictionary _d_.

Add this code at the end of your program, then run the module.
```python
print("mode(1, 2, (1, 3), 3, [1, 3, 4]) is:", mode(1, 2, (1, 3), 3, [1, 3, 4]))
```

If you have defined **mode()** correctly, you should get either **(1, 3)** or **(3, 1)**, since 1 and 3 each occur 3 times in the argument list, whereas 2 and 4 only occur one time each.
* * *
### 3. **(10 points) Modules**

- a. Open the **my\_stat\_test.py** file (uploaded to Canvas as part of this homework) for editing and running with Python. You will see that **my\_stat\_test.py** contains several tests of the functions that you developed in **mystats.py** , such as:
```phthon
print("mean of int_list1:", ms.mean(int_list1))
```
It also makes use of some more random number generator functions, **rand()** and **randint()**, that you should learn about in the Python NumPy documentation.

Add an appropriate **import** statement at the top of **my\_stat\_test.py** so that **mystats.py** is imported with the abbreviated name **ms**. Run the **my\_stat\_test.py** module. You should see that it works, but all of the testing code in **mystats.py** is also executed when **mystats.py** is imported. This is not the behavior that an importer of a library expects.

- b. Modify **mystats.py** so that its testing code is only executed when **mystats.py** is the main module. Then, run **my\_stat\_test.py** as the main module, and confirm that although the functions defined in **mystats.py** are available in **my\_stat\_test.py** , the testing code in **mystats.py** is _not_ executed when **mystats.py** is imported.
* * *
### 4. **(30 points) NumPy**
- a. In lecture, we introduced NumPy and its N-dimensional array type, **ndarray**. We looked at ways to create **ndarray** objects, and at three ways for accessing rows/columns/sections of an **ndarray** : slices, Boolean indexes, and "fancy" or integer indexes.

There is _much_ more to NumPy than we have time to talk about. In Python for Data Analysis, 2nd Ed., read through sections 4.2: Universal Functions, 4.3: Array-Oriented Programming, and 4.4: File Input and Output, and try out all of the examples in a Jupyter notebook.
* * *
***When finished, put your hw3.1.py, mystats.py and my_stat_test.py source code files and your Jupyter notebook into a zip archive named TeamN_HW3.zip file, where N is your team number, then upload your .zip archive to Canvas.***
