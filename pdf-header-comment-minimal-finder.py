#!/usr/bin/env python3

import sys

# import z3

# b1, b2, b3, b4 = z3.BitVecs('b1 b2 b3 b4', 8)

# s = z3.Solver()

# # High bit set constraints
# s.add(b1 >= 0x80, b2 >= 0x80, b3 >= 0x80, b4 >= 0x80)

# # UTF-8 constraints for two 2-byte characters
# # First byte of each 2-byte character should be between 0xC2 and 0xDF
# s.add(0xC2 <= b1, b1 <= 0xDF)
# s.add(0x80 <= b2, b2 <= 0xBF)
# s.add(0xC2 <= b3, b3 <= 0xDF)
# s.add(0x80 <= b4, b4 <= 0xBF)

results_str = []
results_bytes = []
# finished = False
# while True:
#     check_res = s.check()
#     if check_res != z3.sat:
#         finished = True
#         break
#     m = s.model()
#     result_bytes = bytes((m[b1].as_long(), m[b2].as_long(), m[b3].as_long(), m[b4].as_long()))
#     results_bytes.append(result_bytes)
#     results_str.append(result_bytes.decode())
#     # Block the current solution
#     s.add(z3.Or(b1 != result_bytes[0], b2 != result_bytes[1], b3 != result_bytes[2], b4 != result_bytes[3]))


finished = False
num_tries = 0
num_failures = 0
for b1 in range(0xC2, 0xE0):
    for b2 in range(0x80, 0xC0):
        num_tries += 1
        sbytes = bytes((b1, b2))
        try:
            s = sbytes.decode()
            results_bytes.append(sbytes)
            results_str.append(s)
        except UnicodeDecodeError:
            num_failures += 1
            continue

finished = True

print(
    f"Finished: {finished} Number of tries: {num_tries} Number of failures: {num_failures} Number of results: {len(results_bytes)}",
    file=sys.stderr,
    flush=True,
)
sys.stdout.flush()
sys.stderr.flush()

for i in range(len(results_bytes)):
    s = results_str[i]
    b = results_bytes[i]
    print(f"UTF-8 String: '{s}'{' ' * (4 - len(s))}, Hex: {' '.join(f'0x{x:02x}' for x in b)}")
