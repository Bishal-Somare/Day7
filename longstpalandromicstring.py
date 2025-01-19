def longest_palindromic_substring(s):
    if not s:
        return ""

    start, max_length = 0, 0

    def expand_around_center(left, right):
        nonlocal start, max_length
        while left >= 0 and right < len(s) and s[left] == s[right]:
            current_length = right - left + 1
            if current_length > max_length:
                start = left
                max_length = current_length
            left -= 1
            right += 1

    for i in range(len(s)):
        expand_around_center(i, i)      # Odd-length palindromes
        expand_around_center(i, i + 1)  # Even-length palindromes

    return s[start:start + max_length]

# Example Input
string = "babad"
result = longest_palindromic_substring(string)
print(f"Longest Palindromic Substring: {result}")
