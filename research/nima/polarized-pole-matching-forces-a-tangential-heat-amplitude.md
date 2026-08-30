# Polarized pole matching forces a tangential heat amplitude

The quarter-heat Gram before amplitude normalization is

[
Q(r,t)
=
rac1{pi(r+t)}
-rac1{12}
+O(r+t).
]

It depends only on the normal variable (r+t). The normalized Euler max
kernel, however, has seam residue

[
P_E(a)
=
rac{1}
{a(1-a)zeta(1+a)zeta(2-a)}
]

at (b=1-a).

Therefore one constant Euler–theta amplitude cannot match the polarized pole.
The amplitude must be a tangential field (c(a)) satisfying

[
rac{c(a)^2}{pi}=P_E(a).
]

Hence the positive pole-matching choice is forced:

[
c(a)
=
sqrt{
rac{pi}
{a(1-a)zeta(1+a)zeta(2-a)}
}.
]

At (a=1/2),

[
c(1/2)=rac{2sqrtpi}{zeta(3/2)},
]

recovering the previously derived central amplitude.

The same forced amplitude transports the quarter-heat Todd coefficient to

[
F_{mathrm{heat}}(a)
=
-rac{c(a)^2}{12}
=
-rac{pi}
{12a(1-a)zeta(1+a)zeta(2-a)}.
]

Thus the finite defect that the remaining source cells must carry is the
explicit symmetric function

[
Delta(a)
=
operatorname{FP}_{a}G_E
+
rac{pi}
{12a(1-a)zeta(1+a)zeta(2-a)}.
]

At the central point,

[
Delta(1/2)
approx0.2419315360.
]

## Categorical consequence

The amplitude is no longer a scalar comparison constant. It is a positive
metric field over the open seam. Therefore the proposed Euler–theta
Beck–Chevalley cell must establish all of the following:

1. (c(a)) is source-derived rather than fitted pointwise;
2. reciprocal reflection satisfies (c(1-a)=c(a));
3. multiplication by (c(a)) is uniformly bi-bounded on every compact open
   seam region;
4. its connection term is included when the seam coordinate moves;
5. the residual finite return is exactly (Delta(a)), not only its central
   value.

The connection warning is essential. A varying amplitude can match every
fiberwise pole while introducing extra transport under tangential
differentiation:

[

abla_a(c(a)g)=c(a)
abla_a g+c'(a)g.
]

Consequently a fiberwise Gram match does not yet define a coherent moving-seam
constructor. The logarithmic derivative

[
rac{c'(a)}{c(a)}
=
-rac12
left[
rac1a-rac1{1-a}
+rac{zeta'(1+a)}{zeta(1+a)}
-rac{zeta'(2-a)}{zeta(2-a)}
ight]
]

is the forced scalar connection correction. It is odd under
(aleftrightarrow1-a), exactly as reciprocal transport requires.

This is the next smallest mixed Adams–seam plaquette datum: pole matching
forces not only an amplitude field but its reciprocal-odd connection.
