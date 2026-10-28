{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyDifferentEdgeBadSide where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (true)
open import RamseyEndpointPolicy using (base; complement)
import RamseyFourFacetVertexCells as F
import RamseyCommonSelection as K
import RamseyEndpointFamily as H
bad : K.vertex-move base complement F.route-ab-0-1-2 ≡ H.family complement base F.edge-1-0 true
bad = refl
