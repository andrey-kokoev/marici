# The first normal jet separates the collapsed split components

## Exact global-to-central expansion

Let \(K_E(a,b)\) be the Cayley--Menger double-cover polynomial after the literal residue substitution

\[
c=-E,
\qquad z=E-x-y,
\]

using the source convention \(K=-\tfrac12\det(\mathrm{CM})\). At \(E=0\),

\[
K_0=R^2,
\qquad
R=xa^2+yb^2-xy(x+y).
\]

Direct differentiation gives

\[
\boxed{
\left.\partial_EK_E\right|_{E=0}
=-2(x+y)(a^2-y^2)(b^2-x^2).
}
\]

Thus the first deformation of the cover vanishes on both collapsed supports \(b=\pm x\). The separating information is not a fixed-wall deformation; it appears only after following the moving split fibers.

## Moving-wall jets at b=x

The colliding fibers are

\[
q_2=x-E,
\qquad q_3=x+E.
\]

Along \(b=x+\sigma E\), \(\sigma=\pm1\),

\[
\left.\frac d{dE}K_E(a,x+\sigma E)\right|_{E=0}
=4\sigma xy\,R(a,x).
\]

Since \(K_0=R^2\), the compatible square-root jet is

\[
\boxed{
\left.\frac d{dE}\sqrt{K_E(a,x+\sigma E)}\right|_{E=0}
=2\sigma xy.
}
\]

Hence the two fibers that coincide at \(b=x\) have opposite first square-root velocities \(\pm2xy\).

## Moving-wall jets at b=-x

The other pair is

\[
q_1=-x+E,
\qquad q_4=-x-E.
\]

Their velocities again produce opposite square-root jets; with the fixed central branch \(\sqrt{K_0}=R\), they are \(-2xy\) and \(+2xy\), respectively.

## Coherence meaning

The missing comparison must retain this normal jet. Its first geometric input is the antisymmetric unit after removing the common kinematic scale:

\[
\frac{(+2xy)-(-2xy)}{4xy}=1.
\]

This is not yet the integral period of \(v_{\rm alg}\), because the absolute Picard-to-de Rham Gysin map is still needed. It does show that the pairwise collision has a canonical primitive antisymmetric first-order channel rather than an unresolved scalar family.

The information flow is therefore

\[
(d_2,d_3)
\longrightarrow
\text{opposite moving-wall velocities}
\longrightarrow
\text{normalized antisymmetric normal jet}
\longrightarrow
\text{missing absolute Gysin comparison}.
\]

Verification:

- `research/voevodsky/checkers/check_split_fiber_first_normal_jet.py`
- `research/voevodsky/results/split_fiber_first_normal_jet.json`
