#KMP algorithm
def kmpsearch(pattern, text):
    lps = [0] * len(pattern)
    j = 0
    i = 1
    
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                lps[i] = 0
                i += 1
    i = 0
    j = 0
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            print(f"pattern found at index {i-j}")
            j = lps[j-1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
text = "asdfjldnfkdjfgkdfg"
pattern = "asdf"
kmpsearch(pattern,text)
            
