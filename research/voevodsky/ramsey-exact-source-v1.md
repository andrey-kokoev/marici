# Uniform exact translated source inputs

This is a source-interpretation result on `native-task-package-lift`. It constructs the missing geometric inputs in an explicit exact-integer local-PN model, rather than assuming an all-N array of opaque strings. It does **not** identify that model with the entire intended operational space.

## All-index construction and completeness

Let p=(x,y,z) be an integer triple with even sum. Define

delta(p)=(-(x+y+z), x+y-z, x+z-y, y+z-x)/2.

Each coordinate is integral: subtracting twice a coordinate from the even total preserves parity. The four coordinates sum to zero. Conversely a zero-sum shift (-a-b-c,a,b,c) has marked point (a+b,a+c,b+c). Substituting the displayed inverse gives p exactly; solving the same three linear equations gives a,b,c uniquely. This is an all-index proof, not an inference from a bounded replay.

For any N>=0, loop over the finite integer cube [-N,N]^3 and retain precisely the even-sum triples. Every required point appears once, no other point appears, and the nested loops terminate after (2N+1)^3 iterations. L_0 contains exactly the origin. Equivalently, the formal region is the type of source shifts whose projected coordinates have absolute values at most N. The inverse above proves these representations equivalent and the formal region finite. This finiteness/completeness proof is written mathematics, not kernel certification of the executable enumerator.

## Derived full local references

At delta, translate the five canonical reference vectors

C0=e0, M0=e1, C1=e2, M1=e3, C2=-e0+e1+e3.

The P primitive has C0,M0,C1,M1; the N primitive has M0,C1,M1,C2 and belongs to the fixed split octahedron at delta-e0. They share exactly the complete M0,C1,M1 face. Translation preserves distinctness, primitive faces, owner incidence and the outside C2 reference. It preserves every equality and candidate-face test in the declared integer geometry/completeP/PN validation rules. Thus the canonical local completion and PN interface translate to every delta; no arbitrary new move is introduced.

The PN permutation is (3,1,2,0,4), not a four-coordinate truncation. Its square is identity and its phase increment is zero. The formal source computes all five references and both primitive bodies from a single source shift. Its actual C0 projection is the indexed point by construction; an origin context cannot independently be relabelled 110 as in the previous opaque interface.

## Source policy, queries and substitution

For each radius the prepared-input policy admits exactly the derived context/color rows indexed by the bounded source region. It is fixed before requests and independent of any monochromatic answer. Existing native WG P/E rules construct the whole input family, a word-indexed program and the requested query; all three histories are retained.

A supplied pattern is converted to source shifts using the inverse. The word sum is computed in source-shift coordinates. The formal projection homomorphism proves its actual marked point equals the sum of the original pattern points. Decidable exact bounds produce either a region index with its membership proof or a retained nonmembership certificate, without a caller-supplied selected index. Variable-word substitution uses the same source policy; the formal projected base-plus-repeat equation and the previous positive-multiplicity theorem give the positive-integral geometric homothety law.

Colors are the supplied complete coloring evaluated at these derived points, not independent inconsistent labels for duplicate positions. Across cutoffs the context at a common point is exactly the same intrinsic record. Under restriction of the coloring this yields the literal seed-policy inclusion; the recursive seed/apply transport from the earlier construction then preserves native derivation states and rule histories. No equivalence of the larger whole input package with the smaller one follows.

## Namespace comparison and operational boundary

Exact contexts use intrinsic coordinate-scoped identifiers, not mutable heap ordinals. A legacy comparison explicitly renames its two cell/chart/packet identifiers and PN operation identifier, checks all five references, both bodies, owner origins, phase windows, shared face and complete permutation, and retains the **whole original record** beside the exact record and witness. It is not a literal seed-policy identity or a complete-cache isomorphism.

Exact decimal BigInt arithmetic realizes the construction without machine-integer rounding. Tests at very large translated points exercise this exact model only. They do not show the existing Number-valued `makeLatticeItem`/geometry API executes all integer inputs exactly. The all-index geometry argument establishes the exact interpretation of its local laws; runtime legacy binding is bounded evidence for that local interpretation.

The remaining admission question is substantive: does this exact prepared source interpretation embed incidence- and operation-preservingly into the intended full operational space, including the required continuations and policy? A local PN renaming is not that global map. Physical policy admission, canonical-leaf reachability, global occupied assembly, autonomous native forcing and all-operation/cache equivalence are not asserted.

## Verification scope

Kernel checks cover derived references, actual point binding, shared face, five-slot PN permutation, projected addition/word sums, uniform bounds, actual native input/program/query histories, point/color squares and projected substitution. D3 completeness and local source-law covariance are the written all-index arguments above, supported by independent exact controls and bounded source API replay. Sector JavaScript is not kernel interpreted.

The initial trials (`ac15f2c2466a3f5c`, `97cce398c646778a`) passed the exact/source controls but stopped at Agda notation errors (qualified module import, then parenthesizing negation inside a rule-parameter tuple). These are verification-code repairs, not geometric counterexamples. Revised sources are refrozen before rerunning.

Artifacts: `contracts/ramsey-exact-source-attempt.v1.json`, `ramsey-exact-source.mjs`, `agda/RamseyExactSource.agda`, `checkers/check_ramsey_exact_source.py`, and `results/ramsey-exact-source-v1.json`.
