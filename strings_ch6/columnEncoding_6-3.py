# Convert a spreadsheet column id to the corresponding integer
# A = 1, D = 4, AA = 27, ZZ = 702

def ss_decode_col_id(col):
    base = 26 ** (len(col) - 1)

    answer = 0
    for c in col:
        answer += (ord(c) - ord('A') + 1) * base
        base //= 26

    return answer

if __name__ == "__main__":
    print(ss_decode_col_id('ZY'))