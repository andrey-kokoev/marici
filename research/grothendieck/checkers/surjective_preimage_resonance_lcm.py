from math import gcd, lcm


cases = [
    {
        "name": "(S3xC5)->S3 over A3",
        "kernel_label": 5,
        "target_label": 6,
        "preimage_label": 30,
    },
    {
        "name": "Q8->C2xC2 over C2",
        "kernel_label": 2,
        "target_label": 2,
        "preimage_label": 2,
    },
]

for case in cases:
    assert case["preimage_label"] == lcm(case["kernel_label"], case["target_label"])
    indices = range(1, 61)
    U_kernel = {n for n in indices if gcd(n, case["kernel_label"]) == 1}
    U_target = {n for n in indices if gcd(n, case["target_label"]) == 1}
    U_preimage = {n for n in indices if gcd(n, case["preimage_label"]) == 1}
    assert U_preimage == U_kernel & U_target
    case["spectrum_sizes_1_to_60"] = [len(U_kernel), len(U_target), len(U_preimage)]

print({"cases": cases, "checks": "pass"})
