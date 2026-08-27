# Authority audit for the affine-discriminant orbit constructor

## Associated theorem

The constructor

\[
\mathcal A_F(O)
=\operatorname{coker}(F)\otimes\widetilde{\mathbb Z}[O]
\]

is exact as an associated integral object.  It produces

\[
\operatorname{coker}(F)\cong\mathbb Z/7
\]

and embeds its reduced free-orbit packet as

\[
\{(x,-x):x\in\mathbb Z/7\}.
\]

At every exceptional even grade, the primitive vector \(w_g=v_g/7\)
canonically identifies the affine discriminant with the ray-content quotient.

## Ordinary physical comparison is impossible

The completed physical carrier is a characteristic-zero vector space and is
therefore torsion-free as an additive group.  Every additive map

\[
\phi:\mathbb Z/7\to V
\]

must vanish, because

\[
7\phi(1)=\phi(7)=0
\]

and multiplication by seven is injective on \(V\).

Therefore the missing comparison cannot be an ordinary additive inclusion of
the discriminant object into the completed physical carrier.  Any such claim
is false before dynamics or positivity are considered.

## Canonical dual comparison

The affine frame does supply a canonical finite duality.  For

\[
D_F=\operatorname{coker}F,
\qquad
D_{F^T}=\operatorname{coker}F^T,
\]

define

\[
\lambda_F([x],[y])
=y^TF^{-1}x\pmod{\mathbb Z}.
\]

This is well defined and perfect:

\[
\lambda_F:D_F\times D_{F^T}\to\mathbb Q/\mathbb Z.
\]

Exponentiation gives a canonical phase-valued pairing

\[
\exp(2\pi i\lambda_F):D_F\times D_{F^T}\to U(1).
\]

For the present frame, a generator pair has value \(3/7\), hence a primitive
seventh-root phase.  This realizes seven distinguishable characters without
embedding torsion into a characteristic-zero additive carrier.

## Smallest missing constructor

The remaining physical constructor is not a state inclusion.  It is a
phase-sensitive observation correspondence:

```text
DiscriminantPhasePort
  affine_discriminant D_F
  dual_discriminant D_FT
  reduced_reflection_orbit
  perfect_linking_pairing
  physical_phase_record
  executable_domain
  source_authority
```

The source already supplies the first four fields mathematically.  It does not
yet supply a physical phase record or an executable instrument coupling that
record to the magnetic completed carrier.

An alternative repair would be a source-derived integral physical lattice
whose reduction modulo seven is nonzero and reflection-equivariant.  No such
lattice comparison is presently established.

## Verdict

The objective is resolved at associated combinatorial strength: the oriented
affine-discriminant orbit constructor is the unique minimal combined object
identified so far.  Promotion to a physical or executable source constructor
is blocked by a proved torsion-free no-go.  The narrow missing arrow is either:

- a discriminant phase port based on the canonical linking pairing; or
- a reflection-equivariant mod-seven physical lattice.

Neither may be inferred from equal cardinalities or from the existence of the
completed complex carrier.
