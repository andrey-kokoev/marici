# 578 — Fixed-Pole Polynomial IBP Does Not Recover the Physical Top Module

## Hard-to-vary claim

The physical three-variable top module is **not** the finite quotient obtained by freezing every source denominator to a simple pole and reducing only by polynomial-vector-field integration-by-parts relations.

This is a falsification of one coefficient-lattice model. It is not evidence for a new carrier stratum.

## Frozen ablation

Use variables

\[
(c,a,b)=(y_{12},y_{23},y_{31})
\]

and the source Cayley--Menger polynomial \(K\) at the two generic specializations

\[
(X_1,X_2,X_3)=(2,3,4),\qquad(3,5,6).
\]

For a selected product \(D\) of

\[
q_{g_1}=c+b+X_1,qquad
q_{g_2}=c+a+X_2,qquad
q_{\mathcal G_{12}}=c+X_1+X_2+X_3,
\]

freeze the top form

\[
\Omega_P=\frac{P\,dc\wedge da\wedge db}{D\sqrt K}.
\]

For each polynomial vector field \(V\), clear the fixed denominator in the exact-form relation. Its numerator is

\[
\boxed{
KD\,\operatorname{div}V
-\frac D2V(K)
-KV(D).
}
\]

At total-degree cutoff \(N\), quotient all polynomial numerators of degree at most \(N\) by these relations, admitting precisely the polynomial vector fields whose cleared numerators remain within the cutoff.

The calculation is exact over \(\mathbb F_{32003}\). No generic critical exponents, fitted support summands, or new cells are used.

## Census

In mask order

\[
000,001,010,011,100,101,110,111,
\]

the quotient dimensions at \((2,3,4)\) are

\[
\begin{array}{c|rrrrrrrr}
N&000&001&010&011&100&101&110&111\\
\hline
8&27&67&67&105&66&105&105&135\\
10&27&79&79&131&74&128&128&181\\
12&27&91&91&157&82&150&150&219
\end{array}
\]

The second generic point \((3,5,6)\) reproduces the complete \(N=8,10\) rows exactly.

The required physical deletion cube is

\[
\boxed{(7,8,8,9,16,18,18,21).}
\]

The ablation fails in two independent ways:

1. even the denominator-free sector stabilizes at \(27\), not \(7\);
2. every sector containing a \(q\)-divisor grows with the cutoff.

## Narrow interpretation

Specializing the twist to the physical half-weight before choosing the correct logarithmic lattice leaves a large resonant affine excess. Fixed simple poles and polynomial vector fields do not implement the localized twisted de Rham quotient.

The absent datum is coefficient-side:

\[
\boxed{
\text{localized/rational logarithmic vector fields}
\quad\text{or an equivalent compatible higher-pole lattice.}
}
\]

Nothing in this failure requires modifying the energy/Cut carrier.

## Surviving conjecture

The physical rank packet may still be obtained from the same three source divisors and Cayley--Menger cover, but only after constructing the correct localized logarithmic de Rham/IBP complex at exponent \(-\tfrac12\).

## Next falsifier

Predeclare a finite higher-pole or localization filtration, prove that its exact differential closes, and test whether its deletion ranks stabilize to

\[
(7,8,8,9,16,18,18,21)
\]

at both generic kinematic points.

Only after that calibration may its two-parameter Gauss--Manin connection be used to classify the rank-nine/rank-five extension.

## Artifacts

- `research/benincasa/marici-gm/src/bin/physical_top_log_ibp_rank.rs`
- `research/benincasa/physical-top-log-ibp-rank.json`
