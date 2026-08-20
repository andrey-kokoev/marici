# Published-boundary-value uniqueness certificate

Date: 2026-08-15

## Frozen inputs

1. Albayrak--Benincasa--Duaso Pueyo, arXiv:2305.19686v2,
   equations (4.18)--(4.20): every external site energy and internal edge
   energy is continued with negative imaginary part.
2. Benincasa--Vazão, arXiv:2402.06558, equations (3.1), (3.4), and
   (3.6)--(3.9): the loop chain is the oriented real Euclidean
   Cayley--Menger region, with the loop measure positive in its interior.
3. Benincasa et al., arXiv:2408.16386v2, equations (57)--(58):
   the three-site polar coordinate is
   \[
   q_{\mathcal G_{12}}=E+y_{12},
   \qquad dq_{\mathcal G_{12}}=dy_{12}.
   \]
4. The literal residue normalization and marked surface already certified
   in Marici entries 161--178. No carrier modification is admitted.

## Predeclared uniqueness criterion

Let \(T_-\) be the tube in which every source energy has negative imaginary
part. A source-admissible residue lift is the boundary value, at
\(q_{\mathcal G_{12}}=0\), of the fixed oriented positive
Cayley--Menger chain transported inside \(T_-\). It is unique if:

- \(T_-\) is path connected and simply connected;
- the integrand and square-root measure have a fixed germ on the physical
  chain;
- the polar coordinate is transverse with source-fixed Jacobian;
- admissible equivalence is analytic continuation of that germ, not
  arbitrary addition of an absolute cycle.

## Verification

The inequalities \(\operatorname{Im}x_s<0\) and
\(\operatorname{Im}y_e<0\) define a convex tube. Hence any two paths with
the same endpoints in \(T_-\) are homotopic there.

On the physical real chain, the source measure is positive. This selects
the positive Cayley--Menger square-root sheet and the standard loop-edge
orientation. Analytic continuation in \(T_-\) transports both uniquely
until a frozen discriminant is crossed.

For
\[
q=E+y_{12},
\]
the source deformation gives \(\operatorname{Im}q<0\), and
\[
dq=dy_{12}.
\]
Therefore the one-dimensional boundary-value identity fixes the Leray
orientation and multiplicity:
\[
\frac1{q-i0}=\operatorname{PV}\frac1q+i\pi\delta(q),
\qquad
\operatorname{Disc}\frac1{q-i0}=2\pi i\,\delta(q).
\]
With
\[
a=y_{23},\qquad b=y_{31},\qquad y_{12}=-E,
\]
the induced residue chain is the analytic continuation of the positive
Cayley--Menger section
\[
\Gamma^{\rm res}_E:
\quad
K_0(a,b)\ge0,\quad
\text{all source-required signed minors}\ge0,\quad
w=+\sqrt{K_0(a,b)},
\]
oriented by \(da\wedge db\), with multiplicity one.

An added closed residue-surface cycle is not another continuation of the
same source chain. It changes the period germ. It is therefore excluded by
the frozen-source criterion, rather than being a uniqueness ambiguity.

## Narrow conclusion

The published negative-imaginary boundary value plus the literal oriented
positive Cayley--Menger chain uniquely determines the local
\(q_{\mathcal G_{12}}\) Leray residue class (up to ordinary relative
homology) on every generic transverse patch.

This removes the local sheet/orientation/multiplicity blocker identified in
entry 178.

It does **not** yet compute
\[
\operatorname{Var}_{\mathcal Q}(\Gamma^{\rm res}_{\rm phys}).
\]
That requires transporting this now-canonical germ around a generic
\(\mathcal Q=0\) loop in a simultaneous resolution of the frozen marked
pair. Nor does the theorem assert that \(\mathcal Q\) is genuine support.

## Classification

- existing carrier: unchanged;
- source-defined coefficient/chain datum: canonical boundary-value residue
  germ;
- new carrier datum: none;
- next falsifier: compute whether the canonical residue germ has nonzero
  variation around generic \(\mathcal Q=0\).
