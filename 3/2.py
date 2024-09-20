file = 'user_input.txt'

try:
    with open(file, 'a') as f:
        f.write(input()+'\n')
except Exception as e:
    print(f"Error: {e}")
