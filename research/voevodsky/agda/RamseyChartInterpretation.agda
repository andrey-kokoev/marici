{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyChartInterpretation where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Nat.Base using (ℕ)
open import Cubical.Data.Int.Base using (ℤ; _+_; -_)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Relation.Nullary using (¬_)
open import RamseyUniformRelative using (Slot)
open import RamseyUniformSigned using (zero3)
import RamseyExactSource as X
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
import NativeTableResolution as Resolution
module G = Tables.Core ℓ-zero
module N = Rules.Native ℓ-zero

data Canonical : Type where
  root-context : Canonical
canonical-reference : Canonical → X.Label → X.Bary
canonical-reference root-context = X.reference (X.prepared zero3)
translate : X.Shift → X.Bary → X.Bary
translate (a , (b , c)) (d , (u , (v , w))) = (-(a + (b + c)) + d) , ((a + u) , ((b + v) , (c + w)))
chart-reference : X.Shift → Canonical → X.Label → X.Bary
chart-reference s c l = translate s (canonical-reference c l)
reference-square : (s : X.Shift) (l : X.Label) → chart-reference s root-context l ≡ X.reference (X.prepared s) l
reference-square s X.C0 = refl
reference-square s X.M0 = refl
reference-square s X.C1 = refl
reference-square s X.M1 = refl
reference-square s X.C2 = refl

module Interpretation (radius r : ℕ) (color : X.Region radius → Slot r) where
  Index = X.Region radius
  SourceRow : Type
  SourceRow = Σ X.Context (λ _ → Slot r)
  LocalRow : Type
  LocalRow = Σ Canonical (λ _ → Slot r)
  source-fiber : Index → G.Package
  source-fiber i = N.pack (G.atom-node SourceRow) (X.region-context i , color i)
  local-fiber : Index → G.Package
  local-fiber i = N.pack (G.atom-node LocalRow) (root-context , color i)
  SourceAdmit TargetAdmit : G.Package → Type (ℓ-suc ℓ-zero)
  SourceAdmit q = Σ Index (λ i → q ≡ source-fiber i)
  TargetAdmit q = Σ Index (λ i → q ≡ local-fiber i)
  module S = Resolution.Full ℓ-zero SourceAdmit
  module T = Resolution.Full ℓ-zero TargetAdmit
  -- Target seeds contain only the one canonical local context and input color.
  -- Source shifts are introduced by the existing native E operation.
  chart-fiber : Index → G.Package
  chart-fiber i = N.E-package X.Shift (λ _ → local-fiber i) (fst i)
  chart-proof : (i : Index) → T.Resolve (chart-fiber i)
  chart-proof i = T.apply (N.E-kind , X.Shift , (λ _ → local-fiber i) , fst i)
    (λ { (lift s) → T.seed (i , refl) })
  row-law : Iso SourceRow (Σ X.Shift (λ _ → LocalRow))
  Iso.fun row-law (X.prepared s , c) = s , (root-context , c)
  Iso.inv row-law (s , (root-context , c)) = X.prepared s , c
  Iso.rightInv row-law (s , (root-context , c)) = refl
  Iso.leftInv row-law (X.prepared s , c) = refl

  -- Exactly the source operation fragment required by the query compiler.
  data Program : Type (ℓ-suc ℓ-zero) where
    input : Index → Program
    all : (I : Type) → (I → Program) → Program
    pick : (I : Type) → (I → Program) → I → Program
  source target : Program → G.Package
  source (input i) = source-fiber i
  source (all I F) = N.Pi-package I (λ i → source (F i))
  source (pick I F j) = N.E-package I (λ i → source (F i)) j
  target (input i) = chart-fiber i
  target (all I F) = N.Pi-package I (λ i → target (F i))
  target (pick I F j) = N.E-package I (λ i → target (F i)) j
  source-proof : (p : Program) → S.Resolve (source p)
  source-proof (input i) = S.seed (i , refl)
  source-proof (all I F) = S.apply (N.P-kind , I , (λ i → source (F i))) (λ { (lift i) → source-proof (F i) })
  source-proof (pick I F j) = S.apply (N.E-kind , I , (λ i → source (F i)) , j) (λ { (lift i) → source-proof (F i) })
  target-proof : (p : Program) → T.Resolve (target p)
  target-proof (input i) = chart-proof i
  target-proof (all I F) = T.apply (N.P-kind , I , (λ i → target (F i))) (λ { (lift i) → target-proof (F i) })
  target-proof (pick I F j) = T.apply (N.E-kind , I , (λ i → target (F i)) , j) (λ { (lift i) → target-proof (F i) })

  value-law : (p : Program) → Iso (N.Ty (source p)) (N.Ty (target p))
  value-law (input i) = row-law
  Iso.fun (value-law (all I F)) v i = Iso.fun (value-law (F i)) (v i)
  Iso.inv (value-law (all I F)) v i = Iso.inv (value-law (F i)) (v i)
  Iso.rightInv (value-law (all I F)) v = funExt (λ i → Iso.rightInv (value-law (F i)) (v i))
  Iso.leftInv (value-law (all I F)) v = funExt (λ i → Iso.leftInv (value-law (F i)) (v i))
  Iso.fun (value-law (pick I F j)) (i , v) = i , Iso.fun (value-law (F i)) v
  Iso.inv (value-law (pick I F j)) (i , v) = i , Iso.inv (value-law (F i)) v
  Iso.rightInv (value-law (pick I F j)) (i , v) t = i , Iso.rightInv (value-law (F i)) v t
  Iso.leftInv (value-law (pick I F j)) (i , v) t = i , Iso.leftInv (value-law (F i)) v t
  value-square : (p : Program) → Iso.fun (value-law p) (N.value (source p)) ≡ N.value (target p)
  value-square (input i) = refl
  value-square (all I F) = funExt (λ i → value-square (F i))
  value-square (pick I F j) t = j , value-square (F j) t
  input-reference-square : (i : Index) (l : X.Label)
    → chart-reference (fst (N.value (chart-fiber i))) (fst (snd (N.value (chart-fiber i)))) l
      ≡ X.reference (X.region-context i) l
  input-reference-square i l = reference-square (fst i) l
  input-color-square : (i : Index) → snd (snd (N.value (chart-fiber i))) ≡ color i
  input-color-square i = refl

  module Queries (k n : ℕ) (letters : Slot k → X.Shift) where
    module Q = X.Query radius k n r letters color
    empty-program : Program
    empty-program = all ⊥ (λ ())
    empty-source : source empty-program ≡ Q.empty-package
    empty-source = cong (N.Pi-package ⊥) (funExt (λ ()))
    body-program : (s : X.Shift) → Q.Decision s → Program
    body-program s (Q.inside h) = pick Index input (s , h)
    body-program s (Q.outside h) = pick (¬ X.Member radius s) (λ _ → empty-program) h
    body-source : (s : X.Shift) (d : Q.Decision s) → source (body-program s d) ≡ Q.body s d
    body-source s (Q.inside h) = refl
    body-source s (Q.outside h) = cong (λ q → N.E-package (¬ X.Member radius s) (λ _ → q) h) empty-source
    instruction-program : Q.Request → Program
    instruction-program w = body-program (Q.A.phi w) (Q.classify (Q.A.phi w))
    instruction-source : (w : Q.Request) → source (instruction-program w) ≡ Q.instruction w
    instruction-source w = body-source (Q.A.phi w) (Q.classify (Q.A.phi w))
    result-program : Q.Request → Program
    result-program w = all Q.Component (λ { Q.prepared-input → all Index input
      ; Q.compiled-program → all Q.Request instruction-program
      ; Q.answer → pick Q.Request instruction-program w })
    result-source : (w : Q.Request) → source (result-program w) ≡ Q.result-package w
    result-source w = cong (N.Pi-package Q.Component) (funExt (λ
      { Q.prepared-input → refl
      ; Q.compiled-program → cong (N.Pi-package Q.Request) (funExt instruction-source)
      ; Q.answer → cong (λ F → N.E-package Q.Request F w) (funExt instruction-source) }))
    interpreted-result : (w : Q.Request) → T.Resolve (target (result-program w))
    interpreted-result w = target-proof (result-program w)
    interpreted-value : (w : Q.Request)
      → Iso.fun (value-law (result-program w)) (N.value (source (result-program w)))
        ≡ N.value (target (result-program w))
    interpreted-value w = value-square (result-program w)
