# The de Branges target is vertical modulus transport, not slice positivity

Status: exact bridge reduction and scope correction; no RH claim

Grothendieck's denominator-free kernel for

\[
X(z)=\xi\!\left(\frac12+iz\right)
\]

is

\[
\mathcal D(z,w)=
\frac{X'(z)\overline{X(w)}-X(z)\overline{X'(w)}}
{\pi(\bar w-z)}.
\]

This note tests whether the completed prime-two level-44 positivity theorem
supplies a reusable transport mechanism for this kernel.

## Exact diagonal reduction

Put (z=x+iy), (y>0), and (U(x,y)=|X(x+iy)|^2). Holomorphy gives

\[
\partial_yX=iX',\qquad
\partial_y\overline X=-i\overline{X'}.
\]

Therefore

\[
\partial_yU
=iX'\overline X-iX\overline{X'}
=2\operatorname{Im}(X\overline{X'}),
\]

and hence

\[
\boxed{
\mathcal D(z,z)=\frac{1}{2\pi y}\partial_y|X(z)|^2.
}
\]

Thus the one-point Hermite--Biehler target is precisely

\[
\boxed{
\partial_y|X(x+iy)|^2>0
\quad(x\in\mathbb R,\ y>0).
}
\]

The imaginary-axis anchor is the special case (x=0), where the fixed theta
contour is nonoscillatory. The missing theorem is not merely continuation of
a positive scalar value: it is preservation of outward modulus monotonicity
under horizontal displacement.

## Why the level-44 proof does not transfer formally

The prime-two theorem has three special resources:

1. an operator decomposition (T=A+c|1\rangle\langle1|);
2. a positive folded odd kernel controlling every Riccati pole;
3. a source-fixed rank-one channel repairing the unique negative direction of
   (A).

The theta de Branges reduction currently supplies none of these three data.
In particular, fixed-sum Wigner slices of the two-copy theta density cannot
all be Fourier-positive: Hudson rigidity would force the completed theta
kernel to be Gaussian. Consequently no legal proof may promote positivity
of each slice to positivity of the source-prescribed hyperbolic mixture.

The transferable content of the prime-two argument is therefore conditional:

> An anchor positivity theorem propagates only after the source provides (i)
> a typed defect sector, (ii) a positive comparison controlling chart or
> resolvent singularities, and (iii) a fixed repair map whose rank matches the
> defect.

At present the de Branges problem has an anchor and a faithful two-copy
current, but no derived finite-defect decomposition. Calling horizontal
continuation itself a repair would merely rename RH.

## Maximum-principle audit

The obvious scalar maximum-principle shortcut also fails without new source
structure. Since (X) is holomorphic,

\[
\Delta U=4|X'(z)|^2\ge0,
\]

so (U) is subharmonic. But the desired quantity is (U_y), and

\[
\Delta U_y=4\partial_y|X'|^2
\]

has no source-independent sign. Subharmonicity of (U) therefore does not
propagate (U_y>0) from the imaginary axis. The anchor ray is codimension one
inside the domain and is not boundary data for a positive harmonic function.

On the real boundary, (U_y(x,0)=0), while

\[
U_{yy}(x,0)=2\bigl(X'(x)^2-X(x)X''(x)\bigr).
\]

This is the classical Laguerre expression. It identifies the first normal
grade of the global target, but proving it and every higher compatibility
grade is not yet a propagation theorem.

## Sharp next gate

The prime-two analogy becomes operational only if the fixed theta source
derives one of the following:

1. a positive evolution or comparison equation for (U_y);
2. a boundary/relative complex whose defect has controlled finite rank and a
   source-fixed repair channel;
3. a canonical-system or de Branges energy identity making
   \(\mathcal D(z,w)\) a Gram kernel directly.

The third is the cleanest target. The finite falsifier for any proposed
construction is exact: its Gram representation must reproduce the two-copy
Bezoutian, including the oscillatory phase, before positivity is invoked.

## Conclusion

The level-44 theorem supplies a model of how source completion can repair a
typed positivity defect, but it does not yet supply the missing RH map. The
new exact bridge is

\[
\boxed{
\text{Hermite--Biehler positivity}
\Longleftrightarrow
\text{outward vertical monotonicity of }|X|^2,
}
\]

and the new no-go is that neither slice-wise Wigner positivity nor bare
subharmonicity can establish that monotonicity. A successful proof must derive
additional transport structure from the completed theta source itself.
