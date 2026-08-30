# 3256 — The Quarter Resonances Belong to Order-Four Kummer Sectors

Date: 2026-08-27

Status: exact coefficient-typing theorem, conditional only on the frozen
exponent convention already audited in Entries 3250 and 3253.

## Hard question

Can source dimensional transport connect the physical residue at

\[
\gamma=-\frac12
\]

to either quarter resonance without changing the coefficient object?

## Local inertia

The rank-one twist (K^\gamma) has local inertia around (K=0)

\[
\chi_\gamma=\exp(2\pi i\gamma).
\]

Therefore

\[
\begin{array}{c|c}
\gamma&\chi_\gamma\\
\hline
-1/2&-1\\
-5/4&-i\\
-7/4&+i.
\end{array}
\]

The physical residue belongs to the order-two Kummer sector. The two quarter
fibers belong to the two conjugate order-four Kummer sectors.

## Admitted exponent shifts

Multiplication or division by an integral power of (K) changes

\[
\gamma\longmapsto\gamma+n,qquad n\in\mathbb Z,
\]

and preserves \(\chi_\gamma\). Such meromorphic gauge transformations cannot connect the
physical character (-1) to either quarter character.

Continuous differentiation in the dimensional regulator gives

\[
\partial_\epsilon K^{\epsilon-1/2}
=
\log K\,K^{\epsilon-1/2}.
\]

The logarithmic generator is not an object of the frozen rational relative de
Rham presentation. Adjoining it would be a coefficient enlargement, not a
recurrence already supplied by the current source complex.

## Narrow conclusion

The proposed relative dimensional recurrence does not exist inside the frozen
rational coefficient category. The universal exponent pencil places several
Kummer characters in one algebraic family, but that parameter-space packaging
does not canonically identify their fibers.

Consequently the quarter defects cannot be residues of physical
dimension-shift transport unless an independently derived order-four Kummer or
logarithmic coefficient extension is supplied. No new Carrier geometry is
indicated.

This sharpens Entry 3253:

- the quarter fibers are source-coordinate-visible;
- they are not in the physical coefficient sector;
- their (S_3) covariance expresses shared occurrence geometry, not equality
  of coefficient objects.

## Programme consequence

Retire the quarter branch as a candidate physical cosmological support. Retain
it as evidence that the shared occurrence carrier admits distinct
sector-indexed Kummer coefficient systems. Reopen only if the source derives a
logarithmic or order-four Kummer comparison functor together with its physical
relative cycle.

## Artifacts

- `research/benincasa/checkers/exponent_adapter_kummer_characters.py`
- `research/benincasa/results/exponent_adapter_kummer_characters.json`
- sequence claim `seqclaim-715e1a99035bd1abc46b9dfe`
