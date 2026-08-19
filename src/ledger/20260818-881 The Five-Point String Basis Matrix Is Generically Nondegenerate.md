# 881 — The Five-Point String Basis Matrix Is Generically Nondegenerate

## Record

Date: 2026-08-18

Status: exact matrix-structure and field-theory-leading nondegeneracy theorem for the two-cycle five-point basis. The result combines Entries 879--880 and adds physical kinematic closure plus a nonadjacent control. It does not give a closed-form determinant at arbitrary \(\alpha'\).

## Frozen basis and kinematics

Use

\[
\mathcal B=
\bigl(
\widetilde{\mathsf C}(12345),
\widetilde{\mathsf C}(13245)
\bigr).
\]

The five planar invariants are

\[
(s_{12},s_{23},s_{34},s_{45},s_{51}).
\]

The second cyclic order introduces no independent kinematics:

\[
\boxed{
s_{13}=s_{45}-s_{12}-s_{23},
\qquad
s_{24}=s_{51}-s_{23}-s_{34}.
}
\]

## Matrix structure

The diagonal entries are the native face sums of Entry 879 for cyclic orders

\[
(12,23,34,45,51)
\]

and

\[
(13,23,24,45,51).
\]

The off-diagonal entries are the shared-\((23)\)-facet reduction of Entry 880. Thus every matrix entry is derived from:

\[
\text{face incidence}
+
\text{normal orientation}
+
\text{Koba--Nielsen branch transport}.
\]

For the leading \(\alpha'^{-2}\) coefficient, remove the common nonzero normalization and write

\[
D(x_0,\ldots,x_4)
=
\sum_{i\in\mathbb Z/5}
\frac1{x_i x_{i+2}},
\]

\[
O=
\frac1{s_{23}}
\left(\frac1{s_{45}}+\frac1{s_{51}}\right).
\]

Then

\[
M_{m lead}
\sim
\begin{pmatrix}
D(s_{12},s_{23},s_{34},s_{45},s_{51})&O\\
O&D(s_{13},s_{23},s_{24},s_{45},s_{51})
\end{pmatrix}.
\]

At the exact physical sample

\[
(s_{12},s_{23},s_{34},s_{45},s_{51})=(2,3,5,11,17),
\]

one has

\[
(s_{13},s_{24})=(6,9)
\]

and

\[
\boxed{
\det M_{m lead}=\frac{245}{15147}\neq0
}
\]

after the stated common normalization. Therefore the leading determinant is not the zero rational function. The finite-\(\alpha'\) twisted intersection matrix is generically nondegenerate near \(\alpha'=0\), away from its declared resonance divisors.

## Nonadjacent control

The chambers

\[
12345,qquad13524
\]

share no face in \(\widetilde{\mathcal M}_{0,5}(\mathbb R)\). Their twisted-cycle intersection therefore vanishes, matching the primary source.

## Narrow update

The complete five-point evidence now supports:

\[
\boxed{
\text{shared associahedral incidence/Gysin calculus}
+
\text{string-specific Koba--Nielsen pairing}
}
\]

for diagonal, adjacent, and nonadjacent intersection types. Carrier incidence determines which terms may occur; the coefficient local system determines their trigonometric weights and half-monodromies.

This is evidence for the shared-carrier/sector-specific-coefficients hypothesis. It is not evidence that string and scattering coefficient objects are identical.

## Next falsifier

Move from the intersection matrix to its circuit identity. Freeze the source two-cycle and two-cocycle bases and test whether the Marici support calculus reconstructs the five-point twisted period/KLT relation, including basis changes and normalization. This is the first test involving both homology and cohomology rather than the cycle pairing alone.

## Certificate

Run:

```text
cargo run --quiet --bin string_five_point_basis_matrix
```

Artifacts:

- `research/benincasa/marici-gm/src/bin/string_five_point_basis_matrix.rs`
- `research/benincasa/string-five-point-basis-matrix.json`

## Source

Sebastian Mizera, *Combinatorics and Topology of Kawai--Lewellen--Tye Relations*, arXiv:1706.08527, Sections 3.4 and 4.3.
