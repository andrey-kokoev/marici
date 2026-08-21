# Five independent certificates for a paired physical Mackey object

## The certificate stack

The completed coefficient analysis separates five certificates that must not
be inferred from one another:

1. **Contravariant selector descent.** For `q:G->G/K`, a frozen selector `c`
   is a pullback from the quotient exactly when `K subset Stab_R(c)`, or
   equivalently `K subset K_c` for normal `K`.
2. **Power--Mackey compatibility.** Once `K` is fixed, the basis-level
   power correspondence commutes exactly for `n in U(K)`, controlled by
   `R(K)=rad(exp(K)exp(A_K))`.
3. **Covariant transfer normalization.** Unnormalized fiber-sum preserves
   `delta_0` and has norm `|K|`; averaging splits pullback but rescales
   selection. No equivariant weighted left inverse does both.
4. **Automorphism naturality.** A section can preserve selection and split
   pullback only by choosing lifts. Sections form a derivation torsor and may
   have no automorphism-invariant point, even for split extensions.
5. **Betti realization.** A physical paired object additionally needs a
   source-derived relative-chain pushforward, boundary covariance,
   orientation/multiplicity normalization, and an exact pairing square.

The first four certificates are now classified algebraically. The fifth is
not available for the five-site branch quotient.

## Independence controls

- Five-site `delta_0` fails certificate 1 for every nontrivial kernel even
  though odd indices can pass certificate 2 algebraically.
- `A4->C3` with its quotient selector passes certificate 1 but fails
  certificate 2 at `n=3`; degree localization cannot repair it.
- `C4->C2` averaging is equivariant and split but fails frozen selection,
  while a section transfer repairs selection by giving up certificate 4.
- `C2 x C2->C2` is split, yet its section torsor has no natural point, so
  abstract splitting does not imply certificate 4.
- The formal five-site coefficient system supplies none of the missing
  relative-chain data in certificate 5.

## Proposed paired object

The algebraic coefficient half is the resonance-enriched surjection category
with bidegree

`(|ker q|, R_G(ker q))`,

selector object cost `R(K_c)`, unnormalized covariant fiber-sum, and
contravariant pullback. A physical paired Mackey object is an extension of
this structure by certificate 5, not a consequence of it.

## Falsifier

The separation would be falsified by a canonical source-derived five-site
relative-chain map that simultaneously supplies boundary covariance,
orientation/multiplicity normalization, strict composition, and the exact
coefficient--Betti pairing while requiring none of the missing lift data.
No such map is currently present.
