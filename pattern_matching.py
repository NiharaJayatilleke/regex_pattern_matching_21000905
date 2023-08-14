def kmp_search_at_position(text, pattern, current_position, pi):
    if current_position > len(text) - len(pattern):
        return False

    matched_characters = 0

    for i in range(len(pattern)):
        if text[i + current_position] != pattern[i]:
            break
        matched_characters += 1

    if matched_characters == len(pattern):
        return True

    if matched_characters == 0:
        return kmp_search_at_position(text, pattern, current_position + 1, pi)

    return kmp_search_at_position(text, pattern, current_position + (matched_characters - pi[matched_characters - 1][1]), pi)

def kmp_search(string, pattern):
    pi_values = []
    for i in range(len(pattern) + 1):
        suffixes = []
        prefixes = []
        max_prefix_length = 0

        sub_pattern = "".join(pattern[:i])
        for j in range(1, i):
            prefixes.append(sub_pattern[:j])
            suffixes.append(sub_pattern[i - j:])

        for j in range(len(prefixes)):
            if prefixes[j] in suffixes:
                if len(prefixes[j]) > max_prefix_length:
                    max_prefix_length = len(prefixes[j])

        if i != 0:
            pi_values.append([pattern[i - 1], max_prefix_length])

    return kmp_search_at_position(string, pattern, 0, pi_values)

def start_of_line(text, pattern):
    if kmp_search(text[: len(pattern) - 1], "".join(pattern[1:])):
        return True
    else:
        return False

def end_of_line(text, pattern):
    if kmp_search(text[len(text) - len(pattern) + 1:], "".join(pattern[0: len(pattern) - 1])):
        return True and regex_search(text, "".join(pattern[:len(pattern) - 1]))
    else:
        return False

def start_of_line_end_of_line(text, pattern):
    if kmp_search(text, "".join(pattern[1: len(pattern) - 1])) and len(text) == len(pattern) - 2:
        return True
    else:
        return False

def regex_search(text, pattern):
    if any(char == '|' for char in pattern):
        return regex_search(text, pattern.split('|')[0]) or regex_search(text, pattern.split('|')[1])

    if pattern[0] == "^" and pattern[-1] == "$":
        return start_of_line_end_of_line(text, pattern)
    elif pattern[0] == "^":
        return start_of_line(text, pattern)
    elif pattern[-1] == "$":
        return end_of_line(text, pattern)
    
    return kmp_search(text, pattern)

