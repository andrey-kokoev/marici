# 3983 — Endpoint Non-Descent Forbids a Descended Joint Infinity Map

Status: retracted by Entry 3987. Its categorical implication was valid conditionally, but the claimed endpoint non-descent premise was false.

## Functorial obstruction

Suppose the physical infinity target is a relative extension
\[
0\longrightarrow W_{\rm compact}
\longrightarrow W_{\rm joint}
\xrightarrow{\pi}
W_{\rm endpoint}
\longrightarrow0.
\]

If a primal map
\[
q:V_{26}\longrightarrow W_{\rm joint}
\]
descends through the physical rank-twenty-six quotient, then its composite
\[
\pi q:V_{26}\longrightarrow W_{\rm endpoint}
\]
also descends.

This is formal functoriality. It is independent of a choice of splitting and of whether the extension class is trivial.

Entry 3979 proves at two exact primes that the completed endpoint functional does not descend through the current rank-twenty-six relations. Therefore no descended joint map with that endpoint quotient can exist.

Compact coordinates cannot repair failure of a canonical endpoint quotient.

## Correction to the frontier

The proposal that

- the full compact-plus-endpoint square closes, while
- the canonical endpoint marginal fails,

is impossible when the endpoint map is the quotient morphism \(\pi\) of a source-derived exact sequence.

A nontrivial extension class can obstruct splitting. It cannot obstruct composition with its own quotient map.

Thus Entry 3979's phrase “the next typed object must retain compact and endpoint ports jointly” was too optimistic. Jointness remains geometrically appropriate, but it cannot by itself cure the observed non-descent.

## Remaining alternatives

At least one of the following must hold.

### A. Wrong domain quotient

The twenty-six-dimensional absolute physical quotient is not the domain of the relative infinity residue map. The correct source object must retain a relative boundary or localization cell that was killed in forming \(V_{26}\).

Then the endpoint map may descend from a larger relative complex while failing on the absolute quotient.

### B. Incomplete endpoint morphism

The degree-five through degree-seven packet is not yet the canonical endpoint quotient morphism. A source-derived boundary-current or exact-lift term must alter the endpoint map itself.

This cannot be a compact coordinate added only in the target. It must modify the source-to-endpoint chain map before quotienting.

### C. Misidentified exact relations

The relations used to form the rank-twenty-six presentation are not preserved by the intended relative residue operation. They are legitimate absolute relations but not relative ones.

Then a relative presentation must be derived rather than reusing the absolute quotient.

### D. Normalization defect

The endpoint finite-part construction has a source-normalization or orientation error despite its two-prime replication and degree-five guard.

This remains a live but narrower implementation falsifier.

## Deck-character refinement

Entry 3981 remains valid:

\[
H^1(E\setminus D)=H^1_+\oplus H^1_-,
\qquad
(\dim H^1_+,\dim H^1_-)=(2,5).
\]

The physical \(W^{-1}\) forms lie in \(H^1_-\). But constructing the rank-five target does not evade the functorial obstruction: its canonical residue quotient is still the rank-three anti-invariant endpoint space.

## Next finite test

Audit the formation of the rank-twenty-six quotient against the relative residue operation.

For every generating exact relation \(r\), compute the completed endpoint residue
\[
\operatorname{Res}_{\partial}(r).
\]

Classify the first nonzero result by source provenance:

- discarded relative boundary;
- absolute exact form whose primitive has puncture support;
- missing localization/Gysin term;
- normalization error.

The output should identify the first relation that is exact absolutely but not relatively. That relation determines the missing source cell.

Do not attempt a compact correction until this domain audit closes.

## First relative-relation witnesses

The order-two checker now exports, for each of the three endpoints and at both primes, an explicit normalized relation
[
sum_{i+jleq7}c_{ij}[a^ib^j]=0
quad	ext{in }V_{26},
]
whose completed endpoint residue equals one:
[
sum_{i+jleq7}c_{ij}operatorname{Res}_{partial}(a^ib^j)=1.
]

Each certificate is verified twice:

- its quotient-coordinate sum is zero;
- its endpoint residue is the normalized nonzero unit.

These are constructive witnesses that the absolute quotient kills relative information. They do not yet identify which primitive exact generator creates the loss; tracing each dense relation back through the presentation pivots is the next provenance calculation.

Artifact:

- `research/benincasa/checkers/check_rank26_infinity_order2_endpoint_descent.py`
- `research/benincasa/results/rank26-infinity-order2-endpoint-descent-p32009.json`
- `research/benincasa/results/rank26-infinity-order2-endpoint-descent-p32003.json`

## Scope

This is a categorical consequence of Entries 3979 and 3981. It does not decide which of alternatives A--D is realized.

Sequence claim: \`seqclaim-6a71f21ceccf89cc64870b86\`.
