def check_input(element):
    return isinstance(element, str)

def get_substring(s):
    start = 0
    max_length = 0
    max_substring = ""
    seen = {}

    for i, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = i
        current_length = i - start + 1

        if current_length > max_length:
            max_length = current_length
            max_substring = s[start:i + 1]

    return max_substring

def main(lst):
    max_index = -1
    max_length = 0
    longest_string = ""

    for i, element in enumerate(lst):
        if check_input(element) and len(element) > max_length:
            max_length = len(element)
            longest_string = element
            max_index = i

    if max_index == -1:
        print(-1, "")
    else:
        longest_substring = get_substring(longest_string)
        print(max_index, repr(longest_substring))