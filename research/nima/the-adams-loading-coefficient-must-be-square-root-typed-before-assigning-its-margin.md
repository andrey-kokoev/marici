# The Adams loading coefficient must be square-root typed before assigning its margin

## Correction scope

The previous conditional estimate inserted the Euler half-density (p^{-k/2}) directly as an operator amplitude. The valuation square-current audit shows that this placement is not automatic. A linear half-density staircase and a quadratic Green loading use different coefficient lenses.

At depth (k), the desired linear half-density exponent is

[
rac{k}{2}.
]

If an operator amplitude has exponent (alpha k), then its quadratic energy has exponent

[
2alpha k.
]

Matching the half-density energy therefore forces

[
2alpha k=rac{k}{2},
qquad
alpha=rac14.
]

Thus the source-compatible amplitude candidate is

[
ho_{p^k}=p^{-k/4},
]

not (p^{-k/2}), whenever the Euler half-density belongs to the quadratic Green coefficient.

## Corrected loading estimate

Let

[
K_{p^k}
=
p^{-k/4},
mathsf D(I+mathsf D^*mathsf D)^{-1/2}.
]

Since the unweighted normalized derivative has norm one,

[
|K_{p^k}|=p^{-k/4}.
]

Over all nontrivial prime-power grades,

[
sup_{p,;kge1}|K_{p^k}|
=
2^{-1/4}<1.
]

Hence the corrected norm margin is

[
delta_{mathrm{amp}}
=
1-2^{-1/4}.
]

At the energy level,

[
K_{p^k}^*K_{p^k}
le
p^{-k/2}I
le
2^{-1/2}I,
]

so the corrected energy margin is

[
delta_{mathrm{energy}}
=
1-2^{-1/2}.
]

The earlier value (1-2^{-1/2}) was therefore an energy-level margin mislabeled as an operator-norm margin.

## Two legitimate constructor types

There are two possible source typings:

1. Amplitude-typed half-density: the source explicitly supplies (p^{-k/2}) as a linear operator coefficient. Then the earlier operator norm (p^{-k/2}) is correct, but its squared Green contribution is (p^{-k}).

2. Energy-typed half-density: the source supplies (p^{-k/2}) in the quadratic Green form. Then the linear lift must be (p^{-k/4}), and the corrected margins above apply.

Scalar Euler coefficients do not decide between these cases. The constructor must declare whether the coefficient lives before or after polarization.

## Relation to the square-current hostile

Using (p^{-k/2}) unchanged as both a linear amplitude and a quadratic transport coefficient doubles the intended exponent at depth two and beyond. This is exactly the naive-half-density hostile isolated by the valuation square-current packet.

The correction does not destroy strictness: both (2^{-1/2}) and (2^{-1/4}) are below one. It changes the quantitative margin and, more importantly, prevents mixing additive and quadratic coefficient lenses.

## Tensor unit

For either typing, (p^k=1) still has coefficient one and no strict margin. The tensor unit remains separately typed.

## Result

Before assigning any Adams loading margin, freeze the coefficient level:

[
	ext{linear amplitude}
quad	ext{or}quad
	ext{quadratic Green energy}.
]

If the frozen Euler half-density (p^{-k/2}) is an energy coefficient, the source-authorized operator lift is quarter-density:

[
p^{-k/4}.
]

The immediate source theorem is therefore a polarization diagram showing where the Euler coefficient enters. Until that diagram is supplied, event 10410's strictness conclusion remains valid only qualitatively; its operator-norm constant must not be treated as frozen.
