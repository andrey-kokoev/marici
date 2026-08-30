# The raw one-sided transform Wronskian is an oscillatory centroid, not a positive norm

## Claim

The one-sided theta-tail transform is a natural candidate outgoing section, but positivity of its forcing does not by itself make the section Hermite–Biehler. The missing condition is an operator-derived positive Wronskian identity.

Let the source convention be

[
E(x)=int_0^infty f(q)e^{-ixq},dq
]

for real (f) with enough decay to differentiate under the integral. Then

[
E'(x)=-iint_0^infty qf(q)e^{-ixq},dq
]

and, wherever (E(x)
eq0),

[
rac{d}{dx}arg E(x)
=
rac{operatorname{Im}(E'(x)overline{E(x)})}{|E(x)|^2}.
]

The numerator is

[
operatorname{Im}(E'(x)overline{E(x)})
=
-rac12
int_0^infty!!int_0^infty
(q+r)f(q)f(r)cos(x(q-r)),dq,dr.
]

Thus the raw phase velocity is an oscillatory cosine centroid. Even when (fge0), it is not manifestly of one sign away from (x=0). Positivity and rapid decay of the theta forcing therefore do not authorize Wronskian positivity.

The opposite outgoing convention (e^{ixq}) reverses the sign. That convention must be fixed by the causal source orientation rather than selected to obtain the desired inequality.

## Consequence for the Hermite–Biehler step

Writing

[
E=A-iB
]

in the convention above gives

[
rac{d}{dx}arg E(x)
=
-rac{W_{A,B}(x)}{|E(x)|^2}.
]

Hence the Wronskian odd port diagnoses the exact missing gate, but does not close it. To prove that (E) is Hermite–Biehler, the programme still needs a source-derived completion in which

[
pm W_{A,B}(x)
=
|Gamma_x|_{mathcal K}^{2}
]

or an equivalent strictly positive Green boundary form, with the sign fixed by the outgoing convention.

This completion may require the endpoint augmentation, wall channel, or closed theta-tail history already present in the constructor system. It cannot be inferred from the scalar transform alone.

## Minimal hostiles

1. A nonnegative rapidly decaying forcing whose cosine centroid changes sign.
2. Two opposite exponential conventions with identical scalar even data and opposite Wronskians.
3. A raw transform with nonnegative Wronskian on a tested interval but no source identity preventing a later sign change.
4. A fitted positive metric that repairs the Wronskian but is not the pullback of the authorized Green system.

## Reduced frontier

The next theorem is not merely a transform estimate. It is an intertwining identity:

[
	ext{completed theta-tail Green energy}
longrightarrow
	ext{boundary Wronskian}
]

whose pullback proves a strict one-sign phase velocity on the full real boundary. Only after that theorem may the one-sided section be called Hermite–Biehler and used to derive the reciprocal inner function and the two extension spectra.
