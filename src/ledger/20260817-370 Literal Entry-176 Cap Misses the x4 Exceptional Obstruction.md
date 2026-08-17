# Literal Entry-176 Cap Misses the x4 Exceptional Obstruction

## Result

The literal relative cap proved in Entry 176 cannot repair the full
three-class exceptional obstruction packet of Entry 369.  The obstruction is
already visible from support, rank, and degree:

\[
\mathsf T_E=
\mathsf T_{D_{03},x_1}[1]
\oplus
\mathsf T_{D_{03},x_1,x_4}
\oplus
\mathsf T_{D_{03},x_1,x_3},
\]

whereas Entry 176 supplies one degree-\(-1\), rank-one cap supported on the
physical edge \(e_r=\{D_{03},x_3\}\).  Even granting the strongest possible
typed extension of that cap between the \(x_3\)-branch class and the center
class, the \(x_4\)-branch class is outside its support and survives.

Therefore

\[
\boxed{\text{the literal Entry-176 cap is insufficient for }
\omega_{q|\widetilde G_E}.}
\]

This is not merely the earlier global type mismatch.  It is a precise local
support no-go after exceptional restriction.

## Rank-and-degree certificate

On the surviving associated packet, the incidence ranks are

\[
\operatorname{rank}\mathsf T_E^0=2,
\qquad
\operatorname{rank}\mathsf T_E^1=1.
\]

The two degree-zero generators are the \(x_3\) and \(x_4\) branch triples;
the degree-one generator is the center pair.  The strongest differential
compatible with the literal Entry-176 support has matrix

\[
d_{176}=\begin{bmatrix}1&0\end{bmatrix},
\]

up to a primitive sign.  Its homology ranks are

\[
(\operatorname{rank}H^0,\operatorname{rank}H^1)=(1,0).
\]

The surviving \(H^0\) line is the unsupported \(x_4\) branch.  Virtual
Cartier cancellation

\[
L^{-1}[1]\otimes L[-1]\simeq\mathcal O
\]

does not change this support rank; it cancels the determinant and shift, not
the unrelated completion-dual coefficient.

## The minimal viable reduction

There is nevertheless a sharp positive gate.  Pass first to a physical
support quotient in which the nonphysical \(x_4\)-branch obstruction is
zero.  The packet then has one generator in each of degrees zero and one:

\[
\mathsf T_E^{\mathrm{phys}}=
\mathsf T_{D_{03},x_1}[1]
\oplus
\mathsf T_{D_{03},x_1,x_3}.
\]

A primitive degree-\(-1\) map between these two lines has matrix \([1]\) and
an acyclic cone.  Thus Entry 176 has exactly the correct **numerical** rank
and degree after the \(x_4\) quotient.

What remains unproved is the essential coefficient statement.  Entry 176's
\(k=1\) is a primitive map of finite relative cellular orientation lines.
It has not been typed as a morphism

\[
\mathsf T_{D_{03},x_1,x_3}
\longrightarrow
\mathsf T_{D_{03},x_1}[1]
\]

between the actual multi-localization dual modules occurring in
\(q^!\).  Rank compatibility cannot manufacture that map.

## Correct next experiment

The next construction is now minimal and binary:

1. Define the physical support quotient functor that kills the
   \(x_4\)-branch sector and verify that it retains the center and \(x_3\)
   exceptional sectors.
2. Lift the Entry-176 cap through that functor to the displayed
   localization-dual module map.
3. Compute its scalar on the two rank-one associated classes.  A unit gives
   a perfect cone; zero or a nonunit leaves a nonperfect completion class.

This replaces the vague question “is Entry 176 the dualizing object?” by one
explicit unit test.

## Delegated audit

The read-only low-cognition worker run
`run-b5419e7134564f5bafbb940bcdcd6897` independently confirmed that Entry 176
proves only one local rank-one channel, has no support-typed map to the full
three-class packet, and cannot by itself establish annihilation of that
packet.  The worker result is supporting audit evidence; the repository
checker supplies the exact certificate.

## Evidence boundary

`research/voevodsky/check_d03_exceptional_cap_packet_gate.rs` verifies the
rank, support, and degree no-go and the reduced \([1]\)-matrix gate.  It does
not construct the physical quotient or the localization-dual coefficient
map.  No perfectness claim is made before that map is built and evaluated.
