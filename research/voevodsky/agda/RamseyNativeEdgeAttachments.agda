{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyNativeEdgeAttachments where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Agda.Builtin.String using (String)
open import RamseyUniformRelative using (Slot)
open import RamseySingleFrameFaces using (Vertex; c0; m0; c1; m1; face)
import RamseyNativePNOverlapSpan as Span

data Edge : Type where
  e01 e02 e03 e12 e13 e23 : Edge
ends : Edge → Vertex × Vertex
ends e01 = c0 , m0
ends e02 = c0 , c1
ends e03 = c0 , m1
ends e12 = m0 , c1
ends e13 = m0 , m1
ends e23 = c1 , m1
endpoint : Bool → Edge → Vertex
endpoint false e = fst (ends e)
endpoint true e = snd (ends e)
InFace : Vertex → Vertex → Type
InFace v f = Σ (Slot 3) (λ i → face f i ≡ v)

module Attachments (Chart : Type) (Permit : Chart → Vertex → Type)
  (packet : (c : Chart) (f : Vertex) → Permit c f → String) where
  EdgePermit : Chart → Edge → Type
  EdgePermit c e = Σ Vertex (λ f → Σ (Permit c f) (λ _ → InFace (fst (ends e)) f × InFace (snd (ends e)) f))
  VertexPermit : Chart → Vertex → Type
  VertexPermit c v = Σ Vertex (λ f → Σ (Permit c f) (λ _ → InFace v f))
  edge-packet : (c : Chart) (e : Edge) → EdgePermit c e → String
  edge-packet c e (f , (p , members)) = packet c f p
  vertex-packet : (c : Chart) (v : Vertex) → VertexPermit c v → String
  vertex-packet c v (f , (p , member)) = packet c f p
  module S = Span.Spans Chart Edge EdgePermit edge-packet
  module V = Span.Spans Chart Vertex VertexPermit vertex-packet
  restrict : (side : Bool) (c : Chart) (e : Edge) → EdgePermit c e → VertexPermit c (endpoint side e)
  restrict false c e (f , (p , (left , right))) = f , (p , left)
  restrict true c e (f , (p , (left , right))) = f , (p , right)
  restriction-packet : (side : Bool) (c : Chart) (e : Edge) (p : EdgePermit c e)
    → edge-packet c e p ≡ vertex-packet c (endpoint side e) (restrict side c e p)
  restriction-packet false c e p = refl
  restriction-packet true c e p = refl
  restriction-admit : (side : Bool) {q : Span.G.Package} → S.Admit q → V.Admit q
  restriction-admit false ((c , (e , (f , (p , (left , right))))) , eq) =
    (c , (fst (ends e) , (f , (p , left)))) , eq
  restriction-admit true ((c , (e , (f , (p , (left , right))))) , eq) =
    (c , (snd (ends e) , (f , (p , right)))) , eq
  transport-derivation : (side : Bool) {q : Span.G.Package} → S.R.Resolve q → V.R.Resolve q
  transport-derivation side (S.R.seed a) = V.R.seed (restriction-admit side a)
  transport-derivation side (S.R.apply r ds) = V.R.apply r (λ i → transport-derivation side (ds i))
  restrict-common : (side : Bool) {a b : Chart} → S.Common a b → V.Common a b
  restrict-common side {a} {b} (e , (p , q)) = endpoint side e , (restrict side a e p , restrict side b e q)
  restricted-selection : (side : Bool) (a b : Chart) (x : S.Common a b)
    → V.R.Resolve (V.selected-package a b (restrict-common side x))
  restricted-selection side a b x = V.selected-proof a b (restrict-common side x)
  restrict-triple : (side : Bool) {a b c : Chart} → S.Triple a b c → V.Triple a b c
  restrict-triple side {a} {b} {c} (e , (p , (q , r))) =
    endpoint side e , (restrict side a e p , (restrict side b e q , restrict side c e r))
  ab-restriction-cell : (side : Bool) (a b c : Chart) (t : S.Triple a b c)
    → restrict-common side (S.ab-index t) ≡ V.ab-index (restrict-triple side t)
  ab-restriction-cell side a b c t = refl
  bc-restriction-cell : (side : Bool) (a b c : Chart) (t : S.Triple a b c)
    → restrict-common side (S.bc-index t) ≡ V.bc-index (restrict-triple side t)
  bc-restriction-cell side a b c t = refl
  ac-restriction-cell : (side : Bool) (a b c : Chart) (t : S.Triple a b c)
    → restrict-common side (S.ac-index t) ≡ V.ac-index (restrict-triple side t)
  ac-restriction-cell side a b c t = refl
