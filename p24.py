import utils

"""
    Start with the lowest permutation: For your case, that's 012. This is your starting point.

    Find the next permutation:
        Step 1: Look for the rightmost number that's smaller than the number immediately after it. This is your pivot.
        Step 2: Now, look for the smallest number to the right of the pivot that's larger than the pivot itself.
        Step 3: Swap those two numbers.
        Step 4: Reverse the order of all the numbers to the right of where the pivot was.

    Repeat until no more permutations: Keep doing this until there's 
    no number that can serve as a pivot, meaning you've reached the highest permutation.
    
0123
"""

"012 if 1 > 0, or if string[q] > string[i-1] "


def lexicographic_perms_i(string, index):
    string = list(string)
    ciel = utils.factorial_iterative(len(string))
    for p in range(ciel):

        if p == index - 1:
            return ''.join(string)

        # i will act as our pivot
        i = len(string) - 1

        # find the first element from the right hand side that is
        # greater than string[i]
        while i > 0 and string[i - 1] > string[i]:
            i -= 1

        # reverse the string around the pivot
        string[i:] = reversed(string[i:])

        if i > 0:
            q = i
            # find the first element to the left of the pivot such that
            # string[q] > string[i-1]
            while string[i - 1] > string[q]:
                q += 1
            string[i - 1], string[q] = string[q], string[i - 1]


one_mil = 1000_000


# print(lexicographic_perms_i("0123456789", one_mil))
# 2783915460


def permute(a, l, r, ans=[]):
    if l == r:
        ans.append(''.join(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]
    return ans


string = "ABC"
n = len(string)
a = list(string)
print(permute(a, 0, n))
# for i in sorted(ans):
#     print(i)
