# The half-density gauge audit forces a relative modular pairing

## Status

Correction and narrowing of the modular half-density candidate. The diagonal
kernel calculation is exact, but by itself it is a change of source rather
than a new physical energy. The surviving construction must compare two
independently typed Haar sectors.

## Synthesis and diagonal gauge

Let \(A_X\) synthesize normalized seam-history atoms:

\[
A_Xe_n=u_n.
\]

For a diagonal label weight

\[
D_\alpha e_n=n^\alpha e_n,
\]

the reweighted synthesis is

\[
A_X'=A_XD_\alpha.
\]

If this is only a basis change, the coefficient packet must transform as

\[
c'=D_\alpha^{-1}c.
\]

Then the physical state is unchanged:

\[
A_X'c'=A_Xc.
\]

The Gram matrix changes by congruence,

\[
K_X'=D_\alpha^*K_XD_\alpha,
\]

but its value on the transformed physical packet does not:

\[
(c')^*K_X'c'=c^*K_Xc.
\]

Therefore diagonal congruence alone cannot create an orientation law.

## Mellin exponent shift

If the coefficients are instead held fixed while the atoms are multiplied by
\(n^\alpha\), then

\[
n^{-s}n^\alpha=n^{-(s-\alpha)}.
\]

Thus the scalar synthesis is shifted from \(s\) to \(s-\alpha\). For
\(\alpha=1/2\), the candidate weighted Gram generally represents a different
Dirichlet section, not a new norm on the original section.

The factor

\[
K_{1/2}(pn,pm)=pK_{1/2}(n,m)
\]

is algebraically correct. It becomes physically relevant only if one source
constructor fixes the atom weight while an independent source constructor
fixes the Mellin coefficient, forbidding contragredient cancellation.

## Existing theta normalization

The labelled theta source already obeys

\[
\phi_n(u)=n^{-1/2}\phi_1(u+\log n).
\]

Hence the half-density is not missing from the source grammar. It already
appears with a source-fixed sign and placement. Replacing the normalized
translate \(u_n\) by \(\sqrt n\,u_n\) does not merely reveal this existing
factor; it reverses its placement unless another typed comparison map requires
that operation.

The naive single-sector weighted-Gram proposal is therefore not presently
authorized.

## Coordinate derivation

For \(x=e^q\), additive Haar measure becomes

\[
dx=e^q,dq.
\]

The unitary map from additive \(L^2\) to logarithmic \(L^2\) is

\[
(\mathcal Wf)(q)=e^{q/2}f(e^q).
\]

For the unnormalized dilation

\[
(R_pf)(x)=f(px),
\]

one obtains

\[
\mathcal W R_p\mathcal W^{-1}
=
p^{-1/2}T_{\log p},
\]

where \(T_{\log p}\) is logarithmic translation. The Mellin transform becomes

\[
Z(f,s)
=
\int_{-\infty}^{\infty}
(\mathcal Wf)(q)e^{(s-1/2)q}\,dq.
\]

This proves that the half-offset is source-derived. It also proves that a
consistent coordinate change transports the state, measure, and character
together. Nothing in this unitary equivalence alone supplies a new positive
inequality.

## The surviving two-sector object

The real structure is relative rather than diagonal. Keep separately

\[
\mathcal H_{\mathrm{add}}=L^2(\mathbb R_+,dx)
\]

and

\[
\mathcal H_{\mathrm{mult}}=L^2(\mathbb R_+,d^\times x).
\]

Their dilation representations have different modular characters. A source
comparison between them carries the half-density. That comparison has content
only because the two sectors have independently fixed source roles:

- additive Fourier and Poisson propagation;
- multiplicative Mellin and Tate aggregation.

The required energy must therefore be a relative form

\[
\mathcal E_{\mathrm{rel}}(f,g)
=
\langle f,\mathcal Jg\rangle
\]

or a positive Gram derived from both typed legs, where \(\mathcal J\) is the
source comparison. It cannot be the norm of one sector after an arbitrary
diagonal reweighting.

## Gauge-invariance gate

Any proposed orientation mechanism must pass the following test. Under every
admissible change of label frame

\[
A_X\mapsto A_XD,
\qquad
c\mapsto D^{-1}c,
\]

the claimed confinement identity must remain unchanged. A sign or growth
factor that disappears under this simultaneous transformation is a coordinate
artifact.

The relative modular comparison survives only if \(D\) is not an admissible
common gauge because it acts on one source sector but not the other. That
failure of common gauge must be proved from source typing, not asserted from
the desired exponent.

## Revised decisive square

The next source calculation is the square

\[
\begin{CD}
\mathcal S(\mathbb R_+),dx @>{\mathcal F_{\mathrm{add}}}>>
\mathcal H_{\mathrm{add}}\\
@V{\mathcal J}VV @VV{\mathcal W}V\\
\mathcal T(\mathbb R_+^\times),d^\times x @>{\mathcal M_s}>>
\mathcal H_{\mathrm{mult}}.
\end{CD}
\]

One must compute its exact cocycle under \(x\mapsto px\). If the cocycle is
removed by simultaneous transport of all four legs, it explains the
functional equation but supplies no orientation. If a source-fixed residual
modular character remains in the relative Green form, that residual is the
candidate RH-bearing energy.

## Finite falsifier

At cutoff \(X\), write the complete scalar synthesis in both frames. If

\[
F_X'(s)=F_X(s-1/2)
\]

rather than

\[
F_X'(s)=F_X(s),
\]

the weighted construction changed the source and is rejected. Equality may
not be repaired by redefining the readout after seeing the result.

## Verdict

The half-density explanation of the critical offset survives. The claim that
\(\sqrt nK_0\sqrt m\) is already the missing faithful oriented energy does
not survive the gauge audit without an independently sourced two-sector
comparison. The next object is a relative modular colligation, not a weighted
single-sector Gram.
