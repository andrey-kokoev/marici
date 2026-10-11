{-# OPTIONS --safe --cubical --guardedness #-}
module NestedAttachmentOrder where

open import Cubical.Foundations.Prelude hiding (Path; empty)
open import Cubical.Data.Bool.Base using (Bool; true; false; not)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import NestedWitnessTransport

-- The only operation available in the present marked model is append.
-- No state-dependent electronic action or commutation law is added.
data Step : Term → Term → Type where
  append : (parent : Term) (e : Bool) → Step parent (attach parent e)

data Path (s : Term) : Term → Type where
  empty : Path s s
  link : {t u : Term} → Step s t → Path t u → Path s u

exchange-step : {s t : Term} → Step s t → Step (exchange s) (exchange t)
exchange-step (append parent e) = append (exchange parent) (not e)

exchange-path : {s t : Term} → Path s t → Path (exchange s) (exchange t)
exchange-path empty = empty
exchange-path (link e rest) = link (exchange-step e) (exchange-path rest)

forward : Path core (attach (attach core false) true)
forward = link (append core false)
  (link (append (attach core false) true) empty)

opposite-order : Path core (attach (attach core true) false)
opposite-order = link (append core true)
  (link (append (attach core true) false) empty)

-- Full path comparison, including intermediate objects and append witnesses.
transported-forward-is-opposite : exchange-path forward ≡ opposite-order
transported-forward-is-opposite = refl

Route : Type
Route = Σ[ t ∈ Term ] Path core t
forward-route opposite-route : Route
forward-route = _ , forward
opposite-route = _ , opposite-order

-- Without exchanging all marks, neither endpoints nor full routes commute.
fixed-label-routes-distinct : forward-route ≡ opposite-route → ⊥
fixed-label-routes-distinct equality = nested-distinct (cong fst equality)

-- First attachments also differ at fixed labels; the history was not checked
-- merely by projecting both paths to their two-edge length.
first-attachments-distinct : attach core false ≡ attach core true → ⊥
first-attachments-distinct equality = false≢true (cong outer-label equality)
