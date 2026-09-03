# Theta-envelope common-mode selection

Author: `marici.Grothendieck`
Status: interior common-mode implication refuted
Predecessors: `theta-bilateral-kernel-normalization.md`, `source-current-row-programme-synthesis.md`

## Question

Does scalar-zero closure of the theta-compatible common-forcing envelope select the interior common-mode constraint needed by the earlier conditional closure extension?

## Claim boundary

Use

\[
u(q)=e^{-zq}a_\theta(q),
\qquad
v(q)=e^{zq}b(q),
\]

with the approved common-forcing compatibility equation

\[
b'(q)=e^{-2zq}a_\theta'(q).
\]

At a noncentral scalar zero, the exact theta moment permits a choice of integration constant for which both envelopes vanish at both ends. Hence the common mode \(w=u+v\) vanishes at the endpoints.

Interior common-mode vanishing would require

\[
v=-u,
\qquad
b=-e^{-2zq}a_\theta.
\]

Differentiating this relation and comparing it with common-forcing compatibility gives

\[
e^{-2zq}a_\theta'
=2ze^{-2zq}a_\theta-e^{-2zq}a_\theta',
\]

or equivalently

\[
a_\theta'=z a_\theta.
\]

The theta envelope is not a single exponential on any open interval. Therefore no constant spectral parameter \(z\) makes the scalar-zero compatible response satisfy \(w=0\) throughout the path. The exact interior residual is

\[
2e^{-2zq}\left(a_\theta'-za_\theta\right).
\]

## Integrated common-mode identity

Let

\[
w=u+v,
\qquad
r=u-v.
\]

The common-forcing flow gives

\[
w'=-zr-2F,
\qquad
r'=-zw.
\]

At a scalar zero, the theta construction gives \(w=0\) at both endpoints. Solving the first equation for \(F\), integrating by parts, and using the second equation yields

\[
\begin{aligned}
R
&=\operatorname{Re}\int F\bar r\,dq\\
&=-\frac12\operatorname{Re}\int w'\bar r\,dq
  -\frac12\operatorname{Re}(z)\int|r|^2dq\\
&=-\frac12\operatorname{Re}(z)
\int\left(|w|^2+|r|^2\right)dq.
\end{aligned}
\]

Since

\[
|w|^2+|r|^2=2(|u|^2+|v|^2),
\]

this recovers

\[
R=-\operatorname{Re}(z)B.
\]

The formula rules out weaker integrated common-mode conditions as a work-sewing mechanism. Vanishing of \(\int w\), an averaged phase, or cancellation between common and relative channels cannot cancel a sum of their squared norms. For a nonzero response, \(R=0\) still forces \(\operatorname{Re}(z)=0\).

## Multiple-zero jet test

The two-sided compatibility residual is

\[
C(z)=\int_{\mathbb R}e^{-2zq}a_\theta'(q)dq
=2z\,\xi\!\left(\tfrac12+z\right).
\]

If \(z_0\ne0\) is a scalar zero of multiplicity \(m\), then

\[
C^{(k)}(z_0)=0
\qquad (0\le k<m).
\]

Equivalently, the first \(m\) parameter derivatives of the linear endpoint obstruction vanish; these are weighted moments of \(a_\theta'\). They provide jet-level closure of the compatible envelope family.

This additional linear information does not change the zeroth-order Hermitian work identity. At the same parameter,

\[
R_\theta(z_0)=-\operatorname{Re}(z_0)B_\theta(z_0),
\qquad B_\theta(z_0)>0.
\]

Thus a hypothetical multiple zero with \(\operatorname{Re}(z_0)\ne0\) consistently has nonzero work despite all closure derivatives through order \(m-1\). Multiplicity strengthens the boundary jet but supplies no work orthogonality.

## Phase-gauge invariance

A global source phase acts by

\[
(a_\theta,b,u,v,F)
\longmapsto
e^{i\vartheta}(a_\theta,b,u,v,F).
\]

It preserves common-forcing compatibility. The scalar moment acquires the same nonzero factor, so its zero set is unchanged. The positive bulk is invariant, and the work pairing satisfies

\[
\operatorname{Re}\int
(e^{i\vartheta}F)
\left(\overline{e^{i\vartheta}u}-
      \overline{e^{i\vartheta}v}\right)dq
=R.
\]

Thus no global phase can tune nonzero work to zero. Independent phases on the two sheets are not admissible gauges: with nonzero forcing, the equations require the same transformed \(F\) in both sheets, forcing the phases to agree. A relative phase therefore changes the source system rather than selecting an equivalent response.

## Dilation-origin invariance

Translate the logarithmic coordinate by a real constant \(q_0\) and transport every source field with it:

\[
\widetilde a(q)=a_\theta(q-q_0),
\quad
\widetilde u(q)=u(q-q_0),
\quad
\widetilde v(q)=v(q-q_0),
\quad
\widetilde F(q)=F(q-q_0).
\]

The flow equations and endpoint decay are unchanged. The scalar moment transforms as

\[
\int e^{-2zq}\widetilde a(q)dq
=e^{-2zq_0}\xi\!\left(\tfrac12+z\right),
\]

so its zero set is invariant. Translation of the integration variable also gives

\[
\widetilde B=B,
\qquad
\widetilde R=R.
\]

Thus the arbitrary origin of the logarithmic dilation coordinate cannot tune accumulated work. Recentring only the envelope while leaving the response, forcing, or endpoint identification fixed is not a coordinate gauge; it changes the source realization.

## Integration-constant rigidity

The compatible second envelope has the affine family

\[
b_C(q)=C+\int_{q_*}^{q}e^{-2zt}a_\theta'(t)dt,
\qquad
v_C(q)=e^{zq}b_C(q).
\]

If \(\operatorname{Re}(z)>0\), any uncancelled constant in \(b_C(+\infty)\) makes \(v_C\) grow at \(+\infty\); if \(\operatorname{Re}(z)<0\), the analogous condition occurs at \(-\infty\). On the critical line, a nonzero limiting constant has constant modulus and is not square-integrable at either end. Thus finite bulk fixes \(C\) uniquely by the growing or nondecaying endpoint.

The difference between the two limiting constants is

\[
b_C(+\infty)-b_C(-\infty)
=2z\,\xi\!\left(\tfrac12+z\right).
\]

At a noncentral scalar zero, the unique constant that closes one endpoint closes the other as well. No remaining homogeneous constant can tune \(R\) while preserving both endpoint closure and finite positive bulk.

## Affine boundary-mismatch characterization

Fix the source-selected first sheet

\[
u=e^{-zq}a_\theta,
\qquad
F=-e^{-zq}a_\theta',
\]

and solve the second equation \(v'=zv-F\) on \(\mathbb R\). Writing \(v=e^{zq}b\) gives

\[
b'=e^{-2zq}a_\theta'.
\]

The boundary mismatch of this affine problem is

\[
E_{\rm aff}(z):=b(+\infty)-b(-\infty)
=2z\,\xi\!\left(\tfrac12+z\right).
\]

For \(z\ne0\), a finite-bulk solution satisfying both endpoint conditions exists exactly when \(E_{\rm aff}(z)=0\), equivalently when \(\xi(\tfrac12+z)=0\). Integration-constant rigidity makes that solution unique. Thus \(2z\xi\) is the exact affine boundary-mismatch function for the theta-compatible common-forcing problem.

The factor \(z\) is a genuine central degeneracy: at \(z=0\), the derivative moment vanishes as a total derivative even though \(\xi(\tfrac12)\ne0\). It must be removed before identifying the noncentral scalar zero set.

This characterization realizes scalar zeros as two-ended affine boundary compatibility, not as eigenvalues of a homogeneous selfadjoint operator. It supplies endpoint closure but no adjoint or work-sewing theorem.

## Homogeneous-kernel test

The difference of any two second-sheet solutions satisfies

\[
h'=zh,
\qquad
h(q)=Ce^{zq}.
\]

No nonzero such solution lies in \(L^2(\mathbb R)\): it grows at one end when \(\operatorname{Re}(z)\ne0\) and has constant modulus when \(\operatorname{Re}(z)=0\). The first-sheet homogeneous variation \(Ae^{-zq}\) has the same obstruction. Therefore the two-ended homogeneous kernel is trivial at every \(z\), including zeros of \(\xi\).

The scalar zeros mark solvability of a forced affine boundary problem, not nontrivial kernel of a homogeneous spectral operator. Calling \(2z\xi\) an Evans function without the qualifier `affine boundary-mismatch` would incorrectly import homogeneous eigenvalue meaning. The terminology above is narrowed accordingly.

## Source-amplitude augmented kernel

Introduce a source amplitude \(c\) and the spectral source profile

\[
F_z(q)=-e^{-zq}a_\theta'(q).
\]

The triangular augmented system

\[
u'=-zu-cF_z,
\qquad
v'=zv-cF_z,
\qquad
c'=0
\]

is homogeneous and linear in the augmented state \((u,v,c)\), although its coefficients depend nonlinearly on \(z\). For \(c=0\), the two-ended kernel is trivial. For \(c\ne0\), division by \(c\) reduces to the unique affine response. Consequently, at every noncentral scalar zero the augmented geometric kernel is exactly one-dimensional, spanned by

\[
(u_z,v_z,1).
\]

This supplies a homogeneous augmented-kernel realization of the scalar zero set and narrows the preceding result: the obstruction applies to the unaugmented sheet operator.

The augmentation is not a positive selfadjoint realization. It is triangular, the source coordinate has no reciprocal state-to-source equation, and its natural Green metric is degenerate in the \(c\) direction. Adding the reciprocal equation restores the accumulated-work boundary coordinate rather than closing it. Scalar multiplicity may appear as algebraic multiplicity of the boundary function, but the geometric kernel remains one-dimensional.

## Sturm--Liouville reduction test

The compatible envelope equation implies

\[
b''+2zb'=e^{-2zq}a_\theta''.
\]

For \(v=e^{zq}b\), this becomes

\[
v''-z^2v=e^{-zq}a_\theta''.
\]

This is not a homogeneous Sturm--Liouville eigenvalue equation: the right-hand side depends on both the fixed theta source and the spectral parameter. Absorbing it into a potential would require

\[
V_z(q)=-\frac{e^{-zq}a_\theta''(q)}{v_z(q)},
\]

which is spectral-dependent, response-dependent, and singular at zeros of \(v_z\). It is therefore a fitted potential rather than a source operator.

Even discarding the forcing does not isolate the target line. A selfadjoint equation with eigenvalue \(z^2\) would force \(z^2\) real, allowing both the real and imaginary \(z\)-axes. Critical-line confinement requires the imaginary axis alone. The affine, parameter-dependent boundary condition supplies no source rule excluding the real branch.

Hence the affine boundary-mismatch realization does not descend to a fixed-domain selfadjoint Sturm--Liouville problem.

## Disposition

Scalar nullity derives two-endpoint envelope closure but not the interior common-mode constraint. The conditional extension's path constraint remains an independent sector selection. The next executable question is whether a weaker integrated common-mode relation, rather than pointwise vanishing, can annihilate the work pairing without being equivalent to confinement.
