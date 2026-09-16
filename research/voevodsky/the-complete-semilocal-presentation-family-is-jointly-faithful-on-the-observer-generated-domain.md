# The complete semilocal presentation family is jointly faithful on the observer-generated domain

## Question

Do the complete semilocal presentations determine a source observer, giving the presentation system a Yoneda-style separation property?

## Claim boundary

Yes on the declared observer-generated domain, because the paired canonical-dual spectral presentation already has the constructed inverse \(C_{31}\). This is joint faithfulness of a concrete presentation family, not the full Yoneda lemma and not faithfulness of scalar Weil readout.

Let \(\mathsf{Obs}_S\) be the admitted source observer domain and

$$
C_{13}:\mathsf{Obs}_S\longrightarrow V_3
$$

its complete paired canonical-dual spectral transform. Prior construction supplies

$$
C_{31}:\operatorname{im}C_{13}\longrightarrow\mathsf{Obs}_S
$$

with

$$
C_{31}C_{13}=\operatorname{id}_{\mathsf{Obs}_S}.
$$

Therefore \(C_{13}\) is injective. If \(f,g\in\mathsf{Obs}_S\) satisfy

$$
C_{1i}f=C_{1i}g
$$

for every complete presentation in the family, then in particular

$$
C_{13}f=C_{13}g.
$$

Applying \(C_{31}\) gives \(f=g\). Hence the family is jointly faithful.

Equivalently, the combined observation map

$$
\mathcal Y(f)=\bigl(C_{12}f,C_{13}f,q_4f\bigr)
$$

is injective on \(\mathsf{Obs}_S\), independently of whether \(C_{12}\) or \(q_4\) is separately faithful.

## Determination of transformations

If two source transformations \(T,T'\) preserve the admitted domain and have identical complete spectral shadows,

$$
C_{13}T=C_{13}T',
$$

then

$$
T=C_{31}C_{13}T=C_{31}C_{13}T'=T'.
$$

Thus compatible complete presentation shadows determine source transformations uniquely. In particular, the reciprocal half-turn is uniquely determined by its canonical-dual swap-reflection shadow.

## Limits

1. This does not prove that \(q_4\) alone is faithful.
2. It does not construct an intrinsic continuous inverse from the fourth presentation and therefore does not close analytic \(C_{41}\).
3. Scalar Weil readout is not faithful and cannot replace the complete paired spectral record.
4. This is not the abstract Yoneda lemma: no representable Hom-functor equivalence has been asserted.

## Disposition

The complete semilocal presentation family separates source observers and source transformations on the observer-generated domain. The result is a concrete Yoneda-style faithfulness theorem, with the paired canonical-dual transform serving as the conservative probe.