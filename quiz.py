questions = {
    "who is the CM of Andhra Pradesh" : "nara chandra babu naidu",
    "what is the capital of Andhra Pradesh" : "Amaravathi",
    "what is the capital of India" : "New Delhi",
    "who is the prime minister of India" : "Narendra Modi",
    "who is the CM of tamilnadu" : "vijay joseph"
}
score = 0
for question,answer in questions.items():
    print(question)
    user_answer = input("enter your answer: ")
    if user_answer.lower==answer.lower:
        print("correct")
        score += 1
    else:
        print("wrong answer")
print(f"your score is {score}/5")