# BPS-wall separation-modulus fiber: WP758

## Question

Does BPS saturation repair WP757 by fixing the domain-wall profile strongly
enough to select the asymmetric portal magnitude?

## Claim boundary

Grant the most favorable case: a single source superpotential produces a BPS
kink and fixes the relevant flavor zero-mode exponent to one. The normalized
profile on the covering line is then

\[
\frac{|f(y)|^2}{k}
=\frac{1}{2}\operatorname{sech}^2(k(y-y_0)),
\]

where \(k\) is the inverse wall width and \(y_0\) is the wall position. BPS
saturation and quantum corrections to supersymmetric wall sectors are treated
in [Shizuya](https://arxiv.org/abs/hep-th/0405073).

This grant is stronger than generic flavor constructions. Supersymmetry fixes
the Yukawa relation for fields in the wall multiplet; an independent spectator
flavor hypermultiplet can retain its own wall coupling. The result below asks
whether even the stronger identification is sufficient.

## Exact residual fiber

Let a readout boundary lie a distance \(d\) from the wall and define

\[
a=kd>0.
\]

The dimensionless density contrast between the wall center and that boundary
is

\[
\Delta(a)
=\frac{1}{2}\left(1-\operatorname{sech}^2 a\right)
=\frac{1}{2}\tanh^2 a.
\]

The BPS charge, wall tension relation, and unit local profile exponent are the
same for every translated wall. Nevertheless,

\[
a_1=\operatorname{arctanh}\frac{1}{2},
\qquad
a_2=\operatorname{arctanh}\frac{3}{4}
\]

give

\[
\Delta(a_1)=\frac18,
\qquad
\Delta(a_2)=\frac{9}{32}.
\]

Indeed every \(0<\Delta<1/2\) is obtained from

\[
a=\operatorname{arctanh}\sqrt{2\Delta}.
\]

Thus BPS normalization can remove a local shape coefficient while leaving the
global wall–boundary separation continuous. On a compact interval this is the
translation/radion or boundary-position modulus unless the same source action
stabilizes it. Reversing the wall orientation still reverses the labelled
contrast.

## Disposition

BPS structure is a local profile normalizer and conditional localization
rigidifier, not a global numerical selector. The failure is not an arbitrary
counterterm: two configurations in the same BPS sector and with the same local
shape have different physical boundary overlaps.

The successor must contain a source-derived stabilization equation with a
unique dimensionless separation \(kd\), a fixed labelled orientation, and no
independent spectator Yukawa ratio. Its prediction must then survive
supersymmetry breaking, Kaluza–Klein and wall thresholds, RG transport,
`physical16` descent, and a calibrated experimental channel.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp758_bps_wall_separation_modulus_fiber.py

Generated result:
research/flavor/results/wp758_bps_wall_separation_modulus_fiber.json
