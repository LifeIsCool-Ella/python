print("Python", "Java","JavaScript", sep=",")
print("Python", "Java","JavaScript", sep=",", end="?")
print("무엇이 더 재밌을까요?")

import sys 
print("Python", "Java", file=sys.stdout)
print("python", "Java", file=sys.stderr)