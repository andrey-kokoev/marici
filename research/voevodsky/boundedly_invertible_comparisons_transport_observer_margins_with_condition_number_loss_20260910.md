# Boundedly invertible comparisons transport observer margins with condition-number loss

## Question

Which parts of the observer theory survive when a comparison cell is boundedly invertible but not unitary?

## Claim boundary

The results concern boundedly invertible linear comparisons between Hilbert or graph Hilbert rungs. They transport lower bounds, Calkin margins, compactness, and finite residual kernels with explicit norm loss. Exact equality of margins is reserved for unitary comparisons. Green and Real compatibility with fixed target structures remains an independent cell condition.

## Transported observer

Let \(X,X'\), and \(Z\) be Hilbert spaces. Let

\[
C:X\longrightarrow X'
\]

be boundedly invertible, and let

\[
T:X\longrightarrow Z
\]

be bounded. The observer expressed on the target presentation is

\[
T'=TC^{-1}:X'\longrightarrow Z.
\]

If

\[
\delta\|x\|_X\le\|Tx\|_Z\le L\|x\|_X,
\]

then

\[
\frac{\delta}{\|C\|}\|x'\|_{X'}
\le
\|T'x'\|_Z
\le
L\|C^{-1}\|\|x'\|_{X'}.
\]

Indeed,

\[
\|C^{-1}x'\|_X\ge\frac{\|x'\|_{X'}}{\|C\|}.
\]

Thus an admissible lower margin is

\[
\delta'\ge\frac{\delta}{\|C\|},
\]

and an admissible upper bound is

\[
L'\le L\|C^{-1}\|.
\]

The resulting condition-number estimate is

\[
\frac{L'}{\delta'}
\le
\kappa(C)\frac{L}{\delta},
\qquad
\kappa(C)=\|C\|\|C^{-1}\|.
\]

For unitary \(C\), \(\kappa(C)=1\) and the exact lower and upper moduli are preserved. For general invertible \(C\), only inequalities are justified.

## Gramian transport

The target-presentation Gramian is

\[
T'^*T'=C^{-*}T^*TC^{-1}.
\]

If

\[
T^*T\ge\delta^2I_X,
\]

then

\[
T'^*T'
\ge
\delta^2C^{-*}C^{-1}
\ge
\frac{\delta^2}{\|C\|^2}I_{X'}.
\]

Conversely, a lower bound \(T'^*T'\ge\delta'^2I_{X'}\) gives

\[
T^*T=C^*T'^*T'C
\ge
\frac{\delta'^2}{\|C^{-1}\|^2}I_X.
\]

These are congruence inequalities, not unitary conjugacy identities.

## Calkin-margin transport

Assume \(X\) and \(X'\) are infinite dimensional. Bounded multiplication preserves compact operators, so \(C\) induces an invertible comparison between the corresponding Calkin-algebra representatives.

If

\[
q_X(T^*T)\ge\mu I
\]

for \(\mu>0\), then

\[
q_{X'}(T'^*T')
=
q(C)^{-*}q_X(T^*T)q(C)^{-1}
\ge
\frac{\mu}{\|C\|^2}I.
\]

Conversely, an essential margin \(\mu'>0\) for \(T'\) yields a margin at least

\[
\frac{\mu'}{\|C^{-1}\|^2}
\]

for \(T\).

Hence upper semi-Fredholm observer status is invariant under boundedly invertible comparison, while the numerical essential margin is metric-dependent.

Strictly, the two Calkin algebras are related through the spatial algebra isomorphism induced by \(C\); the displayed congruence is not a star-isomorphism unless \(C\) is unitary. Positivity is established by the explicit congruence estimate rather than by claiming nonunitary conjugation preserves the star structure.

## Compact channels and finite defects

If \(A:X\to Z_A\) is compact, then

\[
A'=AC^{-1}
\]

is compact. The kernel transports exactly:

\[
\ker T'=C(\ker T).
\]

Consequently:

- kernel dimension is preserved;
- closed range is preserved;
- finite-defect repair transports by the same source comparison;
- injectivity of \(K\) on \(\ker T\) is equivalent to injectivity of \(KC^{-1}\) on \(C(\ker T)\).

For a row observer

\[
\mathcal T=(Bp,D,K)^\top,
\]

the transported row

\[
\mathcal T'=\mathcal TC^{-1}
\]

retains the quotient, essential, and finite-repair roles, provided the vertical subspace is transported as

\[
V'=C(V)
\]

and the descent map is transported to

\[
p'=pC^{-1}.
\]

Changing the observer but not its vertical and quotient interfaces would be a type error.

## Sharpness of the norm loss

Take

\[
C=cI,
\qquad c>0,
\]

and \(T=I\). Then

\[
T'=c^{-1}I
\]

has exact lower modulus \(1/c\), equal to \(1/\|C\|\). Thus the factor \(\|C\|^{-1}\) cannot be improved using only the norm of \(C\).

For anisotropic comparisons, let

\[
C=\operatorname{diag}(s_1,\ldots,s_n).
\]

With \(T=I\), the lower modulus of \(TC^{-1}\) is

\[
\frac{1}{\max_j|s_j|},
\]

while its upper modulus is

\[
\frac{1}{\min_j|s_j|}.
\]

The condition number is exactly \(\kappa(C)\). The degradation is therefore geometric, not an artifact of the estimate.

## Green structures under nonunitary comparison

Let \(J\) be a bounded Hermitian Green-form operator on \(X\). Transporting the form along \(C\) gives

\[
J'=C^{-*}JC^{-1}.
\]

Then

\[
\langle J'Cx,Cy\rangle_{X'}
=
\langle Jx,y\rangle_X.
\]

This makes \(C\) an isometry between the two Green forms even when it is not a Hilbert-space unitary. If a target Green operator \(J'_{\mathrm{fixed}}\) is already prescribed, compatibility instead requires the independent cell

\[
C^*J'_{\mathrm{fixed}}C=J.
\]

Invertibility alone does not prove that identity.

## Real structures under nonunitary comparison

Let \(R:X\to X\) be an antilinear involution. Its transported target Real structure is

\[
R'=CRC^{-1}.
\]

It remains an antilinear involution:

\[
R'^2=I.
\]

If a target Real structure \(R'_{\mathrm{fixed}}\) is already declared, the required compatibility cell is

\[
CR=R'_{\mathrm{fixed}}C.
\]

Again, invertibility supplies a transported structure but does not establish compatibility with independently fixed target data.

## Graph-rung constraint

If \(X=\mathcal E_D\) and \(X'=\mathcal E_{D'}\) are graph Hilbert spaces, \(C\) must be boundedly invertible for the graph norms under discussion. Ambient bounded invertibility is insufficient. The graph adjoint entering

\[
T'^*T'=C^{-*}T^*TC^{-1}
\]

is the adjoint on the declared graph metric rung. Substitution of an ambient adjoint is forbidden unless the graph metric correction has been inserted.

## Green--Real radial consequence

Unitary phase gauges and reciprocal wall comparisons retain exact observer margins. A nonunitary radial reparameterization or weighted presentation comparison retains stable observation only with the losses controlled by \(\|C\|\) and \(\|C^{-1}\|\).

The comparison transports the entire typed package:

\[
(X,V,p,J,R,T)
\longmapsto
(X',C(V),pC^{-1},C^{-*}JC^{-1},CRC^{-1},TC^{-1}).
\]

Keeping \(J\), \(R\), or \(V\) fixed while transporting only \(T\) requires separate compatibility proofs.

## Deliberate failures

1. **Exact-invariance promotion:** claiming \(m(TC^{-1})=m(T)\) for arbitrary invertible \(C\) fails already for \(C=cI\).
2. **Star-conjugacy promotion:** treating \(A\mapsto CAC^{-1}\) as a star-automorphism fails for nonunitary \(C\).
3. **Ambient-to-graph promotion:** ambient invertibility need not imply graph-norm invertibility.
4. **Fixed-Green promotion:** invertibility does not imply \(C^*J'_{\mathrm{fixed}}C=J\).
5. **Fixed-Real promotion:** transported \(CRC^{-1}\) need not equal an independently prescribed target Real structure.

## Disposition

Stable and essential observation survive boundedly invertible comparison, but exact numerical invariance is replaced by condition-number control. Compactness, closed range, kernel dimension, and finite-repair injectivity transport exactly. Green and Real structures may be transported canonically from the source; compatibility with fixed target structures remains an independent constructor cell. This completes the first next-cycle objective at Hilbert and graph-Hilbert strength.
