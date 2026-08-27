# The RH pentagon shadow lifts to a six-channel hyperbolic dual

Author: `marici.Nima`

Date: 2026-08-26

Status: exact categorical typing correction

## Question

The provisional five-channel census resembles the Flavor (D_5) packet. Does
the same mechanism give a source-derived order-five rotation in the theta/Tate
lane?

No. The comparison fails before invariant theory. The five entries are not
five objects of one type.

Let the source carrier be the coflag

\[
0\longrightarrow T\longrightarrow V\longrightarrow W\longrightarrow0,
\qquad \dim T=2,\quad \dim W=1.
\]

The provisional packet is

\[
E_5=T\oplus W\oplus(\det T)^*\oplus W^*.
\]

Its fifth coordinate is an exterior-area coherencer. It is not a second linear
tail observer. Consequently a pentagon obtained by forgetting these types is
an automorphism of the forgotten incidence picture, not an automorphism of the
source carrier.

## Finite naturality falsifier

Scale the tail presentation by \(t\mapsto\lambda t\). The five weights are

\[
(1,1,0,-2,0).
\]

A presentation-natural bilinear coefficient between weights \(r_i,r_j\) can
be nonzero only if \(r_i+r_j=0\). Neither tail coordinate of weight \(1\) has
a partner of weight \(-1\). Every invariant bilinear form therefore contains
the whole tail plane in its radical.

This is a one-parameter source change, so it is already a complete finite
falsifier of a natural nondegenerate five-channel Clifford carrier. No
order-five permutation can repair the absent dual type.

## Canonical lift

Linear source naturality instead applies the hyperbolic functor

\[
\mathbb H(V)=V\oplus V^*.
\]

For a source map \(A:V\to V\), its lift is

\[
\mathbb H(A)=A\oplus A^{-T}.
\]

The canonical evaluation form is

\[
Q_{\mathrm{ev}}=
\begin{pmatrix}
0&I_3\\
I_3&0
\end{pmatrix},
\]

and it obeys

\[
\mathbb H(A)^TQ_{\mathrm{ev}}\mathbb H(A)=Q_{\mathrm{ev}}.
\]

The six-channel object has signature \((3,3)\). Its determinant line remains a
derived exterior readout, but it cannot replace \(T^*\) before the linear
pairing is formed.

## Categorical DPC

The five-channel hypothesis predicts a natural transformation from the
coflag category to nondegenerate five-dimensional quadratic spaces whose
underlying carrier is \(E_5\).

The scaling witness proves that no such natural transformation exists.

The repaired construction is the functor

\[
\mathbb H:\mathrm{Vect}^{\simeq}_3\longrightarrow
\mathrm{Quad}^{\mathrm{split}}_{3,3},
\qquad V\longmapsto V\oplus V^*.
\]

Its arrows preserve the evaluation pairing without fitted coefficients.

## What survives from the pentagon

The five-fold pattern remains meaningful as a compressed presentation:

- two tail coordinates;
- one wall coordinate;
- one oriented tail-area readout;
- one wall covector.

It may organize scalar or exterior invariants. It does not carry the full
source-natural linear relationship. Any apparent \(D_5\) rotation must
therefore be typed as a quotient or presentation symmetry and must not be
promoted to source transport.

The next genuine symmetry question belongs to the six-channel hyperbolic
carrier and its Mellin--Parseval duality. Its ambient symmetry is the split
orthogonal geometry of \(Q_{\mathrm{ev}}\), not a presumed pentagon.

## Decisive consequence

The RH lane and Flavor lane share the same diagnostic method but not the same
answer. Flavor's five channels can be peers. The theta/Tate five are not.
Here the census discovers a missing dual observer, and source naturality lifts
the object from five to six channels.

## Verification

`research/nima/checkers/check_rh_five_to_six_channel_lift.py` checks the
five-channel radical under tail scaling, the full rank and signature of the
six-channel evaluation form, and its exact preservation under a nontrivial
rational source transfer.
