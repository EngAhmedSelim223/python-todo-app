# import json
# with open("files/questions.json", "r", encoding="utf-8") as f:
#     content = f.read()
# questions = json.loads(content)
# result = 0
# print("Let's begin this Quiz...")
# for q in questions:
#     print(q["question"])
#     for number, answer in enumerate(q["answers"]):
#         print(f"{number + 1} - {answer}")
#     user_answer = int(input("Enter your answer number: "))
#     if user_answer == q["correct"]:
#         result += 1
# print(f"Your Score is: {result} / {len(questions)}")
import random
lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))
result = random.randint(lower_bound, upper_bound)
print(result)
