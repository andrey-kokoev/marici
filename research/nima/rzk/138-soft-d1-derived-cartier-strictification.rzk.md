# Soft D1 derived Cartier strictification

```rzk
#lang rzk-1
#data NimaSoftD1CarrierReduction
  := nima-odd-exact-image-order-one
  | nima-ordinary-doubled-carrier-reduction-fails
  | nima-reduced-carrier-reduction-descends
#define nima-soft-D1-carrier-reduction : NimaSoftD1CarrierReduction
  := nima-reduced-carrier-reduction-descends
#data NimaSoftD1DerivedReplacement
  := nima-two-term-Cartier-complex-Rmodz-to-R
  | nima-even-and-odd-maps-received
  | nima-no-new-carrier-datum
#define nima-soft-D1-derived-replacement : NimaSoftD1DerivedReplacement
  := nima-two-term-Cartier-complex-Rmodz-to-R
#data NimaSoftD1PrincipalStrictification
  := nima-A2-sector-map-strict
  | nima-source-action-a2f-a2p-minus-hf
  | nima-principal-cell-required
#define nima-soft-D1-principal-strictification : NimaSoftD1PrincipalStrictification
  := nima-A2-sector-map-strict
#data NimaSoftD1StrictificationScope
  := nima-local-derived-chain-map-constructed
  | nima-homotopy-fibre-cohomology-uncomputed
  | nima-global-road-Cech-identification-open
#define nima-soft-D1-strictification-scope : NimaSoftD1StrictificationScope
  := nima-local-derived-chain-map-constructed
```
