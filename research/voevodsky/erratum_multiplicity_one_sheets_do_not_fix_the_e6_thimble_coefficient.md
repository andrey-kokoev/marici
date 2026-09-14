# Erratum: multiplicity-one sheets do not fix the e6 thimble coefficient

## Withdrawn claim

The preceding response asserted

\[
2m=e_6\pmod{2\langle e_6,v_{\rm alg}\rangle}
\]

from the two multiplicity-one components of the semistable central fiber. That inference is not valid and is withdrawn.

## Dimension mismatch

The total-energy degeneration is a family of complex surfaces. Its central components

\[
S_+,S_-\cong\mathbb P^2
\]

are complex surfaces, hence real four-cycles in the central fiber and divisors in the total threefold. By contrast,

\[
e_6,v_{\rm alg}\in H^2(S_E)
\]

are dual to real two-cycles/complex curve classes in a smooth surface fiber.

Therefore the oriented difference \(S_+-S_-\) is not an \(H_2\) class that can be identified with \(e_6\). Multiplicity one controls the semistable divisor, not the algebraic coordinates of a lifted Lefschetz thimble.

## Local equation does not select the ambient lift

The local model

\[
UV=E
\]

constructs the vanishing circle and its local thimble. It fixes the width-two monodromy after the source Kummer twist. It does not compute intersections of an ambient lifted two-chain with curve classes dual to \(e_6\) and \(v_{\rm alg}\).

This agrees with the already verified local-thimble no-go: all four relations

\[
2m=a e_6+bv_{\rm alg},
\qquad(a,b)\in(\mathbb Z/2)^2,
\]

have the same local \(UV=E\) germ and elliptic monodromy.

## What remains established

The source-relative wall and endpoint pieces contribute even \(v_{\rm alg}\) parity, and the endpoint divisor is principal. These facts show that those particular pieces do not supply an odd correction. They do not rule out an intrinsic algebraic shift in the ambient lift of the closed elliptic cycle.

Thus the integral column remains uncomputed:

\[
(a,b)\in\{(0,0),(1,0),(0,1),(1,1)\}.
\]

## Required computation

A valid determination must construct a real two-chain

\[
\widetilde{\mathcal T}_\delta
\subset S_E\setminus D_\infty
\]

whose Gysin boundary is the primitive elliptic vanishing cycle, then evaluate two integral intersections

\[
\#(\widetilde{\mathcal T}_\delta, e_6^\vee),
\qquad
\#(\widetilde{\mathcal T}_\delta, v_{\rm alg}^\vee)
\pmod2.
\]

Neither central sheet multiplicity nor a rational de Rham functional supplies these intersections.

Verification:

- `research/voevodsky/checkers/check_sheet_dimension_thimble_no_go.py`
- `research/voevodsky/results/sheet_dimension_thimble_no_go.json`
