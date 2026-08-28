# Sequential SO(5) Two-Vector Projector Repair

## Question

Does the simple-parent route contain an independently required breaking
sector that escapes the one-field projector no-go of WP739--WP741?

## Source-required sequential frame

The subgroup chain used by the product-parent construction is

\[
SO(5)\supset SO(4)\supset SO(3)_{\rm diag}.
\]

A nonzero fundamental vector \(u\in\mathbb R^5\) has stabilizer \(SO(4)\).
A second nonzero vector \(v\in u^\perp\) has joint stabilizer \(SO(3)\).
Thus a sequential realization of this declared chain requires two ordered
fundamental directions. They are not matter added after inspecting a beta
function.

The vector carrier then decomposes with source-retained projectors as

\[
\mathbb R^5=E_3\oplus L_v\oplus L_u,
\qquad
P_u=\frac{uu^T}{|u|^2},
\qquad
P_v=\frac{vv^T}{|v|^2}.
\]

The two residual singlets are no longer identified merely by their common
\(SO(3)\) label. They retain distinct source provenance from the two stages of
breaking.

## Exact global vacuum

Consider the renormalizable \(SO(5)\)-invariant potential

\[
V(u,v)=
\frac{\lambda_u}{4}(|u|^2-a^2)^2
+\frac{\lambda_v}{4}(|v|^2-b^2)^2
+\frac{\kappa}{2}(u\mathbin\cdot v)^2,
\]

with \(a,b,\lambda_u,\lambda_v,\kappa>0\). It is a sum of nonnegative
squares, so its global minima are exactly

\[
|u|=a,qquad |v|=b,qquad u\mathbin\cdot v=0.
\]

Every minimum is gauge-equivalent to

\[
u_*=ae_5,qquad v_*=be_4.
\]

The stabilizer is precisely the \(SO(3)\) acting on the first three
coordinates.

There are ten real field coordinates and a seven-dimensional gauge orbit.
After removing those seven zero modes, the three physical Hessian eigenvalues
are

\[
2\lambda_u a^2,qquad
2\lambda_v b^2,qquad
\kappa(a^2+b^2).
\]

They are strictly positive throughout the declared domain. This is a stable
open family, not the isolated saddle found for the one-field \(14\) in WP741.

## Repair of the WP739 fiber

Under the residual \(SO(3)\) alone, the two singlets admit an \(O(2)\)
commutant. Requiring preservation of both ordered projectors reduces that
singlet action to independent signs. A continuous rotation mixing \(L_u\)
and \(L_v\) fails to preserve \(P_u\) and \(P_v\). Hence the exact
\(R(\pi/2)\) hostile of WP739 is no longer a morphism of the source-retained
packet.

A threshold mass operator of the form

\[
M^2=m_3^2P_3+m_v^2P_v+m_u^2P_u
\]

and every function of it preserve the labelled projectors. This gives a
precise conditional threshold intertwiner. It does not derive the three mass
eigenvalues or prove that an experimental channel resolves them.

## What this repairs and what it does not

This construction repairs the first obstruction that prevented calculation
of the full simple-parent beta system:

- the simple group forces the complete \(3+1+1\) carrier;
- the required two-stage breaking supplies an ordered rank-one projector for
  each singlet;
- the projector vacuum is globally stable modulo gauge;
- source-functional thresholds preserve the labels.

It does not yet fix the portal magnitude. The ratios \(a/b\), the scalar and
Yukawa couplings, and the singlet mass gaps remain continuous. Nor has the
full anomaly-free \(Spin(5)\times U(1)_Y\times SU(3)_c\) gauge--Yukawa system
been derived. Therefore the construction is a source-generated projector
selector and threshold rigidifier, not yet the requested end-to-end portal
selector.

## Smallest exact falsifiers

- If \(\kappa=0\), the relative angle is flat and the \(O(2)\) fiber returns.
- If the threshold contains an off-diagonal term
  \(\epsilon(uv^T+vu^T)\), it does not commute with either labelled
  projector and the source-functional threshold theorem fails.
- Changing \(a/b\) preserves the subgroup chain and projector labels while
  changing all radial normalizations. The breaking geometry alone does not
  fix the portal magnitude.

## Next calculation

The newly opened bounded calculation is the complete simple-parent
gauge--Yukawa fixed-point system with the two compulsory fundamental breaking
fields and the full spinor/vector matter multiplets. Its interactions must be
fixed by the unique parent invariants before solving the beta equations. If
that source has no controlled attractive fixed point, the minimal
simple-parent branch closes without any optional matter scan.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp877_sequential_so5_two_vector_projector_repair.py
~~~

