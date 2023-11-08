"""Practicing for in loops in class."""

# Example 2 in code. 
pets: list[str] = ["Louie", "Bo", "Bear"]
for elem in pets:
    print(f"Good boy, {(elem)}!")

# Example of using range() in a for... in loop. 
names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0,3): 
    elem: str = names[idx]
    print(f"{idx} : {elem}")


