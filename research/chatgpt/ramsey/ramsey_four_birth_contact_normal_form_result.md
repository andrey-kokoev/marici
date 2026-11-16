# Four-birth contact normal forms: independent exact audit

## Scope

Carrier: the folded 7-cube, the Cayley graph on `F_2^6` with A-generators
`{1,2,4,8,16,32,63}`. Four disjoint oriented birth operations edit all
8 lower four-vertex squares. An A-contact to a newborn excludes its port
from a B-group. The threshold forbids a B-group of 23.

This note records an audit independent of the previously computed 52 symmetry
orbits of complete four-birth matchings. It does **not** establish the
normal-form theorem for arbitrary folded cubes or arbitrary Ramsey colorings.

## Reduction to the Clebsch quotient

Write an old B-group avoiding selected newborn ports as a lower part
`I ⊆ {0,...,31}` and an upper part. The involution `v ↦ v xor 31` partitions
the lower coordinates into 16 antipodal classes. Let `D(I)` be the classes
meeting `I`, `U=Q\D(I)`, and `p=|I|-|D(I)|`.

The upper graph restricted to U is the bipartite double cover of the Clebsch
graph `Q=Cayley(F_2^4,{1,2,4,8,15})` induced on U. By König's theorem,

    beta(T) = 16 + max_I (p(I) + h(U(I)))
    h(U) = max(0, max_{X subset U, X independent in Q}
                        (|X| - |N_Q(X) intersect U|)).

There are exactly **392** nonempty independent subsets X of Q, with sizes
1..5 in counts 16,80,160,120,16. All 16 independent five-sets are the
five-element neighborhoods N_Q(q) of the 16 quotient vertices.

Inside each lower square the allowed positions are independent sets of the
three-edge edited path, excluding marked newborn ports. For high neighboring
squares c,d with `c xor d ∈ {1,2,4}`, a chosen low position cannot appear in
both squares. Enumerating these local choices and evaluating the displayed
finite Hall expression is an exact computation of beta(T), without a graph
maximum-independent-set or bipartite matching solver.

## Smaller contact classes suffice

For a singleton or pair of selected newborns, the old graph and their
excluded ports depend only on (a) which four square cells are first contacts,
(b) which of those belong to selected births, and (c) which second-contact
cells belong to selected births. They do **not** depend on how first and
second cells are paired into the other births.

The high-cube translations and coordinate permutations (48 maps), together
with the simultaneous exchange of first/second orientation, form a 96-element
symmetry action on those marked contact patterns.

| Selected births | Marked contact patterns | Symmetry orbits |
| --- | ---: | ---: |
| One | 1,120 | 24 |
| Two | 2,520 | 48 |
| Three | 1,120 | 24 |
| Four | 70 | 6 |

## Normal forms: exact finite completeness

For one newborn, a forbidden B23 must have at least 22 old B-vertices.
In all 24 singleton-pattern orbits, this occurs **if and only if** a witness
has 12 lower vertices and both upper lifts of five independent Clebsch
quotient neighbors (12+10).

For two mutually B-connected newborns, the threshold is 21 old B-vertices.
In all 48 pair-pattern orbits, this occurs **if and only if** a witness has
one of the following forms:

- **11+10, D=9:** eleven lower vertices touching nine quotient classes;
  ten upper vertices obtained from both lifts of a five-cell Clebsch
  neighborhood.
- **11+10, D=8:** eleven lower vertices touching eight quotient classes;
  the same ten-upper construction.
- **10+11:** ten lower vertices touching at most five quotient classes;
  eleven upper vertices from one fixed parity class.

Every predicted witness was checked against all original Cayley edges, all
square edits, and the selected newborn ports. In all other orbits the exact
Hall expression is below the corresponding obstruction threshold.

| Marked pattern (selected one) | Number out of 1,120 |
| --- | ---: |
| No singleton obstruction | 1,072 |
| 12+10 obstruction | 48 |

| Marked pattern (selected pair) | Number out of 2,520 |
| --- | ---: |
| No pair obstruction | 1,932 |
| 11+10, nine touched classes | 228 |
| 11+10, eight touched classes | 144 |
| 10+11 | 216 |

Each marked singleton pattern represents 6 matchings of the other three
births; each marked pair pattern represents 4 matchings. Hence the full
four-birth assemblies contain 288 blocked labeled singleton incidences and
2,352 blocked labeled pair incidences (including nonminimal ones).

**Correction:** The earlier 11+10 description prescribed exactly nine
touched quotient classes. Eight are also possible. However, every one of
the 576 assembly-weighted eight-class pair obstructions has at least one
already forbidden singleton. Thus the two-form description for *minimal*
pair obstructions—11+10 with D=9, or 10+11—remains valid.

## Complete four-birth complexes without the prior 52-orbit audit

The further 24 three-birth and six four-birth marked-pattern orbits were
checked by the same quotient-Hall identity. For three selected births, the
old B-link capacity is either 19 or 20. The 20 case may arise without
parity consistency, but in that situation at least one pair is already
forbidden. Thus a **minimal** forbidden triple occurs exactly when its
contact-parity equations are consistent. For four selected births, the
capacity is 17,18, or 20. In the 20 case every selected triple already
fails; there is no minimal four-way obstruction.

The finite contact classifier therefore consists of the singleton forms,
minimal pair forms, contact parity for minimal triples, and no genuinely
four-way missing face. Running it over 1,680 oriented assemblies reproduces
every exact capacity-derived completion complex with **zero disagreements**.

Homology of the resulting complexes:

| Ordinary Betti numbers (b0,b1,b2) | Assemblies |
| --- | ---: |
| (1,0,0) | 984 |
| (2,0,0) | 192 |
| (1,1,0) | 456 |
| (1,2,0) | 48 |

No nonzero H_2 occurs in this declared family.

## Logical status

The Clebsch-Hall identity is a theorem. The normal-form completeness is
proved by a small, explicit **finite** computation over 72 marked orbits,
independent of the older catalogue and matching audit. The four-birth
classification is independently regenerated from 24+48+24+6 marked orbit
tests. A dimension-independent proof of why these witness forms exhaust
all possibilities remains open. None of this proves the general Ramsey
coherence conjecture.

## Reproducibility

Run the files in this order:

    python ramsey_four_birth_72_orbit_hall_proof.py
    python ramsey_four_birth_completion_from_contact_orbits.py

Both use the Python standard library only. They write corresponding JSON
certificates and independently verify witness A/B incidences.
