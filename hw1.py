
def read():
	print('> ', end='')
	input()

def main():
    done = False;
    while (done == False):
        equation = read()
        result = evaluate(equation)
        #include something in evaluate so that if the equation is a blank line the result is "Goodbye!" and if it is an error it prints "ERROR"
        if result != "Goodbye!":
        	print(result)
        else:
        	done = True

main()

