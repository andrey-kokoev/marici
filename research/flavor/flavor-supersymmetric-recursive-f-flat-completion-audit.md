# Supersymmetric Recursive F-Flat Completion Audit

## Question

Can exact supersymmetry convert WP849's chosen positive potential into a
source-stable recursive vacuum, so the Aspect completion hostile of WP850 no
longer moves the selected orbit?

## Source grammar

Take chiral fields

\[
S_1,S_2,S_3,\overline S_1
\]

of charges \(-1,-2,-3,+1\), all with \(R\)-charge zero. Introduce driving
fields \(A_0,A_2,A_3\) of charges \(0,+2,+3\) and \(R\)-charge two. With a
neutral dimension-one parameter (v), the recursive superpotential is

\[
W=A_0(S_1\overline S_1-v^2)
 +A_2(vS_2-S_1^2)
 +A_3(vS_3-S_1S_2).
\]

Every term is gauge invariant, has \(R\)-charge two, and is renormalizable.

## Exact F-flat orbit

The three driving-field equations give

\[
S_1\overline S_1=v^2,
\qquad
S_2=S_1^2/v,
\qquad
S_3=S_1S_2/v.
\]

On the nonzero branch, the remaining F equations force

\[
A_0=A_2=A_3=0.
\]

After imposing the usual conjugate real section
\(overline S_1=S_1^*\), the vacuum set is precisely the WP849 orbit.

For every positive invertible Kähler metric (K_{i\bar j}),

\[
V_F=F_i(K^{-1})^{i\bar j}\overline F_{\bar j}=0
\quad\Longleftrightarrow\quad F_i=0.
\]

Consequently Kähler completion, including the WP850 mass-metric hostile,
cannot move the exact supersymmetric zero locus. It can still change canonical
normalization, masses, and detector couplings.

## Holomorphic completion hostile

The same charge, dimension, and \(R\)-charge grammar does not fix the displayed
relative coefficients. Exhausting homogeneous quadratic monomials gives

\[
\begin{array}{c|c}
A_0 & S_1\overline S_1,\ v^2\\
A_2 & vS_2,\ S_1^2,\ \overline S_1S_3\\
A_3 & vS_3,\ S_1S_2.
\end{array}
\]

Thus the most general admitted superpotential is

\[
W=A_0(aS_1\overline S_1-bv^2)
 +A_2(cvS_2-dS_1^2+g\overline S_1S_3)
 +A_3(evS_3-fS_1S_2).
\]

Its nonzero F-flat branch obeys

\[
S_1\overline S_1=(b/a)v^2,
\quad
S_2=\frac{dS_1^2}{v(c+gbf/(ae))},
\quad
S_3=(f/e)S_1S_2/v.
\]

The smallest hostile turns on only \(g\). It changes the projective kernel ray
while preserving every declared charge, \(R\)-charge, degree, holomorphy, and
exact-supersymmetry condition. Even forbidding that term would leave the
ratios \(b/a,d/c,f/e\) free.

## Aspect verdict

Exact supersymmetry repairs WP850's nonholomorphic completion escape: positive
Kähler completion cannot move an F-flat zero. It does not make the equal-VEV
orbit unavoidable. The coefficient fiber has merely moved from the scalar
potential to three holomorphic relation ratios.

The missing source principle must canonically normalize the multiplication
maps

\[
S_1^2\to vS_2,
\qquad
S_1S_2\to vS_3,
\]

in the same physical metric used for thresholds and readout. A graded-algebra
presentation can set their structure constants to one, but without a
source-derived positive pairing that statement is a basis convention.

## Classification

This is a genuine completion improvement and a negative selection result.
The operation is an F-flat relational rigidifier and a conditional selector;
it is not yet the source-generated portal selector demanded by the programme.
Sign, magnitude, RG basin, threshold survival, and calibrated `physical16`
readout remain unproved.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp851_supersymmetric_recursive_f_flat_completion_audit.py
```
