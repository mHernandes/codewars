"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should 
replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']


https://www.codewars.com/kata/split-strings
"""
#######################################
"""
tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
)
"""


def solution(s):
  if len(s) % 2:
    s += "_"
  return [s[i:i+2] for i in range(0, len(s), 2)]


def main(): 
	teste = 'asdfads'
	solution(teste)


if __name__ == "__main__": main()