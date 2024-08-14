import tkinter as tk

root = tk.Tk()
root.geometry("800x600")
root.title("Tkinter Homeworks")

def create_scrollable_frame(container):
    canvas = tk.Canvas(container, borderwidth=0, bg="#f0f0f0")
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    return scrollable_frame

def homework1_page():
    homework1_frame = create_scrollable_frame(main_frame)
    text = """Python Built-in Functions Examples:

1. abs()
print(abs(-5))    Output: 5

2. all()
print(all([True, True, False]))    Output: False

3. any()
print(any([True, False, False]))    Output: True

4. ascii()
print(ascii('ä'))    Output: '\xe4'

5. bin()
print(bin(10))    Output: '0b1010'

6. bool()
print(bool(0))    Output: False

7. bytearray()
print(bytearray([65, 66, 67]))    Output: bytearray(b'ABC')

8. bytes()
print(bytes([65, 66, 67]))    Output: b'ABC'

9. callable()
def example_func():
    pass
print(callable(example_func))    Output: True

10. chr()
print(chr(97))    Output: 'a'

11. classmethod()
class Example:
    @classmethod
    def demo(cls):
        return 'class method called'
print(Example.demo())    Output: 'class method called'

12. compile()
code = compile('print(5)', 'test', 'exec')
exec(code)    Output: 5

13. complex()
print(complex(1, 2))    Output: (1+2j)

14. delattr()
class Person:
    name = "John"
p = Person()
delattr(p, 'name')
print(p.name)  This would raise an AttributeError

15. dict()
print(dict(a=1, b=2))    Output: {'a': 1, 'b': 2}

16. dir()
print(dir([]))    Output: [..., '__len__', '__lt__', ...]

17. divmod()
print(divmod(10, 3))    Output: (3, 1)

18. enumerate()
for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)
Output: 
0 a
1 b
2 c

19. eval()
print(eval('1 + 2'))    Output: 3

20. exec()
exec('print("Hello, World!")')    Output: Hello, World!

21. filter()
print(list(filter(lambda x: x > 0, [-1, 0, 1, 2])))    Output: [1, 2]

22. float()
print(float('3.14'))    Output: 3.14

23. format()
print(format(255, '02x'))    Output: 'ff'

24. frozenset()
print(frozenset([1, 2, 3]))    Output: frozenset({1, 2, 3})

25. getattr()
class Car:
    color = "blue"
c = Car()
print(getattr(c, 'color'))    Output: 'blue'

26. globals()
print(globals())  Outputs the global namespace as a dictionary

27. hasattr()
print(hasattr(c, 'color'))    Output: True

28. hash()
print(hash('test'))    Output: hash value (int)

29. help()
help(print)    Uncomment to see the help text for print function

30. hex()
print(hex(255))    Output: '0xff'

31. id()
print(id(c))    Output: Unique identifier for c

32. input()
name = input("Enter your name: ")    Uncomment to use

33. int()
print(int('10'))    Output: 10

34. isinstance()
print(isinstance(5, int))    Output: True

35. issubclass()
class A:
    pass
class B(A):
    pass
print(issubclass(B, A))    Output: True

36. iter()
my_list = iter([1, 2, 3])
print(next(my_list))    Output: 1

37. len()
print(len("Hello"))    Output: 5

38. list()
print(list((1, 2, 3)))    Output: [1, 2, 3]

39. locals()
def example():
    a = 1
    print(locals())
example()    Output: {'a': 1}

40. map()
print(list(map(lambda x: x * 2, [1, 2, 3])))    Output: [2, 4, 6]

41. max()
print(max(1, 2, 3))    Output: 3

42. memoryview()
m = memoryview(b'abc')
print(m[0])    Output: 97

43. min()
print(min(1, 2, 3))    Output: 1

44. next()
print(next(iter([1, 2, 3])))    Output: 1

45. object()
print(object())    Output: <object object at 0x...>

46. oct()
print(oct(8))    Output: '0o10'

47. open()
file = open('test.txt', 'w')  # Uncomment to use

48. ord()
print(ord('a'))    Output: 97

49. pow()
print(pow(2, 3))    Output: 8

50. print()
print("Hello, World!")    Output: Hello, World!

51. property()
class Student:
    def __init__(self, age):
        self._age = age
    
    @property
    def age(self):
        return self._age
s = Student(20)
print(s.age)    Output: 20

52. range()
print(list(range(5)))    Output: [0, 1, 2, 3, 4]

53. repr()
print(repr("Hello"))    Output: "'Hello'"

54. reversed()
print(list(reversed([1, 2, 3])))    Output: [3, 2, 1]

55. round()
print(round(3.14159, 2))    Output: 3.14

56. set()
print(set([1, 2, 2, 3]))    Output: {1, 2, 3}

57. setattr()
setattr(c, 'color', 'red')
print(c.color)    Output: 'red'

58. slice()
s = slice(1, 5, 2)
print([0, 1, 2, 3, 4, 5][s])    Output: [1, 3]

59. sorted()
print(sorted([3, 1, 2]))    Output: [1, 2, 3]

60. staticmethod()
class MyClass:
    @staticmethod
    def static_method():
        return 'static method called'
print(MyClass.static_method())    Output: 'static method called'

61. str()
print(str(123))    Output: '123'

62. sum()
print(sum([1, 2, 3]))    Output: 6

63. super()
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        super().show()
        print("Child")

c = Child()
c.show()
Output: 
Parent
Child

64. tuple()
print(tuple([1, 2, 3]))    Output: (1, 2, 3)

65. type()
print(type(123))    Output: <class 'int'>

66. vars()
print(vars(c))    Output: {}

67. zip()
print(list(zip([1, 2, 3], ['a', 'b', 'c'])))    Output: [(1, 'a'), (2, 'b'), (3, 'c')]

68. __import__()
math_module = __import__('math')
print(math_module.sqrt(4))    Output: 2.0
    """
    lb = tk.Label(homework1_frame, text=text, bg="#f0f0f0", font=('Helvetica', 12), justify=tk.LEFT)
    lb.pack(pady=20, padx=20)

def homework2_page():
    homework2_frame = create_scrollable_frame(main_frame)
    text = """Fibonacci Sequence using Recursive Function:

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Example usage
    """
    lb = tk.Label(homework2_frame, text=text, bg="#f0f0f0", font=('Helvetica', 12), justify=tk.LEFT)
    lb.pack(pady=20, padx=20)

def homework3_page():
    homework3_frame = create_scrollable_frame(main_frame)
    text = """Tower of Hanoi using Recursive Function:

def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, auxiliary, destination, source)

tower_of_hanoi(3, 'A', 'C', 'B')  # Example usage
    """
    lb = tk.Label(homework3_frame, text=text, bg="#f0f0f0", font=('Helvetica', 12), justify=tk.LEFT)
    lb.pack(pady=20, padx=20)

def hide_indicators():
    home1_indicate.config(bg='#f0f0f0')
    home2_indicate.config(bg='#f0f0f0')
    home3_indicate.config(bg='#f0f0f0')

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#007acc')
    delete_pages()
    page()

options_frame = tk.Frame(root, bg='#f0f0f0', highlightbackground='black', highlightthickness=1)

home1_button = tk.Button(options_frame, text='Homework 1', font=('Helvetica', 12), fg='#333', bg='#e6e6e6',
                         activebackground='#d9d9d9', relief='flat',
                         command=lambda: indicate(home1_indicate, homework1_page))
home1_button.grid(row=0, column=1, sticky='w', pady=10, padx=10)

home1_indicate = tk.Label(options_frame, text='', bg='#f0f0f0')
home1_indicate.grid(row=0, column=0, sticky='e', padx=5)

home2_button = tk.Button(options_frame, text='Homework 2', font=('Helvetica', 12), fg='#333', bg='#e6e6e6',
                         activebackground='#d9d9d9', relief='flat',
                         command=lambda: indicate(home2_indicate, homework2_page))
home2_button.grid(row=1, column=1, sticky='w', pady=10, padx=10)

home2_indicate = tk.Label(options_frame, text='', bg='#f0f0f0')
home2_indicate.grid(row=1, column=0, sticky='e', padx=5)

home3_button = tk.Button(options_frame, text='Homework 3', font=('Helvetica', 12), fg='#333', bg='#e6e6e6',
                         activebackground='#d9d9d9', relief='flat',
                         command=lambda: indicate(home3_indicate, homework3_page))
home3_button.grid(row=2, column=1, sticky='w', pady=10, padx=10)

home3_indicate = tk.Label(options_frame, text='', bg='#f0f0f0')
home3_indicate.grid(row=2, column=0, sticky='e', padx=5)

options_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

main_frame = tk.Frame(root, bg='#f0f0f0', highlightbackground='black', highlightthickness=1)
main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()