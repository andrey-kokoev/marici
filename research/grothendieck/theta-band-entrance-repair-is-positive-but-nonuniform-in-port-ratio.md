# Theta band-entrance repair is positive but nonuniform in port ratio

## Bounded question

Does the globally positive translation-defect current orient the full
conditional adjacent-band residual pointwise at the band entrance?

## Full residual

For \(L=\pi/b\), the aggregate conditional residual has the form

\[
R(D)
=
\beta\cos(bD)
\left[J_a(D)-J_a(D+L)\right]
+
\alpha\sin(bD)
\left[
D W_a(D)-(D+L)W_a(D+L)
\right].
\]

The preceding theorem gives

\[
A_0
:=
J_a(0)-J_a(L)
>0
\]

for \(a,L>0\).

## Weighted term at the entrance

Since \(W_a(L)>0\),

\[
D W_a(D)-(D+L)W_a(D+L)
=
-L W_a(L)+O(D).
\]

Also,

\[
\sin(bD)=bD+O(D^3),
\qquad
\cos(bD)=1+O(D^2).
\]

Therefore

\[
R(D)
=
\beta A_0
-
\alpha bL W_a(L)D
+
O(\beta D+\alpha D^2).
\]

## Consequences

For every fixed \(\alpha,\beta>0\), the positive current \(A_0\) repairs the
negative weighted term in a sufficiently small interval next to \(D=0\).

But the repair is not uniform in the port ratio. Its leading boundary-layer
scale is

\[
D_{\mathrm{repair}}
\asymp
\frac{\beta}{\alpha}
\frac{A_0}{bL W_a(L)}.
\]

As \(\beta/\alpha\downarrow0\), this protected interval collapses.

On the face \(\beta=0\),

\[
R(D)
=
-\alpha bL W_a(L)D+O(D^2)<0
\]

for sufficiently small positive \(D\).

## Result

The globally oriented \(J\)-current is a genuine boundary repair, but it
cannot yield pointwise nonnegativity uniformly over independent outer
coefficients \(\alpha,\beta\ge0\).

Therefore one of the following must hold for the larger programme:

1. the physical source fixes a positive lower relation between
   \(\beta\) and \(\alpha\);
2. only the strict open quadrant is required, with a parameter-dependent
   boundary layer;
3. the canonical band integral is positive despite a local negative lobe;
4. a larger source-derived block supplies an additional boundary current.

The first must be derived from the original parameter map. The second does not
give uniform closure near the quadrant face. The third is now the minimal
surviving mechanism.

## Relation to ordered flags

This calculation exhibits why full Gram or curvature data are too coarse. The
ordered \(J\)-flag and weighted \(W\)-flag have different port coefficients.
Their competition, not the ambient rank, determines the scalar residual.

## Sharp falsifier

If the target domain includes \(\beta=0\), pointwise conditional-band
positivity is already falsified near \(D=0\). If only \(\beta>0\) is allowed,
the next falsifier is a negative canonical block integral for a sequence with
\(\beta/\alpha\to0\).
