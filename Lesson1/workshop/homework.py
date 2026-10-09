

print("Welcome, lets set a program that lets user to send brithday card")
print()
print()
rec_name = input("1. Recipient's name?")
birth_year = int(input ("2. Year of Brith?"))
custom_message = input("3. Your custom message?")
sender_name = input ("4. Sender's name?")

current_year = 2026
age = int(current_year - birth_year)
message = f"""
{rec_name}, let's celebrate your {age} years of awesomeness!
Wishing you a day filled with joy and laughter as you turn {age}!
 
 {custom_message}
 
 With love and best wishes,
 {sender_name}
"""
print(message)


