# The retained seam incidence does not lift the unweighted diagonal theta forcing

## Retained labelled incidence

On the primitive prime-labelled carrier, the exact seam incidence has columns

\[
b_p=p^{-1/2}u_p,
\]

where \(u_p\) is the retained theta-cut vector in the \(p\)-labelled analytic
fibre and

\[
\|u_p\|=\|\Phi\|
\]

independently of \(p\).

The source coefficient metric is

\[
\|x\|_U^2
=
\sum_p(\log p)|x_p|^2.
\]

The labelled incidence is

\[
Bx=(p^{-1/2}x_pu_p)_p.
\]

## Diagonal forcing target

The unweighted diagonal theta forcing is

\[
\Phi_{\rm diag}=(u_p)_p.
\]

If \(Bx=\Phi_{\rm diag}\), prime-label faithfulness forces

\[
p^{-1/2}x_p=1
\]

for every prime.  Hence

\[
x_p=p^{1/2}.
\]

Its source norm is

\[
\|x\|_U^2
=
\sum_p p\log p
=
\infty.
\]

Therefore

\[
\Phi_{\rm diag}\notin\operatorname{ran}B
\]

on the retained seam coefficient space.

## Weighted forcing that is in range

The Euler-loaded labelled packet

\[
(p^{-1/2}u_p)_p
\]

is formally \(B\mathbf1\), but the constant coefficient vector also fails the
seam norm because

\[
\sum_p\log p
=
\infty.
\]

Only sufficiently decaying source coefficients lie in the Hilbert incidence
domain.  The Hilbert--Schmidt property of \(B\) controls such inputs; it does
not make the unweighted diagonal forcing an image vector.

## Unlabelled target requires codiagonalization

The analytic Evans forcing \(\Phi\) is one unlabelled history vector.  To
obtain it from the labelled prime packet, one would need a codiagonal map

\[
\bigoplus_pH_p\longrightarrow H
\]

that sums or otherwise identifies the prime fibres.  Such terminal prime
pushforward lies outside the retained G1--G3 Green carrier and can be
unbounded in the seam topology.

Applying it before the vector-valued residual test would erase exact prime
diagonality and could manufacture cancellations unavailable labelwise.

## Consequence for the Evans promotion residual

The equation

\[
Bx_\Phi=\Phi
\]

used in the simplest Evans-to-Green promotion is not defined on the retained
labelled seam carrier.  Thus the residual

\[
B^\dagger u_z+D_U(z)x_\Phi
\]

cannot yet be formed with a source state \(x_\Phi\) in that space.

A valid promotion must instead do one of the following:

1. formulate a labelwise Evans family with an admissible decaying source
   packet;
2. construct a bounded source-authorized codiagonal after the G3 complement
   test;
3. use a different arithmetic reservoir whose source topology contains the
   required diagonal forcing;
4. prove that the completed theta forcing belongs to a smaller closed range
   selected by the full three-stratum incidence.

## Relation to bi-bounded front-to-cut comparison

The front-to-cut map \(Jq_{p,k}=u_{p,k}\) is bi-bounded fibrewise.  It does not
supply an all-prime coefficient vector in \(U\).  Fibrewise invertibility
therefore cannot be used to infer the global range statement
\(\Phi\in\operatorname{ran}B\).

## Disposition

The natural Xi Evans state exists on the analytic history carrier, but its
forcing has no lift through the current retained seam incidence.  This is an
earlier obstruction than the arithmetic interpolation residual.  G4 requires
a source-compatible forcing lift or a later authorized codiagonal before the
Evans state can enter the paired arithmetic--analytic pencil.  No RH
conclusion is authorized.
