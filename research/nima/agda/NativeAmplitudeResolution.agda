{-# OPTIONS --safe --cubical --guardedness #-}
module NativeAmplitudeResolution where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
import NativeTableRules as Rules
import NativeTableResolution as Resolution

-- Supplied coefficient algebra and supplied, individually marked factors.
-- No division, field theory or physical weight is derived from the table.
module Algebra (A W : Type) (weight : A → W)
  (zero one : W) (add multiply : W → W → W) where
  module N = Rules.Native ℓ-zero
  module G = N.G
  module O = N.O
  module R = N.R
  data Mode : Type where
    sum-mode product-mode : Mode
  operation : Mode → W → W → W
  operation sum-mode = add
  operation product-mode = multiply
  data Expr : Type where
    zero-expr one-expr : Expr
    factor : A → Expr
    binary : Mode → Expr → Expr → Expr
  data Port : Type where
    operator left right : Port
  evaluate : Expr → W
  evaluate zero-expr = zero
  evaluate one-expr = one
  evaluate (factor a) = weight a
  evaluate (binary m l r) = operation m (evaluate l) (evaluate r)

  scalar : W → G.Package
  scalar w = N.pack (G.atom-node W) w
  marked : A → G.Package
  marked a = N.pack (G.retain-node (G.atom-node A) a (G.atom-node W)) (weight a)
  operator-package : Mode → G.Package
  operator-package m = N.pack (G.atom-node Mode) m
  old-scalar : W → O.Complete
  old-scalar w = O.pack (O.atom W) w
  old-marked : A → O.Complete
  old-marked a = O.pack (O.retain (O.atom A) a (O.atom W)) (weight a)
  old-operator : Mode → O.Complete
  old-operator m = O.pack (O.atom Mode) m
  family : Mode → G.Package → G.Package → Port → G.Package
  family m l r operator = operator-package m
  family m l r left = l
  family m l r right = r
  old-family : Mode → O.Complete → O.Complete → Port → O.Complete
  old-family m l r operator = old-operator m
  old-family m l r left = l
  old-family m l r right = r
  package : Expr → G.Package
  package zero-expr = scalar zero
  package one-expr = scalar one
  package (factor a) = marked a
  package (binary m l r) = N.Pi-package Port (family m (package l) (package r))
  old-package : Expr → O.Complete
  old-package zero-expr = old-scalar zero
  old-package one-expr = old-scalar one
  old-package (factor a) = old-marked a
  old-package (binary m l r) = O.Pi-package Port (old-family m (old-package l) (old-package r))

  -- Independent native readout: read the actual operator row and both child
  -- values. It does not decode an old package or use evaluate as its answer.
  readout : (e : Expr) → G.Value (fst (package e)) → W
  readout zero-expr v = v
  readout one-expr v = v
  readout (factor a) v = v
  readout (binary m l r) v = operation (v operator) (readout l (v left)) (readout r (v right))
  old-readout : (e : Expr) → O.El (O.expression (old-package e)) → W
  old-readout zero-expr v = v
  old-readout one-expr v = v
  old-readout (factor a) v = v
  old-readout (binary m l r) v = operation (v operator) (old-readout l (v left)) (old-readout r (v right))
  native-correct : (e : Expr) → readout e (snd (package e)) ≡ evaluate e
  native-correct zero-expr = refl
  native-correct one-expr = refl
  native-correct (factor a) = refl
  native-correct (binary m l r) = cong₂ (operation m) (native-correct l) (native-correct r)
  old-correct : (e : Expr) → old-readout e (O.value (old-package e)) ≡ evaluate e
  old-correct zero-expr = refl
  old-correct one-expr = refl
  old-correct (factor a) = refl
  old-correct (binary m l r) = cong₂ (operation m) (old-correct l) (old-correct r)
  readouts-agree : (e : Expr) → readout e (snd (package e)) ≡ old-readout e (O.value (old-package e))
  readouts-agree e = native-correct e ∙ sym (old-correct e)

  -- Seeds are marked local inputs, algebra constants and operation tokens.
  -- The constructed execution never admits the computed amplitude as a seed.
  data Seeds : G.Package → Type₁ where
    zero-seed : Seeds (scalar zero)
    one-seed : Seeds (scalar one)
    factor-seed : (a : A) → Seeds (marked a)
    operator-seed : (m : Mode) → Seeds (operator-package m)
  module Run = Resolution.Full ℓ-zero Seeds
  native-run : (e : Expr) → Run.Resolve (package e)
  native-run zero-expr = Run.seed zero-seed
  native-run one-expr = Run.seed one-seed
  native-run (factor a) = Run.seed (factor-seed a)
  native-run (binary m l r) = Run.apply (N.P-kind , Port , family m (package l) (package r))
    (λ { (lift operator) → Run.seed (operator-seed m)
       ; (lift left) → native-run l ; (lift right) → native-run r })
  old-run : (e : Expr) → R.Resolve Run.OldSeeds (old-package e)
  old-run zero-expr = R.seed zero-seed
  old-run one-expr = R.seed one-seed
  old-run (factor a) = R.seed (factor-seed a)
  old-run (binary m l r) = R.apply (R.Pi-rule Port (old-family m (old-package l) (old-package r)))
    (λ { (lift operator) → R.seed (operator-seed m)
       ; (lift left) → old-run l ; (lift right) → old-run r })
  package-commutes : (e : Expr) → G.encode-package (old-package e) ≡ package e
  package-commutes zero-expr = refl
  package-commutes one-expr = refl
  package-commutes (factor a) = refl
  package-commutes (binary m l r) =
    N.output-commutes (R.Pi-rule Port (old-family m (old-package l) (old-package r)))
      ∙ cong (N.Pi-package Port)
        (funExt (λ { operator → refl ; left → package-commutes l ; right → package-commutes r }))
  original : Expr → R.Closure Run.OldSeeds
  original e = old-package e , old-run e
  direct-native : Expr → Run.Closed
  direct-native e = package e , native-run e
  translated : Expr → Run.Closed
  translated e = equivFun Run.closure-equivalence (original e)
  endpoint : (e : Expr) → fst (translated e) ≡ package e
  endpoint e = Run.endpoint-commutes (original e) ∙ package-commutes e
  original-recovered : (e : Expr) → invEq Run.closure-equivalence (translated e) ≡ original e
  original-recovered e = retEq Run.closure-equivalence (original e)

  -- A readout at a marked endpoint transports its actual selected value.
  aligned-value : (e : Expr) → G.Value (fst (package e))
  aligned-value e = transport (cong (λ q → G.Value (fst q)) (endpoint e)) (snd (fst (translated e)))
  aligned-selected : (e : Expr) → aligned-value e ≡ snd (package e)
  aligned-selected e = fromPathP (λ i → snd (endpoint e i))
  translated-amplitude : (e : Expr) → readout e (aligned-value e) ≡ evaluate e
  translated-amplitude e = cong (readout e) (aligned-selected e) ∙ native-correct e
  direct-and-translated : (e : Expr) → readout e (snd (fst (direct-native e))) ≡ readout e (aligned-value e)
  direct-and-translated e = sym (cong (readout e) (aligned-selected e))
