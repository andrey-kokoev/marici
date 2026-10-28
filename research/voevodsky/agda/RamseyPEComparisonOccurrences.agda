{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPEComparisonOccurrences where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (tt)
open import Agda.Builtin.String using (String)
import RamseyPEConstructorComparison as Constructor

module OccurrenceLift (Source : Type) (payload : Source → String)
  (LeafRelation : Source → Source → Type) where
  module C = Constructor.Compare Source payload LeafRelation
  map-occurrence : {s t : C.T.Tree} → C.Correspondence s t → C.T.Occurrence s → C.T.Occurrence t
  map-occurrence (C.leaf s t witness) tt = tt
  map-occurrence (C.product I J e f g branches) (i , o) = fst e i , map-occurrence (branches i) o
  map-occurrence (C.selection I J e f g selected target agreement branches) (i , o) = fst e i , map-occurrence (branches i) o
  origin-law : {s t : C.T.Tree} (comparison : C.Correspondence s t) (o : C.T.Occurrence s)
    → LeafRelation (C.T.origin s o) (C.T.origin t (map-occurrence comparison o))
  origin-law (C.leaf s t witness) tt = witness
  origin-law (C.product I J e f g branches) (i , o) = origin-law (branches i) o
  origin-law (C.selection I J e f g selected target agreement branches) (i , o) = origin-law (branches i) o
