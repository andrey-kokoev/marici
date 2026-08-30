"""Exact two-ray hostile test of the native versus Gram shell determinant."""

z1 = 1 + 0j
z2 = 0 + 1j
a = (z1 + z2) / 2
b = (z1 - z2) / 2
native_schur = a - b * b / a
native_full = a * native_schur
positive_gram = 1 + b.conjugate() * b

assert native_full == z1 * z2
assert native_schur == z1 * z2 / a
assert positive_gram == 1.5
assert native_full != positive_gram

result = {
    "native_block_factorization_exact": True,
    "native_full_determinant": "i",
    "positive_gram_correction": "3/2",
    "automatic_identification_falsified": True,
    "required_extra_datum": "a source-derived oriented B,-B* coefficient-Betti double",
    "scope": "falsifies automatic relevance, not the abstract positivity identity",
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "two-ray-shell-schur-determinant-falsifier.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")

