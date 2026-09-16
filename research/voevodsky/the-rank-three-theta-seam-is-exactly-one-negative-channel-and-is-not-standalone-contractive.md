# Correction: the rank-three theta seam has signature (1,2), and its invariant trace repairs it exactly

## Sign audit

For

\[
X(z)=F(z)+F(-z),
\]

differentiation gives

\[
X'(z)=F'(z)-F'(-z),
\qquad
X''(z)=F''(z)+F''(-z).
\]

The seam term in

\[
XX''-(X')^2
\]

is therefore

\[
\mathscr S_F(z)
=
F(z)F''(-z)+F(-z)F''(z)+2F'(z)F'(-z).
\]

For real \(x\),

\[
F(-x)=\overline{F(x)},
\qquad
F'(-x)=-\overline{F'(x)}.
\]

Hence the correct real-axis formula is

\[
\boxed{
\mathscr S_F(x)
=
2\operatorname{Re}(F''(x)\overline{F(x)})
-2|F'(x)|^2.
}
\]

The previously copied plus sign was incorrect.

## Exact signature

Put

\[
h_+=\frac{F+F''}{\sqrt2},
\qquad
h_-=\frac{F-F''}{\sqrt2}.
\]

Then

\[
\boxed{
\mathscr S_F
=
|h_+|^2-|h_-|^2-2|F'|^2.
}
\]

Thus the seam has signature

\[
\boxed{(1,2),}
\]

not \((2,1)\).

## Invariant-trace repair

The direct source formula is

\[
\boxed{
\mathscr S_F(x)
=
-
\iint_{(0,\infty)^2}
(u+v)^2f(u)f(v)

e^{ix(u-v)}
\,du\,dv.
}
\]

Its rotation-invariant trace energy is the total mass

\[
E_{\rm seam}
=
\iint
(u+v)^2f(u)f(v)
\,du\,dv.
\]

Writing moments

\[
M_k=\int_0^\infty u^kf(u)\,du,
\]

gives

\[
\boxed{
E_{\rm seam}=2(M_0M_2+M_1^2).
}
\]

Since \(1-\cos\theta\ge0\),

\[
\begin{aligned}
E_{\rm seam}+\mathscr S_F(x)
&=
\iint
(u+v)^2f(u)f(v)
[
1-
\cos(x(u-v))
]
\,du\,dv\\
&\ge0.
\end{aligned}
\]

Therefore

\[
\boxed{
|h_-|^2+2|F'|^2
\le
|h_+|^2+E_{\rm seam}.
}
\]

This is an exact source-derived contraction inequality for the seam block after adjoining its invariant trace energy.

At \(x=0\), equality holds.

## Computational check

The corrected checker

`research/voevodsky/checkers/scout_rank_three_theta_seam_contraction.py`

scans the completed theta half-source on \(0\le x\le40\). It finds the minimum combined positive-to-negative ratio equal to one at \(x=0\), as forced by the exact identity.

Result:

`research/voevodsky/results/rank-three-theta-seam-contraction-scout.json`.

The numerical scan is only a consistency check; the inequality follows analytically from \(1-\cos\ge0\).

## What has been constructed

The seam block now has a noncircular positive completion:

\[
\boxed{
\text{one positive seam channel}
+
\text{invariant trace bulk}
-
\text{two negative seam channels}
\ge0.
}
\]

The completion is source-derived from the same kernel \((u+v)^2f(u)f(v)\); it is not defined from the desired Xi sign.

## What remains

This repairs the opposite-sheet seam block, but it does not yet orient the same-sheet spin-two curvature

\[
FF''-(F')^2.
\]

For that block, the invariant trace similarly dominates the absolute spin-two component, but replacing spin two by its trace changes the target unless the excess trace is coupled back through an exact Green identity.

Thus the next exact task is to combine:

1. the repaired seam identity above;
2. the two same-sheet difference energies;
3. the completed curvature \(XX''-(X')^2\);

and calculate the residual trace surplus. If the surplus is an exact positive Green bulk or a source boundary square, the first Laguerre form closes by construction. If it is merely discarded, the argument is not faithful.

## Disposition

The corrected rank-three experiment succeeds in its proper scope:

\[
\boxed{
E_{\rm seam}+\mathscr S_F(x)\ge0.
}
\]

The seam is constructively repaired. The remaining obstruction is the faithful recombination of this repair with the same-sheet spin-two channels.
