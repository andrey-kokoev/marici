# Source row manifests need exact rational ordered encoding

Fresh `check_exact_source_row_encoding.py` normalizes integer and exact fraction string row normals/bounds to reduced rational strings before hashing a versioned ORDERED row sequence. Integer `1`, string `1/1` and `2/2` agree where mathematically equal; reordering rows changes digest because multiplier coordinates depend on row positions. Float `1.0`, JSON Boolean `true`, decimal string `1.0` and exponent string `1e0` are refused rather than silently coerced.

This digest distinguishes local mathematical source matrices under a specified encoding, not an owner-issued source or a signature. Analytic S,A,R,C,G mapping deferred.

Next test NEGATIVE ZERO and alternative numerator/denominator signs: accept only the documented integer/fraction grammar, normalize `-0` to `0`, and refuse denominator sign notation not in the grammar. Require that unusual lexical variants do not create inconsistent row digests.
