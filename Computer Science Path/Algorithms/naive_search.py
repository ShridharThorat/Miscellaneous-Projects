# Define pattern_search
def pattern_search(text, pattern):
    if len(text) == 0 or len(pattern) == 0:
        return False
    elif len(text) < len(pattern):
        return False

    last_starting_index = len(text) - len(pattern)
    i = 0
    for i in range(0,last_starting_index):
        if text[i:i+len(pattern)] == pattern:
            return True


text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern = "NEEDLE"
# Invoke pattern_search
print(pattern_search(text, pattern))
