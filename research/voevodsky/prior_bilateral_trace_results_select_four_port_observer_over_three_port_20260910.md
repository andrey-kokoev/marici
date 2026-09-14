# Prior bilateral trace results select the four-port observer over the provisional three-port model

## Question

Does prior research leave the seam-flux channel \(J\) hypothetical, or has a source-derived independent value--flux pair already been constructed?

## Claim boundary

This review compares the prior packets with the new finite residue classifiers. It concludes that the analytic source already supplies an independent reciprocal-even/odd trace pair and therefore selects the four-port observer at that level. It does not prove that every arithmetic stratum maps onto the complete four-port packet or supply physical acquisition semantics.

## Source-derived trace pair

The bilateral completed theta packet contains

\[
\Phi=\left(\partial_u^2-\frac14\right)h
\]

and its source-derived derivative \(\Phi'\). Define the two reciprocal half-density traces

\[
M_-(g)=\int_{\mathbb R}e^{-u/2}g(u)\,du,
\qquad
M_+(g)=\int_{\mathbb R}e^{u/2}g(u)\,du.
\]

The theta modular law makes \(\Phi\) even, while \(\Phi'\) is odd. Prior exact integration by parts gives

\[
(M_-(\Phi),M_+(\Phi))=m(1,1),
\]

and

\[
(M_-(\Phi'),M_+(\Phi'))=\frac m2(1,-1).
\]

Their determinant is

\[
- m^2,
\]

which is nonzero when \(m\ne0\). The same packets establish a positive explicit normalization in the selected theta realization. Differentiation commutes with the completion operator, so the odd companion descends through the completion quotient rather than being an arbitrary test vector.

## Value--flux coordinates

Define

\[
M=\frac{M_-+M_+}{2},
\qquad
J=\frac{M_+-M_-}{2}.
\]

Reciprocal reflection acts by

\[
M\mapsto M,
\qquad
J\mapsto-J.
\]

On the source states \(\Phi,\Phi'\), the value and flux rows are linearly independent. Equivalently, the alternating boundary pairing

\[
\omega((M,J),(M',J'))=MJ'-JM'
\]

is nonzero on a source-generated pair. This passes the prior fourth-observer acceptance test: the two ports are not merely names for one graph-related coordinate.

## Consequence for the residue classifier

The provisional three-port state

\[
(P,Q,M)
\]

omits the independently sourced odd seam trace. The selected analytic state is therefore at least

\[
(P,Q,M,J).
\]

For the visible even readout

\[
\rho_4(P,Q,M,J)=(P+Q+M,M),
\]

the full finite kernel is

\[
\ker\rho_4
=
\{(r,-r,0,j):r,j\in V_N\}.
\]

Thus its source-shaped residue object has two odd channels:

\[
\mathcal R_N
=
V_N^{\mathrm{tail,odd}}
\oplus
V_N^{\mathrm{seam,odd}},
\]

with classifier

\[
h_4(r,j)=(r,-r,0,j).
\]

The earlier map \(h_3(r)=(r,-r,0)\) remains the restriction to \(J=0\); it is not the full classifier on the bilateral trace packet.

## Four-port geometry

Prior work further identifies the four ports with a candidate joint boundary trace space

\[
\mathcal B\oplus\mathcal B
\]

for reciprocal deficiency index two. Tail and seam each carry an oriented two-plane. Reciprocal sewing reverses both constituent orientations and preserves their combined four-dimensional orientation. Omitting \(J\) leaves an unmatched orientation reversal.

This supplies a structural reason for four ports beyond rank counting: the odd seam coordinate is the orientation partner of reciprocal-tail exchange.

## Remaining source gate

The analytic existence and independence of \(M,J\) are closed by the bilateral theta packet. What remains is not whether a fourth analytic port exists. It is whether the complete arithmetic primitive, square, and connected strata map into the same four-port joint trace carrier with:

1. continuous stratum-specific incidence;
2. reciprocal covariance;
3. cutoff naturality;
4. preservation of the boundary pairing;
5. record-labelled update compatibility.

## Disposition

At the analytic observer level, the three-port model is superseded. The active candidate is the four-port observer

\[
(P,Q,M,J),
\]

and its residue classifier has two odd summands. The finite four-port classifier constructed in `four_port_hostile_to_three_observer_odd_residue_classifier.v1.json` matches this prior source evidence. Completed cross-stratum incidence and instrument lineage remain unconstructed.
