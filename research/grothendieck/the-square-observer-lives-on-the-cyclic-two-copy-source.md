# The square observer lives on the cyclic two-copy source

## Question

The global observer programme asked for primitive and prime-square components

\[
\mathcal J_1,\qquad \mathcal J_2
\]

from the additive theta source. Can both be linear components of one map out
of the one-copy source carrier?

## One loop and its cyclic grades

At finite arithmetic cutoff, let the source construction assign an operator
`A_phi` to a source packet `phi`, linearly wherever addition is defined. The
regularized determinant packet begins with

\[
\tau_1(A_\phi)=\operatorname{Tr}A_\phi,
\qquad
\tau_2(A_\phi)=\frac12\operatorname{Tr}(A_\phi^2).
\]

The first expression is linear in the one-copy source. The second is not:

\[
\tau_2(A_\phi+A_\psi)
=
\tau_2(A_\phi)+\tau_2(A_\psi)
+\operatorname{Tr}(A_\phi A_\psi).
\]

Consequently no linear map from the same additive carrier can be the
prime-square observer while also retaining the source-authorized mixed cyclic
term.

The canonical linearization is instead the cyclic two-copy map

\[
\widetilde{\mathcal J}_2:
\operatorname{Sym}^2 A
\longrightarrow
\mathcal B_2,
\qquad
\widetilde{\mathcal J}_2(\phi\odot\psi)
=\frac12\operatorname{Tr}
\left(A_\phi A_\psi+A_\psi A_\phi\right).
\]

On the diagonal this gives

\[
\widetilde{\mathcal J}_2(\phi\odot\phi)
=\operatorname{Tr}(A_\phi^2),
\]

so the conventional square cumulant is one half of the diagonal value. The
factor `1/2` is therefore forced by cyclic symmetrization rather than fitted
at scalar determinant level.

## Correct observer tower

The observer does not pass directly from one additive state to five unrelated
boundary coordinates. Its arithmetic part factors through the cyclic bar or
Fock tower:

\[
A
\longrightarrow
\left(A,\operatorname{Sym}^2A,\operatorname{Cyc}^{\ge3}A\right)
\longrightarrow
\left(\tau_1,\tau_2,\det_3\right)
\longrightarrow
\mathcal L_{\mathrm{rel}}.
\]

Thus primitive, square, and connected-tail data are three evaluations of one
loop object at different cyclic arities. Seam and archimedean data remain
relative incidence channels; they are not additional cyclic powers of that
loop.

This corrects the earlier notation

\[
\mathcal J=(\mathcal J_1,\mathcal J_2,\ldots).
\]

The notation is harmless only if its domains are recorded:

\[
\mathcal J_1:A\to\mathcal B_1,
\qquad
\widetilde{\mathcal J}_2:\operatorname{Sym}^2A\to\mathcal B_2.
\]

## What prime dilation supplies

For the labelled Gaussian atoms, prime multiplication and real dilation obey

\[
UT_p=R_pU,
\qquad
a_{pn}R_p=pR_pa_n.
\]

Tensoring this cell supplies the corresponding two-copy covariance:

\[
(U\otimes U)(T_p\otimes T_p)
=(R_p\otimes R_p)(U\otimes U).
\]

Therefore prime dilation genuinely transports the carrier on which the square
observer must live. It does not yet produce the cyclic closure or the global
Fourier--Tate action on that closure.

## Naturality gate

If source Fourier transport induced a source-derived similarity

\[
A_{\mathcal F\phi}=W A_\phi W^{-1},
\]

then cyclicity would immediately give naturality of both first grades and of
the regularized determinant. But the known Gaussian prime-dilation square
only proves equivariance of labelled synthesis. It does not construct this
similarity on the Euler feedback loop, and global Poisson transport does not
preserve finite Euler cutoff.

The first honest missing cell is therefore

\[
\mathcal F_A
\Longrightarrow
\mathcal F_{\mathrm{Cyc}}
\]

on the completed cyclic source object, together with its relative seam and
archimedean incidence. Fourier naturality of the determinant packet is a
consequence only after that cell exists.

## Falsifiers

A proposed observer lift fails if any of the following occurs:

1. the square component is declared linear on the one-copy additive carrier;
2. the polarization term `Tr(A_phi A_psi)` is absent;
3. primitive and square currents are installed as independent boundary
   operators;
4. finite Euler cutoff is assumed invariant under global Poisson transport;
5. similarity on the cyclic loop is inferred from the Gaussian dilation
   square without constructing the intervening source map;
6. naturality appears only after scalar determinant reconstruction.

## Result

The primitive and square observer components are not parallel linear maps.
They are the one-copy and cyclic two-copy evaluations of one source loop. The
prime-dilation cell transports both copy levels, but the completed
Fourier--cyclic comparison is still missing. This is the real obstacle before
authorized quasidiagonality: construct the Fourier action on the cyclic source
tower, not another scalar boundary current.
