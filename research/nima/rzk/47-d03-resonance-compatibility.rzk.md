# D03 two-annihilator resonance packet

This module retains the chain-level compatibility between the two reported
annihilating primitives.  It deliberately does not replace the packet by the
cyclic quotient module with annihilator `(u03, mu)`.

```rzk
#lang rzk-1

#define NimaD03ResonanceMonomial : U
  := Sigma (_ : MariciNat), Sigma (_ : MariciNat),
     Sigma (_ : MariciNat), Sigma (_ : MariciNat),
     Sigma (_ : MariciNat), Sigma (_ : MariciNat),
     Sigma (_ : MariciNat), MariciNat

#data NimaD03ResonanceState
  := nima-d03-resonance-omega
  | nima-d03-resonance-Wu
  | nima-d03-resonance-Wmu

#define NimaD03ResonanceBasis : U
  := Sigma (_ : NimaD03ResonanceState), NimaD03ResonanceMonomial
#define NimaD03Resonance : U := NimaZSum NimaD03ResonanceBasis

#define nima-d03-mul-u03 (m : NimaD03ResonanceMonomial)
  : NimaD03ResonanceMonomial
  := let (a,(b,(c,(d,(e,(f,(g,h))))))) := m in
     (a,(b,(c,(d,(e,(marici-succ f,(g,h)))))))

#define nima-d03-mul-mu (m : NimaD03ResonanceMonomial)
  : NimaD03ResonanceMonomial
  := let (a,(b,(c,(d,(e,(f,(g,h))))))) := m in
     (a,(b,(c,(marici-succ d,(marici-succ e,
       (f,(marici-succ g,marici-succ h)))))))

#define nima-d03-resonance-column : NimaD03ResonanceBasis -> NimaD03Resonance
  := \ (q,m) -> match q
       (nima-d03-resonance-omega => nima-sum-zero NimaD03ResonanceBasis
       | nima-d03-resonance-Wu => nima-sum-atom NimaD03ResonanceBasis
          (nima-d03-resonance-omega,nima-d03-mul-u03 m)
       | nima-d03-resonance-Wmu => nima-sum-atom NimaD03ResonanceBasis
          (nima-d03-resonance-omega,nima-d03-mul-mu m))

#define nima-d03-resonance-d : NimaD03Resonance -> NimaD03Resonance
  := nima-sum-bind NimaD03ResonanceBasis NimaD03ResonanceBasis
       nima-d03-resonance-column

#define nima-d03-resonance-column-square : (v : NimaD03ResonanceBasis) ->
  nima-sum-equal NimaD03ResonanceBasis
    (nima-d03-resonance-d (nima-d03-resonance-column v))
    (nima-sum-zero NimaD03ResonanceBasis)
  := \ (q,m) -> (match q into (\ k -> (m' : NimaD03ResonanceMonomial) ->
       nima-sum-equal NimaD03ResonanceBasis
         (nima-d03-resonance-d (nima-d03-resonance-column (k,m')))
         (nima-sum-zero NimaD03ResonanceBasis)) (
    nima-d03-resonance-omega => \ m' probe -> refl
  | nima-d03-resonance-Wu => \ m' probe -> refl
  | nima-d03-resonance-Wmu => \ m' probe -> refl
  )) m

#define nima-d03-resonance-square (p : NimaD03Resonance)
  : nima-sum-equal NimaD03ResonanceBasis
      (nima-d03-resonance-d (nima-d03-resonance-d p))
      (nima-sum-zero NimaD03ResonanceBasis)
  := nima-sum-column-square NimaD03ResonanceBasis
       nima-d03-resonance-column nima-d03-resonance-column-square p

#define nima-d03-zero-monomial : NimaD03ResonanceMonomial
  := (marici-zero,(marici-zero,(marici-zero,(marici-zero,
       (marici-zero,(marici-zero,(marici-zero,marici-zero)))))))
#define nima-d03-u03-monomial : NimaD03ResonanceMonomial
  := nima-d03-mul-u03 nima-d03-zero-monomial
#define nima-d03-mu-monomial : NimaD03ResonanceMonomial
  := nima-d03-mul-mu nima-d03-zero-monomial

#define nima-d03-theta : NimaD03Resonance
  := nima-sum-add NimaD03ResonanceBasis
       (nima-sum-atom NimaD03ResonanceBasis
         (nima-d03-resonance-Wmu,nima-d03-u03-monomial))
       (nima-sum-neg NimaD03ResonanceBasis
         (nima-sum-atom NimaD03ResonanceBasis
           (nima-d03-resonance-Wu,nima-d03-mu-monomial)))

#define nima-d03-theta-cycle
  : nima-sum-equal NimaD03ResonanceBasis
      (nima-d03-resonance-d nima-d03-theta)
      (nima-sum-zero NimaD03ResonanceBasis)
  := nima-sum-add-inverse NimaD03ResonanceBasis
       (nima-d03-resonance-column
         (nima-d03-resonance-Wmu,nima-d03-u03-monomial))

#define nima-d03-theta-probe : NimaD03ResonanceBasis -> MariciInt
  := \ (q,m) -> match q
       (nima-d03-resonance-omega => marici-int-zero
       | nima-d03-resonance-Wu => marici-int-zero
       | nima-d03-resonance-Wmu => marici-int-one)

#define nima-d03-column-theta-probe-zero : (v : NimaD03ResonanceBasis) ->
  nima-sum-eval NimaD03ResonanceBasis nima-d03-theta-probe
    (nima-d03-resonance-column v) = marici-int-zero
  := \ (q,m) -> (match q into (\ k -> (m' : NimaD03ResonanceMonomial) ->
       nima-sum-eval NimaD03ResonanceBasis nima-d03-theta-probe
         (nima-d03-resonance-column (k,m')) = marici-int-zero) (
    nima-d03-resonance-omega => \ m' -> refl
  | nima-d03-resonance-Wu => \ m' -> refl
  | nima-d03-resonance-Wmu => \ m' -> refl
  )) m

#define nima-d03-boundary-theta-probe-zero (p : NimaD03Resonance)
  : nima-sum-eval NimaD03ResonanceBasis nima-d03-theta-probe
      (nima-d03-resonance-d p) = marici-int-zero
  := nima-frame-concat MariciInt
       (nima-sum-eval NimaD03ResonanceBasis nima-d03-theta-probe
         (nima-d03-resonance-d p))
       (nima-sum-eval NimaD03ResonanceBasis
         (\ v -> nima-sum-eval NimaD03ResonanceBasis nima-d03-theta-probe
           (nima-d03-resonance-column v)) p)
       marici-int-zero
       (nima-sum-eval-bind NimaD03ResonanceBasis NimaD03ResonanceBasis
         nima-d03-resonance-column nima-d03-theta-probe p)
       (nima-any-eval-zero-atoms NimaD03ResonanceBasis
         (\ v -> nima-sum-eval NimaD03ResonanceBasis nima-d03-theta-probe
           (nima-d03-resonance-column v))
         nima-d03-column-theta-probe-zero p)

#define nima-d03-theta-primitive-value
  : nima-sum-eval NimaD03ResonanceBasis nima-d03-theta-probe nima-d03-theta
      = marici-int-one
  := refl

#define nima-d03-theta-not-boundary
  (p : NimaD03Resonance)
  (boundary : nima-sum-equal NimaD03ResonanceBasis
    (nima-d03-resonance-d p) nima-d03-theta)
  : marici-int-zero = marici-int-one
  := nima-frame-concat MariciInt marici-int-zero
       (nima-sum-eval NimaD03ResonanceBasis nima-d03-theta-probe
         (nima-d03-resonance-d p)) marici-int-one
       (nima-frame-rev MariciInt
         (nima-sum-eval NimaD03ResonanceBasis nima-d03-theta-probe
           (nima-d03-resonance-d p)) marici-int-zero
         (nima-d03-boundary-theta-probe-zero p))
       (boundary nima-d03-theta-probe)
```
