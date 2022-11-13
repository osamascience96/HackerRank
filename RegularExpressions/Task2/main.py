# ? is used for 0 or 1 occurance frequency only.
# ^$ is used in regex in the beginning and end for the full match
regex_pattern = r"^(.{3}\.?)(.{3}\.?)(.{3}\.?)(.{3}\.?)$" 

import re
import sys

test_string = input()
match = re.match(regex_pattern, test_string) is not None
print(str(match).lower())