# The polarized Euler normal finite part is explicit

Start from the exact meromorphic split

[
egin{aligned}
T(a,b)
={}&
zeta(a+b)
left(rac1{1-a}+rac1{1-b}ight)\
&+zeta(b)zeta(1+a)+zeta(a)zeta(1+b)
+mathcal R(a,b),
end{aligned}
]

where

[
mathcal R(a,b)
=
sum_{nge1}rac{R_b(n)}{n^{1+a}}
+
sum_{nge1}rac{R_a(n)}{n^{1+b}}
]

is locally normally convergent near the open seam.

Freeze a tangential seam coordinate (a_0in(0,1)), put
(b_0=1-a_0), and approach normally by

[
a=a_0+rac u2,
qquad
b=b_0+rac u2.
]

Then

[
zeta(a+b)=rac1u+gamma+O(u)
]

and

[
rac1{1-a}+rac1{1-b}
=
A_0+uA_1+O(u^2),
]

with

[
A_0=rac1{a_0}+rac1{b_0}
=rac1{a_0b_0},
]

[
A_1=
rac12left(rac1{a_0^2}+rac1{b_0^2}ight).
]

Therefore

[
T(a,b)
=
rac{A_0}{u}
+
operatorname{FP}_{a_0}T
+
O(u),
]

where the normal finite part is

[
egin{aligned}
operatorname{FP}_{a_0}T
={}&
rac{gamma}{a_0b_0}
+
rac12left(rac1{a_0^2}+rac1{b_0^2}ight)\
&+zeta(b_0)zeta(1+a_0)
+zeta(a_0)zeta(1+b_0)
+mathcal R(a_0,b_0).
end{aligned}
]

This formula separates four source candidates exactly:

1. the Euler constant multiplying the polar carrier;
2. the normal derivative of the endpoint denominators;
3. the two asymmetric zeta endpoint returns;
4. the convergent discrete remainder.

## Normalized primitive states

For

[
G_E(a,b)
=
rac{T(a,b)}
{zeta(1+a)zeta(1+b)},
]

write

[
D_0=zeta(1+a_0)zeta(1+b_0)
]

and

[
ell_0=
rac12
left[
rac{zeta'(1+a_0)}{zeta(1+a_0)}
+
rac{zeta'(1+b_0)}{zeta(1+b_0)}
ight].
]

Then

[
G_E(a,b)
=
rac{A_0/D_0}{u}
+
operatorname{FP}_{a_0}G_E
+
O(u),
]

with

[
operatorname{FP}_{a_0}G_E
=
rac{
operatorname{FP}_{a_0}T-A_0ell_0
}{D_0}.
]

At (a_0=b_0=1/2), this reduces to the previously computed diagonal
constant

[
rac{C_E}{zeta(3/2)^2}
-
rac{4zeta'(3/2)}{zeta(3/2)^3}.
]

## Constructor consequence

The required finite interface is now a function of the tangential seam
coordinate, not a single number. A source-authorized archimedean or Todd cell
must reproduce

[
a_0longmapstooperatorname{FP}_{a_0}G_E
]

after the polarized quarter-heat finite part is subtracted.

The decomposition also supplies an audit: assigning all of the central
discrepancy to a gamma factor is invalid unless the gamma cell reproduces the
endpoint-derivative and asymmetric tangential dependence, or unless separate
source cells are shown to carry those terms.
