import re

# At least 8 char long
# Contain any sort of letters, numbers,$%#@
# Has to end with number

password = "thisisatestpassword1"

pattern = r"[a-zA-Z0-9$%#@]{7,}\d"

if re.fullmatch(pattern, password):
    print("valid")
else:
    print("invalid")
