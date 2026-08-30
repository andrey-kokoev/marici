# Full-source outer diagonal Loewner theorem

## Use the faithful completed source

Let

\[
C(w)=\int_0^\infty
\Phi(u)\cosh(\sqrt w\,u)\,du,
\]

with the removable entire interpretation at \(w=0\). The completed theta
source satisfies

\[
\Phi(u)>0
\]

and decays superexponentially. Therefore this integral and all its
\(w\)-derivatives converge for every real \(w>0\).

This is the faithful source representation. The analogous probability
argument for the renormalized precursor was restricted to \(w<1/4\); no such
restriction occurs for \(\Phi\).

## Tilted completed-source law

For \(x>0\), define

\[
d\nu_x(u)=
\frac{\Phi(u)\cosh(\sqrt x\,u)}{C(x)}\,du
\]

and

\[
q_x(u)=\partial_x\log\cosh(\sqrt x\,u)
=\frac{u\tanh(\sqrt x\,u)}{2\sqrt x}.
\]

Then

\[
\frac{C'(x)}{C(x)}=\mathbb E_xq_x
\]

and

\[
\partial_x\mathbb E_xq_x
=\mathbb E_x(\partial_xq_x)+\operatorname{Var}_x(q_x).
\]

For

\[
H(x)=\left(x-\frac14\right)\frac{C'(x)}{C(x)},
\]

we obtain the exact identity

\[
\boxed{
H'(x)=
\mathbb E_x\left[q_x+(x-1/4)\partial_xq_x\right]
+(x-1/4)\operatorname{Var}_x(q_x).
}
\]

## Pointwise sign

Put \(r=\sqrt x\,u\). For \(u>0\),

\[
\partial_xq_x<0,
\]

because

\[
r\operatorname{sech}^2r-\tanh r<0.
\]

On the other hand,

\[
q_x+x\partial_xq_x
=\frac{u^2}{4r}
\left(\tanh r+r\operatorname{sech}^2r\right)>0.
\]

Hence, with \(c=1/4\),

\[
q_x+(x-c)\partial_xq_x
=\left(q_x+x\partial_xq_x\right)-c\partial_xq_x>0.
\]

For \(x>c\), the variance coefficient is also positive. Therefore

\[
\boxed{
H'(x)>0
\qquad\text{for every }x>1/4.
}
\]

Since

\[
L_C(x,x)=C(x)^2H'(x),
\]

we have the exact source theorem

\[
\boxed{
L_C(x,x)>0
\qquad(x>1/4).
}
\]

No zero locations, analytic continuation of a divergent measure, or finite
numerical scan enters the proof.

## What this advances

The entire outer positive-real ray passes the diagonal Loewner test by a
universal completed-source mechanism:

\[
\text{positive pointwise response}
+\text{positive fluctuation}
>0.
\]

The source-forced center is again exact. Beyond \(1/4\), fluctuations help;
inside \(1/4\), their coefficient is hostile and requires the separate
central inequality/certificate.

This theorem concerns rank one only. Matrix monotonicity does not follow from
scalar monotonicity. The first coupled outer theorem remains the positivity
of

\[
\det
\begin{pmatrix}
K_H(x,x)&K_H(x,y)\\
K_H(y,x)&K_H(y,y)
\end{pmatrix}
\]

for arbitrary \(x,y>1/4\).

## Next source attack

The kernel

\[
\phi_x(u)=\cosh(\sqrt x\,u)
\]

has the positive series expansion

\[
\phi_x(u)=\sum_{n\ge0}\frac{x^nu^{2n}}{(2n)!}.
\]

This suggests a total-positivity property in the pair \((x,u^2)\). The next
legitimate question is whether that total positivity, combined with the
specific response observable \(q_x\), yields the two-point Loewner determinant
without decomposing the completed source.

The falsifier is a pair \(x,y>1/4\) where the coupled determinant is negative.
Such a failure would leave the diagonal theorem intact while killing the
proposed total-positive lift to rank two.

The rank-two gate now reduces exactly to concavity of
\(H'(x)^{-1/2}\), equivalently nonnegativity of the Schwarzian derivative of
\(H\). See `theta-outer-rank-two-schwarzian-gate.md`.
