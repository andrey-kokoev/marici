# 959 — Composite Corner Resonance Is Diagonal Inertia, Not Iterated-Boundary Support

## Correction to Entry 958

Entry 958 correctly identifies the existing two-normal chamber corners and
their labelled multiplicities.  Its conclusion that this supplies full
carrier provenance for the composite Fitting factors is too strong.

Let \(m,n\) be the two facet monodromies at one of those corners.  The
ordinary loaded iterated boundary carries coefficient

\[
(m-1)(n-1).
\]

The source Fitting factor found in Entries 943 and 958 is instead

\[
mn-1.
\]

These polynomials are neither associates nor support-equivalent.

## Finite falsifier

At the generic normal-torus point

\[
m=2,qquad n=\frac12,
\]

one has

\[
mn-1=0,
\qquad
(m-1)(n-1)=-\frac12\neq0.
\]

Thus the composite resonance may occur while neither facet monodromy is
trivial and while the ordinary iterated-boundary coefficient is invertible.

## Correct typing

The four factors are attached to the existing corners as **diagonal inertia**
in their two-dimensional normal tori:

\[
\begin{array}{c|c}
ZA_2&12|35\\
ZA_2B_{24}&124|35\\
A_3/Z&13|25\\
A_3B_{34}/Z&134|25.
\end{array}
\]

Their occurrence counts \((1,2,1,2)\) remain valid.  What is withdrawn is
the implication

\[
\text{compatible corner}
\Longrightarrow
\text{ordinary iterated-Gysin support }mn=1.
\]

The surviving architecture is

\[
\boxed{
\text{existing two-normal carrier corner}
+
\text{diagonal coefficient inertia }(mn-1).
}
\]

## Blowup qualification

Blowing up the corner makes the product monodromy \(mn\) the monodromy of an
exceptional divisor.  But such an exceptional carrier cannot be introduced
after observing the Fitting factor.  It is admissible only if the required
log/wonderful refinement was independently frozen for all corners.

Without that prior refinement, \(mn-1\) remains coefficient support over the
unchanged corner, not a new carrier divisor.

## Revised falsifier

Audit the predeclared six-point compactification/refinement.  Determine
whether it already contains the barycentric or log blowup of every compatible
two-facet corner, with occurrence-natural exceptional orientations.

- If yes, derive the exceptional boundary map and compare its monodromy with
  \(mn\).
- If no, retain the diagonal-inertia coefficient object on the normal torus;
  do not add exceptional facets selectively.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_corner_inertia_gate.rs`;
- packet:
  `research/benincasa/string-six-point-corner-inertia-gate.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_corner_inertia_gate`;
- allocator claim:
  `seqclaim-1896cdf86e636de513336e93`.
- epistemic event:
  `ev-000000000576-ff7fe177-66c4-48bf-b0ee-7eac5b9d2861`.
