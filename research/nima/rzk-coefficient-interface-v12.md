# v12: full loaded differential squares and finite-to-Cech chain law

**Superseded endpoint status:** see
[`rzk-coefficient-interface-v13.md`](rzk-coefficient-interface-v13.md). A
literal 199-state endpoint-relative complex, its square-zero theorem, and the
215-to-199 chain projection now pass fresh headless closure checks.

The concrete 215-state coefficient foundation has crossed its two previously
blocked matrix gates. This checkpoint does not identify the setoid presentation
with an identity quotient and does not claim derived-Hom realization.

## Checked results

- `rzk/20-loaded-coefficient-square.rzk.md` now contains all 215 finite and all
  215 Cech generator proofs, plus the two extension theorems for arbitrary
  finite integral coefficient expressions.
- Both actual loaded differentials square to zero in the evaluation setoid.
  The proof covers all 522 signed arrows and every legal Laurent monomial.
- `rzk/21-loaded-finite-cech-chain.rzk.md` proves on all 215 generators, then
  on every finite coefficient expression, that

      Lambda (d_fin p) = d_Cech (Lambda p).

- No global normal localization was introduced. A new definitional operation
  for the Laurent predecessor represents n-1 when a radial arrow first opens a
  Cech normal coordinate. It is definitionally compatible with normal-removal
  followed by Lambdath Cech comparison, avoiding an artificial integer
  normalization proof.

Fresh headless transitive closure checks passed:

- `results/20-loaded-coefficient-square.typecheck.json` (795.73 s)
- `results/21-loaded-finite-cech-chain.typecheck.json` (846.14 s)

The Rzk LSP was deliberately not used for these generated modules: the former
monolithic 4.28 MB term crashed the Pi process. Removing the redundant expanded
syntax trees reduced module 20 to about 2.07 MB; both large certificates were
checked by bounded headless processes instead.

## What “concrete foundation” now means

Established:

1. full finite and legal Cech carriers;
2. actual 215 cell constructors and 522 arrows;
3. finite integral additive/setoid laws and integer scalar laws;
4. typed polynomial action operations;
5. both concrete square-zero laws;
6. the actual diagonal finite-to-Cech chain map;
7. coherent integer cochain indices and degree-sorted carrier types.

Still separate from this foundation:

- packaging the polynomial presentation as a single record of all R0-module
  axioms (the component laws are not yet one identity-based structure);
- an explicit 199-state endpoint quotient and its restriction maps in Rzk;
- quotient/setoid completion or a setoid-native replacement of the existing
  identity-based Hom interface;
- K-projective/derived localization and the physical normalization/Gysin map.

Thus the computational coefficient-complex bottleneck is closed. The next
formal task should not rerun matrix cancellation; it should package the
endpoint-relative setoid complex and bridge that interface to derived Hom.
