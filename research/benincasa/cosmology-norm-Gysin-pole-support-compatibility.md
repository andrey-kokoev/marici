# Norm–Gysin support comparison lacks a base map

Conjecture: every pole of the norm residual lies in the weighted Gysin singular
support.

Exact reduction gives denominator `u*(u-1)*(u-2)*D`, with residues `2` at
`u=0,1,2` and residue `-1` at each simple root of `D`. The Gysin connection's
declared denominator is `s1*s2*s3*Lambda_P` over a different coordinate ring.

Support containment requires a source-derived ring map from
`Q[s1,s2,s3]` to `Q[u]`. No such map is present, so the Gysin divisors cannot be
pulled back and the conjecture is ill-typed under the active source envelope.
This is stronger than merely failing to match named factors.

The next leaf searches the p-locus parametrization artifacts for assignments of
all three `s` variables and tests the pulled-back denominator if they exist.
