# All-moment cancellation on a compactly supported front erases the front

## Theorem

Let \(\varphi\in C_c^\infty(\mathbb R)\). If every moment vanishes,
\[
m_j(\varphi)=\int_{\mathbb R}x^j\varphi(x)\,dx=0
\qquad(j\ge0),
\]
then
\[
\varphi=0.
\]

Indeed, the Fourier transform
\[
\widehat\varphi(\xi)=\int\varphi(x)e^{-2\pi i x\xi}\,dx
\]
is entire by compact support, and
\[
\widehat\varphi^{(j)}(0)=(-2\pi i)^jm_j(\varphi)=0
\]
for every \(j\). Its Taylor series at the origin is therefore zero, so the identity theorem gives \(\widehat\varphi\equiv0\), hence \(\varphi=0\).

## Consequence for primitive principal-value completion

The previous no-go showed that cancelling only finitely many moments leaves an algebraic Hilbert tail and cannot survive primitive exponential aggregation. The theorem above closes the opposite extreme on a single compactly supported front:

- finite moment cancellation is analytically insufficient;
- all-moment cancellation annihilates the compactly supported front itself.

Therefore no moment-subtraction operator acting solely within one compactly supported front channel can both preserve a nonzero odd orientation residue and remove the complete algebraic principal-value tail.

The required cancellation must be relative between distinct source carriers, or must leave the compact-support category.

## What a valid nonperturbative sewing must do

A valid constructor cannot merely impose
\[
m_j(\varphi_{\mathrm{reg}})=0
\quad\text{for every }j
\]
on a compactly supported regularized front. It must instead produce a relative pair
\[
(\varphi,\psi)
\]
whose principal-value responses cancel at infinity while a separately typed odd boundary class survives.

The surviving class may live in a quotient or mapping cone, a noncompact analytic carrier with exponential Fourier control, a hyperfunction or Hardy boundary-value space, or a relative Čech cocycle whose two chart representatives cancel asymptotically but not cohomologically.

Any such choice requires a source-derived comparison map. Moving to a larger carrier merely to evade the theorem is not authority.

## Strong hostile

Suppose a proposed compact-front coherencer claims exact exponential principal-value decay by killing every moment while retaining a nonzero compactly supported odd residual. The two claims are incompatible: all moments zero force that residual to vanish.

Thus the finite model
\[
(0,1,1)+(0,-1,0)=(0,0,1)
\]
is only a typing model. If the last coordinate is represented by the same compactly supported scalar front, it cannot possess all-order moment cancellation.

## Revised frontier

The earliest viable object is not a regularized single front but a relative two-chart class:
\[
[\varphi_-,\varphi_+]
\in
\operatorname{Cone}(\text{overlap sewing}).
\]

The theorem to seek is an exact relative identity in which the two chart Hilbert tails cancel while their anti-diagonal Čech class remains nonzero. Only after that identity is established should one construct its interval-history lift and apply the zero-trace projector.

This reduces the search space sharply: single-channel compact-front renormalizations are closed negative.
