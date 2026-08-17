# 20260817-356 — Cyclic Occurrence Rees Assembly Closes, but It Is Not a Čech Gluing

## Question

Entry 355 proposed transporting the double-soft presentation across all three marked-Cut sectors and sewing the six lower-denominator occurrences.

The source defines two different notions that must not be conflated:

1. a cyclic sum of six physical period integrands;
2. potential transition maps between the three distinct residue coefficient modules.

Only the first is printed and geometrically normalized.

The hard-to-vary claim tested here is:

[
oxed{
	ext{the source cyclic occurrence data already define a global Čech
differential between the three rank-twelve residue sectors.}
}
]

## Frozen occurrences

In source order, the six terms are

[
(12|23),(12|31),(23|31),(23|12),(31|12),(31|23),
]

all with coefficient (+1).

The cyclic rotation has two orbits:

[
(12|23)	o(23|31)	o(31|12)	o(12|23),
]

[
(12|31)	o(23|12)	o(31|23)	o(12|31).
]

Its order is exactly three.

## Occurrence-forgetting map

Forgetting which lower denominator accompanies a marked Cut gives

[
F:mathbb Z^6	omathbb Z^3,
]

[
F=
egin{pmatrix}
1&1&0&0&0&0\
0&0&1&1&0&0\
0&0&0&0&1&1
end{pmatrix}.
]

It has rank three and saturated kernel

[
ker F
=
mathbb Z(1,-1,0,0,0,0)
oplus
mathbb Z(0,0,1,-1,0,0)
oplus
mathbb Z(0,0,0,0,1,-1).
]

The physical all-positive source vector obeys

[
oxed{
F(1,1,1,1,1,1)=(2,2,2).
}
]

Thus the factor two is precisely lower-denominator occurrence identification. It introduces no new torsion prime or carrier incidence.

## Cyclic soft-Rees covariance

The three local two-axis presentations are

[
(1,2X_1,2X_2),
]

[
(1,2X_2,2X_3),
]

[
(1,2X_3,2X_1).
]

They are transported into one another by the source cyclic relabeling. Hence the exact soft and double-soft physical comparisons from Entries 353 and 355 assemble as a (C_3)-equivariant direct sum.

No sign repair, fitted permutation, or additional support divisor is required.

## Type verdict

The cyclic covariance is an isomorphism obtained by relabeling the entire source sector. It does not make the three residue surfaces into an open cover of one already constructed coefficient space.

The primary source supplies:

- the six summands;
- their all-positive coefficients;
- cyclic covariance;
- sector-local residue maps;
- occurrence forgetting.

It does not supply:

- pairwise overlap objects between distinct (q_{mathcal G_{ij}})-residue surfaces;
- restriction maps to such overlaps;
- a Čech differential;
- a proof that the period sum is a colimit or descent object in the coefficient category.

Therefore the tested claim is falsified:

[
oxed{
	ext{cyclic period assembly}

otRightarrow
	ext{Čech gluing of residue coefficient modules}.
}
]

The admissible global result is narrower:

[
oxed{
	ext{the six physical occurrences form a canonical }
C_3	ext{-equivariant Rees direct sum with multiplicity-two forgetting}.
}
]

## Classification

| Datum | Classification |
|---|---|
| two three-cycles | source occurrence structure |
| all-positive signs | source integrand normalization |
| saturated rank-three kernel | occurrence-resolved coefficient lattice |
| ((2,2,2)) | occurrence-identification multiplicity |
| cyclic local Rees forms | existing signed-energy/soft support |
| cross-sector Čech arrows | absent, not zero |
| new carrier datum | none inferred |

## Consequence for H2

The local and cyclic-equivariant evidence continues to support

[
	ext{shared carrier/calculus}
+
	ext{sector-specific filtered coefficient objects}.
]

But a global descended coefficient object has not been constructed. H2 is not upgraded to global Čech descent merely because the physical periods add.

## Evidence

- `research/benincasa/cyclic-occurrence-rees-certificate.json`;
- `research/benincasa/marici-gm/src/bin/cyclic_occurrence_rees.rs`;
- primary six-term source support;
- Entries 229, 338, 353, and 355.

## Next falsifier

Derive a genuine cross-sector correspondence from the frozen pre-residue three-variable integrand, rather than from the sum of its residues.

The first finite target is the pair

[
q_{mathcal G_{12}}=q_{mathcal G_{23}}=0,
]

with all source lower-denominator occurrences retained. Compute its iterated-residue correspondence into both rank-twelve sector modules and test whether the two maps agree up to the frozen residue orientation.

If the pre-residue geometry supplies the correspondence, it becomes the first valid overlap arrow. If it does not, global assembly remains an equivariant sum rather than Čech descent. No zero map may be inserted for the missing arrow.
