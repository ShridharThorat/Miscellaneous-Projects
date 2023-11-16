# crude
def pattern_search(text, pattern):
    for index in range(len(text)):
        match_count = 0
        for char in range(len(pattern)):
            if pattern[char] == text[index+char]:
                match_count += 1
            else:
                break

# Define pattern_search


def pattern_search(text, pattern):
    print("Searching for `{}` in the text below:".format(pattern))
    print(text)
    if len(text) == 0 or len(pattern) == 0:
        return False
    elif len(text) < len(pattern):
        return False

    last_starting_index = len(text) - len(pattern) + 1
    for i in range(0, last_starting_index):
        if text[i:i+len(pattern)] == pattern:
            print("{} found at {} in text".format(pattern, i))

    print()


text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern = "NEEDLE"
# Invoke pattern_search
pattern_search(text, pattern)

# New inputs to test
text2 = "SOMEMORERANDOMWORDSTOpatternSEARCHTHROUGH"
pattern2 = "pattern"
text3 = "This   still      works with    spaces"
pattern3 = "works"
text4 = "722615457824612704202682179992552072047396"
pattern4 = "42"
pattern_search(text2, pattern2)
pattern_search(text3, pattern3)
pattern_search(text4, pattern4)
