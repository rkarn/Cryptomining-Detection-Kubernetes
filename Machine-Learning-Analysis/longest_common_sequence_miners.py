#Longest common sequence of syscalls between the miners.
#https://www.bogotobogo.com/python/python_longest_common_substring_lcs_algorithm_generalized_suffix_tree.php
def lcs(S,T): 
    m = len(S)
    n = len(T)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_set = set()
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(S[i-c+1:i+1])
                elif c == longest:
                    lcs_set.add(S[i-c+1:i+1])

    return lcs_set

#print lcs(syscalldict[syscalldict.keys()[0]],syscalldict[syscalldict.keys()[1]])

#Longest common sequence of syscalls between the miners.
#https://www.geeksforgeeks.org/sequencematcher-in-python-for-longest-common-substring/
from difflib import SequenceMatcher 
def longestSubstring(str1,str2): 
    # initialize SequenceMatcher object with 
    # input string 
    seqMatch = SequenceMatcher(None,str1,str2) 

    # find match of longest sub-string 
    # output will be like Match(a=0, b=0, size=5) 
    match = seqMatch.find_longest_match(0, len(str1), 0, len(str2)) 

    # print longest substring 
    if (match.size!=0): 
        return (str1[match.a: match.a + match.size]) 
    else: 
        print ('No longest common sub-string found') 

if __name__ == "__main__": 
    syscalldict_keys = syscalldict.keys()
    for i in range(len(syscalldict_keys)):
        for j in range(len(syscalldict_keys)):
            if i != j:
                print 'Longest continuous sequence between {0} and {1} is {2}.'.format(syscalldict_keys[i],syscalldict_keys[j],longestSubstring(syscalldict[syscalldict_keys[j]],syscalldict[syscalldict_keys[i]]))
        print '-------------------------------------------------------------------------------'
