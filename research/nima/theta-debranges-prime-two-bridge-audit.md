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

## The minimal four-state repair is unique but changes the source

Grothendieck's minimal local closure can be written with transport state
(t=(c,s)^T), accumulator state (a=(A,B)^T), and

\[
R=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
C(r)=\begin{pmatrix}\Phi(r)&0\\0&-r\Phi(r)\end{pmatrix}.
\]

The uncorrected triangular equations are

\[
t'=zRt,
\qquad
a'=Ct.
\]

Ask for a four-state Lagrange identity with the block symplectic form

\[
\Omega=\operatorname{diag}(-R,-R)
\]

and positive spectral Hamiltonian

\[
H=\Omega\operatorname{diag}(R,0)=
\operatorname{diag}(I_2,0)\succeq0.
\]

Because a positive semidefinite block matrix with zero accumulator diagonal
cannot have transport--accumulator cross terms, this block form is forced by
the declared spectral action. Add a reverse source coupling (D(r)a) to the
transport equation:

\[
t'=zRt+Da,
\qquad
a'=Ct.
\]

The zero-order symplectic condition is

\[
(-R)D+C^T(-R)=0,
\]

so the repair is uniquely fixed:

\[
\boxed{
D=RC^TR
=\begin{pmatrix}r\Phi(r)&0\\0&-\Phi(r)\end{pmatrix}.
}
\]

Thus the repaired equations are

\[
\begin{aligned}
c'&=-zs+r\Phi A,&
s'&=zc-\Phi B,\\
A'&=\Phi c,&
B'&=-r\Phi s.
\end{aligned}
\]

This is a genuine positive canonical system. It also exposes the obstruction:
the reverse coupling changes the source transform it was meant to realize.
For the natural zero-spectral initial data

\[
c(0)=1,\quad s(0)=A(0)=B(0)=0,
\]

the (z=0) equations give

\[
s=B=0,
\qquad
A'=\Phi c,
\qquad
c'=r\Phi A.
\]

For (r>0), positivity of the completed theta kernel gives (A>0), hence
(c'>0) and (c>1). Consequently

\[
A(L)=\int_0^L\Phi(r)c(r)\,dr
>\int_0^L\Phi(r)\,dr.
\]

The repaired terminal accumulator is not the original theta transform even
at (z=0). The discrepancy is a source-derived nonlinear dressing, not a
normalization accident.

Therefore the most obvious realization attempt has a precise disposition:

\[
\boxed{
\text{positive four-state repair exists, but violates terminal source
faithfulness.}
}
\]

A successful canonical system must either carry additional boundary/state
data whose reduction removes this dressing, or derive a different carrier
coordinate in which the completed theta transform is already the terminal
solution. Merely adding the missing reverse arrow is not enough.

## A varying Green form cannot rescue the triangular closure

The preceding calculation used the simplest constant symplectic form. There
is a stronger intrinsic no-go. In the real source frame, allow an arbitrary
carrier-dependent skew Green form

\[
\Omega(r)=
\begin{pmatrix}
P(r)&Q(r)\\
-Q(r)^T&S(r)
\end{pmatrix}
\]

on the original triangular system

\[
Y'=(A_0+zA_1)Y,
\qquad
A_0=\begin{pmatrix}0&0\\C&0\end{pmatrix},
\qquad
A_1=\begin{pmatrix}R&0\\0&0\end{pmatrix}.
\]

Suppose its Lagrange identity has a positive, spectral-independent density
(H(r)\succeq0). Comparing coefficients of (z) and (ar w) forces

\[
H=\Omega A_1
=\begin{pmatrix}PR&0\\-Q^TR&0\end{pmatrix}.
\]

The accumulator diagonal block of (H) is zero. Positivity of a Hermitian
block matrix with a zero diagonal block forces its off-diagonal block to
vanish. Since (R) is invertible,

\[
Q=0.
\]

The zero-order Green equation

\[
\Omega'+A_0^T\Omega+\Omega A_0=0
\]

then has transport--accumulator block

\[
Q'+C^TS=C^TS=0.
\]

For every (r>0) with (Phi(r)>0),

\[
C(r)=\operatorname{diag}(\Phi(r),-r\Phi(r))
\]

is invertible. Therefore (S(r)=0) throughout the open carrier. It cannot
approach the nondegenerate terminal accumulator form required to reproduce

\[
X'(z)\overline{X(w)}-X(z)\overline{X'(w)}.
\]

Hence

\[
\boxed{
\text{No carrier-dependent positive Green form on the original four-state
triangular closure can produce the terminal theta Bezoutian.}
}
\]

This removes the normalization loophole. The next admissible construction
must change the dynamics or enlarge the state/boundary complex; it cannot
repair the original accumulator merely by choosing a clever local metric.

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
