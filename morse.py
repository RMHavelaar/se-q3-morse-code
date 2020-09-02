__author__ = 'Robert Havelaar, with help from group c Study group. '

from morse_dict import MORSE_2_ASCII
import re
# This module provides regular expression
# matching operations similar to
# those found in Perl.
#


def decode_bits(bits):
    pattern_one = re.split(r'(0+)', bits.strip('0'))
    unit_rate = len(sorted(pattern_one, key=len)[0])
    results = []
    for match in pattern_one:
        if '1' in match:
            if len(match) // unit_rate == 1:
                results.append('.')
            else:
                results.append('-')
        else:
            if len(match) // unit_rate == 1:
                results.append('')
            elif len(match) // unit_rate == 3:
                results.append(' ')
            else:
                results.append('   ')
    clean = ''.join(results)
    return clean


def decode_morse(morse):
    pattern = re.split(r'(\s+)', morse)
    results = []
    for match in pattern:
        if match == '   ':
            results.append(match)
        elif match in MORSE_2_ASCII:
            results.append(MORSE_2_ASCII[match])
    clean_up = ''.join(results).replace("   ", " ").strip()
    return clean_up


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "11001100110011000000110000001111110011001111110011111100000000000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"  # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
