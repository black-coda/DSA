def countDown(num: int) -> None:
    print(num)
    if num <= 0:
        # base case
        return
    else:
        # recursive case
        countDown(num - 1)

# callstack

def bye():
    print("Bye!!!")

def greet2(name: str):
    print(f"How are you {name}?")

def greet(name: str):
    print(f"Hello, {name}!!!")
    greet2(name)
    print("getting ready to say bye")
    bye()

if __name__ == "__main__":
    greet("Solo")