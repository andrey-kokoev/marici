{-# OPTIONS --safe --cubical --guardedness #-}
module TetrahedralWitnessControl where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
import RetainedTetrahedralPackage as Retained
import TetrahedralEdgeReadout as Read

module L = Retained.LossyDiagonal

-- Prepared source probe and target reference are explicit inputs. This is
-- an active observation of an edge witness, not transport round the boundary.
disagrees : Bool → Bool → Bool
disagrees false false = false
disagrees false true = true
disagrees true false = true
disagrees true true = false

control : L.O.Package → Bool → Bool → Bool
control p source-probe target-reference =
  disagrees (transport (L.first-edge p) source-probe) target-reference

ordinary-control : control L.ordinary false false ≡ false
ordinary-control = cong (λ b → disagrees b false) (Read.ordinary01 false)
twisted-control : control L.twisted false false ≡ true
twisted-control = cong (λ b → disagrees b false) (Read.twisted01 false)

-- Retaining the question preserves the full package rather than replacing
-- it by the single control bit.
record Question : Type₁ where
  constructor question
  field
    package : L.O.Package
    source-probe target-reference : Bool

answer : Question → Bool
answer q = control (Question.package q) (Question.source-probe q) (Question.target-reference q)

record Answered : Type₁ where
  constructor answered
  field
    retained-question : Question
    value : Bool
    agrees : value ≡ answer retained-question

ask : Question → Answered
ask q = answered q (answer q) refl
recover-question : (q : Question) → Answered.retained-question (ask q) ≡ q
recover-question q = refl
