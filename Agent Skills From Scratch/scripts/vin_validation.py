#!/usr/bin/env python3
"""
Validate a vehicle identification number (VIN)

Ensure the VIN is 17 alphanumeric characters in lenght
Determine the expected value of the check-digit and compare to the actual value
"""

import argparse
import sys

LETTERS = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
    "J": 1, "K": 2, "L": 3, "M": 4, "N": 5, "P": 7, "R": 9,
    "S": 2, "T": 3, "U": 4, "V": 5, "W": 6, "X": 7, "Y": 8, "Z": 9,
}

WEIGHTS = {
    1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 10,
    9: 0, 10: 9, 11: 8, 12: 7, 13: 6, 14: 5, 15: 4, 16: 3, 17: 2,
}

parser = argparse.ArgumentParser(
        description="Fill a Manufacturer's Certificate of Origin PDF"
    )
parser.add_argument(
    "--vin",
    required=True,
    help="Vehicle Identification Number"
)

args = parser.parse_args()

if len(args.vin) != 17:
    print(f'FAILURE: {args.vin} is not valid VIN. Exepected VIN length of 17 characters but found {len(args.vin)} characters instead.')
    sys.exit(1)

sum_product = 0

for i,v in enumerate(args.vin, 1):
    current_letter_value=LETTERS[v] if v in LETTERS else int(v)
    current_weight_value=WEIGHTS[i]
    product_letter_weight=current_letter_value * current_weight_value
    sum_product = sum_product + product_letter_weight

check_digit= 'X' if sum_product % 11 == 10 else str(sum_product % 11)

is_valid_vin = check_digit == args.vin[8]

if is_valid_vin:
    print(f'SUCCESS: {args.vin} is a valid VIN.')
else:
    print(f'FAILURE: {args.vin} is not valid VIN. Check digit "{check_digit}" was expected but found "{args.vin[8]}" instead.')