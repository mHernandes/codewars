"""
https://www.codewars.com/kata/52597aa56021e91c93000cb0
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]

Test.assert_equals(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]),["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])
Test.assert_equals(move_zeros([0,1,None,2,False,1,0]),[1,None,2,False,1,0,0])
"""


def move_zeros(lista):
    # Create a list for the zeros
	zeros = []
	new = []
	for element in lista:
    # If element == 0 and not a boolean (as isinstance(True/False, int) -> True)
		if element == 0 and not isinstance(element, bool):
			zeros.append(element)
		else:
			new.append(element)
	return new + zeros


teste = [1, False, 0, True, 2, 3, "a", None]


def main():
	move_zeros(teste)


if __name__ == "__main__": main()