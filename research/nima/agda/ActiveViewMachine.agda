{-# OPTIONS --safe --cubical --guardedness #-}
module ActiveViewMachine where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (compEquiv; invEquiv)
open import Cubical.Foundations.HLevels using (isContrΣ)
open import Cubical.Data.Bool.Base using (Bool; not)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Nat.Base using (ℕ; suc)
open import Cubical.Data.List.Base using (List; []; _∷_; length)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Empty.Base using (⊥)
open import TypedGeneratorPresentation using (Reduction; contractRemainder; fromEquivalence)
open import TypedGeneratorCoherence using (AllDimensions; certify-reduction)
import TypedGeneratorTransport as D
import DependentTransportMachine as M

-- The runtime's closed, ordered instruction vocabulary. No reordering or
-- cancellation of source occurrences is permitted, including explicit stays.
data Action : Type where
  stay turn : Action

step : Action → Bool → Bool
step stay b = b
step turn b = not b

execute : List Action → Bool → Bool
execute [] b = b
execute (a ∷ h) b = execute h (step a b)

trace : List Action → Bool → List Bool
trace [] b = b ∷ []
trace (a ∷ h) b = b ∷ trace h (step a b)

trace-length : (h : List Action) (b : Bool) → length (trace h b) ≡ suc (length h)
trace-length [] b = refl
trace-length (a ∷ h) b = cong suc (trace-length h (step a b))

route : List Action → M.Route ⊥
route [] = M.stay
route (stay ∷ h) = M.follow M.stay (route h)
route (turn ∷ h) = M.follow M.turn (route h)

route-agreement : (h : List Action) (b : Bool) → M.run-route (route h) b ≡ execute h b
route-agreement [] b = refl
route-agreement (stay ∷ h) b = route-agreement h b
route-agreement (turn ∷ h) b = route-agreement h (not b)

module MB = D.MachineBridge
module E = D.Layer3 MB.P.transport-layer

layer3-agreement : (h : List Action) (b : Bool)
  → E.execute (MB.history (route h)) b ≡ execute h b
layer3-agreement h b = MB.route-agreement (route h) b ∙ route-agreement h b

-- Retain the instruction syntax independently of its compilation to paths.
Request : Type
Request = List Action × Bool

Output : Request → Type
Output (h , b) = Σ[ v ∈ Bool ] (execute h b ≡ v)
Trace : Request → Type
Trace (h , b) = Σ[ v ∈ List Bool ] (trace h b ≡ v)

output-complete : (r : Request) → isContr (Output r)
output-complete (h , b) = (execute h b , refl) , λ { (v , p) i → p i , λ j → p (i ∧ j) }
trace-complete : (r : Request) → isContr (Trace r)
trace-complete (h , b) = (trace h b , refl) , λ { (v , p) i → p i , λ j → p (i ∧ j) }

data Mode : Type where
  full output-only trace-only compact : Mode

Body : Mode → Request → Type
Body full r = Output r × Trace r
Body output-only r = Output r
Body trace-only r = Trace r
Body compact r = Unit

body-complete : (m : Mode) (r : Request) → isContr (Body m r)
body-complete full r = isContrΣ (output-complete r) (λ _ → trace-complete r)
body-complete output-only r = output-complete r
body-complete trace-only r = trace-complete r
body-complete compact r = tt , λ { tt → refl }

View : Mode → Type
View m = Σ Request (Body m)

boundary-reduction : (m : Mode) → Reduction {ℓF = ℓ-zero} (View m) Request
boundary-reduction m = contractRemainder (Body m) (body-complete m)

change : (m n : Mode) → Reduction {ℓF = ℓ-zero} (View m) (View n)
change m n = fromEquivalence (compEquiv
  (Reduction.equivalence (boundary-reduction m))
  (invEquiv (Reduction.equivalence (boundary-reduction n))))

request-preserved : (m n : Mode) (v : View m)
  → fst (Reduction.compact (change m n) v) ≡ fst v
request-preserved m n v = refl

coherent-change : (m n : Mode) → AllDimensions (change m n)
coherent-change m n = certify-reduction (change m n)
