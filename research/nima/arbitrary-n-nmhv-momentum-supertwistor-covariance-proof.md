# Arbitrary-n NMHV momentum-supertwistor covariance

## Theorem

For every `n>=6`, the standard NMHV BCFW sum

$$
\mathcal A_n^{\rm NMHV}
=
\sum_{2\le i\le n-2\atop i+2\le j\le n-1}
[n,i-1,i,j-1,j]
$$

is independently projective in every external momentum supertwistor, invariant under `SL(4)` acting on bosonic twistors, has the expected canceling `GL(4)` determinant weight, and inherits total antisymmetry of each five-bracket.

## Five-bracket formula

For five momentum supertwistors `mathcal Z_a=(Z_a,eta_a)`, define

$$
[a,b,c,d,e]
=
\frac{\delta^{0|4}(Q_{abcde})}
{\langle abcd\rangle
 \langle bcde\rangle
 \langle cdea\rangle
 \langle deab\rangle
 \langle eabc\rangle},
$$

where

$$
Q_{abcde}
=
\eta_a\langle bcde\rangle+
\eta_b\langle cdea\rangle+
\eta_c\langle deab\rangle+
\eta_d\langle eabc\rangle+
\eta_e\langle abcd\rangle.
$$

## Independent projectivity

Rescale one complete supertwistor by

$$
\mathcal Z_a\longmapsto t_a\mathcal Z_a.
$$

The four denominator brackets containing `a` each acquire one factor `t_a`; the unique denominator bracket omitting `a` is unchanged. Thus the denominator has weight `t_a^4`.

Every term in `Q_abcde` has weight `t_a`: the `eta_a` term acquires `t_a` through `eta_a`, while each other term acquires `t_a` through its bosonic four-bracket. Since a fermionic delta of degree four scales as

$$
\delta^{0|4}(t_aQ)=t_a^4\delta^{0|4}(Q),
$$

the numerator and denominator weights cancel. Therefore each five-bracket has weight zero in each of its five labels. Labels absent from the bracket act trivially. Every summand, and hence the complete amplitude, is independently projective in all `n` external supertwistors.

## Linear covariance

For `g in GL(4)`, every bosonic four-bracket transforms by

$$
\langle gabcd\rangle
=\det(g)\langle abcd\rangle.
$$

The denominator therefore has weight `det(g)^5`. The argument `Q` has weight `det(g)`, so its fermionic delta has weight `det(g)^4`. Thus the bosonic formula has net `GL(4)` determinant weight `det(g)^(-1)` under this convention. For `g in SL(4)`, the determinant is one and the five-bracket is invariant. If the standard projective measure or supertwistor density is included, its compensating determinant character restores the declared `GL(4)` scalar convention.

This calculation is termwise and independent of `n`.

## Antisymmetry

An adjacent exchange of two labels reverses every bosonic determinant containing both and permutes the five denominator factors. Tracking the alternating determinant signs and the degree-four fermionic numerator gives one net minus sign. Hence

$$
[\sigma(a),\sigma(b),\sigma(c),\sigma(d),\sigma(e)]
=\operatorname{sgn}(\sigma)[a,b,c,d,e]
$$

for every permutation `sigma` of the five labels.

The ordered BCFW sum therefore carries the orientations assigned to its cells. This is the same antisymmetry used by the arbitrary-n facet cancellation theorem.

## Consequence

The finite covariance checks are promoted to arbitrary multiplicity because no identity between different BCFW terms is needed: every term separately has the stated covariance. The number of terms affects only the finite sum, not the transformation law.

## Claim boundary

This theorem does not prove cyclic or reflection invariance of the complete BCFW representation, because those symmetries relate different sets of five-bracket cells and require triangulation independence or six-term identities. It also does not assert Yangian invariance beyond the stated momentum-supertwistor covariance.
