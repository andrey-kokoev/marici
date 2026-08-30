# 3323 — The e6 Logarithmic Torsor Is a Cyclic Leray Descent Connection

## Question

Entry 3320 excludes a single moving-wall Leray interval as the selection map
for the primitive (e_6) logarithmic torsor. Does the missing (X_3=0)
component arise when the full cyclic occurrence descent datum is retained?

## Frozen input

Entry 304 fixes the common normalized wall frame in the
(mathcal G_{12}) occurrence sector:

\[
n_{12}=-\frac{1}{2X_1X_2}.
\]

Entries 756 and 764 derive the labelled, orientation-sensitive occurrence
transport and its cyclic closure. Applying that transport, rather than an
untyped parameter substitution, gives the three cyclic frames

\[
n_{12}=-\frac{1}{2X_1X_2},\qquad
n_{23}=-\frac{1}{2X_2X_3},\qquad
n_{31}=-\frac{1}{2X_3X_1}.
\]

The Poincaré-residue signs are constant units. They affect oriented frames but
not their logarithmic transition connections.

## Cyclic transition cocycle

The transition functions are

\[
g_{12,23}=\frac{n_{23}}{n_{12}}=\frac{X_1}{X_3},
\]

\[
g_{23,31}=\frac{n_{31}}{n_{23}}=\frac{X_2}{X_1},
\]

and

\[
g_{31,12}=\frac{n_{12}}{n_{31}}=\frac{X_3}{X_2}.
\]

Their Čech product closes exactly:

\[
g_{12,23}g_{23,31}g_{31,12}=1.
\]

Thus the logarithmic class is not an isolated fitted pole. It is an edge of a
source-normalized cyclic descent cocycle.

## Homogeneous specialization

On the (mathcal G_{12}) homogeneous chart,

\[
X_1=1,\qquad X_2=\frac{v-2}{2},\qquad X_3=-\frac v2.
\]

Therefore

\[
g_{31,12}=\frac{X_3}{X_2}=-\frac{v}{v-2}
\]

and

\[
d\log g_{31,12}
=d\log\frac{v}{v-2}
=-\frac{2\,dv}{v(v-2)}.
\]

Its ordered residues at (v=0,2) are

\[
(1,-1).
\]

This is exactly the primitive logarithmic form isolated in Entry 3315. With
the source double-pole coefficient

\[
C_2=-\frac18,
\]

the candidate is

\[
\frac{dv}{4v(v-2)}
=C_2\,d\log g_{31,12}.
\]

## Result

The primitive (e_6) logarithmic torsor has a source-derived geometric home:
it is the connection on the (mathcal G_{31}	omathcal G_{12}) cyclic
Leray-frame transition.

This explains simultaneously:

- why both soft divisors (X_3=0) and (X_2=0) occur;
- why their residues are primitive and opposite;
- why the class is globally logarithmic but locally regular away from the
  soft boundary;
- why one occurrence chart alone cannot produce it;
- why the three occurrence transitions carry no residual cyclic obstruction.

## Typing limit

This result derives the logarithmic class as occurrence-descent data. It does
not yet prove that the common four-stratum rank-twelve reduction selects this
class as its off-diagonal extension coordinate (B_{e_6,q_0}).

The distinction is now narrow:

- the class and its normalization have source provenance;
- its insertion into the rank-twelve extension remains a comparison-map
  question.

No new carrier divisor or physical singularity is introduced. The class is
transition data over the existing soft-divisor arrangement.

## Next falsifier

Construct the labelled cyclic transition on the rank-twelve
(W_3\oplus M_9) extension and project its lower-left block to the
((e_6,q_0)) coordinate. The candidate survives only if this projection equals
(C_2d\log g_{31,12}) independently of the common primitive section.

## Verification

The exact checker is
`research/benincasa/checkers/audit_cyclic_leray_transition_torsor.py`; its
packet is
`research/benincasa/results/cyclic_leray_transition_torsor.json`.
