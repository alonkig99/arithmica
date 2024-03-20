import arithmica
print("Welcome To Arithmica Interpreter. Type man for manual")
while True:
    user_input = input(">>> ").strip()
    if user_input.lower() == 'exit':

        break

    try:
        result = arithmica.run(user_input)
        print(result)
    except Exception as e:
        print("Error:", e)





