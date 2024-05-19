S_BOX = [
    0x6, 0x4, 0xC, 0x5,
    0x0, 0x7, 0x2, 0xE,
    0x1, 0xF, 0x3, 0xD,
    0x8, 0xA, 0x9, 0xB
]

def generate_inverse_s_box(s_box):
    inv_s_box = [0] * len(s_box)
    for i, val in enumerate(s_box):
        inv_s_box[val] = i
    return inv_s_box

INV_S_BOX = generate_inverse_s_box(S_BOX)
def s_block_substitution(data, s_box):
    return s_box[data]

def s_block_inverse_substitution(data, inv_s_box):
    return inv_s_box[data]

PERMUTATION = [3, 1, 2, 0]

def permute(data, permutation):
    permuted_data = 0
    for i, pos in enumerate(permutation):
        bit = (data >> pos) & 1
        permuted_data |= (bit << i)
    return permuted_data

def test_s_block():
    test_data = 0x5
    substituted = s_block_substitution(test_data, S_BOX)
    assert substituted == 0x7
    inversely_substituted = s_block_inverse_substitution(substituted, INV_S_BOX)
    assert inversely_substituted == test_data
    print("S-block test passed.")

def test_p_block():
    test_data = 0b1100
    permuted = permute(test_data, PERMUTATION)
    assert permuted == 0b1001
    print("P-block test passed.")

if __name__ == "__main__":
    test_s_block()
    test_p_block()
  
