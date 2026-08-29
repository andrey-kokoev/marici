# The Primitive and Square Currents Are the det3 Anomaly Coordinates

## The common-factor hostile is answered by a differential source law

Chart transitions and axial normalization do not select a divisor-bearing
section. A relative perturbation determinant carries stronger data. For a
trace-class resolvent difference its logarithmic derivative is fixed by the
source operator pair:

$$
\frac{d}{d\zeta}\log\Delta(\zeta)
=-\operatorname{Tr}\left((A-\zeta)^{-1}-(A_0-\zeta)^{-1}\right),
$$

up to the sign convention used for the determinant.

If another section is $h\Delta$ and obeys the same identity, then

$$
\frac{h'}h=0
$$

away from its zeros. Analytic continuation makes $h$ constant, and one source
normalization fixes that constant. A divisor-bearing common factor cannot
preserve the resolvent-trace law. It would require a different operator pair.

This is section authority rather than transition authority.

## The three-level arithmetic filtration selects det3

The existing theta/Tate completion separates connected prime-power depth into

$$
k=1,\qquad k=2,\qquad k\ge3.
$$

This is exactly the algebra of a third-order regularized determinant. For
$K$ in the Schatten class $\mathcal S_3$,

$$
\log\det_3(I+K)
=\sum_{k\ge3}\frac{(-1)^{k+1}}k\operatorname{Tr}(K^k)
$$

whenever the expansion converges, followed by analytic continuation. The
discarded first two logarithmic terms are

$$
\operatorname{Tr}K,
\qquad
-\frac12\operatorname{Tr}(K^2).
$$

They are not errors to erase. They are precisely the primitive and square
boundary currents already forced by the source analysis. Formally,

$$
\det(I+K)
=\exp\left(\operatorname{Tr}K-rac12\operatorname{Tr}(K^2)\right)
\det_3(I+K).
$$

Thus the full determinant object has the exact typed form

$$
(J_1,J_2,\det_3),
$$

where $J_1$ and $J_2$ retain the two anomaly coordinates and the connected
$k\ge3$ tail supplies the ordinary regularized determinant.

This explains why deleting the primitive and square currents repeatedly
destroyed completion faithfulness: doing so forgets the data needed to lift a
regularized determinant back to the source-normalized section.

## Consequences

The common-factor ambiguity is narrowed sharply. A factor such as
$1+\varepsilon e^{\zeta^2}$ may preserve a chart ratio and axial asymptotics,
but it changes the logarithmic derivative and hence the resolvent-trace
defect. It is rejected before its zeros are inspected unless it comes from a
change of the source operator pair.

Regularization still permits an exponential polynomial anomaly of degree at
most two if the first two trace coordinates are omitted. Retaining $J_1$ and
$J_2$ fixes that anomaly. Such exponential factors are nowhere zero in any
case, so the divisor is already fixed by $\det_3$; the first two currents fix
the actual section and its normalization.

## Remaining construction gate

This is an architectural theorem, not yet an RH operator. The programme must
construct from theta/Tate data an analytic family $K(\zeta)$ satisfying:

1. $K(\zeta)\in\mathcal S_3$ in each resolvent chart;
2. the primitive and square source currents equal the renormalized first and
   second trace coordinates of $K$;
3. reciprocal sewing transports all three components coherently;
4. the resulting source-normalized determinant section equals framed Xi;
5. the operator pair is self-adjoint and fixed before the section is read;
6. the determinant has no inherited uncoupled modes or transition zeros;
7. the finite spectral compressions converge in a topology strong enough to
   pass the regularized determinant and both anomaly currents.

The decisive new candidate is therefore not an arbitrary determinant line.
It is a source-derived third-order perturbation determinant equipped with its
first two trace anomalies as explicit boundary coordinates.

This is the first construction in the current lane that simultaneously
explains the three arithmetic completion grades and rejects the common-divisor
hostile by an operator identity rather than by growth fitting.
