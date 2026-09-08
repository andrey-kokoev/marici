# v17: constructive augmentation-ideal primitives

**Gap closed:** [`rzk-coefficient-interface-v18.md`](rzk-coefficient-interface-v18.md)
normalizes every arbitrary finite top coefficient into its explicit boundary
part plus its constant integer multiple of tau.

`rzk/28-supported-augmentation-boundaries.rzk.md` introduces a typed positive
`(u,s,t)` monomial presentation. Its constructors record the first factored
variable:

- positive u exponent;
- zero u and positive s exponent;
- zero u,s and positive t exponent.

For every such monomial it constructs an explicit degree-zero primitive using
respectively the alpha, s, or t source column. Structural recursion extends the
construction to arbitrary finite integral sums, negatives, and integer scales.
Rzk proves that applying the actual local differential returns the represented
top cochain in evaluation-setoid equality.

A fresh 72-file headless closure passed in 33.47 seconds. Evidence:
`results/28-supported-augmentation-boundaries.typecheck.json`.

Together with module 27 this proves:

- boundaries have zero constant residue;
- tau has residue one;
- every cochain explicitly presented in the augmentation ideal `(u,s,t)` has a
  constructed boundary.

The formerly remaining normalization step is completed in v18, without
polynomial division.
