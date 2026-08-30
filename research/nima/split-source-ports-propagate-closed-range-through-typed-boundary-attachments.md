# Split source ports propagate closed range through typed boundary attachments

## General propagation lemma

Let \(B_j\) be consecutive boundary carriers, with attachment maps

\[
T_j:B_j\to B_{j+1}.
\]

Suppose each carrier has a source-recovery port

\[
\pi_j:B_j\to H_j
\]

and the attachment square intertwines it with a transport

\[
U_j:H_j\to H_{j+1}:
\qquad
\pi_{j+1}T_j=U_j\pi_j.
\]

Assume

\[
\|\pi_j b\|\ge c_j\|b\|
\]

on the declared source-generated relation and

\[
\|U_jh\|\ge m_j\|h\|.
\]

Then

\[
\|\pi_{j+1}T_jb\|
=
\|U_j\pi_jb\|
\ge
m_jc_j\|b\|.
\]

Therefore \(T_j\) preserves a closed source-generated range whenever
\(m_jc_j>0\).

For a composite \(T_{r-1}\cdots T_0\), the derived lower bound is

\[
c_r
\ge
c_0\prod_{j=0}^{r-1}m_j.
\]

This is useful only if the product is uniformly separated from zero over the
admitted constructor depth. Unitary transports have \(m_j=1\).

## Initial Adams port

The paired Adams interface

\[
J_Pf=(f,\Theta_{\mathrm{ren}}f)
\]

has the recovery port

\[
\pi_0(f,\Theta_{\mathrm{ren}}f)=f
\]

and lower bound \(c_0=1\). Thus every later loss of closed range must occur at
an attachment that either fails to intertwine this port or transports it with
a collapsing lower bound.

## Endpoint loading

The source endpoint observer already supplies the matrix

\[
V_p
=
\frac12
\begin{pmatrix}
1&p^{-1}\\
p^{-1}&1
\end{pmatrix}.
\]

Its wall and jump eigenvalues are

\[
\lambda_{\mathrm{wall},p}
=
\frac12(1+p^{-1}),
\qquad
\lambda_{\mathrm{jump},p}
=
\frac12(1-p^{-1}).
\]

For all primes,

\[
\sigma_{\min}(V_p)\ge\frac14.
\]

Therefore endpoint loading preserves the split port with \(m_{\mathrm{end}}\ge
1/4\), provided the endpoint attachment actually intertwines the Adams
wall--jump coordinates with \(V_p\). The matrix estimate is complete; the live
gate is the typed intertwining square.

## Reciprocal sewing

A source-unitary reciprocal sewing cell has \(m_{\mathrm{rec}}=1\). Hence it
cannot reduce the port margin. But unitarity of an ambient sewing map is
insufficient: the recovery port must transform covariantly,

\[
\pi_{\mathrm{opp}}T_{\mathrm{rec}}
=
U_{\mathrm{rec}}\pi_{\mathrm{same}}.
\]

If reciprocal sewing mixes the source port with an unobserved radical, the
ambient norm can remain unitary while source recovery fails.

## Archimedean attachment

Adjoining an independent archimedean coordinate by a direct graph map

\[
b\longmapsto(b,A_\infty b)
\]

preserves the old recovery port by projection and therefore has lower bound at
least one on the old source relation. A quotient attachment does not receive
this conclusion automatically.

Thus the safe archimedean constructor is initially an extension. Any later
identification must pass the quotient test below.

## Radical reduction

Let \(q:B\to B/N\) be quotient by a Green radical \(N\). A recovery port
\(\pi:B\to H\) descends exactly when

\[
N\subseteq\ker\pi.
\]

If it descends to \(\bar\pi\), closed-range control additionally requires a
lower bound on the reduced source relation:

\[
\|\bar\pi\,q b\|
\ge
c_{\mathrm{red}}\|q b\|.
\]

Radical annihilation alone proves well-definedness, not uniform faithfulness.
The quotient norm can collapse relative to the port even when every finite
cutoff descends.

## Direct-sum assembly over primes

For primewise ports with bounds \(c_p\), the Hilbert direct sum obeys

\[
\left\|
\bigoplus_p\pi_pb_p
\right\|^2
\ge
\left(\inf_pc_p\right)^2
\sum_p\|b_p\|^2.
\]

The endpoint estimate supplies \(\inf_pc_p\ge1/4\) before later reductions.
Euler half-density weights control the upper prime sum. Therefore cross-prime
failure cannot arise in this split model unless an attachment mixes prime
idempotents or the radical quotient couples them.

## Concrete audit table

The complete Adams-to-boundary path now has the following status:

| stage | quantitative port result | remaining authority test |
|---|---|---|
| paired unit/theta graph | lower bound \(1\) | closed |
| endpoint matrix | lower bound \(1/4\) | prove attachment intertwining |
| reciprocal sewing | no loss if source-unitary | prove port covariance |
| archimedean extension | no loss as direct graph | derive source attachment |
| Green radical quotient | none automatic | prove descent and reduced lower bound |
| prime direct sum | inherits infimum bound | prove every attachment commutes with prime idempotents |

## Typing correction: two different source ports

The paired Adams graph recovers an analytic source vector such as \(b_p\). The
endpoint matrix \(V_p\) acts instead on the doubled signal fiber

\[
\mathcal S_p=\mathbb C e_p^+\oplus\mathbb C e_p^-.
\]

These spaces cannot be identified merely because both constructions are
primewise and two-port data appear downstream. Therefore the previously
suggested square with \(V_p\pi_{\mathrm{Adams}}\) was ill-typed.

The endpoint square that is already proved is

\[
\operatorname{Tr}_{\mathrm{end}}\mathcal I_p=V_p,
\]

where

\[
\mathcal I_p(c_+,c_-)
=
p^{-1/2}
\left(
c_+\tau_L\Phi,\,
c_-\tau_{-L}\Phi
\right).
\]

This gives a closed, uniformly faithful signal-to-history endpoint port, but
it does not attach the analytic Stieltjes source \(b_p\) to
\(\mathcal S_p\).

## First unresolved comparison

The earliest missing cell is a map

\[
A_p:
\mathcal H_{b,p}\longrightarrow\mathcal S_p
\]

or an authorized relation with the same typing, such that the analytic
base-plus-curvature Green solution and the doubled theta-history incidence
have the same endpoint boundary:

\[
\operatorname{Tr}_{\mathrm{end}}T_{\mathrm{hist},p}J_P
=
V_pA_p.
\]

Only after constructing \(A_p\) may the endpoint margin be propagated back to
the Adams source. If

\[
\|A_pf\|\ge a_0\|f\|
\]

on the relevant source-generated subspace, then the inherited endpoint lower
bound is \(a_0/4\).

No such lower bound follows from \(V_p\) alone.

## Verdict

The local closed-range problem factors into source-port intertwining squares,
but the Adams unit port and doubled endpoint signal port are distinct.

The paired Adams graph has margin one, and the endpoint incidence has margin
one quarter on \(\mathcal S_p\). The exact frontier is the typed comparison
\(A_p\) between those source objects. Scalar agreement or equality of their
two-dimensional shadows cannot supply it.

