# The source-pulled ordered metric makes the interior theta-profile map exactly natural

## Closed differentiated comparison

Let

\[
Jq_{p,k}=u_{p,k}
\]

be the existing labelled front-to-cut comparison. On the reduced labelled
front carrier, `J` is injective, bi-bounded in the differentiated topology,
and has closed range.

Equip the source instead with the ordered primitive graph norm

\[
\|q\|_{F,\mathrm{ord}}^2
=
\frac14\|Sq\|_{\mathrm{res}}^2.
\]

For the source atoms,

\[
\|q_{p,k}\|_{F,\mathrm{ord}}^2
=
\|W_{k\log p}\|_{\mathrm{res}}^2
=:\omega_{p,k}^2
\asymp k\log p.
\]

## Pulled-back metric on the cut range

Do not alter the constructor formula by inserting an unexplained amplitude.
Instead define the ordered cut metric on the closed source-generated range by

\[
\langle Jx,Jy\rangle_{I,\mathrm{ord}}
:=
\langle x,y\rangle_{F,\mathrm{ord}}.
\]

This is well-defined because `J` is injective on the reduced carrier. Its
completion is canonically isometric to the ordered source completion, and

\[
J:
\mathcal H_{F,\mathrm{ord}}
\longrightarrow
\mathcal H_{I,\mathrm{ord}}
\]

is unitary onto its range by construction.

In the unnormalized cut basis this says

\[
\|u_{p,k}\|_{I,\mathrm{ord}}^2
=
\omega_{p,k}^2.
\]

Equivalently one may use constant-norm cut atoms in the old Green metric and
the weighted sections `omega_(p,k)u_(p,k)`. The source-pulled formulation is
preferable because it leaves the actual synthesis arrow unchanged.

## Interior observer

The gamma-field is now exactly the existing constructor:

\[
\gamma_\theta^{\mathrm{ord}}e_{p,k}
=u_{p,k}.
\]

Its adjoint is the interior theta-profile observer in the pulled-back metric,
and its kernel is

\[
K_\theta^{\mathrm{ord}}(\alpha,\beta)
=
\langle u_\beta,u_\alpha\rangle_{I,\mathrm{ord}}
=
\langle q_\beta,q_\alpha\rangle_{F,\mathrm{ord}}.
\]

Positivity, closability, and zero radical follow from the source Gram and the
injectivity of `J`; they are not imposed by fitting target coefficients.

## Cutoff naturality

Prime and grade cutoffs are label-diagonal and commute with `J`, `D`, and the
retained ordered graph coordinates. Therefore

\[
JP_X=P_XJ
\]

and

\[
\|P_XJx-Jx\|_{I,\mathrm{ord}}
=
\|P_Xx-x\|_{F,\mathrm{ord}}
\longrightarrow0.
\]

Thus the projective completion and every cofinal cutoff yield the same
interior observer.

## Reciprocal and Fourier transport

Reflection exchanges the two half-density source sheets and satisfies

\[
RSR=-S.
\]

Hence the ordered Hermitian metric is reflection-even while the unsquared
ordered current is odd. Transport the reciprocal/Fourier action to the cut
range by

\[
\mathcal F_I^{\mathrm{ord}}
=J\mathcal F_FJ^{-1}.
\]

Then

\[
\mathcal F_I^{\mathrm{ord}}J
=J\mathcal F_F
\]

holds identically, and the transported action is unitary for the pulled-back
metric. This is a source-derived representation on the closed range, not an
asserted Fourier invariance of individual prime walls.

## Adams covariance

Grade raising sends `(p,k)` to `(p,rk)`. The ordered metric transports with
the exact cocycle

\[
c_{p,k}^{(r)}
=
\frac{\omega_{p,rk}}{\omega_{p,k}},
\]

which is comparable to `sqrt(r)` uniformly in `p,k` by the two-sided scale
law. Declaring this ratio rather than a fitted `sqrt(r)` preserves the exact
resolved source normalization.

## Scope

This constructs the weighted interior theta-profile observer and its
Fourier/reciprocal/cutoff naturality on the source-generated cut range. It does
not identify that range with the native broken-`H1` wall-observer range.
Instead the two remain separate legs in their orthogonally coupled faithful
joint graph.

The remaining conservative question is whether the source-pulled interior
observer and native wall observer admit the required Green/Weyl coupling on
that joint graph. No native-adjoint equality or Douglas domination is needed
or possible.
