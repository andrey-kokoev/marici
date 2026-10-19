{-# OPTIONS --safe --cubical --guardedness #-}
module TickSpectralFactorOperators where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Sigma.Base using (_×_; _,_)
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import CauchyMetricEquivalence using (MetricCompletionCandidate)
open import ConstructiveComplexCompletion using (conjugateComplex)
open import TickCompletionPhase using (phase)
open import TickMachinPiEndpointContract using (machinPi)
open import TickComplexCompletionRing using (ComplexCompletionCommRing)
import TickSpectralLocalOperators as L
import TickSpectralLocalInverse as Inv
import TickSpectralHamiltonian as H

module Factor (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  module S = L.Algebra R
  Matrix = Bool → Bool → fst R
  Vector = Bool × Bool → fst R
  left right : Matrix → Vector → Vector
  left A v (i , j) = A i false · v (false , j) + A i true · v (true , j)
  right A v (i , j) = A j false · v (i , false) + A j true · v (i , true)
  compose : Matrix → Matrix → Matrix
  compose A B i j = A i false · B false j + A i true · B true j

  spectral : fst R → fst R → Matrix
  spectral h z false false = h · (1r + z)
  spectral h z false true = h · (1r + (- z))
  spectral h z true false = h · (1r + (- z))
  spectral h z true true = h · (1r + z)
  generator : fst R → fst R → Matrix
  generator p h false false = p · h
  generator p h false true = - (p · h)
  generator p h true false = - (p · h)
  generator p h true true = p · h

  flip : Bool → Bool
  flip = L.V.flip

  abstract
    spectral-forward : (h z x y : fst R) → (h · (1r + z)) · x + (h · (1r + (- z))) · y ≡ S.spectral h z x y
    spectral-forward h z x y = solve! R
    spectral-backward : (h z x y : fst R) → (h · (1r + (- z))) · x + (h · (1r + z)) · y ≡ S.spectral h z y x
    spectral-backward h z x y = solve! R
    generator-forward : (p h x y : fst R) → (p · h) · x + (- (p · h)) · y ≡ p · S.minus h x y
    generator-forward p h x y = solve! R
    generator-backward : (p h x y : fst R) → (- (p · h)) · x + (p · h) · y ≡ p · S.minus h y x
    generator-backward p h x y = solve! R

    left-compose : (A B : Matrix) (v : Vector) → left A (left B v) ≡ left (compose A B) v
    left-compose A B v = funExt λ { (i , j) → solve! R }
    right-compose : (A B : Matrix) (v : Vector) → right A (right B v) ≡ right (compose A B) v
    right-compose A B v = funExt λ { (i , j) → solve! R }
    factors-commute : (A B : Matrix) (v : Vector) → left A (right B v) ≡ right B (left A v)
    factors-commute A B v = funExt λ { (i , j) → solve! R }

    left-spectral : (h z : fst R) (v : Vector) → left (spectral h z) v ≡ (λ { (i , j) → S.spectral h z (v (i , j)) (v (flip i , j)) })
    left-spectral h z v = funExt λ { (false , j) → spectral-forward h z (v (false , j)) (v (true , j)) ; (true , j) → spectral-backward h z (v (false , j)) (v (true , j)) }
    right-spectral : (h z : fst R) (v : Vector) → right (spectral h z) v ≡ (λ { (i , j) → S.spectral h z (v (i , j)) (v (i , flip j)) })
    right-spectral h z v = funExt λ { (i , false) → spectral-forward h z (v (i , false)) (v (i , true)) ; (i , true) → spectral-backward h z (v (i , false)) (v (i , true)) }
    left-generator : (p h : fst R) (v : Vector) → left (generator p h) v ≡ (λ { (i , j) → p · S.minus h (v (i , j)) (v (flip i , j)) })
    left-generator p h v = funExt λ { (false , j) → generator-forward p h (v (false , j)) (v (true , j)) ; (true , j) → generator-backward p h (v (false , j)) (v (true , j)) }
    right-generator : (p h : fst R) (v : Vector) → right (generator p h) v ≡ (λ { (i , j) → p · S.minus h (v (i , j)) (v (i , flip j)) })
    right-generator p h v = funExt λ { (i , false) → generator-forward p h (v (i , false)) (v (i , true)) ; (i , true) → generator-backward p h (v (i , false)) (v (i , true)) }

module F = Factor ComplexCompletionCommRing
module V = L.V
localMatrix inverseMatrix : MetricCompletionCandidate → F.Matrix
localMatrix t = F.spectral L.halfComplex (phase machinPi t)
inverseMatrix t = F.spectral L.halfComplex (conjugateComplex (phase machinPi t))
hamiltonianMatrix : F.Matrix
hamiltonianMatrix = F.generator H.piComplex L.halfComplex

abstract
  left-matrix : (t : MetricCompletionCandidate) (v : V.Vector) → F.left (localMatrix t) v ≡ L.leftLocal t v
  left-matrix t = F.left-spectral L.halfComplex (phase machinPi t)
  right-matrix : (t : MetricCompletionCandidate) (v : V.Vector) → F.right (localMatrix t) v ≡ L.rightLocal t v
  right-matrix t = F.right-spectral L.halfComplex (phase machinPi t)
  left-inverse-matrix : (t : MetricCompletionCandidate) (v : V.Vector) → F.left (inverseMatrix t) v ≡ Inv.leftInverse t v
  left-inverse-matrix t = F.left-spectral L.halfComplex (conjugateComplex (phase machinPi t))
  right-inverse-matrix : (t : MetricCompletionCandidate) (v : V.Vector) → F.right (inverseMatrix t) v ≡ Inv.rightInverse t v
  right-inverse-matrix t = F.right-spectral L.halfComplex (conjugateComplex (phase machinPi t))
  left-hamiltonian-matrix : (v : V.Vector) → F.left hamiltonianMatrix v ≡ H.hamiltonian V.left v
  left-hamiltonian-matrix = F.left-generator H.piComplex L.halfComplex
  right-hamiltonian-matrix : (v : V.Vector) → F.right hamiltonianMatrix v ≡ H.hamiltonian V.right v
  right-hamiltonian-matrix = F.right-generator H.piComplex L.halfComplex

  left-conjugates-own-factor : (t : MetricCompletionCandidate) (A : F.Matrix) (v : V.Vector) →
    L.leftLocal t (F.left A (Inv.leftInverse t v)) ≡ F.left (F.compose (localMatrix t) (F.compose A (inverseMatrix t))) v
  left-conjugates-own-factor t A v = sym (left-matrix t (F.left A (Inv.leftInverse t v)))
    ∙ cong (λ w → F.left (localMatrix t) (F.left A w)) (sym (left-inverse-matrix t v))
    ∙ cong (F.left (localMatrix t)) (F.left-compose A (inverseMatrix t) v)
    ∙ F.left-compose (localMatrix t) (F.compose A (inverseMatrix t)) v
  right-conjugates-own-factor : (t : MetricCompletionCandidate) (A : F.Matrix) (v : V.Vector) →
    L.rightLocal t (F.right A (Inv.rightInverse t v)) ≡ F.right (F.compose (localMatrix t) (F.compose A (inverseMatrix t))) v
  right-conjugates-own-factor t A v = sym (right-matrix t (F.right A (Inv.rightInverse t v)))
    ∙ cong (λ w → F.right (localMatrix t) (F.right A w)) (sym (right-inverse-matrix t v))
    ∙ cong (F.right (localMatrix t)) (F.right-compose A (inverseMatrix t) v)
    ∙ F.right-compose (localMatrix t) (F.compose A (inverseMatrix t)) v

  left-commutes-other-factor : (t : MetricCompletionCandidate) (A : F.Matrix) (v : V.Vector) →
    L.leftLocal t (F.right A v) ≡ F.right A (L.leftLocal t v)
  left-commutes-other-factor t A v = sym (left-matrix t (F.right A v))
    ∙ F.factors-commute (localMatrix t) A v ∙ cong (F.right A) (left-matrix t v)
  right-commutes-other-factor : (t : MetricCompletionCandidate) (A : F.Matrix) (v : V.Vector) →
    L.rightLocal t (F.left A v) ≡ F.left A (L.rightLocal t v)
  right-commutes-other-factor t A v = sym (right-matrix t (F.left A v))
    ∙ sym (F.factors-commute A (localMatrix t) v) ∙ cong (F.left A) (right-matrix t v)

  left-fixes-other-factor : (t : MetricCompletionCandidate) (A : F.Matrix) (v : V.Vector) →
    L.leftLocal t (F.right A (Inv.leftInverse t v)) ≡ F.right A v
  left-fixes-other-factor t A v = left-commutes-other-factor t A (Inv.leftInverse t v)
    ∙ cong (F.right A) (Inv.left-inverse-before t v)
  right-fixes-other-factor : (t : MetricCompletionCandidate) (A : F.Matrix) (v : V.Vector) →
    L.rightLocal t (F.left A (Inv.rightInverse t v)) ≡ F.left A v
  right-fixes-other-factor t A v = right-commutes-other-factor t A (Inv.rightInverse t v)
    ∙ cong (F.left A) (Inv.right-inverse-before t v)

  local-legs-commute : (s t : MetricCompletionCandidate) (v : V.Vector) →
    L.leftLocal s (L.rightLocal t v) ≡ L.rightLocal t (L.leftLocal s v)
  local-legs-commute s t v = cong (L.leftLocal s) (sym (right-matrix t v))
    ∙ left-commutes-other-factor s (localMatrix t) v ∙ right-matrix t (L.leftLocal s v)

  left-hamiltonian-other-factor : (A : F.Matrix) (v : V.Vector) →
    H.hamiltonian V.left (F.right A v) ≡ F.right A (H.hamiltonian V.left v)
  left-hamiltonian-other-factor A v = sym (left-hamiltonian-matrix (F.right A v))
    ∙ F.factors-commute hamiltonianMatrix A v ∙ cong (F.right A) (left-hamiltonian-matrix v)
  right-hamiltonian-other-factor : (A : F.Matrix) (v : V.Vector) →
    H.hamiltonian V.right (F.left A v) ≡ F.left A (H.hamiltonian V.right v)
  right-hamiltonian-other-factor A v = sym (right-hamiltonian-matrix (F.left A v))
    ∙ sym (F.factors-commute A hamiltonianMatrix v) ∙ cong (F.left A) (right-hamiltonian-matrix v)
