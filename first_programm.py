user_string = input("Enter please: ")
user_string = str(user_string)
user_feedback_hi = "Goodbye"
user_feedback_else = "Tell me: Hi"

if user_string == "Hi":
    print(user_feedback_hi)
else:
    print(user_feedback_else)