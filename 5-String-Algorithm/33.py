def bad_char_heuristic(pattern, size):
    bad_char = [-1] * 256  # assuming extended ASCII charset

    for i in range(size):
        bad_char[ord(pattern[i])] = i

    return bad_char

def BoyerMoore(text, pattern):
    m = len(pattern)
    n = len(text)

    # Preprocess bad character heuristic
    bad_char = bad_char_heuristic(pattern, m)

    s = 0  # s is the shift of the pattern with respect to the text
    while s <= n - m:
        j = m - 1

        # Keep reducing index j while pattern and text characters are matching
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            print(f"Pattern occurs at index {s}")
            s += (m - bad_char[ord(text[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - bad_char[ord(text[s + j])])


text = "ABAAABCDABCABC"
pattern = "ABC"
BoyerMoore(text, pattern)
