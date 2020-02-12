"""
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
"""


input_string = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"

#output should be "542 -214"


def high_and_low(numbers):
	l = numbers.split(" ")
	l = sorted(l, key=int)
	print (l[-1] + " " + l[0])


def main():
	high_and_low(input_string)


if __name__ == "__main__": main()