# Refinement reveals a parity-polarized metric theory

## Pair insertion

Take an ordered even configuration and insert two new points into one of its gaps. Write the three new sub-gap propagators as

\[
\ell,\quad m,\quad r,
\]

so the old gap propagator is \(\ell mr\). The inserted pair itself has amplitude \(m\).

There are two cases.

### Insertion between existing pairs

If the gap follows an even number of points, it lies between adjacent matched pairs. The two inserted points pair with each other, and

\[
\boxed{
\frac{Z(\text{refined})}{Z(\text{old})}=m.
}
\]

### Insertion inside an existing pair

If the gap follows an odd number of points, it lies inside one matched pair. Refinement breaks that pair and reconnects its endpoints to the inserted points. Then

\[
\boxed{
\frac{Z(\text{refined})}{Z(\text{old})}=m^{-1}.
}
\]

The outer factors \(\ell\) and \(r\) cancel in both comparisons.

## Consequence

Arbitrary subdivision is not invisible. Its effect depends on the parity polarization of the gap:

\[
Z(\text{refined})
=
Z(\text{old})\,Z(\text{inserted pair})^{\pm1}.
\]

Therefore the structure is not an ordinary topological field theory. Metric interval data and a choice of pairing polarization remain essential.

A sharper kind name is

\[
\boxed{
\text{a parity-polarized one-dimensional fermionic metric factorization algebra}.
}
\]

“Metric” means amplitudes depend on interval lengths. “Polarized” means alternating gaps carry mutually dual roles. “Factorization” means admissible cuts and insertions obey local composition laws.

## Duality meaning

The sign change is naturally read as evaluation versus coevaluation:

- an inserted pair between pairs contributes its amplitude;
- an inserted pair inside a contraction contributes the inverse amplitude required to re-pair the boundary legs.

Thus alternating gaps behave like a line and its dual. The ordered chain carries a hidden checkerboard polarization

\[
L,L^*,L,L^*,\ldots
\]

rather than a homogeneous collection of indistinguishable intervals.

This polarization explains why odd configurations retain one exposed state line: the alternation has one unmatched boundary leg.

## Verification

The exact-rational checker verifies 500 insertion cases in configurations of sizes two through ten:

```text
python research/coherence/check_pair_insertion_refinement_law.py
```

Artifacts:

- `check_pair_insertion_refinement_law.py`
- `pair-insertion-refinement.v1.json`
