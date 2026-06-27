def has_unique_chars(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i]==s[j]:
                return "NOT UNIQUE" 
    return "TRUE"

print(has_unique_chars("harikrishnan"))
print(has_unique_chars("hema"))
print(has_unique_chars("python"))