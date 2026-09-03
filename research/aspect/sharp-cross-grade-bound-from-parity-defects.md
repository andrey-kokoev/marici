# Sharp cross-grade bound from parity defects

## Question

How strongly does approximate target-parity intertwining constrain the cross pairing of primitive and square route amplitudes?

## Spectral decomposition

Let \(U\) be a unitary self-adjoint involution on the physical target, with spectral projections \(Q_+\) and \(Q_-\). For route amplitudes \(b_+\) and \(b_-\), define the parity defects

\[
\delta_+=(U-I)b_+,
\qquad
\delta_-=(U+I)b_-.
\]

Write

\[
b_+=p+q,
\qquad
b_-=r+s,
\]

with \(p,r\in\operatorname{im}Q_+\) and \(q,s\in\operatorname{im}Q_-\). Then

\[
\delta_+=-2q,
\qquad
\delta_-=2r.
\]

Orthogonality of the target parity sectors gives

\[
\langle b_+,b_-\rangle
=
\langle p,r\rangle+
\langle q,s\rangle.
\]

Set

\[
B_+=\|b_+\|,
\quad B_-=\|b_-\|,
\quad \epsilon_+=\|\delta_+\|,
\quad \epsilon_-=\|\delta_-\|.
\]

The exact component norms are

\[
\|p\|=\sqrt{B_+^2-\epsilon_+^2/4},
\qquad
\|s\|=\sqrt{B_-^2-\epsilon_-^2/4}.
\]

Therefore

\[
|\langle b_+,b_-\rangle|
\le
\frac12\left(
\epsilon_-\sqrt{B_+^2-\epsilon_+^2/4}
+
\epsilon_+\sqrt{B_-^2-\epsilon_-^2/4}
\right).
\]

The weaker linear estimate

\[
|\langle b_+,b_-\rangle|
\le \frac12(B_+\epsilon_-+B_-\epsilon_+)
\]

follows immediately.

## Sharpness

On a two-dimensional target with \(U=\operatorname{diag}(1,-1)\), take

\[
b_+=(4,3),
\qquad
b_-=(5,12).
\]

Then \(B_+=5\), \(B_-=13\), \(\epsilon_+=6\), and \(\epsilon_-=10\). The cross pairing and sharp bound both equal \(56\). Thus no smaller universal bound follows from these four norms alone.

## Confinement consequence

Exact intertwining is the zero-defect endpoint and forces the cross pairing to vanish. Approximate intertwining yields quantitative control only when the physical route norms and both defect norms are bounded. Small source-label mismatch without a target norm estimate does not imply a small Pauli \(X\) coefficient.

For a positive reciprocal return \(K=aI+xX+zZ\), this estimate controls \(|x|\). Strict return still requires the joint radial inequality

\[
a+\sqrt{x^2+z^2}<1.
\]

A bound on \(|x|\) alone cannot certify it without bounds on \(a\) and \(z\).

## Verification

`research/aspect/checkers/check_parity_defect_bound.py` verifies the spectral defects, saturation at \(56\), the weaker bound, and the exact-symmetry endpoint using rational arithmetic.

## Disposition

Parity defects provide a sharp route-level bound on cross-grade mixing but do not independently prove scalar-null confinement. The remaining executable question is how this mixing bound combines with diagonal-load uncertainty to produce a sufficient strict-return margin.
