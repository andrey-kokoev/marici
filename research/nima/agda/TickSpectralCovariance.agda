{-# OPTIONS --safe --cubical --guardedness #-}
module TickSpectralCovariance where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Sigma.Base using (_,_)
open import CauchyMetricEquivalence using (MetricCompletionCandidate)
open import ConstructiveComplexCompletion
open import TickCompletionClippedTime using (firstTime; secondTime)
import TickCompletionMetricInterval as I
import TickSpectralLocalOperators as L
import TickSpectralHamiltonian as H
import TickSpectralGlobalPath as Path
import TickSpectralProjectorLaws as P
import TickSpectralRetainedReturn as R
import TickComplexNativeBasis as B
import TickComplexCompletionRing as Ring
open import TickCompletionPhase using (phase)
open import TickMachinPiEndpointContract using (machinPi)
module V = L.V
module G = R.G

-- Reindexing naturality. For bijective e this is the free-linearized
-- relabeling (pullback by e). The law needs only the intertwining equation.
reindex : Path.IndexMap → V.Vector → V.Vector
reindex e v j = v (e j)

abstract
  local-natural : (e a b : Path.IndexMap) → ((j : V.Label) → a (e j) ≡ e (b j)) →
    (t : MetricCompletionCandidate) (v : V.Vector) →
    reindex e (L.local (Path.permute a) t v) ≡ L.local (Path.permute b) t (reindex e v)
  local-natural e a b intertwine t v = funExt λ j →
    cong (λ y → L.A.spectral L.halfComplex (phase machinPi t) (v (e j)) (v y)) (intertwine j)

  hamiltonian-natural : (e a b : Path.IndexMap) → ((j : V.Label) → a (e j) ≡ e (b j)) →
    (v : V.Vector) → reindex e (H.hamiltonian (Path.permute a) v) ≡ H.hamiltonian (Path.permute b) (reindex e v)
  hamiltonian-natural e a b intertwine v = funExt λ j →
    cong (λ y → H.piComplex ·complex L.A.minus L.halfComplex (v (e j)) (v y)) (intertwine j)

  global-natural : (e a b c d : Path.IndexMap) →
    ((j : V.Label) → a (e j) ≡ e (c j)) → ((j : V.Label) → b (e j) ≡ e (d j)) →
    (t : MetricCompletionCandidate) (v : V.Vector) →
    reindex e (Path.glued a b t v) ≡ Path.glued c d t (reindex e v)
  global-natural e a b c d first second t v =
    local-natural e b d second (secondTime t) (L.local (Path.permute a) (firstTime t) v)
    ∙ cong (L.local (Path.permute d) (secondTime t)) (local-natural e a c first (firstTime t) v)

exchangeIndex : Path.IndexMap
exchangeIndex (a , b) = b , a

abstract
  exchange-left-local : (t : MetricCompletionCandidate) (v : V.Vector) → V.exchange (L.leftLocal t v) ≡ L.rightLocal t (V.exchange v)
  exchange-left-local = local-natural exchangeIndex P.leftIndex P.rightIndex (λ j → refl)
  exchange-right-local : (t : MetricCompletionCandidate) (v : V.Vector) → V.exchange (L.rightLocal t v) ≡ L.leftLocal t (V.exchange v)
  exchange-right-local = local-natural exchangeIndex P.rightIndex P.leftIndex (λ j → refl)
  exchange-left-hamiltonian : (v : V.Vector) → V.exchange (H.hamiltonian V.left v) ≡ H.hamiltonian V.right (V.exchange v)
  exchange-left-hamiltonian = hamiltonian-natural exchangeIndex P.leftIndex P.rightIndex (λ j → refl)
  exchange-right-hamiltonian : (v : V.Vector) → V.exchange (H.hamiltonian V.right v) ≡ H.hamiltonian V.left (V.exchange v)
  exchange-right-hamiltonian = hamiltonian-natural exchangeIndex P.rightIndex P.leftIndex (λ j → refl)

  exchange-basis : (s : V.Label) → V.exchange (B.basis s) ≡ B.basis (exchangeIndex s)
  exchange-basis (a , b) = funExt λ { (c , d) → Ring.Operational.mul-comm (B.Operational.delta a d) (B.Operational.delta b c) }

swapSchedule : G.Schedule → G.Schedule
swapSchedule G.leftFirst = G.rightFirst
swapSchedule G.rightFirst = G.leftFirst

abstract
  exchange-target : (s : V.Label) → V.exchange (R.nativeTarget s) ≡ R.nativeTarget (exchangeIndex s)
  exchange-target s = V.exchange-right (V.left (B.basis s))
    ∙ cong V.left (V.exchange-left (B.basis s))
    ∙ V.flips-commute (V.exchange (B.basis s))
    ∙ cong (λ v → V.right (V.left v)) (exchange-basis s)

  exchange-return : (r : G.Schedule) (s : V.Label) (t : I.ReturnInterval) →
    V.exchange (R.returnPath r s t) ≡ R.returnPath (swapSchedule r) (exchangeIndex s) t
  exchange-return G.leftFirst s t = global-natural exchangeIndex P.rightIndex P.leftIndex P.leftIndex P.rightIndex
    (λ j → refl) (λ j → refl) (fst t) (R.nativeTarget s)
    ∙ cong (Path.glued P.leftIndex P.rightIndex (fst t)) (exchange-target s)
  exchange-return G.rightFirst s t = global-natural exchangeIndex P.leftIndex P.rightIndex P.rightIndex P.leftIndex
    (λ j → refl) (λ j → refl) (fst t) (R.nativeTarget s)
    ∙ cong (Path.glued P.rightIndex P.leftIndex (fst t)) (exchange-target s)

-- Every Bool permutation is represented by identity or flip. The following
-- explicit family covers all factorwise renamings without deciding completion.
rename : Bool → Bool → Bool
rename false a = a
rename true a = V.flip a
rename-flip : (p a : Bool) → V.flip (rename p a) ≡ rename p (V.flip a)
rename-flip false a = refl
rename-flip true a = refl
renameIndex : Bool → Bool → Path.IndexMap
renameIndex p q (a , b) = rename p a , rename q b
rename-left : (p q : Bool) (j : V.Label) → P.leftIndex (renameIndex p q j) ≡ renameIndex p q (P.leftIndex j)
rename-left p q (a , b) = cong (λ x → x , rename q b) (rename-flip p a)
rename-right : (p q : Bool) (j : V.Label) → P.rightIndex (renameIndex p q j) ≡ renameIndex p q (P.rightIndex j)
rename-right p q (a , b) = cong (λ x → rename p a , x) (rename-flip q b)

rename-involutive : (p a : Bool) → rename p (rename p a) ≡ a
rename-involutive false a = refl
rename-involutive true a = V.flip-involutive a
renameIndex-involutive : (p q : Bool) (j : V.Label) → renameIndex p q (renameIndex p q j) ≡ j
renameIndex-involutive p q (a , b) = cong₂ _,_ (rename-involutive p a) (rename-involutive q b)

abstract
  relabel-left-hamiltonian : (p q : Bool) (v : V.Vector) →
    reindex (renameIndex p q) (H.hamiltonian V.left v) ≡ H.hamiltonian V.left (reindex (renameIndex p q) v)
  relabel-left-hamiltonian p q = hamiltonian-natural (renameIndex p q) P.leftIndex P.leftIndex (rename-left p q)
  relabel-right-hamiltonian : (p q : Bool) (v : V.Vector) →
    reindex (renameIndex p q) (H.hamiltonian V.right v) ≡ H.hamiltonian V.right (reindex (renameIndex p q) v)
  relabel-right-hamiltonian p q = hamiltonian-natural (renameIndex p q) P.rightIndex P.rightIndex (rename-right p q)

  relabel-left-local : (p q : Bool) (t : MetricCompletionCandidate) (v : V.Vector) →
    reindex (renameIndex p q) (L.leftLocal t v) ≡ L.leftLocal t (reindex (renameIndex p q) v)
  relabel-left-local p q = local-natural (renameIndex p q) P.leftIndex P.leftIndex (rename-left p q)
  relabel-right-local : (p q : Bool) (t : MetricCompletionCandidate) (v : V.Vector) →
    reindex (renameIndex p q) (L.rightLocal t v) ≡ L.rightLocal t (reindex (renameIndex p q) v)
  relabel-right-local p q = local-natural (renameIndex p q) P.rightIndex P.rightIndex (rename-right p q)

  relabel-basis : (p q : Bool) (s : V.Label) → reindex (renameIndex p q) (B.basis s) ≡ B.basis (renameIndex p q s)
  relabel-basis false false s = refl
  relabel-basis true false s = B.Operational.basis-left s
  relabel-basis false true s = B.Operational.basis-right s
  relabel-basis true true s = cong V.right (B.Operational.basis-left s) ∙ B.Operational.basis-right (P.leftIndex s)

  relabel-target : (p q : Bool) (s : V.Label) →
    reindex (renameIndex p q) (R.nativeTarget s) ≡ R.nativeTarget (renameIndex p q s)
  relabel-target p q s =
    (funExt λ j → cong (B.basis s) (cong P.leftIndex (rename-right p q j) ∙ rename-left p q (P.rightIndex j)))
    ∙ cong (λ v → V.right (V.left v)) (relabel-basis p q s)

  relabel-return : (p q : Bool) (r : G.Schedule) (s : V.Label) (t : I.ReturnInterval) →
    reindex (renameIndex p q) (R.returnPath r s t) ≡ R.returnPath r (renameIndex p q s) t
  relabel-return p q G.leftFirst s t = global-natural (renameIndex p q) P.rightIndex P.leftIndex P.rightIndex P.leftIndex
    (rename-right p q) (rename-left p q) (fst t) (R.nativeTarget s)
    ∙ cong (Path.glued P.rightIndex P.leftIndex (fst t)) (relabel-target p q s)
  relabel-return p q G.rightFirst s t = global-natural (renameIndex p q) P.leftIndex P.rightIndex P.leftIndex P.rightIndex
    (rename-left p q) (rename-right p q) (fst t) (R.nativeTarget s)
    ∙ cong (Path.glued P.leftIndex P.rightIndex (fst t)) (relabel-target p q s)
