# 956 — The Saturating Coordinate Lifts Are Not Yet Twisted Chambers

## Provenance audit of Entry 946

Entry 946 correctly computes the Smith form of the displayed two-seed shift
orbit and shows that adjoining four of six available coordinate directions
can saturate its rank-six lattice.

Its checker implements the six proposed chamber lifts by

\[
e_1,\ldots,e_6,
\]

the standard coordinate basis of the serialized six-word module.  For a
chosen subset it appends the corresponding unit columns and recomputes the
determinantal divisors.

The artifact does **not** serialize:

- six cyclic disk chambers or their word labels;
- their associahedral facets;
- a chamber-to-facet incidence matrix;
- loaded twisted-boundary coefficients;
- residue or boundary orientations.

Therefore the exact Smith result

\[
(1,1,1,1,1,1)
\]

after four coordinate lifts is an algebraic statement about the ambient
labelled word lattice.  It does not yet prove that four source-normalized
twisted Betti chambers realize those lifts.

## Correction

The following part of Entry 946 survives:

\[
\boxed{
L_{\rm orbit}\subset \mathbb Z^6
\text{ has Smith invariants }(1,1,2,2,2,4),
\text{ and four coordinate lifts can saturate it.}
}
\]

The stronger identification

\[
\mathbb Z^6=L_{\rm chamber}
\]

is not source-derived by that checker.  It must be treated as an unproved
choice of integral frame until the actual twisted chamber chains and their
boundaries are supplied.

This also blocks the tempting repair of Entry 949 by adjoining one local
boundary cell for every factor of the source Fitting minor.  Such cells would
be selected after seeing the target unless they arise from the frozen chamber
incidence complex.

## Consequence

The present six-point packet establishes:

\[
\text{rational word/intersection data}
+
\text{an abstract integral coordinate lattice}
+
\text{local twisted-boundary factors}.
\]

It does not establish the comparison

\[
\text{integral twisted chamber complex}
\longrightarrow
\text{six-word de Rham lattice}.
\]

Hence the wall multiplicities of Entry 943 remain comparison support, not a
derived chamber-boundary matrix.

## Next falsifier

Freeze six actual ordered disk chambers in a common convention.  For each
chamber, derive its oriented codimension-one facets and the loaded boundary

\[
\partial_\Phi\gamma
=
\sum_F \varepsilon(\gamma,F)(M_F-1)F.
\]

Only then compare the resulting chamber-to-facet matrix with the six-word
coordinate frame and test whether four geometrically specified chambers
saturate the orbit lattice.  Failure of that comparison is a de Rham--Betti
lattice defect, not a new carrier divisor.

## Durable audit

- audited checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_orbit_two_primary.rs`;
- audited packet:
  `research/benincasa/string-six-point-orbit-two-primary.json`;
- allocator claim:
  `seqclaim-4afb641b7f9e7600c5eedbbd`.
- epistemic event:
  `ev-000000000573-dc69733c-68ef-4076-82ec-f79ac52609cd`.
