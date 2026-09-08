# Reduced seven-state cellular Q complex

The six exponent coordinates are ordered
`(X03,X14,X25,u03,u14,u25)`. All are natural: no long occurrence or normal is
inverted.

```rzk
#lang rzk-1

#data NimaQCellState
  := nima-q-cell-T
  | nima-q-cell-h03
  | nima-q-cell-h14
  | nima-q-cell-h25
  | nima-q-cell-p03
  | nima-q-cell-p14
  | nima-q-cell-p25

#define NimaQLongMonomial6 : U
  := Sigma (_ : MariciNat), Sigma (_ : MariciNat), Sigma (_ : MariciNat),
     Sigma (_ : MariciNat), Sigma (_ : MariciNat), MariciNat
#define NimaQCellBasis : U := Sigma (_ : NimaQCellState), NimaQLongMonomial6
#define NimaQCell : U := NimaZSum NimaQCellBasis

#define nima-q-shift-X03 : NimaQLongMonomial6 -> NimaQLongMonomial6
  := \ (x03,(x14,(x25,(u03,(u14,u25))))) ->
       (marici-succ x03,(x14,(x25,(u03,(u14,u25)))))
#define nima-q-shift-X14 : NimaQLongMonomial6 -> NimaQLongMonomial6
  := \ (x03,(x14,(x25,(u03,(u14,u25))))) ->
       (x03,(marici-succ x14,(x25,(u03,(u14,u25)))))
#define nima-q-shift-X25 : NimaQLongMonomial6 -> NimaQLongMonomial6
  := \ (x03,(x14,(x25,(u03,(u14,u25))))) ->
       (x03,(x14,(marici-succ x25,(u03,(u14,u25)))))
#define nima-q-shift-u03 : NimaQLongMonomial6 -> NimaQLongMonomial6
  := \ (x03,(x14,(x25,(u03,(u14,u25))))) ->
       (x03,(x14,(x25,(marici-succ u03,(u14,u25)))))
#define nima-q-shift-u14 : NimaQLongMonomial6 -> NimaQLongMonomial6
  := \ (x03,(x14,(x25,(u03,(u14,u25))))) ->
       (x03,(x14,(x25,(u03,(marici-succ u14,u25)))))
#define nima-q-shift-u25 : NimaQLongMonomial6 -> NimaQLongMonomial6
  := \ (x03,(x14,(x25,(u03,(u14,u25))))) ->
       (x03,(x14,(x25,(u03,(u14,marici-succ u25)))))

#define nima-q-cell-column : NimaQCellBasis -> NimaQCell
  := \ (q,m) -> (match q into (\ _ -> NimaQLongMonomial6 -> NimaQCell) (
    nima-q-cell-T => \ n -> nima-sum-add NimaQCellBasis
       (nima-sum-atom NimaQCellBasis (nima-q-cell-p03,nima-q-shift-X03 n))
       (nima-sum-add NimaQCellBasis
         (nima-sum-atom NimaQCellBasis (nima-q-cell-p14,nima-q-shift-X14 n))
         (nima-sum-add NimaQCellBasis
           (nima-sum-atom NimaQCellBasis (nima-q-cell-p25,nima-q-shift-X25 n))
           (nima-sum-zero NimaQCellBasis)))
  | nima-q-cell-h03 => \ n -> nima-sum-add NimaQCellBasis
       (nima-sum-atom NimaQCellBasis (nima-q-cell-p03,nima-q-shift-u03 n))
       (nima-sum-zero NimaQCellBasis)
  | nima-q-cell-h14 => \ n -> nima-sum-add NimaQCellBasis
       (nima-sum-atom NimaQCellBasis (nima-q-cell-p14,nima-q-shift-u14 n))
       (nima-sum-zero NimaQCellBasis)
  | nima-q-cell-h25 => \ n -> nima-sum-add NimaQCellBasis
       (nima-sum-atom NimaQCellBasis (nima-q-cell-p25,nima-q-shift-u25 n))
       (nima-sum-zero NimaQCellBasis)
  | nima-q-cell-p03 => \ n -> nima-sum-zero NimaQCellBasis
  | nima-q-cell-p14 => \ n -> nima-sum-zero NimaQCellBasis
  | nima-q-cell-p25 => \ n -> nima-sum-zero NimaQCellBasis
  )) m

#define nima-q-cell-d : NimaQCell -> NimaQCell
  := nima-sum-bind NimaQCellBasis NimaQCellBasis nima-q-cell-column

#define nima-q-cell-column-square : (v : NimaQCellBasis) ->
  nima-sum-equal NimaQCellBasis
    (nima-q-cell-d (nima-q-cell-column v))
    (nima-sum-zero NimaQCellBasis)
  := \ (q,m) -> (match q into (\ k -> (m' : NimaQLongMonomial6) ->
       nima-sum-equal NimaQCellBasis
         (nima-q-cell-d (nima-q-cell-column (k,m')))
         (nima-sum-zero NimaQCellBasis)) (
    nima-q-cell-T => \ n probe -> refl
  | nima-q-cell-h03 => \ n probe -> refl
  | nima-q-cell-h14 => \ n probe -> refl
  | nima-q-cell-h25 => \ n probe -> refl
  | nima-q-cell-p03 => \ n probe -> refl
  | nima-q-cell-p14 => \ n probe -> refl
  | nima-q-cell-p25 => \ n probe -> refl
  )) m

#define nima-q-cell-square (p : NimaQCell)
  : nima-sum-equal NimaQCellBasis
      (nima-q-cell-d (nima-q-cell-d p))
      (nima-sum-zero NimaQCellBasis)
  := nima-sum-column-square NimaQCellBasis nima-q-cell-column
       nima-q-cell-column-square p
```
