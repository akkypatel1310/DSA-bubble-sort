def hash_values(s, prime, modules):
    h = 0
    for char in s:
        h = (h* prime + ord(char)) % modules
    return h

def RabinKarp(text, pattern):
    prime = 101
    modules = 100 ** 9 + 7
    m,n = len(pattern), len(text)
    
    pattern_hash = hash_values(pattern, prime, modules)
    text_hash = hash_values(text[:m],prime, modules)
    
    for i in range(n-m+1):
        if pattern_hash == text_hash:
            if text[i:i+m] == pattern:
                print(f'patternn found at index {i}')
                
    if i < n -m:
        text_hash = (text_hash - ord(text[i]) * prime ** (m-1)) * prime + ord(text[i+m])
        text_hash %= modules
        
text = "abcdefgehabc"
pattern = "abc"
RabinKarp(text,pattern)
