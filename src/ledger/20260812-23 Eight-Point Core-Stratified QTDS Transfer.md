# Eight-Point Core-Stratified QTDS Transfer

## Record

Date: 2026-08-12

Status: exact symbolic calculation proves that the triangulation-resolved sixth scalar grade at
eight points supplies every part of either QTDS polarity after stratification by parity core.
Full cores give the double-pole terms, one-core fibers redistribute exactly within physical
factorization triangles, and the four zero-core scalar cells give exactly the remaining contact
sum. A unique shortest marked transfer reproduces the two QTDS contact allocations and is
exchanged by one-step rotation.

This is a coefficient-level existence result. It is not yet a scalar-only construction of the
oriented transfer, a cellular chain map, or the filtered comparison to twisted worldsheet chains.

## Scalar cells retained before summation

Work in formal planar eight-point kinematics with twenty independent variables \(X_D\). For every
scalar triangulation \(T\), take its sixth alternating large-parameter grade before summing over
triangulations:

\[
s_T=[t^6]\prod_{D\in T}\frac{1}{X_D+\sigma_D/t}.
\]

The parity core is the subset

\[
\rho(T)=T\cap\mathcal D_{\rm odd},
\]

where \(\mathcal D_{\rm odd}\) is the set of eight admissible QTDS propagator diagonals. The 132
scalar triangulations split as

\[
96\quad(|\rho|=2),
\qquad
32\quad(|\rho|=1),
\qquad
4\quad(|\rho|=0).
\]

There are twelve full cores \(Q\), eight one-channel cores \(D\), and one zero-core sum. Define

\[
G_Q=\sum_{\rho(T)=Q}s_T,
\qquad
H_D=\sum_{\rho(T)=\{D\}}s_T,
\qquad
Z=\sum_{\rho(T)=\varnothing}s_T.
\]

## Exact diagramwise decomposition

Let \(q_Q^\epsilon\) be the QTDS diagram with quadrangulation \(Q\) and polarity
\(\epsilon\in\{+,-\}\). Its Laurent support decomposes uniquely by pole number:

\[
\boxed{
q_Q^\epsilon
=
G_Q
+\sum_{D\in Q}R_{Q,D}^\epsilon
+K_Q^\epsilon.
}
\]

The exact calculation proves all of the following.

First, \(G_Q\) is the complete double-pole part of \(q_Q^\epsilon\), independently of polarity.
No double pole remains after subtraction.

Second, \(R_{Q,D}^\epsilon\) has precisely the single physical denominator \(X_D^{-1}\), and it
vanishes unless \(D\in Q\). For each physical channel,

\[
\boxed{
\sum_{Q\ni D}R_{Q,D}^\epsilon=H_D.
}
\]

The sum runs over the three quadrangulations in the factorization triangle of \(D\). Thus the
one-core scalar grade is redistributed locally and exhaustively on that triangle for each
polarity.

Third, the regular terms satisfy

\[
\boxed{
\sum_QK_Q^\epsilon=Z.
}
\]

Consequently

\[
\sum_Qq_Q^\epsilon
=
\sum_Ts_T
\]

for both polarities, now with the full pole/contact provenance retained rather than checked only
after summation.

## Closed contact grammar

Let \(d_i\), with indices modulo eight, be the compatibility cycle of admissible diagonals. Write

\[
C_i=(d_i,d_{i+1}),
\qquad
M_i=(d_i,d_{i+4}),
\]

for the eight cycle quadrangulations and four antipodal quadrangulations. Let

\[
x_i=X_{i,i+2},
\qquad
h_i=X_{i,i+4},
\]

with \(x_i\) modulo eight and \(h_i\) modulo four. The exact regular contact allocation is

\[
K^+(C_{2k})=K^+(C_{2k+1})
=-(x_{2k-3}+x_{2k-2}),
\]

\[
K^+(M_0)=-(h_0+h_3),
\qquad
K^+(M_2)=-(h_1+h_2),
\qquad
K^+(M_1)=K^+(M_3)=0,
\]

and

\[
K^-(C_{2k-1})=K^-(C_{2k})
=-(x_{2k}+x_{2k+1}),
\]

\[
K^-(M_1)=-(h_0+h_1),
\qquad
K^-(M_3)=-(h_2+h_3),
\qquad
K^-(M_0)=K^-(M_2)=0.
\]

One-step cyclic rotation exchanges the two formulas.

Each of the four zero-core scalar triangulations contributes

\[
s_T=-\sum_{d\in T}X_d.
\]

Hence the scalar source and each polarity target contain exactly twenty marked monomial
occurrences. This equality is finer than equality of their total contact polynomials.

## Shortest marked transfer

Retain a source occurrence as a pair \((T,d)\), rather than forgetting which zero-core cell
contributed \(X_d\). Retain a target occurrence as \((Q,d)\). Among assignments preserving the
mark \(d\), minimize the scalar flip-graph distance from \(T\) to the full-core fiber over \(Q\).

The finite exact assignment problem has, for each polarity:

1. a unique minimum;
2. twenty transfers, all of distance two;
3. exact exchange of the plus and minus matchings by one-step rotation.

This gives a concrete candidate support for an edge-flow representative. It is deliberately not
called an intrinsic derivation: the optimization is supplied with the already known QTDS target
support. A scalar-only rule must construct that support and its orientations without consulting
the target amplitude.

## A useful falsification

Every zero-core cell contains a unique diameter. The four diameter squares are therefore natural
coherence carriers. The exact matching nevertheless proves that some marked contacts leave the
square associated with their source diameter.

Thus the rule

> assign each zero-core scalar contact directly to a quadrangulation in its own diameter square

is false. The squares compare transport paths; they are not independent contact bins. Any valid
lift requires genuine transport across scalar flip edges, followed by square and octagonal
coherence.

## Relation to the octagonal obstruction

Entries 21 and 22 identify the eight triangles and four squares as a Möbius carrier whose
remaining boundary is the octagon. The present calculation now fixes the endpoint coefficients
that an edge transport must realize. The next bounded problem is therefore no longer to guess
the eight-point contact allocation. It is to construct a local, deck-equivariant scalar edge
operator \(T_e\) such that:

\[
T_e\ \text{realizes the marked distance-two transfers},
\]

\[
T_{\gamma_5}=-\mathbf1,
\qquad
T_{\partial O}=+\mathbf1,
\]

and its filtered worldsheet image makes the residue-free octagonal class

\[
\mathfrak o_8\in H^4(K^\bullet_{\rm ct})^-
\]

well-defined and testable.

The full associahedron can fill the bare octagon by a cone. Therefore failure can occur only
after imposing locality, weights, deck parity, and compatibility with physical residues.

## Reproducible audit

Run:

    python research/nima/check_eight_point_transfer.py

The standard-library script performs exact sparse Laurent-polynomial arithmetic in all twenty
formal planar variables. It checks both polarities, every individual quadrangulation, every
physical channel, the closed contact formulas, both minimum-distance matchings, cyclic exchange,
and failure of naive diameter-square confinement.

## Provenance boundary

Established by exact calculation:

1. the core-stratified diagramwise decomposition;
2. channel-local one-core redistribution;
3. the complete contact grammar above;
4. the unique conditional shortest matching;
5. its cyclic polarity exchange;
6. failure of direct diameter-square localization.

Not established:

1. a target-independent scalar construction of the matching;
2. orientations and coefficients on individual scalar flip edges;
3. triangle, square, and octagon identities for those edge operators;
4. a filtered Pochhammer/Cousin comparison;
5. vanishing of the deck-odd octagonal contact class;
6. identification of the octagonal equation with the Jordan identity.

## Decision

The eight-point scalar grade contains the complete QTDS pole and contact data at the level of
core-stratified coefficients. The surviving frontier is categorical rather than numerical:

> derive the marked transfer as a natural scalar edge flow and prove, or falsify, its global
> deck-odd coherence before mapping it to twisted chains.

Entry 24 completes this presentation-level target: alternating scalar coorientation derives the
matching without QTDS input, its local deck-odd edge transport has the required contact boundary,
and its octagonal contact curvature vanishes. The remaining problem is its filtered worldsheet
image.
