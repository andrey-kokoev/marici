# The RH feedback cannot live on the rigid reciprocal two-plane

## Boundary reduction

Let \(S(s)\) be the zero-free open prime propagation and let

\[
U(s):\mathcal B\to\mathcal H,
\qquad
V(s)^*:\mathcal H\to\mathcal B
\]

be source incidence and observation. A finite boundary law \(C(s)\) gives

\[
\widetilde S(s)=S(s)+U(s)C(s)V(s)^*.
\]

Where \(I-S(s)\) is invertible, every spectral defect reduces to

\[
D_{\partial}(s)
=
I_{\mathcal B}-C(s)G(s),
\qquad
G(s)=V(s)^*(I-S(s))^{-1}U(s).
\]

Thus the missing feedback is a constitutive law on the boundary defect carrier, not the reciprocal inverse of the prime propagation.

## The rigid two-plane

The source-derived reciprocal wall–jump return has the form

\[
G_{\mathrm{wj}}(s)
=
\begin{pmatrix}
a(s)&b(s)\\
b(s)&a(s)
\end{pmatrix},
\]

where

\[
a=\frac{m_++m_-}{2},
\qquad
b=\frac{m_+-m_-}{2}.
\]

Chain-compatible or Krein-compatible sewing on this plane is rigid up to a phase:

\[
C=cI
\quad\text{or}\quad
C=cR,
\qquad
R=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

The resulting determinants are

\[
\det(I-cG_{\mathrm{wj}})
=
(1-cm_+)(1-cm_-)
\]

and

\[
\det(I-cRG_{\mathrm{wj}})
=
1-c^2m_+m_-.
\]

Neither is proportional to the completed even readout

\[
\Xi(s)=m_+(s)+m_-(s)
\]

by a source-derived nowhere-zero factor in general.

## Rank-two no-go

Therefore the complete RH boundary feedback cannot be a rigid constitutive law acting only on the reciprocal wall–jump two-plane.

This conclusion survives the prime-loop completion. Replacing \(m_\pm\) by propagated entries of

\[
V^*(I-S)^{-1}U
\]

does not change the algebraic determinant forms as long as the return remains in the commutative span of \(I\) and \(R\) and the sewing remains chain/Krein rigid.

The obstruction is representation-theoretic, not a convergence defect.

## Why arbitrary \(2\times2\) feedback is not a repair

Allowing an arbitrary analytic matrix \(C(s)\) can force

\[
\det(I-C(s)G_{\mathrm{wj}}(s))
\]

to equal any prescribed scalar germ wherever \(G_{\mathrm{wj}}\) is invertible. That merely stores the target zero set in the constitutive coefficient.

A valid enlargement must add a source feature before choosing the boundary law. It may not add free analytic entries to \(C(s)\).

## Minimal enlargement

At least one independently typed boundary direction must remain beyond wall and jump. Natural source candidates are:

- the primitive anomaly line;
- the square anomaly line;
- the connected determinant-three return;
- the archimedean endpoint line;
- the arithmetic–analytic mismatch residue.

Accordingly, the first admissible feedback carrier has the form

\[
\mathcal B_{\mathrm{full}}
=
\mathcal B_{\mathrm{wj}}
\oplus
\mathcal B_{\mathrm{extra}},
\qquad
\dim\mathcal B_{\mathrm{extra}}\ge1,
\]

unless the source supplies a non-rigid two-plane law not covered by the chain/Krein classification.

This is a lower bound on constructor granularity, not a claim that dimension three is sufficient.

## Required mixed return

Writing the propagated boundary return in blocks,

\[
G_{\mathrm{full}}
=
\begin{pmatrix}
G_{\mathrm{wj}}&G_{\mathrm{wx}}\\
G_{\mathrm{xw}}&G_{\mathrm{xx}}
\end{pmatrix},
\]

the enlargement matters only if at least one mixed block survives:

\[
G_{\mathrm{wx}}\ne0
\quad\text{or}\quad
G_{\mathrm{xw}}\ne0.
\]

If both vanish and the extra block contributes only a nowhere-zero determinant, the RH zero divisor remains the forbidden rigid two-plane determinant.

Hence the new direction must interact with the reciprocal plane before scalar totalization.

## Minimality quotient

Boundary directions invisible to both injection and propagated observation must be removed. A direction \(b\in\mathcal B_{\mathrm{full}}\) is irrelevant when

\[
U b=0
\]

or when its propagated image is annihilated by every declared observer. Adding such a direction increases matrix size without changing the spectral mechanism.

The completed boundary object must therefore be the controllable–observable quotient of the full typed incidence carrier. Its dimension is source-derived.

## Next executable calculation

The earliest useful finite matrix is not another \(2\times2\) wall return. It is the mixed return between the wall–jump plane and one authorized extra source port:

\[
G_X^{(3)}(s)
=
V_X^*(I-S_X(s))^{-1}U_X
\]

on

\[
\mathcal B_{\mathrm{wj}}\oplus\mathbb C e_{\mathrm{extra}}.
\]

The audit must determine:

1. whether the extra port is reachable;
2. whether it is observable after prime propagation;
3. whether either mixed return is nonzero;
4. whether reciprocal sewing fixes its boundary law without fitting \(\Xi\);
5. whether the resulting determinant has the completed scalar as its top-exterior shadow.

## Hostiles

1. Keep the rigid two-plane and fit an arbitrary analytic \(C(s)\).
2. Add a third coordinate whose mixed return vanishes.
3. Add a coordinate detected only after scalar aggregation.
4. Use exact reciprocal inverse transport as feedback and obtain an identically zero Schur complement.
5. Match \(\Xi\) while the added coordinate is uncontrollable or unobservable.

## Verdict

The source-derived wall–jump plane closes reciprocal transport but is too small and too rigid to carry the completed RH determinant.

The next constructor must add at least one independently authorized boundary feature with a nonzero mixed propagated return. The first concrete target is therefore a source-derived \(3\times3\) boundary return, not a freer \(2\times2\) sewing matrix.
