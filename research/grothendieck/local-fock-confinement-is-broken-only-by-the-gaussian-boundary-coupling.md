# Local Fock confinement is broken only by the Gaussian boundary coupling

## Bounded question

What is the first source-native structure that couples the multiplicative
valuation labels to the additive Gaussian boundary, and which side first loses
critical-seam confinement?

## Prime valuation chain

Fix a prime (p). On the valuation module with basis (e_k), define

\[
S_pe_k=e_{k+1},
\qquad
Q_pe_k=p^{2k}e_k.
\]

Here (S_p) adds one (p)-adic occupation and (Q_p) records the square of
the corresponding integer scale. They obey the exact quantum-plane relation

\[
Q_pS_p=p^2S_pQ_p.
\]

This is the first mixed algebra joining multiplicative Fock transport to the
quadratic scale seen by the Gaussian heat kernel.

## Canonical half-density Fock chain

Put

\[
\lambda_p(s)=p^{1/2-s}.
\]

The finite canonical occupation packet is

\[
v_{p,K}(s)=\sum_{k=0}^K\lambda_p(s)^ke_k.
\]

Its augmentation is the geometric polynomial

\[
Z_{p,K}(s)
=
\frac{1-\lambda_p(s)^{K+1}}{1-\lambda_p(s)}.
\]

Every zero satisfies

\[
|\lambda_p(s)|=1,
\]

and therefore

\[
\operatorname{Re}s=\frac12.
\]

Thus every finite canonical Fock truncation has exact seam confinement. In the
open right sector, (|\lambda_p(s)|<1), the completed chain is

\[
Z_p(s)=\frac1{1-\lambda_p(s)},
\]

which is zero-free. Local multiplicative completion is therefore strictly
exact on its natural open sector.

## Gaussian boundary deformation

Sampling the Gaussian at the valuation points (p^k) inserts the positive
weights

\[
w_k(t)=e^{-\pi t p^{2k}}.
\]

The relation (Q_pS_p=p^2S_pQ_p) derives these weights from the mixed source
algebra; they are not freely fitted. The first two levels give

\[
G_{p,1}(s;t)
=
w_0(t)+w_1(t)\lambda_p(s).
\]

Its zeros satisfy

\[
|\lambda_p(s)|=\frac{w_0(t)}{w_1(t)}
=
e^{\pi t(p^2-1)}>1.
\]

Hence

\[
\operatorname{Re}s
=
\frac12
-
\frac{\pi t(p^2-1)}{\log p},
\]

strictly away from the seam. The canonical equal-weight Fock confinement is
lost exactly when the archimedean Gaussian boundary is coupled to the
valuation chain.

This finite zero lies outside the direct convergence sector and is not an RH
counterexample. Its role is diagnostic: neither local Fock positivity nor the
Gaussian vacuum separately explains the completed global orientation.

## Result

The source now separates into three sharply typed facts:

1. the prime occupation chain has a canonical half-density coordinate;
2. its finite and infinite augmentations are seam-confined or zero-free;
3. the Gaussian boundary deforms the occupation weights through a rigid
   (p^2)-commutation law and immediately destroys finite confinement.

Thus the missing RH mechanism is not another local positivity statement. It
must explain why the completed all-prime, reciprocal, archimedean coupling
repairs the off-seam defects created by every isolated Gaussian-weighted
valuation chain.

## Next target

Form the full commuting family ({S_p}_p) together with the single quadratic
operator (Q), retain the primitive and square boundary currents, and derive
the compatibility cocycle for

\[
QS_p=p^2S_pQ.
\]

The smallest falsifier is a two-prime square whose two paths to (Q S_pS_q)
leave a nontrivial boundary residual after reciprocal completion. If every
finite prime square commutes exactly, the only remaining obstruction is the
restricted-product limit.
