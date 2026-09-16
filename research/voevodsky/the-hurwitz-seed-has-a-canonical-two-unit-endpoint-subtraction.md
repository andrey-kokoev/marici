# The Hurwitz seed has a canonical two-unit endpoint subtraction

## Question

Can the pole of the radial Mellin seed be removed in a source-natural way while retaining the information needed for Fourier reciprocity?

## Claim boundary

Yes. The symmetric Hurwitz seed has residue two at \(s=1\), independent of the rational shift. Subtracting this universal polar term produces an entire finite-part seed, while the removed coefficient is retained as a separate endpoint port. This establishes distributional completion, not Hilbert or Green-graph membership.

## Polar calculation

For \(0<a<1\), the radial seed is

$$
v_a(s)=\zeta(s,a)+\zeta(s,1-a).
$$

Each Hurwitz zeta function has one simple pole at \(s=1\) with residue one. Therefore

$$
\operatorname*{Res}_{s=1}v_a(s)=2,
$$

independently of \(a\).

Define the finite-part seed

$$
v_a^{\rm fp}(s)
=
v_a(s)-\frac{2}{s-1}.
$$

Since Hurwitz zeta has no other poles, \(v_a^{\rm fp}\) is entire.

## Endpoint port

The subtraction is not a deletion. Record

$$
e_a=2
$$

as the endpoint-residue coordinate and use the completed pair

$$
\widetilde v_a=(v_a^{\rm fp},e_a).
$$

The endpoint coordinate is shift-independent because it comes from the zero-frequency term in Poisson summation, not from the displaced finite support. This is precisely the type of scalar endpoint datum that must remain separate from the radial bulk section.

## Reflection

Replacing \(a\) by \(1-a\) leaves both components invariant:

$$
v_{1-a}^{\rm fp}=v_a^{\rm fp},
\qquad
e_{1-a}=e_a.
$$

Thus the Fourier-square reflection is compatible with the completed seed. The quarter-turn functional equation still exchanges this support seed with the periodic-character section and transports the endpoint atom separately.

## Distributional rung

On every compact vertical strip, standard Hurwitz-zeta estimates give finite-order growth for \(v_a^{\rm fp}\). Hence it defines a continuous functional on the corresponding rapid Mellin test space and belongs to its strong dual. The completion therefore lands in a legitimate rigged distributional target.

This does not show

$$
\widetilde v_a\in\mathcal H_{{\rm rel}}^2
$$

or supply a finite Hilbert norm: entire finite-order vertical growth is weaker than weighted second-order radial Sobolev membership.

## Disposition

The support-port seed now has a canonical completed distributional form: an entire symmetric Hurwitz finite part plus a separately retained residue-two endpoint coordinate. The next interface gate is Green-graph regularity or, failing that, an explicit declaration that the G4 seed lives on the strong-dual rung.