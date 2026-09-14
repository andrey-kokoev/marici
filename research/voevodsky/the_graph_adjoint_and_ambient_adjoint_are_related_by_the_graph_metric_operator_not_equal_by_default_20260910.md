# The graph adjoint and ambient adjoint are related by the graph metric operator, not equal by default

## Question

When a synthesis lands in the domain of a closed Green operator, how are its graph adjoint and ambient Hilbert adjoint related?

## Claim boundary

The two adjoints belong to different typed maps. The adjoint of the graph-domain inclusion inserts the inverse graph metric, while the graph adjoint inserts the graph metric on its natural core. Equality requires an additional metric-intertwining condition and is not implied by Real compatibility alone.

## Problem

Let

\[
D:\mathcal E=\operatorname{Dom}D\subset H\to H
\]

be densely defined and closed. Let \(\mathcal E_D\) carry the graph inner product

\[
\langle x,y\rangle_D
=
\langle x,y\rangle_H+
\langle Dx,Dy\rangle_H.
\]

Let

\[
i:\mathcal E_D\hookrightarrow H
\]

be the continuous inclusion, and let

\[
U:V\to\mathcal E_D
\]

be bounded. Its ambient realization is

\[
\bar U=iU:V\to H.
\]

There are now two adjoints:

\[
U^{*D}:\mathcal E_D\to V
\]

and

\[
\bar U^*:H\to V.
\]

## Bold conjecture

Because \(i\) is the identity on underlying vectors, one may identify \(U^{*D}\) with \(\bar U^*\) without recording the target metric.

## Named rivals

1. The inclusion adjoint \(i^*\) is a nontrivial inverse graph-metric operator.
2. On a natural core, the graph adjoint contains \(I+D^*D\).
3. Real compatibility makes both adjoints equal automatically.
4. Equality can hold for special isometric synthesis ranges.

## Inclusion adjoint

The inclusion adjoint

\[
i^*:H\to\mathcal E_D
\]

is characterized by

\[
\langle ix,h\rangle_H
=
\langle x,i^*h\rangle_D.
\]

Let

\[
G_D=I+D^*D.
\]

The positive self-adjoint operator \(G_D\) is invertible with bounded inverse on \(H\). Its inverse maps \(H\) continuously into \(\operatorname{Dom}(D^*D)\subset\mathcal E_D\). Direct substitution gives

\[
i^*=G_D^{-1}.
\]

Here the codomain is equipped with the graph norm.

## Ambient-to-graph adjoint relation

Since

\[
\bar U=iU,
\]

functoriality of bounded Hilbert adjoints gives

\[
\bar U^*=U^{*D}i^*.
\]

Therefore

\[
\bar U^*
=
U^{*D}G_D^{-1}.
\]

This formula is globally bounded on \(H\).

It already rejects the bold conjecture: the maps have different domains and differ by the inclusion adjoint.

## Graph-to-ambient relation on the operator core

For

\[
x\in\operatorname{Dom}(D^*D),
\]

we have

\[
\langle Uv,x\rangle_D
=
\langle \bar Uv,(I+D^*D)x\rangle_H.
\]

Hence

\[
U^{*D}x
=
\bar U^*G_Dx
\qquad
(x\in\operatorname{Dom}(D^*D)).
\]

This is the inverse relation on the natural core. It must not be extended to all of \(\mathcal E_D\) by writing the generally unbounded expression \(G_Dx\) where it is undefined.

## Gramian distinction

The ambient synthesis Gramian is

\[
\bar U^*\bar U
=U^{*D}i^*iU.
\]

The graph synthesis Gramian is

\[
U^{*D}U.
\]

Since

\[
i^*i\ne I_{\mathcal E_D}
\]

in general, the two Gramians differ. Thus lower bounds, compactness, and singular values must be indexed by the chosen target metric.

## Real comparison

Let \(J_H\) be an antiunitary commuting with \(D\) and preserving \(\mathcal E\). Then it commutes with the graph metric:

\[
J_HG_D=G_DJ_H
\]

in the anti-linear sense, and restricts to a graph antiunitary \(J_D\).

If

\[
J_DU=UJ_V,
\]

then the graph adjoint satisfies

\[
J_VU^{*D}=U^{*D}J_D.
\]

The ambient realization separately satisfies

\[
J_V\bar U^*=\bar U^*J_H.
\]

Both Real squares commute, but they do not identify \(U^{*D}\) with \(\bar U^*\). Rival 3 fails.

## Equality criterion

An equality between the two adjoints can only be stated after a comparison of their domains. Pulling the ambient adjoint back along the inclusion gives

\[
\bar U^*i:
\mathcal E_D\to V.
\]

Then

\[
U^{*D}=\bar U^*i
\]

holds exactly when

\[
U^{*D}(I-i^*i)=0.
\]

Equivalently, the graph and ambient metrics agree on the synthesis range as tested against all graph-domain vectors. A sufficient condition is

\[
DU=0,
\]

because the derivative contribution to \(\langle Uv,x\rangle_D\) then vanishes for every \(x\). This condition is exceptional rather than automatic.

Rival 4 survives only under such an additional metric condition.

## Radial Green example

For

\[
\mathbb D=\operatorname{diag}(\partial_r,-\partial_r)
\]

on the wall domain, the graph metric is

\[
G_{\mathbb D}=I+\mathbb D^*\mathbb D.
\]

A radial synthesis

\[
U^{\rm rad}:V\to\mathcal E_{\mathbb D}
\]

therefore has:

- graph adjoint \((U^{\rm rad})^{*\mathbb D}:\mathcal E_{\mathbb D}\to V\);
- ambient adjoint \((iU^{\rm rad})^*:H_{\rm rad}\to V\).

They satisfy

\[
(iU^{\rm rad})^*
=
(U^{\rm rad})^{*\mathbb D}G_{\mathbb D}^{-1}.
\]

The twisted Real structure \(J_u\) commutes with \(G_{\mathbb D}\), so both adjoint squares are Real-compatible. But the earlier unindexed notation \(U^*=U^\top\) is incomplete until the metric rung is declared.

## Analytic transpose

The same distinction applies to bilinear transpose. If the bilinear form is induced from the graph metric, write

\[
U^{\top_D}=J_VU^{*D}J_D.
\]

If induced from the ambient metric, write

\[
\bar U^\top=J_V\bar U^*J_H.
\]

The two transpose identities are related by \(G_D^{-1}\); neither can replace the other.

## Constructor-role correction

Adjoint-bearing signatures require:

- source and target rungs;
- source and target metrics;
- inclusion maps between rungs;
- the corresponding metric operator;
- the domain on which an unbounded metric expression is used;
- Real structures on each rung.

The roles `graph_adjoint`, `ambient_adjoint`, `graph_transpose`, and `ambient_transpose` are distinct.

## Strongest falsification attempt

The underlying vectors in \(\mathcal E_D\) and \(H\) are identical, and the inclusion is injective. This makes the two adjoints look coordinatewise interchangeable. The explicit formula

\[
i^*=(I+D^*D)^{-1}
\]

shows the missing metric operator. Equality occurs only under an extra range condition and cannot be inferred from Real covariance.

## Disposition

The bold conjecture is rejected. Graph and ambient adjoints are linked by the graph metric but are not equal by default. This is the first metric-rung correction generated by the enriched boundary category and must be propagated to every G4 transpose--adjoint declaration.
