# Singly Linked List in Python

This project implements a **Singly Linked List (SLL)** in Python with the following operations:  
- Append values (at the end)  
- Insert values (at specific index or at the front)  
- Remove values (front, end, by index, or by value)  
- Change a node’s value at a given index  
- Reverse the list  
- Check if the list is empty  
- String representation of the list  

---

## 🐍 1. Basic Usage (easiest way)

If you just want to try the list without installing anything, copy **`linked_list.py`** into the same folder as your project and use:

```python
from linked_list import LinkedList

sll = LinkedList()
sll.append(10)
sll.append(20)
sll.append(30)

print(sll)  # Output: 10 -> 20 -> 30
```

---

## 📦 2. Advanced Usage (install as a package)

If you want to use this as a Python package, you first need **Git installed**.  
👉 [Download Git](https://git-scm.com/downloads) if you don’t already have it.

Then install directly from GitHub using pip:

```bash
pip install git+https://github.com/Ahmedhm1/Linked-List-Python.git
```

Now you can import it anywhere:

```python
from linked_list import LinkedList

sll = LinkedList()
sll.append(5)
sll.append(15)
sll.append(25)
print(sll)  # Output: 5 -> 15 -> 25
```

---

## 🔎 Example Usage

```python
from linked_list import LinkedList

# Create list and insert values
sll = LinkedList()
sll.append(10)
sll.append(20)
sll.insert(5, 0)       # Insert 5 at index 0 (front)
sll.insert(15, 2)      # Insert 15 at index 2

print(sll)  # 5 -> 10 -> 15 -> 20

# Remove values
sll.delete_front()     # Removes 5
sll.pop()              # Removes 20
sll.delete_value(15)   # Removes node with value 15
sll.delete_index(0)    # Removes node at index 0 (now 10)

# Change a value
sll.append(99)
sll.change_value(100, 0)  # Change first element to 100

# Reverse the list
sll.reverse()
print(sll)

# Check if empty
print(sll.is_empty())  # False
```

---

## 📂 Project Structure
```
Linked-List-Python/
│
├── linked_list/            # Package source code
│   ├── __init__.py         # Exports LinkedList
│   └── linked_list.py      # SLL implementation
│
├── test.py                 # Example test file
├── setup.py                # Package setup script
├── pyproject.toml          # (Optional) modern build file
└── README.md
```

---

## 📖 Source Code
➡️ [View `linked_list.py`](./linked_list/linked_list.py) directly if you just want to read the implementation.
