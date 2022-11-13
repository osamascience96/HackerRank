Regex_pattern = r'hackerrank'

import re
Test_String = input()
match = re.findall(Regex_pattern, Test_String)

print("Number of matches: ", len(match))