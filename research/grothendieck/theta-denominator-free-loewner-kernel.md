# Denominator-free Loewner kernel for the theta current

This is the congruence-cleared form of the Loewner kernel already isolated in
the earlier reduced gamma--prime program; it is not a new RH equivalence. The
new contribution is its analytic extension through allowed zeros and its
derivation from the denominator-free energy current. See
`theta-loewner-rediscovery-and-meaning-audit.md`.

## The correct two-point object

Let

\[
c=\frac14,
\qquad
H(w)=(w-c)\frac{C'(w)}{C(w)}.
\]

For real regular points \(x\ne y\), the boundary Loewner kernel is

\[
K_H(x,y)=\frac{H(x)-H(y)}{x-y}.
\]

Clear both transform denominators and define

\[
\boxed{
L_C(x,y)=
\frac{
(x-c)C'(x)C(y)-(y-c)C'(y)C(x)
}{x-y}.
}
\]

Then

\[
\boxed{L_C(x,y)=C(x)C(y)K_H(x,y).}
\]

Although the quotient presentation excludes zeros of \(C\), the numerator
kernel extends analytically across them. It is therefore the faithful object
for a source proof.

On the diagonal,

\[
\boxed{
L_C(x,x)=
C(x)C'(x)
+(x-c)\bigl(C(x)C''(x)-C'(x)^2\bigr).
}
\]

## Congruence theorem

For any finite set of regular real points \(x_1,\ldots,x_n\), put

\[
D=\operatorname{diag}(C(x_1),\ldots,C(x_n)).
\]

Then

\[
[L_C(x_i,x_j)]=D[K_H(x_i,x_j)]D.
\]

Because \(D\) is a real invertible congruence,

\[
\boxed{
[L_C(x_i,x_j)]\succeq0
\quad\Longleftrightarrow\quad
[K_H(x_i,x_j)]\succeq0.
}
\]

By continuity, positivity of the entire kernel \(L_C\) includes configurations
containing real zeros of \(C\). This is exactly the behavior missing from raw
translation total positivity.

## Conditional zero geometry

For interpretation only, suppose

\[
H(w)=a+bw+sum_n\frac{w-c}{w-\rho_n}
\]

with \(b\ge0\) and \(\rho_n<c\) real, after the appropriate convergent
normalization. Then

\[
\boxed{
K_H(x,y)=b+sum_n
\frac{c-\rho_n}{(x-\rho_n)(y-\rho_n)}.
}
\]

Every allowed real zero supplies a positive rank-one Gram term. Thus the
Loewner kernel does not suppress critical-line zeros: it represents them as
positive spectral atoms. A nonreal zero would instead create a pole inside
the Herglotz domain and destroy kernel positivity.

This conditional formula explains the desired theorem but cannot prove it,
because assuming \(\rho_n\in\mathbb R\) assumes the RH zero geometry.

## Relation to angular flow

Positive semidefiniteness of every boundary Loewner matrix is the operator
monotonicity/Pick certificate for \(H\). Under the usual analytic and growth
hypotheses, it yields

\[
\Im H(w)\ge0
\qquad(\Im w>0),
\]

and hence

\[
-\partial_\vartheta|C(w)|^2
=2|C(w)|^2\Im H(w)\ge0.
\]

Strictness requires excluding the degenerate constant case and auditing the
support of the representing measure.

## Source-level target

The sharp new conjecture is:

\[
\boxed{L_C\text{ is a positive-semidefinite real kernel}.}
\]

Unlike the scalar cone inequality, this is a coupled all-points statement.
Unlike PF\(_\infty\) for \(K(x-y)\), it is compatible with—and positively
records—the established critical-line zeros.

The preferred proof route is to substitute

\[
C(w)=\frac12(c-w)\mathcal F(w)
\]

with \(\mathcal F\) the transform of the decaying modular precursor, then
derive a Gram factorization of \(L_C(x,y)\) directly from that source. Any
factorization must retain the centered multiplier and may not replace it by
absolute translation-kernel positivity.

## Falsifiers

The conjecture is finitely falsified by one real tuple and coefficient vector
for which

\[
\sum_{j,k}v_jL_C(x_j,x_k)v_k<0.
\]

The smallest hostile tests are:

1. diagonal negativity \(L_C(x,x)<0\);
2. a negative \(2\times2\) determinant; and
3. a negative \(3\times3\) determinant after the first two pass.

These are tests of the correct kernel: a failure has direct Herglotz meaning
and cannot be dismissed as an artifact of thimble or translation coordinates.

## First coupled reconnaissance

The earlier zero-free evaluator satisfies the exact normalization

\[
\texttt{reduced\_F}(w)=4H(w).
\]

It was reused to form the upper-half-plane Pick matrices

\[
\left[
\frac{H(z_j)-\overline{H(z_k)}}
{z_j-\overline{z_k}}
\right]_{j,k}.
\]

On real coordinates

\[
-100,-30,-10,-3,-1,-0.3,0.3,1,3,10,30,100
\]

at heights \(0.03,0.1,0.3,1\), all sampled principal matrices through order
three passed a depth-36 versus depth-40 stability guard:

\[
\begin{array}{c|r}
\text{order}&\text{matrices tested}\\ \hline
1&48\\
2&264\\
3&880.
\end{array}
\]

The smallest order-two determinant was approximately
\(7.03\times10^{-10}>0\). The smallest printed order-three determinant was a
negative \(8.47\times10^{-21}\), but its independent depth discrepancy was
\(1.61\times10^{-19}\); it is unresolved cancellation, not a sign witness.

This is non-certified reconnaissance and uses no zero locations. Unlike the
raw translation-minor scan, it tests the exact Pick kernel whose global
positivity would imply the desired Herglotz property.

Artifacts:

- checkers/theta_angular_current_pick_matrices.py
- results/theta-angular-current-pick-matrices.json
