# The ambient thimble column reduces to the four enhanced-point exceptional classes

## Semistable cap geometry

At total energy zero, the compact surface is

\[
S_+\cup_C S_-,
\qquad S_\pm\simeq\mathbb P^2,
\]

with double conic

\[
C:\ R_h=0.
\]

The nodal anticanonical boundary has two intersection points on \(C\). Its dual-graph cycle is capped in the total surface by choosing a path in \(C\) between those two points and sweeping the local vanishing circle. Two choices of cap differ by the full conic class.

Before resolving the enhanced points,

\[
[C]=2H
\]

on either \(\mathbb P^2\) sheet, so this cap ambiguity is even and vanishes modulo two.

## Enhanced-point correction

The first smoothing coefficient vanishes at the four source-labelled points

\[
P_{\epsilon\delta}=[\epsilon y:\delta x:1],
\qquad \epsilon,\delta\in\{\pm1\}.
\]

Semistabilizing these points introduces exceptional curve classes \(E_{\epsilon\delta}\). The strict transform of the conic has class

\[
\widetilde C
=2H-
E_{++}-E_{+-}-E_{-+}-E_{--}.
\]

Therefore modulo two,

\[
\boxed{
[\widetilde C]
\equiv
E_{++}+E_{+-}+E_{-+}+E_{--}.
}
\]

The integral thimble/Gysin parity is thus controlled entirely by the image of the four enhanced-point exceptional classes in the algebraic plane \(\langle e_6,v_{\rm alg}\rangle\). The even ambient conic contributes nothing.

## Reduction of the requested column

Let

\[
\pi_{\rm alg}:
\mathbb Z\langle E_{++},E_{+-},E_{-+},E_{--}\rangle
\longrightarrow
\mathbb Z\langle e_6,v_{\rm alg}\rangle
\]

be the integral specialization/Gysin map. Then the desired parity column is

\[
\boxed{
(a,b)
=
\pi_{\rm alg}
(E_{++}+E_{+-}+E_{-+}+E_{--})
\pmod2.
}
\]

This replaces an unbounded ambient-chain construction by a finite four-column incidence computation.

## Available constraints

The physical marked point is \(P_{--}\). Existing wall and endpoint calculations show that its source-relative contribution assembles to an even \(v_{\rm alg}\) coefficient after the two active walls are sewn. They do not serialize the four individual exceptional images under \(\pi_{\rm alg}\).

Cyclic/deck symmetry can reduce the four columns, but cannot set their sum without one absolute normalization.

## Next exact computation

Resolve the four local enhanced germs in one common global blowup marking and express each exceptional curve in the degree-two del Pezzo basis \((H,E_1,\ldots,E_7)\). Then apply the already primitive infinity-Gysin kernel marking and project their sum to \((e_6,v_{\rm alg})\). This directly returns the requested two-bit column.

Verification:

- `research/voevodsky/checkers/check_enhanced_conic_thimble_reduction.py`
- `research/voevodsky/results/enhanced_conic_thimble_reduction.json`
