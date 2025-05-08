Q = 256
B = 101


def get_hash(text):
    global Q, B
    result = 0
    for symbol in text:
        result = (B * result + ord(symbol)) % Q
    return result


def rabin_karp_search(haystack, needle):
    global Q, B
    needle_len = len(needle)
    haystack_len = len(haystack)

    if needle_len > haystack_len:
        return []



    power = 1
    for i in range(needle_len - 1):
        power = (power * B) % Q

    needle_hash = get_hash(needle)
    haystack_hash = get_hash(haystack[:needle_len])
    result_positions = []

    for index in range(haystack_len - needle_len + 1):
        if needle_hash == haystack_hash:
            if haystack[index: index + needle_len] == needle:
                result_positions.append(index)

        if index < haystack_len - needle_len:
            haystack_hash = (
                                    (haystack_hash - ord(haystack[index]) * power ) * B
                                    + ord(haystack[index + needle_len])
                            ) % Q

            if haystack_hash < 0:
                haystack_hash += Q

    return result_positions


haystack = "abcxabcdabcdabcy"
needle = "ab"
print(rabin_karp_search(haystack, needle))
