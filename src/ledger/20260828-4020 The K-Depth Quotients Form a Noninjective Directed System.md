# 4020 — The K-Depth Quotients Form a Noninjective Directed System

## Status

Established in the tested source-reachable finite-field models at prime (32009), independently in residue charts (G_{12}) and (G_{31}). The depth-three quotient ranks were also replicated at prime (32003).

## Frozen comparison

Let (M_{le d}) denote the source-generator module truncated at (K)-pole depth (d), and let (R_{le d}) be the exact-relation submodule supplied by the same frozen presentation.

The labelled inclusion

[
M_{le3}longrightarrow M_{le4}
]

contains every depth-three label.

The first acceptance gate is kernel-pair descent:

[
R_{le3}longrightarrow R_{le4}.
]

All (15412) depth-three pivot relations reduce to zero in the depth-four quotient, in both charts. Therefore the labelled inclusion induces a canonical quotient map

[
overlineiota_{3,4}:
M_{le3}/R_{le3}
longrightarrow
M_{le4}/R_{le4}.
]

## Source-reachable ranks

At depth three:

[
dim M_{le3}^{m reach}=4800,
]

[
dim Q_{le3}^{m reach}=53,
]

[
dim R_{le3}^{m reach}=4747.
]

The canonical generator-distance associated ranks are

[
3, 16, 8, 6, 20.
]

At depth four:

[
dim M_{le4}^{m reach}=9120,
]

[
dim Q_{le4}^{m reach}=1386,
]

[
dim R_{le4}^{m reach}=7734.
]

Its generator-distance associated ranks are

[
3, 16, 8, 0, 6, 235, 430, 430, 215, 43.
]

## Transition theorem

The induced map on the depth-three source-reachable quotient has

[
operatorname{rank}operatorname{im}overlineiota_{3,4}=33,
]

[
dimkeroverlineiota_{3,4}=20.
]

Thus

[
53=20+33.
]

Inside the depth-four quotient, the corresponding cokernel rank is

[
1386-33=1353.
]

The result is identical in (G_{12}) and (G_{31}).

## Filtration warning

The separate (K)-pole and occurrence filtrations do not define a compatible bigraded exact quotient. Among (4800) generated coordinate classes, (4763) exact reductions cross the naive ((K,	ext{occurrence})) grade. The double-difference table even contains a negative entry.

Therefore the pre-quotient factorization

[
3(1+t)^5rac{1+3s}{(1-s)^3}
]

does not descend as an ordinary tensor-product Hilbert series.

The canonical surviving filtration is generator distance, not independent (K)- and occurrence-associated grading.

## Narrow conclusion

A fixed-(K)-depth quotient is not itself an intrinsic coefficient object.

Twenty depth-three classes die under legal extension to depth four, while (1353) new quotient directions appear. The correct object is the directed system

[
Q_{le0}	o Q_{le1}	o Q_{le2}	ocdots
]

together with its transition kernels and cokernels.

This is a continuation phenomenon, not a new carrier divisor.

## Next falsifier

Compute the transition

[
Q_{le4}^{m reach}longrightarrow Q_{le5}^{m reach}
]

without constructing the entire depth-five quotient if possible.

Use the source transition itself:

1. verify relation-kernel descent;
2. compute the image rank of (Q_{le4}^{m reach}) in depth five;
3. classify the kernel by generator distance;
4. determine whether any depth-four classes persist through two consecutive extensions.

The first candidate for intrinsic finite content is the eventual image or derived limit, not any finite-stage rank.

## Artifacts

- `research/benincasa/checkers/check_source_reachable_relation_quotient_hilbert.py`
- `research/benincasa/checkers/check_kdepth3_to4_kernel_pair_gate.py`
- `research/benincasa/checkers/check_kdepth3_to4_source_quotient_transition.py`
- `research/benincasa/results/source-reachable-relation-quotient-hilbert-*.json`
- `research/benincasa/results/kdepth3-to4-kernel-pair-gate-*.json`
- `research/benincasa/results/kdepth3-to4-source-quotient-transition-*.json`

Sequence claim: `seqclaim-974fb40211d84b329eaf1c42`.
