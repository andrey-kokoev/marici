# Theta cumulative prime boundary windows exactly reconstruct seam energy

## Bounded question

Does the vanishing of the terminal prime-shift boundary window imply that seam
energy escapes at infinity?

## Prime-orbit windows

Fix a prime (p) and put (L=\log p). For the cut (q_N=NL), partition its
seam atom

\[
h_{q_N}(t)=\mathbf 1_{0\le t\le NL}\Phi(NL-t)
\]

into the (N) consecutive intervals crossed by successive prime shifts.
After reflecting each interval into the common coordinate (0<u<L), the
(k)-th boundary innovation is

\[
b_k(u)=\Phi(kL+u),
\qquad 0<u<L,
\qquad 0\le k<N.
\]

These are exactly the Hankel windows produced by the unilateral shift defect
at the successive cuts.

## Exact energy identity

The windows occupy disjoint physical intervals before reflection. Therefore

\[
\sum_{k=0}^{N-1}\|b_k\|_{L^2(0,L)}^2
=\sum_{k=0}^{N-1}\int_{kL}^{(k+1)L}|\Phi(v)|^2\,dv
=\int_0^{NL}|\Phi(v)|^2\,dv.
\]

But the last integral is exactly the seam norm:

\[
\|h_{NL}\|^2
=\int_0^{NL}|\Phi(v)|^2\,dv.
\]

Hence

\[
\|h_{NL}\|^2
=\sum_{k=0}^{N-1}\|b_k\|^2.
\]

The cumulative boundary-history transform is an isometry on every finite
prime-power orbit and remains isometric after completion.

## Resolution of the apparent escape

Packet 225 proved

\[
\|b_N\|\longrightarrow0
\]

while

\[
\|h_{NL}\|\longrightarrow\|\Phi\|_2>0.
\]

There is no contradiction. The terminal innovation becomes small because the
theta tail decays, while the earlier innovations remain stored in the causal
boundary record. Testing only (b_N) discards the history accumulated during
the first (N) shifts.

Thus the completion defect was caused by a non-causal readout:

- terminal-window observation is injective at finite cutoff but unstable;
- cumulative-window observation is exactly norm preserving.

## Operator form

Let

\[
\mathcal B_L:L^2(0,\infty)
\longrightarrow
\bigoplus_{k\ge0}L^2(0,L)
\]

be interval restriction followed by translation to the base window:

\[
(\mathcal B_Lf)_k(u)=f(kL+u).
\]

Then

\[
\mathcal B_L^*\mathcal B_L=I.
\]

This is not a fitted norm. It is the canonical causal record of the boundary
strips swept out by repeated multiplication by (p).

## Consequence for the doubled Green programme

The correct boundary state is not one fixed-origin window and not an endpoint
jet. It is the full innovation sequence

\[
(b_0,b_1,b_2,\ldots).
\]

This state is infinite-rank, prime-resolved, completion-stable, and exactly
faithful to seam energy. The remaining RH-bearing question is no longer
observability. It is whether the doubled Green identity assigns these
innovations the oriented coefficient (2\Re s-1), with reciprocal sewing
matching the two causal directions.

## Reciprocal role

On the positive valuation sector, the innovation index (k\ge0) records
outward prime transport. Fourier--Tate reflection supplies the oppositely
oriented history. The two-sector object should therefore compare two complete
innovation towers, rather than compare their terminal windows.

## Reciprocal Mellin orientation

Write \(\sigma=\Re s\) and let

\[
e_k=\|b_k\|^2\ge0.
\]

The direct and reciprocal valuation sectors weight depth (k) by

\[
p^{-2\sigma k}
\qquad;qquad
p^{-2(1-\sigma)k}.
\]

Their paired boundary-energy difference is

\[
\mathcal E_p(\sigma)
=\sum_{k\ge0}
\left(
p^{-2\sigma k}-p^{-2(1-\sigma)k}
\right)e_k.
\]

For every (k\ge1),

\[
p^{-2\sigma k}-p^{-2(1-\sigma)k}
=2p^{-k}\sinh\left((1-2\sigma)k\log p\right).
\]

Every nonzero summand therefore has the sign of (1-2\sigma). If at least one
positive-depth innovation is nonzero, then

\[
\operatorname{sgn}\mathcal E_p(\sigma)
=\operatorname{sgn}(1-2\sigma),
\]

and equality occurs exactly at \(\sigma=1/2\).

Equivalently,

\[
\mathcal E_p(\sigma)
=(1-2\sigma)\mathcal R_p(\sigma),
\]

where

\[
\mathcal R_p(\sigma)
=2\sum_{k\ge1}p^{-k}k\log p
\frac{\sinh((1-2\sigma)k\log p)}
{(1-2\sigma)k\log p}
e_k>0.
\]

The quotient is continued by value (1) on the seam. Thus reciprocal sewing
does orient the complete causal innovation history by an explicit positive
relationship energy. No local prime positivity and no fitted cone are used.

## Remaining bridge

This resolves the local orientation problem for the complete boundary record.
The remaining theorem is whether a scalar zero-state forces the total paired
boundary-energy difference to vanish after all primes and the archimedean
channel are assembled. That is the still-missing Evans/Green bridge. If it
does, the strictly positive factor above forces \(\Re s=1/2\).

## Scope

This packet proves exact finite and completed seam-energy reconstruction by
cumulative prime boundary windows and derives the sign of the reciprocal
Mellin-weighted boundary-energy difference. It does not prove that a scalar
zero annihilates the assembled boundary flux, construct the Evans determinant,
control cross-prime aggregation, or prove RH.
