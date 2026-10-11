{-# OPTIONS --safe --cubical --guardedness #-}
module TickWholeReturnRealization where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Sigma.Base using (_×_)
import TickRetainedStructure as S
import TickGluedSchedules as M
import TickCompletionRealization as C
open import CauchyMetricEquivalence using (MetricCompletionCandidate)

module G = S.G
module V = C.Realization

reverse-order : G.Schedule → G.Schedule
reverse-order G.leftFirst = G.rightFirst
reverse-order G.rightFirst = G.leftFirst

return-run : (r : G.Schedule) (s : Bool × Bool)
  → G.run (reverse-order r) (G.run G.leftFirst s) ≡ s
return-run G.leftFirst (false , false) = refl
return-run G.leftFirst (false , true) = refl
return-run G.leftFirst (true , false) = refl
return-run G.leftFirst (true , true) = refl
return-run G.rightFirst (false , false) = refl
return-run G.rightFirst (false , true) = refl
return-run G.rightFirst (true , false) = refl
return-run G.rightFirst (true , true) = refl

module AtSource (s : Bool × Bool) where
  module T = S.AtSource s

  -- A whole path object, not a Cubical-coordinate state decoder.
  return-path : G.Schedule → M.ScheduleParameter → V.Vector
  return-path r = M.glued (reverse-order r) (G.run G.leftFirst s)

  return-start : (r : G.Schedule)
    → return-path r M.start ≡ V.basis (G.run G.leftFirst s)
  return-start r = M.glued-start (reverse-order r) (G.run G.leftFirst s)

  return-finish : (r : G.Schedule)
    → return-path r M.finish ≡ V.basis s
  return-finish r = M.glued-finish (reverse-order r) (G.run G.leftFirst s)
    ∙ cong V.basis (return-run r s)

  return-continuous : (r : G.Schedule) (j : Bool × Bool)
    (P : M.Predicate MetricCompletionCandidate) → M.ScalarOpen P
    → M.FinalOpen (λ a → P (return-path r a j))
  return-continuous r = M.glued-continuous (reverse-order r) (G.run G.leftFirst s)

  Paths : Type
  Paths = (M.ScheduleParameter → V.Vector) × (M.ScheduleParameter → V.Vector)

  realize-tags : G.Schedule × G.Schedule → Paths
  realize-tags (r , q) = return-path r , return-path q

  realize : T.A.Tick → Paths
  realize t = realize-tags (T.tags t)

  -- Coherence for the entire retained record, including its section.
  reconstruction-coherence : (t : T.A.Tick)
    → realize t ≡ realize (T.rebuild (T.tags t))
  reconstruction-coherence = T.observation-factors realize

  same-tags-coherence : (t u : T.A.Tick) → T.tags t ≡ T.tags u
    → realize t ≡ realize u
  same-tags-coherence t u p = cong realize-tags p

  -- Swapping compared schedules swaps the two realized return paths.
  swap : Paths → Paths
  swap (p , q) = q , p

  schedule-swap : (r q : G.Schedule)
    → realize (T.rebuild (q , r)) ≡ swap (realize (T.rebuild (r , q)))
  schedule-swap r q = refl
