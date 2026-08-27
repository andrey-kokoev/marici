# 3341 — The Global Two-Soft Source Module Does Not Select the e6 Torsor Amplitude

## Question

Entry 3337 proves that neither soft germ locally fixes the residue of
((B_v)_{e_6,q_0}). Can one global rational primitive correlate the two free
germs and select the Entry 3328 no-infinity class with source amplitude
(C_2=-1/8)?

## Predeclared global module

Restrict the 132 cleared rank-twelve source identities to (u=0) and the
(v)-derivative of (q_0). Use the independently derived common denominator

\[
d(v)=v(v-2).
\]

Write the 372 primitive coefficients as

\[
z(v)=\frac{N(v)}{d(v)}.
\]

To impose the Entry 3328 logarithmic no-infinity condition on the target
coordinate, require

\[
N_{e_6,q_0}(v)=c
\]

to be constant. All other primitive numerators remain free through the declared
degree bound. The polynomial equations are

\[
M(v)N(v)=d(v)r_{v,q_0}(v).
\]

No value of (c) is supplied to the solver.

## Degree and prime census

At the default prime, the exact polynomial-module ranks are

\[
\begin{array}{c|c|c|c}
\deg N&\text{variables}&\text{equations}&\text{rank}\\
\hline
4&1860&1371&655\\
6&2604&1637&843\\
8&3348&1903&1031
\end{array}
\]

Every system is consistent. At every degree, the constant target coefficient
(c) is not a pivot.

The degree-eight calculation was repeated at

\[
2305843009213693951
\]

and

\[
2305843009213693921.
\]

Both give rank (1031), consistency, and a non-pivot target. Every source
polynomial interpolation was checked at a held-out point.

## Result

The global no-infinity polynomial module does not select the amplitude of the
primitive (e_6) logarithmic class. The constant numerator remains a free
source-module coordinate.

In particular, the tested module admits:

- the zero class;
- the candidate value (c=1/4), equivalent to (C_2=-1/8);
- arbitrary scalar multiples over each tested field.

Thus the match with (C_2) is compatible with the source reduction but is not
forced by it.

## Epistemic classification

The surviving facts are:

- the class (d\log(X_3/X_2)) has source-derived cyclic Leray provenance;
- its boundary lattice and primitive residues are canonical;
- the two-soft no-infinity conditions leave a unique line;
- (C_2) provides a distinguished compatible scalar.

What fails is selection:

- neither local germ fixes the scalar;
- diagonal occurrence descent cannot insert it;
- the global bounded polynomial source module does not fix it.

Therefore the rank-twelve source reduction defines an admissible torsor line,
not a distinguished point on that line.

## Scope

This is a replicated exact finite-field polynomial-module result through
numerator degree eight. No characteristic-zero primitive witness or theorem of
all-degree stabilization is claimed.

Any stronger selection claim now requires an independently source-authorized
datum outside this reduction module, such as a physical relative-cycle pairing,
integral lattice normalization, or renormalized readout. It may not be supplied
by choosing the compatible value (C_2) after the fact.

## Programme consequence

Under the current frozen source, retire the claim that the rank-twelve
Gauss--Manin reduction selects the (e_6) torsor amplitude. Preserve the line as
coefficient/occurrence-descent structure and classify any future scalar
selection by its independent authority.

## Verification

Module checker:
`research/benincasa/checkers/audit_global_two_soft_polynomial_module.py`.

Aggregate checker:
`research/benincasa/checkers/audit_global_two_soft_selection_closure.py`.

Aggregate packet:
`research/benincasa/results/global_two_soft_selection_closure.json`.

Allocator claim: `seqclaim-b4196c2561c4607edfba8d95`.
