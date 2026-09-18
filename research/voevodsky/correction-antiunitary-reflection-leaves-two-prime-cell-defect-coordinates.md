# Correction: antiunitary reflection leaves two prime-cell defect coordinates

## Error corrected

`the-ordered-bulk-four-block-reduces-to-two-covariances-and-one-wall-diagonal.md` used the linear law

\[
P^*\Delta P=\Delta.
\]

That is not the declared variance of the oriented linking channel. Reflection is antiunitary there, so the correct law is

\[
P^*\Delta P=\overline\Delta.
\]

The prior one-diagonal rigidity conclusion is therefore retracted.

## Correct exact reduction

Write

\[
\Delta=\begin{pmatrix}a&x+iy\\x-iy&d\end{pmatrix},
\quad
F=\begin{pmatrix}0&-1/2\\2&0\end{pmatrix},
\quad
P=\operatorname{diag}(1,-1).
\]

Quarter-turn covariance \(F^*\Delta F=\Delta\) gives

\[
d=a/4,\qquad x=0.
\]

The antiunitary reflection law imposes no further condition on \(y\). Hence

\[
\boxed{
\Delta=
 a\begin{pmatrix}1&0\\0&1/4\end{pmatrix}
+y\begin{pmatrix}0&i\\-i&0\end{pmatrix}.
}
\]

The two surviving real coordinates have distinct meanings:

- \(a\): positive even/odd normalization defect;
- \(y\): oriented Stokes/Wronskian linking defect.

Thus two independently sourced scalar comparisons are necessary and sufficient:

1. one even-wall diagonal equality, forcing \(a=0\);
2. one oriented off-diagonal equality, forcing \(y=0\).

Reflection covariance preserves the second coordinate; it cannot eliminate it.

## Source status

The resolved theta-history form is explicitly defined on \(D(B)\) by

\[
G_\theta=(1+M_\Phi^2)I+B^*B,
\]

with zero radical on its retained graph. But its common-domain quarter-turn intertwiner is not proved globally, and the independently typed oriented linking comparison remains open. The candidate value \(-\kappa_p/(2s_p)\) cannot be inserted until the boundary-Stokes and completed-Wronskian odd lines are identified by a typed half-density map.

## Corrected coordinates

Use

- \(b_{C4}=0\): common-domain quarter-turn covariance unproved;
- \(b_{\rm even}=0\): independent even-wall equality unproved;
- \(b_{\rm link}=0\): oriented linking equality unproved;
- \(b_{\rm ord}=\bot\): full ordered equality follows only after all three;
- \(b_{\rm rad,loc}=1\): local retained response graph has zero radical;
- \(b_{\rm rad,glob}=0\): global arithmetic-pushout radical descent remains open.

Therefore

\[
(b_{C4},b_{\rm even},b_{\rm link},b_{\rm ord},
 b_{\rm rad,loc},b_{\rm rad,glob})
=(0,0,0,\bot,1,0).
\]

## Verification

`check_prime_cell_c4_reflection_rigidity.py` has been replaced by a v2 exact checker using the antiunitary law. It confirms that the imaginary oriented coordinate survives.

## Claim boundary

This fixes the variance and exact dimension of the local defect space. It does not construct the three source comparisons or prove global Green coherence.
