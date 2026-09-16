# Global absolute-Gram Mosco convergence reduces to uniform graph-core and compression control

## Objective

Identify the first genuinely global estimates needed after exact positive-regulator alignment and finite-packet common-edge removal.

## Setup

Let \(\mathcal E_1\subset\mathcal E_2\subset\cdots\) be the coercive finite observer packets, with orthogonal projections \(P_n\to I\) on the completed source \(\mathcal E\). Assume the still-open physical alignment theorem supplies global centered operators/forms

\[
D_\Lambda=G_\Lambda^T-G_\Lambda^0
\]

whose packet restrictions converge to \(W_n=P_nWP_n\). Common-edge removal then gives finite residual positive forms

\[
r_{\Lambda,n}(u)=
\langle u,|P_nD_\Lambda P_n|u\rangle
\longrightarrow
\langle u,|W_n|u\rangle
\]

for \(u\in\mathcal E_n\).

This alone does not define a compatible global form, because

\[
|P_nD_\Lambda P_n|
\ne
P_n|D_\Lambda|P_n
\]

in general.

## Required packet-independent residual

The global residual must be produced before compression. Namely, aligned
positive features and their common edge must give a positive form

\[
r_\Lambda
=
G_\Lambda^T+G_\Lambda^0-2C_\Lambda
\]

on one dense regulator-independent core \(\mathcal C\subset\mathcal E\), with

\[
r_\Lambda|_{\mathcal E_n}=r_{\Lambda,n}.
\]

This is stronger than independently taking the Jordan absolute value on each
packet. It makes packet compatibility a property of the physical residual
feature, not of compressed functional calculus.

## Two estimates sufficient for globalization

Assume each \(r_\Lambda\) is a closed nonnegative form and the proposed limit
is

\[
r(u)=\||W|^{1/2}u\|^2,
\qquad D(r)=D(|W|^{1/2}).
\]

The finite-packet theorem globalizes by the standard Mosco argument if the
following two estimates hold.

### 1. Uniform graph-core recovery

For every \(u\in D(r)\),

\[
\boxed{
\lim_{n\to\infty}
\sup_{\Lambda\ge\Lambda_n}
 r_\Lambda(u-P_nu)=0,}
\]

with also \(r(u-P_nu)\to0\). Then a diagonal choice of packet and regulator
produces the Mosco recovery sequence.

### 2. Asymptotic compression contraction

For every fixed \(n\), there are \(\epsilon_{\Lambda,n}\to0\) such that

\[
\boxed{
r_\Lambda(P_nu)
\le r_\Lambda(u)+
\epsilon_{\Lambda,n}
\bigl(\|u\|^2+r_\Lambda(u)\bigr)}
\]

for all \(u\in D(r_\Lambda)\).

If \(u_\Lambda\rightharpoonup u\) and the right side is bounded, this estimate
allows finite-packet lower semicontinuity to be applied to \(P_nu_\Lambda\).
Taking first \(\Lambda\to\infty\), then \(n\to\infty\), yields

\[
r(u)\le\liminf_\Lambda r_\Lambda(u_\Lambda).
\]

Together these are exactly the Mosco upper and lower conditions. Hence the
associated nonnegative self-adjoint operators converge in strong resolvent
sense.

## Operator form of the compression defect

When \(r_\Lambda(u)=\|R_\Lambda^{1/2}u\|^2\), a concrete sufficient estimate
for compression contraction is control of the off-diagonal block

\[
\boxed{
\|(I-P_n)R_\Lambda^{1/2}P_n\|
\longrightarrow0}
\]

in the appropriate graph-to-Hilbert norm, uniformly over the regulator tail.
Equivalently, the observer filtration must asymptotically reduce the residual
feature. This is precisely what packetwise spectral decomposition does not
supply.

(The displayed norm is understood as
\(\|(I-P_n)R_\Lambda^{1/2}P_n\|\); the
mnemonic “off-diagonal block” is the invariant content.)

## First missing estimate

The repository currently has finite-dimensional norm convergence after fixing
\(n\), but no estimate uniform in both packet and regulator of either boxed
type. In particular, pointwise convergence

\[
P_nD_\Lambda P_n\to P_nWP_n
\]

does not control off-packet Gram leakage.

Therefore, after positive-regulator alignment, the first missing global bound
is:

\[
\boxed{
\text{uniform asymptotic reduction of the global residual feature by the
observer filtration}.}
\]

A reference Widom leading law controls diagonal bulk size; it does not by
itself control this off-diagonal leakage.

## Practical next target

Construct the residual feature \(Y_\Lambda\) before packet compression, so that
\(R_\Lambda=Y_\Lambda^*Y_\Lambda\), and prove a commutator/tail estimate such as

\[
\|[Y_\Lambda,P_n]u\|
\le \eta_n\|u\|_{D(r)},
\qquad \eta_n\to0,
\]

uniformly for sufficiently large \(\Lambda\). This single estimate supplies
both graph-core recovery and compression control after routine polarization.

## Updated channel-2 frontier

1. exact physical positive-regulator alignment: open;
2. packet-independent residual feature: open and must precede compression;
3. fixed-packet common-edge/absolute-Gram convergence: available conditionally;
4. uniform observer-filtration commutator estimate: first missing global
   analytic estimate;
5. Mosco and strong-resolvent convergence: formal after 2 and 4.

## Repository dependencies

- `the-finite-absolute-gram-closure-is-conditional-on-one-exact-positive-regulator-alignment.md`
- `common-widom-edge-removal-closes-the-absolute-gram-gate-on-every-coercive-finite-packet.md`
- `bounded-relative-gram-convergence-transfers-the-reference-widom-law-to-the-tate-regulator.md`
- `prolate-to-tate-bulk-removal-is-exactly-the-absolute-gram-gate-and-is-not-closed-by-signed-sewing.md`
