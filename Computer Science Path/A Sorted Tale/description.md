# A Sorted Tale
You recently began employment at “A Sorted Tale”, an independent bookshop. Every morning, the owner decides to sort the books in a new way.

Some of his favorite methods include:
- By author name
- By title
- By number of characters in the title
- By the reverse of the author’s name


Throughout the day, patrons of the bookshop remove books from the shelf. Given the strange ordering of the store, they do not always get the books placed back in exactly the correct location.

The owner wants you to research methods of fixing the book ordering throughout the day and sorting the books in the morning. It is currently taking too long!


## Instructions

### Get to know the data

- [x] **1.** The owner provides the current state of the bookshelf in a comma-separated values, or csv, file. To get you started, we have provided a function `load_books`, defined in **utils.py**.<br>
    Within **script.py**, we are loading the books from **books_small.csv**. This list of 10 books makes it easier to determine how the algorithms are behaving. We’ll use this to develop the algorithms and then we’ll try them out later on the larger file.<br>
    Add a `for` loop to print the titles within the bookshelf.
    <br>

    Save your code and run it using **python3 script.py** in the terminal.
    <br>


- [x] **2.** Today’s sorting is by title and looking at the bookshelf it’s pretty close. Some patrons have placed books back in slightly the wrong place.<br>
    Before we start solving the problem, we need to do a bit of data manipulation to ensure that we compare books correctly. **Python’s built-in comparison operators compare letters lexicographically based on their Unicode code point.** You can determine the code point of characters using Python’s built-in `ord` function. For example to calculate the code point for “z” you would use the following code: `ord("z")` 
    <br>


- [x] **3.** You may have noticed that the uppercase letters have values less than their lowercase counterparts. When sorting, we don’t want to take into account the case of the letters. For example, “cats” should come before “Dogs”, even though `ord("c") > ord("D")` is `True`. <br>

    We’ll make this happen by converting everything to lowercase prior to comparison. Since we need to do this often, lets save the lowercase author and title as attributes while loading the bookshelf in **utils.py**: <br>
    - `book['author_lower']`
    - `book['title_lower']`


### Fix the midday errors

- [ ] **4.** As we noted, our books are pretty close to being sorted by title. From the sorting lessons, you may remember that bubble sort performs well for nearly sorted data such as this.

    The code for performing bubble sort on an array of numbers is provided in **sorts.py**. However, we are sorting on books which are Python dictionaries. Further, the owner likes to change the ordering of books daily. To make the sort order flexible, add a parameter `comparison_function`. This will allow us to pass in a custom function for comparing the order of two books.
    <br>

- [x] **5.** Our comparison_function will take two parameters, and return True if the first one is “greater than” the second.

    Within the body of the bubble sort function, modify the comparison conditional statement to use the `comparison_function` instead of the built in operators `(if arr[idx] > arr[idx + 1]:)`.
    <br>


- [x] **6.** Now that we have a bubble sort algorithm that can work on books, let’s give it a shot. Within **script.py** define a sort comparison function, `by_title_ascending`.<br>
    It should take `book_a` and `book_b` as arguments. 
    <br>

    It should return `True` if the `title_lower` of `book_a` is “greater than” the `title_lower` of `book_b` and `False` otherwise.
    <br>    


- [x] **7.** Sort the bookshelf using bubble sort. Save the result as `sort_1` and print the titles to the console to verify the order. 
    How many swaps were necessary? 
    <br>


### A new sorting order

- [x] **8.** The owner of the bookshop wants to sort by the author’s full name tomorrow. Define a new comparison function, `by_author_ascending`, within **script.py**. 
    <br>

    It should take `book_a` and `book_b` as arguments.
    <br>

    It should return `True` if the `author_lower` of `book_a` is “greater than” the `author_lower` of `book_b` and `False` otherwise.
    <br>

- [x] **9.** Our sorting algorithms will alter the original bookshelf, so create a new copy of this data, bookshelf_v1.

    This does **NOT** create a copy:
    ```py
    bookshelf_v1 = bookshelf
    ```
    <br>

- [ ] **10.** Try sorting the list of books, `bookshelf_v1` using the new comparison function and bubble sort. Save the result as `sort_2` and `print` the authors to the console to verify the order.

    How many swaps are needed now?


### A new sorting algorithm

- [x] **11.** The number of swaps is getting to be high for even a small list like this. Let’s try implementing a different type of search: `quicksort`.
    <br>

    The code for quicksort of a numeric array is in **sorts.py**. We need to modify it in a similar fashion that we modified bubble sort.
    <br>

    Add `comparison_function` as the final parameter of the `quicksort()` function.
    <br>


- [x] **12.** Within the `quicksort()` function, be sure to pass `comparison_function` as the final argument for the recursive calls.
<br>

- [x] **13.** The last modification we need to make to `quicksort()` is to update the comparison conditional. It is currently using the built in comparison:
    ```py
    if pivot_element > list[i]:
    ```
    Update this to use `comparison_function`.
    <br>


- [x] **14.** Within **script.py** create another copy of bookshelf called `bookshelf_v2`.
<br>


- [x] **15.** Perform `quicksort()`on `bookshelf_v2` using `by_author_ascending()`. This implementation operates on the input directly, so does not return a list. 
    <br>

    Print the authors from `bookshelf_v2` to ensure they are now sorted correctly.


### The last sort

- [x] **16.** The owner has asked for one last sorting order, sorting by the length of the sum of the number of characters in the book and author’s name.
    <br>

    Create a new comparison function, `by_total_length`. It should return `True` if the sum of characters in the title and author of `book_a` is “greater than” the sum in `book_b` and `False` otherwise.
    <br>


- [x] **17.** Load the long list of books from **books_large.csv** into a new variable, `long_bookshelf`. You can use the same `utils.load_books()` function that we used to load books_small.csv at the beginning of **script.py**.
<br>


- [x] **18.** Run bubble sort on `long_bookshelf` using `by_total_length` as the comparison function. Does it seem slow?
<br>


- [x] **19.** Comment out the bubble sort attempt and now try quicksort using the same comparison function. Does it live up to its name?
<br>


### More sorting

- [x] **20.** You’ve met the requirements of the project by the bookshop owner. If you’d like, play with creating your own comparison operators or other sorting functions.