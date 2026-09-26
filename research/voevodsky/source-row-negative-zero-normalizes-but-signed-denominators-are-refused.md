# Source row negative zero normalizes but signed denominators are refused

Fresh `check_source_row_zero_grammar.py` admits exact string integer/fraction forms with an optional leading numerator minus and a positive unsigned denominator. It reduces `-0`, `-0/2` and `0/2` to `0` with the same versioned row-bound digest; `-2/4` reduces to `-1/2`. Signed denominators (`1/-2`, `-1/-2`), leading plus, whitespace and zero denominator are refused. Equivalent accepted rationals cannot split a manifest merely through negative-zero spelling.

This is local exact encoding, not a verified issuer's source declaration. Analytic S,A,R,C,G remains deferred.

Next test ROW LABEL aliases: two row manifests with identical ordered coefficient arrays but different stable row occurrence IDs have identical matrix math yet must not share a provenance-bearing source-manifest commitment. Separate math digest from source row-identity digest.
