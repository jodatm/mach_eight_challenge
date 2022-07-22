# Mach Eight Coding Challenge

This is my implementation of the Mach Eight Code Challenge. 

## Configuration
I used python to solve this problem. It's suggested to create a virtualenv to load the libraries specified in requirements.txt.

`virtualenv env`

`cd env/Scripts`

`activate`

`cd../..`

> **Note:** This commands are for Windows, more information for other operating systems visit [this link](https://virtualenv.pypa.io/en/latest/)


Then you download the dependencies with this command:

`pip install -r requirements.txt`

## Files

**requirements.txt:** Used for downloading the libraries

**mach_eight_challange.py:** In this file its located the function of the code challenge named **find_pairs** 

**find_pairs_test.py:** In this file are locate the unit test using the **pytest** library

## Testing

You can run the unit test using this command

`pytest find_pairs_test.py`


# Complexity

**Complexity Analysis** focus on two main processes:

-  **Hash map construction :**  O(n).  
    A hash map has been used to store **n** players in a dictionary. The maximum length of a given position will be named **k**
- **Find couples:**  O(n*k).  
	The whole array of **n** players is needed to be traversed once.
	In the best scenario, a given player may not have any match so the cost is constant O(1).
	In the worst scenario, a given player may have **k** matches so the cost is O(k).
