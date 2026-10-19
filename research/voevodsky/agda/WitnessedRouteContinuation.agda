{-# OPTIONS --safe --cubical --guardedness #-}
module WitnessedRouteContinuation where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Transport using
  (transportComposite; transport⁻Transport; transportTransport⁻)
open import Cubical.Foundations.GroupoidLaws using (rCancel)
open import Cubical.Foundations.Univalence using (uaβ)
open import Cubical.Foundations.Isomorphism using (isoToEquiv)
open import Cubical.Data.Bool.Base using (Bool; false; true; not)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
import DependentTransportMachine as M
import GradedBoundaryCoherence as G
import MarkedTriangleCoherence as T

module Tri = T.Triangles (Type ℓ-zero)

-- Source: the existing independently defined route syntax and bit machine.
Program : Type
Program = M.Route ⊥

reverse-program : Program → Program
reverse-program (M.slot ())
reverse-program M.stay = M.stay
reverse-program M.turn = M.turn
reverse-program (M.follow p q) = M.follow (reverse-program q) (reverse-program p)

not-twice : (b : Bool) → not (not b) ≡ b
not-twice false = refl
not-twice true = refl

source-return-left : (p : Program) (b : Bool)
  → M.run-route (reverse-program p) (M.run-route p b) ≡ b
source-return-left (M.slot ()) b
source-return-left M.stay b = refl
source-return-left M.turn b = not-twice b
source-return-left (M.follow p q) b =
  cong (M.run-route (reverse-program p)) (source-return-left q (M.run-route p b))
  ∙ source-return-left p b

source-return-right : (p : Program) (b : Bool)
  → M.run-route p (M.run-route (reverse-program p) b) ≡ b
source-return-right (M.slot ()) b
source-return-right M.stay b = refl
source-return-right M.turn b = not-twice b
source-return-right (M.follow p q) b =
  cong (M.run-route q) (source-return-right p (M.run-route (reverse-program q) b))
  ∙ source-return-right q b

-- Target: generated type paths, not all paths of the universe.
type-path : Program → Bool ≡ Bool
type-path (M.slot ())
type-path M.stay = refl
type-path M.turn = G.twisted-filler
type-path (M.follow p q) = type-path p ∙ type-path q

flip-is-not : (b : Bool) → G.flip b ≡ not b
flip-is-not false = refl
flip-is-not true = refl

turn-sound : (b : Bool) → transport G.twisted-filler b ≡ not b
turn-sound b = uaβ (isoToEquiv G.flip-iso) b ∙ flip-is-not b

route-sound : (p : Program) (b : Bool)
  → transport (type-path p) b ≡ M.run-route p b
route-sound (M.slot ()) b
route-sound M.stay b = transportRefl b
route-sound M.turn b = turn-sound b
route-sound (M.follow p q) b = transportComposite (type-path p) (type-path q) b
  ∙ cong (transport (type-path q)) (route-sound p b)
  ∙ route-sound q (M.run-route p b)

-- The source route determines a filled return triangle. The actual edge,
-- its reverse, and cancellation filler are retained; diagonal is always refl.
triangle : Program → Tri.MarkedTriangle Bool Bool Bool
triangle p = type-path p , sym (type-path p) , refl , rCancel (type-path p)

first-edge-retained : (p : Program) → Tri.first-edge (triangle p) ≡ type-path p
first-edge-retained p = refl

same-return : (p q : Program) → Tri.diagonal (triangle p) ≡ Tri.diagonal (triangle q)
same-return p q = refl

-- This continuation CONSUMES the retained path, not just the returned value.
probe : Tri.MarkedTriangle Bool Bool Bool → Bool → Bool
probe t b = transport (Tri.first-edge t) b

probe-sound : (p : Program) (b : Bool) → probe (triangle p) b ≡ M.run-route p b
probe-sound = route-sound

record Completed (p : Program) : Type₁ where
  field
    diagram : Tri.MarkedTriangle Bool Bool Bool
    diagram-is-constructed : diagram ≡ triangle p
    result : Bool → Bool
    continuation-correct : (b : Bool) → probe diagram b ≡ result b
    executions : (b : Bool) → M.Steps (M.carry p (M.bit b)) (M.bit (result b))

compile : (p : Program) → Completed p
compile p = record
  { diagram = triangle p
  ; diagram-is-constructed = refl
  ; result = M.run-route p
  ; continuation-correct = route-sound p
  ; executions = M.route-normalizes p
  }

composition : (p q : Program) (b : Bool)
  → probe (triangle (M.follow p q)) b ≡ probe (triangle q) (probe (triangle p) b)
composition p q b = transportComposite (type-path p) (type-path q) b

-- Reverse path transport is the inverse action, witnessed on every input.
return-left : (p : Program) (b : Bool)
  → transport (sym (type-path p)) (probe (triangle p) b) ≡ b
return-left p b = transport⁻Transport (type-path p) b

return-right : (p : Program) (b : Bool)
  → probe (triangle p) (transport (sym (type-path p)) b) ≡ b
return-right p b = transportTransport⁻ (type-path p) b

-- A typed comparison of full certificates transports continuation equality.
comparison-preserves-probe : (s t : Tri.MarkedTriangle Bool Bool Bool)
  → s ≡ t → (b : Bool) → probe s b ≡ probe t b
comparison-preserves-probe s t alpha b = cong (λ u → probe u b) alpha

-- Higher comparisons between comparisons also remain visible to the probe.
higher-comparison-preserved : (s t : Tri.MarkedTriangle Bool Bool Bool)
  (alpha beta : s ≡ t) → alpha ≡ beta → (b : Bool)
  → comparison-preserves-probe s t alpha b ≡ comparison-preserves-probe s t beta b
higher-comparison-preserved s t alpha beta h b = cong (λ a → cong (λ u → probe u b) a) h

plain-result : probe (triangle M.stay) false ≡ false
plain-result = route-sound M.stay false

twisted-result : probe (triangle M.turn) false ≡ true
twisted-result = route-sound M.turn false

-- Same vertices AND same return diagonal, but a legitimate continuation differs.
continuation-distinguishes : probe (triangle M.stay) false ≡ probe (triangle M.turn) false → ⊥
continuation-distinguishes eq = false≢true (sym plain-result ∙ eq ∙ twisted-result)

no-return-only-continuation : (observe : (Bool ≡ Bool) → Bool)
  → ((p : Program) → observe (Tri.diagonal (triangle p)) ≡ probe (triangle p) false)
  → ⊥
no-return-only-continuation observe correct = false≢true
  (sym plain-result ∙ sym (correct M.stay) ∙ correct M.turn ∙ twisted-result)
