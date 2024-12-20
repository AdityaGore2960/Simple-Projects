def check_password_strength(password):
    points = 0
    feedback_suggestion=[]

    length = len(password)
    if length > 15:
        points = points + 3
    elif length >= 12:
        points = points + 2
    else:
        points = points - 2
        print("Password is of {length} chracters. To make it strong try atleast 15 charcters!")

    if (c.isupper() for c in password):
        points = points + 2
    else:
        print("Add at least one uppercase letter to make password strong.")

    if any(c.islower() for c in password):
        points = points + 2
    else:
        print("Add at least one lowercase letter to make password strong.")

    if any(c.isdigit() for c in password):
        points = points + 2
    else:
        print("Add atleast one digit to make password strong.")

    special_characters = ['@', '$', '!', '%', '*', '?', '&', '_', '-']
    if any(c in special_characters for c in password):
        points = points + 2
    else:
        print("Add atleast one special character like @, $, !, %, *, ?, &, _, -")

    if points < 6:
        strength = "Weak"
    elif points < 10:
        strength = "Moderate"
    else:
        strength = "Strong"

    feedback_suggestion= "\n".join(feedback_suggestion) if feedback_suggestion else "Your password seems secure." 
    
       
    return strength, points, feedback_suggestion

def main():
    password = input("Enter a password.")

    strength, points, feedback_suggestion = check_password_strength(password)
    
    print(f"\nPassword Strength: {strength}")
    print(f"Strength points: {points}")
    print("Feedback for improvement:")
    print(feedback_suggestion)

if __name__ == "__main__":
    main()
