{-# OPTIONS --safe --cubical --guardedness #-}
module ActionChartComparison where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Int.Base using (ℤ; pos; negsuc; _+_; _-_; -_; _·_)
open import Cubical.Data.Int.Properties using (posNotnegsuc)
open import Cubical.Algebra.CommRing.Instances.Int using (ℤCommRing)
open import Cubical.Tactics.CommRingSolver
import ComparisonKineticReadout as Kinetic
import BoundaryGeneratedQuestions as B
import ObservationRespectingBoundary as Q
module O = Q.O
module G = Q.G
module N = Q.N
module Owner = Kinetic.Algebra ℤCommRing

-- Fourth-order coefficient jets. m is mass SQUARED, l is the potential
-- fourth derivative, A=2a is twice the derivative-interaction coefficient.
-- b=6 beta clears chart denominators at the explicit F=U=1 fixture.
Jet : Type
Jet = ℤ × (ℤ × ℤ)
jet : ℤ → ℤ → ℤ → Jet
jet m l a = m , l , a
move : ℤ → Jet → Jet
move b (m , l , a) = m , l + pos 4 · m · b , a + b
observe : Jet → ℤ × ℤ
observe (m , l , a) = m , l - pos 4 · a · m
move-zero : (j : Jet) → move (pos 0) j ≡ j
move-zero (m , l , a) = cong₂ (jet m) (solve! ℤCommRing) (solve! ℤCommRing)
move-compose : (b c : ℤ) (j : Jet) → move c (move b j) ≡ move (b + c) j
move-compose b c (m , l , a) = cong₂ (jet m) (solve! ℤCommRing) (solve! ℤCommRing)
move-undo : (b : ℤ) (j : Jet) → move (- b) (move b j) ≡ j
move-undo b (m , l , a) = cong₂ (jet m) (solve! ℤCommRing) (solve! ℤCommRing)
move-redo : (b : ℤ) (j : Jet) → move b (move (- b) j) ≡ j
move-redo b (m , l , a) = cong₂ (jet m) (solve! ℤCommRing) (solve! ℤCommRing)
chart-iso : ℤ → Iso Jet Jet
Iso.fun (chart-iso b) = move b
Iso.inv (chart-iso b) = move (- b)
Iso.rightInv (chart-iso b) = move-redo b
Iso.leftInv (chart-iso b) = move-undo b
chart-equiv : ℤ → Jet ≃ Jet
chart-equiv b = isoToEquiv (chart-iso b)
move-observed : (b : ℤ) (j : Jet) → observe (move b j) ≡ observe j
move-observed b (m , l , a) = cong (λ l → m , l) (solve! ℤCommRing)
-- Explicit comparison with the owner's convention; not a new physics axiom.
owner-reading : (m l a : ℤ) → snd (observe (m , l , pos 2 · a)) ≡ Owner.effective l a m
owner-reading m l a = solve! ℤCommRing

data Chart : Type where angle ratio sine : Chart
parameter : Chart → ℤ
parameter angle = pos 0
parameter ratio = negsuc 1
parameter sine = pos 1
fixture : Chart → Jet
fixture angle = pos 2 , pos 16 , pos 0
fixture ratio = pos 2 , pos 0 , negsuc 1
fixture sine = pos 2 , pos 24 , pos 1
marked : (c : Chart) → move (parameter c) (fixture angle) ≡ fixture c
marked angle = refl
marked ratio = refl
marked sine = refl

-- Typed declared policy, not inferred from a bare carrier or source symmetry.
-- Analytic domains: |theta|<pi/4, |u|<1, |z|<1/sqrt(2).
-- Trigonometric chart identities are checked separately, not postulated here.
data Policy : Type where
  positive-unit-probe-counting-metric-classical-scalar-F1-U1 : Policy
package : Chart → O.Complete
package c = O.remember (B.retain-filler B.fourQ B.fourQ B.swap-filler)
  (O.pack (O.retain (O.atom Policy) positive-unit-probe-counting-metric-classical-scalar-F1-U1
    (O.retain (O.atom Chart) c (O.atom Jet))) (fixture c))
comparison : (c : Chart) → Q.Observed (package angle) (package c) observe observe
comparison c = (chart-equiv (parameter c) , marked c) , move-observed (parameter c)
between : (s t : Chart) → Q.Observed (package s) (package t) observe observe
between s t = Q.compose {a = package s} {b = package angle} {c = package t}
  {r = observe} {s = observe} {t = observe}
  (Q.inverse {a = package angle} {b = package s} {r = observe} {s = observe} (comparison s))
  (comparison t)
native-comparison : (c : Chart) → Q.NativeObserved
  (G.encode-package (package angle)) (G.encode-package (package c)) observe observe
native-comparison c = Q.to-native {a = package angle} {b = package c}
  {r = observe} {s = observe} observe observe (λ x → refl) (λ x → refl) (comparison c)

record Reader : Type where
  constructor reader
  field
    run : Jet → ℤ × ℤ
    authorized : (j : Jet) → run j ≡ observe j
canonical : Reader
canonical = reader observe (λ j → refl)
record Gate (c : Chart) : Type where
  constructor gate
  field
    left right : Reader
    compatible : (j : Jet) → Reader.run right (move (parameter c) j) ≡ Reader.run left j
admitted : (c : Chart) → Gate c
admitted c = gate canonical canonical (move-observed (parameter c))
gated-native : (c : Chart) → Gate c → Q.NativeObserved
  (G.encode-package (package angle)) (G.encode-package (package c)) observe observe
gated-native c (gate l r h) = (chart-equiv (parameter c) , marked c) , λ j →
  sym (Reader.authorized r (move (parameter c) j)) ∙ h j ∙ Reader.authorized l j
retained : (c : Chart) → Gate c → G.Package
retained c g = N.remember
  (Q.native-retained-certificate {a = G.encode-package (package angle)}
    {b = G.encode-package (package c)} {r = observe} {s = observe} (gated-native c g))
  (N.pack (G.atom-node (Gate c)) g)
recovered : (c : Chart) (g : Gate c) → snd (retained c g) ≡ g
recovered c g = refl

-- Authorization cannot be replaced by potential-only or constant observations.
potential-only : Jet → ℤ × ℤ
potential-only (m , l , a) = m , l
zero-not-sixteen : pos 0 ≡ pos 16 → ⊥
zero-not-sixteen p = posNotnegsuc 15 0 (sym (cong (λ z → z - pos 1) p))
no-potential-reader : ((j : Jet) → potential-only j ≡ observe j) → ⊥
no-potential-reader h = zero-not-sixteen (cong snd (h (fixture ratio)))
no-constant-reader : (v : ℤ × ℤ) → ((j : Jet) → v ≡ observe j) → ⊥
no-constant-reader v h = zero-not-sixteen
  (cong snd (sym (h (pos 2 , pos 0 , pos 0)) ∙ h (fixture angle)))

-- Canonical sixth derivative supplied by the separate symbolic action check:
-- logarithmic=512, quartic truncation=0, while both coarse profiles are (2,16).
-- No function of the mass/quartic profile alone supplies that refinement.
no-sixth-factor : (f : (ℤ × ℤ) → ℤ)
  → f (observe (fixture angle)) ≡ pos 512
  → f (observe (fixture angle)) ≡ pos 0 → ⊥
no-sixth-factor f p q = posNotnegsuc 511 0
  (cong (λ z → z - pos 1) (sym p ∙ q))
