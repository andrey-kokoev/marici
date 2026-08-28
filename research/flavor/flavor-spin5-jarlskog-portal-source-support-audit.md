# Spin(5) Does Not Yet Generate the Normalized Jarlskog Portal

## Question

Can the declared Spin(5) action derive WP360's weak-basis-invariant portal

\[
V_{\mathrm{int}}=\lambda(J^2-cQ)^2
\]

without importing fitted low-energy flavor data?

## Admitted domain and quotient

The source domain is the declared WP879--WP891 Spin(5) completion packet:
its scalar invariants, allowed Yukawa incidence operators, anomaly data, RG
slopes, and finite-threshold matching relations. The target is the
nondegenerate `physical16` quotient with fifteen CP-even coordinates and
signed Jarlskog coordinate (J).

The audit grants that (J^2) and (Q) can be weak-basis invariants once both
are defined. Descent is not the disputed arrow. The disputed arrow is a
source-derived operation from the declared Spin(5) action to that invariant
functional.

## First obstruction: absent source generator

The declared scalar grammar contains Spin(5) radial variables and permitted
Yukawa incidence terms, but it neither fixes their coefficients nor contains
a source operator identified with normalized (J). Any polynomial built only
from the presently declared source scalars is (J)-blind:

\[
\frac{\partial P_{\mathrm{declared}}}{\partial J}=0.
\]

On an open physical16 domain,

\[
\frac{\partial}{\partial J}\lambda(J^2-cQ)^2
=4\lambda J(J^2-cQ),
\]

which is not identically zero. Therefore no expression in the current
declared scalar grammar equals the proposed portal on that domain. This is a
source-support failure, not a coordinate or detector failure.

## Second obstruction: the polynomial substitute is not normalized (J)

The nearest standard weak-basis polynomial is the commutator determinant
(det[H_u,H_d]), proportional on the nondegenerate domain to (J) times the
up- and down-sector mass discriminants. Under the common scaling
(H_u,H_d\mapsto sH_u,sH_d), its square scales as (s^{12}). The product of
the two squared cubic discriminants also scales as (s^{12}), so their ratio
is scale invariant.

Thus a polynomial contact using (|\det[H_u,H_d]|^2) selects a dimensionful
mixture of CP violation and mass gaps. It is not the normalized (J^2)
portal. Recovering (J^2) requires division by independently defined mass
discriminants, which is nonpolynomial and singular on degeneracy strata. A
source action could still provide such an effective construction, but none is
presently declared and its normalization cannot be borrowed from the fitted
physical16 packet.

## Contextual partition and exact hostile

The largest current source-authorized probe family partitions points only by
the declared Spin(5) source records. It can distinguish completion, anomaly,
radial, incidence, RG-slope, and conditional threshold data. It does not
separate physical16 points differing only in the unconnected (J) coordinate.

Take two points with the same declared (Q=1), but (J=0) and (J=2).
Every currently (J)-blind source scalar agrees, whereas (J^2-Q) equals
(-1) and (3). This two-point pair is the smallest exact falsifier of a
factorization of WP360 through the declared source grammar.

The target functional descends under the full weak-basis groupoid by
hypothesis. That fact does not manufacture its missing source arrow. No
reference port repairs source derivation; a port would define a new relational
experiment and still require an independently normalized source coupling.

## Verdict

The current Spin(5) action supplies neither a selector nor a rigidifier on
physical16 through WP360. WP360 remains a valid conditional selector theorem:
if (Q,c,lambda) and their common coupling are independently derived, its
zero set selects a proper shell. At present, appending that portal would be a
new effective interaction, not a consequence of the declared model.

The remaining gate is upstream of detector design: derive a common
weak-basis-invariant source-to-Yukawa operator and independently freeze the
mass-discriminant normalization. Only after that arrow exists does it become
meaningful to construct an instrument measuring (Q) and the CP-odd
invariant and to test the selected shell over the complete fitted ensemble.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp917_spin5_jarlskog_portal_source_support_audit.py
~~~
