import random
print("=" * 40)
print("Welcome to my Quiz!")
print("=" * 40)
print()
name=input("Enter your name : ")
print()
print("Hello " + name.title() + "!")
print()

def classic_way():
    score=0
    choice=input("Enter y(yes) to proceed : ")
    if choice.lower() == "y":
        c1=input("""1.What is the output of print(len("Hello"))?
            a.3
            b.4
            c.5
            d.6
            """).lower()
        if c1 in ["a","b","c","d"]:
            if c1 == "c":
                print("Correct you got it ! ")
                score += 1
            else:
                print("Wrong!") 
        else:     
            print("Invalid input ! ")

        c2=input("""2.Which data type is immutable in Python?
            a. List
            b. Dictionary
            c. Set
            d. Tuple
            """).lower()
        if c2 in ["a","b","c","d"]:
            if c2 == "d":
                print("Correct you got it ! ")
                score += 1
            else:
                print("Wrong!") 
        else:     
            print("Invalid input ! ")

        c3=input("""3.Which keyword is used to define a function in Python?
            a.func
            b.def
            c.define
            d.function
            """).lower()
        if c3 in ["a","b","c","d"]:
            if c3 == "b":
                print("Correct you got it ! ")
                score += 1
            else:
                print("Wrong!") 
        else:     
            print("Invalid input ! ")

        c4=input("""4.What is the output of print(3 * "Hi")?
            a.Hi
            b.HiHiHi
            c.Error
            d.3Hi
            """).lower()
        if c4 in ["a","b","c","d"]:
            if c4 == "b":
                print("Correct you got it ! ")
                score += 1
            else:
                print("Wrong!") 
        else:     
            print("Invalid input ! ")
                    
                    
        c5=input("""5.Which of the following is used for comments in Python?
            a.//
            b.<....>
            c.#
            d.*/
            """).lower()
        if c5 in ["a","b","c","d"]:
            if c5 == "c":
                print("Correct you got it ! ")
                score += 1
            else:
                print("Wrong!") 
        else:     
            print("Invalid input ! ")
                                
    print("=" * 40)
    print("Game Ended ! ")
    print("=" * 40)
    print()
    print(f"{name.title()} you scored {score}")

class random_way:
    def __init__(self):

        self.questions = [

        # 1
        {
            "q": "What is the output of len('Hello')?",
            "options": ["3", "4", "5", "6"],
            "answer": "c"
        },

        # 2
        {
            "q": "Which data type is immutable in Python?",
            "options": ["List", "Dictionary", "Set", "Tuple"],
            "answer": "d"
        },

        # 3
        {
            "q": "Which keyword is used to define a function in Python?",
            "options": ["func", "def", "define", "function"],
            "answer": "b"
        },

        # 4
        {
            "q": "What is the output of print(3 * 'Hi')?",
            "options": ["Hi", "HiHiHi", "Error", "3Hi"],
            "answer": "b"
        },

        # 5
        {
            "q": "Which symbol is used for comments in Python?",
            "options": ["//", "<!-- -->", "#", "/* */"],
            "answer": "c"
        },

        # 6
        {
            "q": "Which data type is used to store True/False values?",
            "options": ["int", "bool", "str", "float"],
            "answer": "b"
        },

        # 7
        {
            "q": "What does the input() function return?",
            "options": ["int", "float", "str", "bool"],
            "answer": "c"
        },

        # 8
        {
            "q": "What is the output of type(5)?",
            "options": ["int", "float", "str", "bool"],
            "answer": "a"
        },

        # 9
        {
            "q": "Which operator is used for exponentiation?",
            "options": ["^", "**", "exp", "//"],
            "answer": "b"
        },

        # 10
        {
            "q": "Which method converts a string to lowercase?",
            "options": ["lower()", "down()", "small()", "toLowerCase()"],
            "answer": "a"
        },

        # 11
        {
            "q": "What is the output of bool(0)?",
            "options": ["True", "False", "None", "0"],
            "answer": "b"
        },

        # 12
        {
            "q": "Which loop is used to iterate over a sequence?",
            "options": ["while", "repeat", "for", "loop"],
            "answer": "c"
        },

        # 13
        {
            "q": "Which method adds an item to a list?",
            "options": ["add()", "insert()", "push()", "append()"],
            "answer": "d"
        },

        # 14
        {
            "q": "What does break do in a loop?",
            "options": ["Stops loop", "Pauses loop", "Skips iteration", "Repeats loop"],
            "answer": "a"
        },

        # 15
        {
            "q": "What is the output of 10 // 3?",
            "options": ["3", "3.33", "4", "Error"],
            "answer": "a"
        },

        # 16
        {
            "q": "How do you start a class definition?",
            "options": ["def class", "class", "define class", "create class"],
            "answer": "b"
        },

        # 17
        {
            "q": "What is the first index of any list?",
            "options": ["0", "1", "-1", "Depends"],
            "answer": "a"
        },

        # 18
        {
            "q": "Which function shows the version of Python?",
            "options": ["python.version()", "version()", "sys.version", "get.version()"],
            "answer": "c"
        },

        # 19
        {
            "q": "Which statement is used to handle exceptions?",
            "options": ["try-except", "handle", "catch", "if-else"],
            "answer": "a"
        },

        # 20
        {
            "q": "Which keyword is used to return a value from a function?",
            "options": ["give", "return", "send", "yield"],
            "answer": "b"
        },]
    def start(self):
        
        choice=input("Enter y(yes) to proceed : ")
        score=0
        
        while choice == "y":
                
                random.shuffle(self.questions)
                for q in self.questions:
                    print("\n" + q["q"])
                    letters=["a","b","c","d"]
                    for i, option in enumerate(q["options"]):
                        print(f"{letters[i]}. {option}")
                    usr=input("Enter option : ").lower()
                    if usr == q["answer"]:
                        print("Correct ! You got it")
                        score += 1
                    else:
                        print("Oops it was wrong ! ")
                    choice = input("Enter y/Y to proceed : ").lower()
                    if choice != "y":
                        break
        print("=" * 40)
        print("Game Ended")
        print("=" * 40)
        print("")     
        print(f"{name.title()} you scored {score}")

random_way().start()


    
          

