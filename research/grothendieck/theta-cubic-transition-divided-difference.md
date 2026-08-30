# Theta cubic transition divided difference

Status: live bounded-transition packet.

## 1. Product kernel

In logarithmic product-ratio coordinates

\[
 u_1=e^{m+v},\qquad u_2=e^{m-v},\qquad v\ge0,
\]

the fixed separation kernel is, up to an irrelevant positive constant,

\[
 \kappa(2m)
 =
 e^{4m}
 \int_0^\infty
 \sinh(2v)
 [W(e^{m+v})-W(e^{m-v})]
 \Phi(e^{m+v})\Phi(e^{m-v})\,dv.                        \tag{1}
\]

The bounded-transition problem asks for a structural order on this kernel,
not isolated moment checks.

## 2. The divided-difference source

The proved stiffening theorem gives

\[
 W'(u)=\frac{Q(u)}{u^2}>0.
\]

Put

\[
 \omega(h)=e^hW'(e^h)=\frac{Q(e^h)}{e^h}.               \tag{2}
\]

Then the score difference in (1) is exactly

\[
 W(e^{m+v})-W(e^{m-v})
 =
 \int_{m-v}^{m+v}\omega(h)\,dh
 =
 \int_{-v}^{v}\omega(m+z)\,dz.                         \tag{3}
\]

This identifies the missing source object: the logarithmic
score-stiffening density \(\omega\), not \(W\) itself.

## 3. Prekopa criterion

If \(\omega\) is log-concave on a chamber, then

\[
 (m,v)\longmapsto
 \int_{-v}^{v}\omega(m+z)\,dz                          \tag{4}
\]

is jointly log-concave there.  Indeed the integrand

\[
 \omega(m+z)\mathbf 1_{\{|z|\le v\}}
\]

is log-concave on its convex support, and integration in \(z\) preserves
log-concavity.

The other factors have compatible signs:

\[
 v\longmapsto\log\sinh(2v)
\]

is strictly concave, while

\[
 (m,v)\longmapsto
 \log\Phi(e^{m+v})+\log\Phi(e^{m-v})
\]

is concave whenever

\[
 h\longmapsto\log\Phi(e^h)
\]

is concave.  The latter condition is

\[
 e^hV'(e^h)+e^{2h}V''(e^h)\ge0.                        \tag{5}
\]

Therefore the paired source conditions

\[
 \boxed{
 (\log\omega)''(h)\le0,
 \qquad
 e^hV'(e^h)+e^{2h}V''(e^h)\ge0
 }                                                       \tag{6}
\]

make the integrand in (1) jointly log-concave.  Prekopa then makes the
restricted product kernel \(\kappa\) log-concave in its product coordinate.

## 4. The criterion cannot be global

For the primitive far carrier,

\[
 Q(u)=uV''(u)-V'(u)
 =x(4u-2)+O(1),
 \qquad x=\pi e^{2u}.
\]

Hence

\[
 \log\omega(\log u)
 =\log\frac{Q(u)}u
 =2u+O(\log u)
 =2e^h+O(h).                                           \tag{7}
\]

Its second \(h\)-derivative is eventually positive.  Thus

\[
 \boxed{
 \omega(h)\text{ is eventually log-convex, not log-concave.}
 }                                                       \tag{8}
\]

The attractive global Prekopa shortcut is therefore false.  This is a
structural no-go, not a failed numerical test.

## 5. Surviving bounded-chamber theorem

The failure in (8) is compatible with the programme because the far chamber
is already controlled by saddle concentration.  The useful target is local:

\[
 \boxed{
 (\log\omega)''(h)\le0
 \quad\text{while }0<e^h\le u_{\rm tr},
 }                                                       \tag{9}
\]

for a source-defined transition endpoint \(u_{\rm tr}\), together with (5).

If (9) holds, the difficult bounded part of the separation kernel is a
log-concave product carrier.  Its exponential tilts then have monotone
likelihood ratios, a unique moving mode, and canonical adjacent size-bias
transport.  The far log-convex part is not patched into this theorem; it is
handed off at the same source-defined chamber boundary to the proved
eventual saddle mechanism.

There is an essential two-copy caution.  Cutting the one-copy source at
\(u_{\rm tr}\) decomposes the separation kernel into

\[
 \kappa
 =\kappa_{\mathrm{bb}}
 +2\kappa_{\mathrm{bf}}
 +\kappa_{\mathrm{ff}},                                \tag{10}
\]

where the middle term contains one bounded and one far source point.  The
local Prekopa argument controls only \(\kappa_{\mathrm{bb}}\).  The eventual
saddle theorem controls the full kernel at sufficiently large tilt; it does
not independently orient \(\kappa_{\mathrm{ff}}\) at low tilt.

Thus a bounded transition theorem must also classify the cross block
\(\kappa_{\mathrm{bf}}\).  This is the canonical seam current produced by
the chamber cut.  Dropping it would repeat the earlier prime-multiplier error
in which finite modular sewing was omitted.

## 6. Exact differential falsifier

Since

\[
 \omega(\log u)=\frac{Q(u)}u,
\]

the local criterion is the explicit source inequality

\[
 \boxed{
 (u\partial_u)^2
 \log\left(\frac{Q(u)}u\right)\le0.
 }                                                       \tag{11}
\]

All quantities are derivatives of the completed theta source.  The next
attack is to expand (10) through
\[
 Q=uV''-V'
\]
using the already-certified two-label transition and tail envelopes.
The first positive value of the left side is the canonical endpoint of the
Prekopa chamber; it must not be moved afterward to fit the cubic answer.

No derivatives beyond the existing degree-two certificate are required.
Indeed,

\[
 Q'(u)=uV'''(u),
\qquad
 (u\partial_u)Q=u^2V'''(u),
\]

and

\[
 (u\partial_u)^2Q
 =2u^2V'''(u)+u^3V''''(u).
\]

Therefore

\[
 \boxed{
 (u\partial_u)^2\log\left(\frac Qu\right)
 =
 \frac{
 Q(2u^2V'''+u^3V'''')
 -u^4(V''')^2
 }{Q^2}.
 }                                                       \tag{12}
\]

The numerator

\[
 \mathfrak P(u)
 :=
 Q(2u^2V'''+u^3V'''')-u^4(V''')^2                    \tag{13}
\]

is the exact bounded-transition falsifier.  The previous packets already
provide signed envelopes for \(Q\), \(V'''\), and \(V''''\) across the
primitive transition.  Hence the next calculation is a finite symbolic
reuse of proved curvature channels, not a new high-derivative hierarchy.

If \(\mathfrak P\le0\) through a nontrivial initial chamber, the Prekopa
mechanism is real there.  If \(\mathfrak P>0\) immediately, this entire
log-concave-product route is falsified and the mixed seam must be attacked
without it.

## 7. The seam falsifies the Prekopa route immediately

Modular completion writes

\[
 \Phi(u)=e^{u/2}f(u),
\]

with \(f\) even.  Hence

\[
 V(u)=-\frac u2-\log f(u),
\]

so

\[
 V'(0)=-\frac12,\qquad V'''(0)=0,\qquad Q(0)=\frac12.
                                                               \tag{14}
\]

The proved seam curvature theorem gives

\[
 v_4:=V''''(0)>0.
\]

Evenness supplies the expansions

\[
 V'''(u)=v_4u+O(u^3),
\qquad
 V''''(u)=v_4+O(u^2),
\qquad
 Q(u)=\frac12+O(u^3).                                  \tag{15}
\]

Substitution in (13) gives

\[
 \boxed{
 \mathfrak P(u)
 =\frac32v_4u^3+O(u^5)>0
 \qquad(0<u\ll1).
 }                                                       \tag{16}
\]

Therefore

\[
 (u\partial_u)^2\log(Q/u)>0
\]

immediately to the right of the modular seam.  The source-stiffening density
is locally log-convex, not log-concave.

This falsifies the proposed bounded Prekopa mechanism at its smallest
possible locus.  There is no initial log-concave chamber to enlarge, and the
endpoint must not be moved to manufacture one.

## 8. Surviving meaning

The failure is informative.  Both the modular seam and the far primitive
tail orient \(\omega\) toward log-convexity.  Thus the theta product kernel is
not governed by ordinary concentration of its divided differences.
The relevant structure, if present, must use one of:

1. reverse total positivity or a log-convex likelihood-ratio order;
2. cancellation between the bounded--bounded and bounded--far blocks;
3. the exact adjacent product-size-bias gate without a Prekopa surrogate.

The strongest next direction is the second.  The cross block
\(\kappa_{\mathrm{bf}}\) is no longer a nuisance left by a failed proof: it is
the only available source channel capable of converting local log-convex
expansion into the bounded cubic contraction.  In physical language, the
modular seam must repair the orientation that ordinary convexity gives in
the wrong direction.
