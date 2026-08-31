# The augmented theta-history Green identity retains a forcing pairing

## Augmented first-order history

Let \(\Phi\) be the source theta forcing and let \(c\) be the retained constant
source coordinate.  The elementary augmented history equation is

\[
(\partial_q-a)u=c\Phi,
\]

where \(a\) is the real displacement from the reciprocal seam.

Equivalently, the augmented operator contains the block

\[
\mathcal D_a=
\begin{pmatrix}
\partial_q-a&-\Phi\\
0&0
\end{pmatrix}.
\]

The constant coordinate is required to make the forced equation a homogeneous
kernel equation on the enlarged carrier.

## Exact Green identity

Assume first that \(u\) has vanishing boundary contribution.  Taking the real
part of the \(L^2\) pairing with \(u\) gives

\[
\operatorname{Re}\langle u,\partial_qu\rangle
-a\|u\|^2
=
\operatorname{Re}\bigl(c\langle u,\Phi\rangle\bigr).
\]

Since

\[
2\operatorname{Re}\langle u,\partial_qu\rangle
=
\left[|u(q)|^2\right]_{-\infty}^{+\infty},
\]

one obtains

\[
2a\|u\|^2
=
-2\operatorname{Re}\bigl(c\langle u,\Phi\rangle\bigr)
+
\left[|u(q)|^2\right]_{-\infty}^{+\infty}.
\]

With full endpoint traces, the last term is replaced by the declared Green
boundary flux.  The forcing pairing remains a bulk term.

## Maximal isotropy is insufficient by itself

The maximal-isotropic Fourier--Poisson boundary condition can force the
endpoint flux to vanish.  It does not force

\[
\operatorname{Re}\bigl(c\langle u,\Phi\rangle\bigr)=0.
\]

Therefore the implication

\[
\text{isotropic boundary trace}
\Longrightarrow
a\|u\|^2=0
\]

is invalid for the augmented forced history unless a second source equation
cancels the forcing pairing.

## Why deleting the constant coordinate is invalid

Setting \(c=0\) removes the residual and recovers the homogeneous first-order
identity.  It also removes the theta forcing and changes the kernel problem.
A Xi zero is represented, if at all, by the forced augmented state with a
nonzero source coordinate.  The constant channel cannot be dropped merely to
obtain positivity.

Assigning zero norm to the constant coordinate does not remove the cross
pairing.  It only makes the augmented metric degenerate while the Green
identity still contains \(c\langle u,\Phi\rangle\).

## Required closed-loop cancellation

A valid complete boundary pencil must contain an arithmetic/source equation
whose Green pairing contributes

\[
+2\operatorname{Re}\bigl(c\langle u,\Phi\rangle\bigr).
\]

Only after exact cancellation across the analytic and arithmetic blocks may
the total identity reduce to

\[
2a\,\mathcal N(\psi)
=
-\Sigma(\operatorname{Tr}_\partial\psi,
        \operatorname{Tr}_\partial\psi).
\]

This cancellation must be proved at the vector level before scalar Mellin or
Wronskian readout.  A norm inequality cannot replace the signed cross-term
identity.

## Relation to the G3 form

The retained G3 energy contains source incidence, disagreement, and analytic
history components.  Its positivity does not alone show that its polarization
is the Green form of \(\mathcal D_a\).  The exact readback residual is now the
specific bilinear term

\[
\mathcal R_{\rm force}(u,c)
=2\operatorname{Re}\bigl(c\langle u,\Phi\rangle\bigr).
\]

The arithmetic block must contribute \(-\mathcal R_{\rm force}\) with the
same normalization, source metric, and reciprocal sign.

## G4 consequence

The earlier off-seam invertibility theorem remains conditional.  Its missing
Green-readback input is not an unspecified comparison: it is exact
cancellation of the augmented theta forcing pairing, together with any
endpoint flux.

Until a source arithmetic block supplies that opposite cross term, maximal
isotropy and G3 coercivity do not exclude off-seam cone kernels.  No RH
conclusion is authorized.
