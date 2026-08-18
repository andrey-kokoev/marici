---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# The Full Soft-Axis Filtered Cokernel Is Quartic Tail Plus a Two-Dimensional Resonance

## Record

Status: full filtered exact-form test following Entries 441--442.

## Hard-to-vary claim

Lower-order terms in the exact-form differential might mix the four
associated-graded quartic generators so strongly that the soft-axis tail
becomes finite or contractible. Alternatively, they might leave precisely
the associated-graded module
[
mathbf F[a,b]/(a^4)
]
with no further filtered extension.

Both claims can be tested on the frozen full soft fibre before introducing
any physical boundary quotient.

## Frozen full fibre

At
[
E=X_2=0
]
the complete, not merely leading, polynomial data are
[
K=a^4,qquad L_1=b+1,qquad L_2=a.
]

All four exact sectors
[
(s_a,s_b)in{(1,1),(1,0),(0,1),(0,0)}
]
are retained. For each polynomial cutoff (D), include every exact-form
generator whose full inhomogeneous image has degree at most (D), and
compute the cumulative image in (mathbf F[a,b]_{le D}).

No boundary quotient, support summand, or fitted truncation is added.

## Exact divisibility

Every full exact-form image is divisible by (a^4), not only its highest
homogeneous symbol. Thus
[
operatorname{im}d_{m ex}subseteq(a^4)
]
on the frozen soft fibre.

The lower term (1) in (L_1=b+1) mixes homogeneous shells but cannot
remove the quartic quotient.

## Computed filtered result

For every tested cutoff
[
12le Dle40,
]
the image has constant codimension two inside the truncated ideal:
[
oxed{
dimoperatorname{im}d_{m ex,le D}
=
dim(a^4)_{le D}-2.
}
]

Since
[
dimigl(mathbf F[a,b]/(a^4)igr)_{le D}=4D-2,
]
the full filtered cokernel satisfies
[
oxed{
dimoperatorname{coker}d_{m ex,le D}=4D.
}
]

Therefore the filtered object is not merely the quartic tail. At the tested
Hilbert-function level it consists of

[
oxed{
	ext{infinite quartic tail}
+
	ext{stable two-dimensional finite resonance}.
}
]

A greedy quotient-basis computation at cutoffs 16 and 20 selected the same
representatives
[
a^4,qquad a^{11}b.
]
These are computational representatives only. They are not asserted to be
a canonical, horizontal, or geometrically split basis.

## Interpretation

The first alternative is falsified: lower-order mixing does not contract or
finitely truncate the quartic tail.

The second alternative is also too small: the complete exact differential
leaves two additional finite classes beyond
(mathbf F[a,b]/(a^4)).

The correct narrow object is a filtered extension whose tested Hilbert
function is that of the quartic module plus length two. No canonical
splitting has been established.

This mirrors the distinction in Nima's recent localization work:

[
	ext{associated symbol}
otRightarrow	ext{complete relative class},
]
while also showing that restoration of lower terms need not erase the
symbol-supported module.

## Comparison with Entry 447

Entry 447 independently constructs the monic Cayley--Menger family
\[
\mathcal M_{CM}=\mathbb Q[u,a,b]/(K),
\]
which is free of rank four over \(\mathbb Q[u,b]\) and has special fibre
\[
\mathcal M_{CM}/u\simeq\mathbb Q[a,b]/(a^4).
\]

The present calculation is therefore the first direct special-fibre
comparison with the actual exact-form image. It shows that the naive
identification
\[
\operatorname{coker}d_{\rm ex}|_{u=0}
\stackrel?=\mathcal M_{CM}/u
\]
is short by a stable two-dimensional piece in the tested filtered range.

This does not falsify Entry 447's flat Cayley--Menger module. It falsifies
only its unextended identification with the complete exact-form cokernel.
The length-two piece must be located in the relative de Rham reduction,
another marked-denominator sector, or a nontrivial extension between them.

## Classification

- existing carrier: unchanged energy/Cut and Cayley--Menger carrier;
- infinite quartic tail: soft-boundary coefficient module;
- two-dimensional excess: finite exact-form coefficient resonance;
- canonical splitting: unproved;
- physical relative-chain annihilation: absent under Entry 442's frozen
  source audit;
- genuinely new carrier datum: none.
- unextended identification with Entry 447's \(\mathcal M_{CM}\): short by
  a tested length-two coefficient piece.

## Epistemic boundary

The rank calculation is exact over one large finite field through cutoff 40.
The stable formulas are verified on (12le Dle40), not proved for all
degrees or in characteristic zero.

Divisibility by (a^4) follows directly from the frozen full formulas.
The length-two excess is a filtered rank result. Its extension class,
multiplication action, Gauss--Manin connection, and nearby-cycle monodromy
remain uncomputed.

## Next falsifier

Compute the induced (a)- and (b)-actions and the first normal
Gauss--Manin operator on the length-two quotient
[
(a^4)/operatorname{im}d_{m ex}.
]
Test whether it is:

1. a split finite Tate/Kummer summand;
2. a nontrivial extension of the quartic tail;
3. killed only after a source-derived sewing operation; or
4. evidence that the finite-field stable range was misleading.

The action and connection must be derived from the frozen differential. No
basis-dependent projection or fitted splitting is admissible.

## Evidence

- `research/benincasa/soft-axis-filtered-exact-module-certificate.json`;
- `research/benincasa/marici-gm/src/bin/marked_tangency_support.rs`;
- Entries 441--442.
- Entry 447.
