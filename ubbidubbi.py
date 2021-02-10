def ubbi_dubbi(word):
    output = []
    for letter in word:
        if letter in 'aeiou':
            output.append(f'ub{letter}')
            # Why append to a list, and not to
            # a string? To avoid allocating too
            # much memory. For short strings,
            # it’s not a big deal. But for long
            # loops and large strings, it’s a
            # bad idea..
        else:
            output.append(letter)
    return ''.join(output)
print(ubbi_dubbi('python'))