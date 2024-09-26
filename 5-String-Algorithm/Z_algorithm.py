def calculate_Z(s):
    Z = [0] * len(s)
    left, right, k = 0, 0, 0

    for i in range(1, len(s)):
        if i > right:
            left, right = i, i
            while right < len(s) and s[right] == s[right - left]:
                right += 1
            Z[i] = right - left
            right -= 1
        else:
            k = i - left
            if Z[k] < right - i + 1:
                Z[i] = Z[k]
            else:
                left = i
                while right < len(s) and s[right] == s[right - left]:
                    right += 1
                Z[i] = right - left
                right -= 1
    return Z

def Z_algo(text, pattern):
    concat = pattern + "$" + text
    Z = calculate_Z(concat)

    pattern_length = len(pattern)
    for i in range(len(Z)):
        if Z[i] == pattern_length:
            print(f"pattern found at index {i - pattern_length - 1}")

text = "abcabdfhdbsdabc"
pattern  = "abc"
Z_algo(text,pattern)
