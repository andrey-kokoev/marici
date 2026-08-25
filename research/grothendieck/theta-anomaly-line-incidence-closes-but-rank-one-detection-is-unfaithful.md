# Theta anomaly-line incidence closes but rank-one detection is unfaithful

## Canonical arithmetic aggregation

Let `S` be a finite prime cutoff.  Write `L_S` for its anomaly line and choose
the source vacuum vector `e_S` supplied by the finite tensor product.  The
bonding maps satisfy

\[
 U_{S,T}e_S=e_T
\]

by definition of transported line vectors; no common scalar trivialization is
chosen.

Packet 179 supplies the common labelled seam trace

\[
 \tau_S(c)=\sum_{q\in Q_S}c_q\Phi(q).
\]

Define the source aggregation

\[
 \boxed{
 \lambda_S(r)=r e_S,
 \qquad
 I_S=\lambda_S\tau_S.}
\]

For the source inclusion `V_(S,T)` which retains every old label with its
coefficient, endpoint locality gives

\[
 \tau_TV_{S,T}=\tau_S.
\]

Therefore

\[
\begin{aligned}
 I_TV_{S,T}
 &=\lambda_T\tau_TV_{S,T}\\
 &=\lambda_T\tau_S\\
 &=U_{S,T}\lambda_S\tau_S\\
 &=U_{S,T}I_S.
\end{aligned}
\]

Thus:

\[
 \boxed{
 I_TV_{S,T}-U_{S,T}I_S=0.}
\]

The remaining rank-one arithmetic incidence square closes exactly.  Its
primitive and square anomalies live in the transported basis `e_S`; they do
not appear as a scalar residual.

## Quotient-surjectivity gate

Although `V_(S,T)` need not be surjective on the full coefficient module, the
endpoint quotient is one-dimensional whenever `tau_S` is nonzero:

\[
 C_S/\ker\tau_S\simeq\mathbb C.
\]

Because `tau_T V_(S,T)=tau_S`, the induced map on these quotients is
surjective.  Hence Kitaev's transported rank-one graph has equality, not only
inclusion.

## The unavoidable detector kernel

Exact transport coherence does not make the detector faithful.  For two
distinct labels `q_1,q_2` with nonzero source values, the coefficient packet

\[
 c=\Phi(q_2)e_{q_1}-\Phi(q_1)e_{q_2}
\]

is nonzero but satisfies

\[
 \boxed{\tau_S(c)=0.}
\]

Thus every endpoint line with at least two visible labels has a nontrivial
kernel.  The anomaly-line incidence can vanish by ordinary orthogonality while
all transition maps remain invertible and perfectly coherent.

This is the source-native version of Kitaev's abstract witness
`T=I, psi=e_1, ell=e_2^*`.

## Consequence for the RH architecture

The scalar endpoint line cannot supply a determinant--kernel bridge for the
full labelled source module:

\[
 \boxed{
 I_S(c)=0
 \not\Rightarrow
 c=0.}
\]

Therefore the direct rank-one incidence route is now closed as an RH proof
mechanism.  It remains the correct scalar readout, but not a faithful state
detector.

The minimal source-derived enlargement is the Cauchy-jet detector

\[
 \mathcal J_S(c)
 =\left(
 \sum_qc_q\Phi^{(k)}(q)
 \right)_{k\ge0},
\]

or equivalently the full seam germ

\[
 t\longmapsto\sum_qc_q\Phi(t+q).
\]

Its degree-zero projection is `tau_S`, while higher jets retain distinctions
that the scalar endpoint discards.  A determinant/kernel theorem must be
proved on this enlarged detector and only then compressed to the scalar Tate
section.

## Next theorem and falsifier

For a finite set of distinct labels, test whether

\[
 \sum_qc_q\Phi(t+q)\equiv0
 \quad\Longrightarrow\quad
 c_q=0\text{ for every }q.
\]

Equivalently, seek a nonzero finite coefficient packet annihilated by every
seam jet.  The smallest such packet is the decisive falsifier.

Even finite-germ faithfulness will not prove RH.  The completed theorem must
also exclude a normalized sequence whose full germs tend to zero in the
source topology.

## Scope

The packet proves exact rank-one incidence descent and gives an explicit
two-label kernel.  It proposes, but does not yet prove, faithfulness or
completion stability of the full Cauchy-jet detector.
