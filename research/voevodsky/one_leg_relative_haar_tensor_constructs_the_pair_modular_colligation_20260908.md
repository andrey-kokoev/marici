# A one-leg relative-Haar tensor constructs the pair modular colligation

Date: 2026-09-08

## Construction

Let

\[
J:\mathcal H_a\supset\operatorname{Dom}J\to\mathcal H_m
\]

be the closed relative-Haar inclusion, satisfying

\[
JU_a(p)=p^{1/2}U_m(p)J.
\]

The ordered pair source has two independently typed slots.  Put the additive
Haar representation in the first slot and the multiplicative Haar
representation in the second:

\[
\mathcal H_{am}^{(2)}
=\mathcal H_a\widehat\otimes\overline{\mathcal H_m}.
\]

Define the closed pair comparison on its algebraic graph core by

\[
J_{\rm pair}=J\widehat\otimes I:
\mathcal H_{am}^{(2)}	o
\mathcal H_m\widehat\otimes\overline{\mathcal H_m}.
\]

Then

\[
J_{\rm pair}
(U_a(p)\otimes\overline{U_m(p)})
=p^{1/2}
(U_m(p)\otimes\overline{U_m(p)})J_{\rm pair}.
\]

Taking the target norm gives exactly

\[
\mathcal E_{\rm pair}
((U_a(p)\otimes\overline{U_m(p)})\Psi)
=p\,\mathcal E_{\rm pair}(\Psi),
\]

where

\[
\mathcal E_{\rm pair}(\Psi)=\|J_{\rm pair}\Psi\|^2.
\]

After Mellin weighting this becomes

\[
p^{1-2\operatorname{Re}s},
\]

the required critical-seam multiplier.

## Why one leg is essential

Applying `J` to both pair slots would give amplitude multiplier `p` and energy
multiplier `p^2`, overcounting the modular character.  Applying it to neither
recovers the old invariant seam Gram with multiplier one.  One additive and
one multiplicative slot is the unique integral-slot choice producing energy
multiplier `p`.

Slot reversal gives the reciprocal colligation

\[
I\otimes\overline J:
\mathcal H_m\widehat\otimes\overline{\mathcal H_a}
\to
\mathcal H_m\widehat\otimes\overline{\mathcal H_m},
\]

so ordered orientation is retained rather than symmetrized away.

## Gauge invariance

The factor is the equivariance defect between two independently normalized
unitary Haar representations.  Separate unitary frame changes conjugate the
operators but cannot remove `p^{1/2}`.  This is not the unauthorized
single-sector replacement `K -> sqrt(nm)K`.

## Domain gate

The construction is closed on

\[
\operatorname{Dom}J\widehat\otimes\overline{\mathcal H_m}.
\]

It does not yet prove that the completed tail--seam pair current, including its
constant endpoint channel, lies in this domain.  Prior relative-Haar analysis
shows that uncancelled constant channels require a boundary reservoir.  The
next test is therefore domain admission of the localized pair packet after its
wall/endpoint correction, not derivation of the modular cocycle.

## G4 consequence

This supplies the previously missing relative pair colligation and its exact
orientation law.  To reach the fixed G4 response one must still:

1. map the source tail--seam Gram current into the mixed-Haar pair domain;
2. prove wall-corrected domain admission;
3. compose with radial shell localization and analytic-transpose orientation;
4. identify the resulting response with the conservative joint-column
   adjoint without altering the Evans divisor.

No residual cancellation or RH conclusion is asserted.
