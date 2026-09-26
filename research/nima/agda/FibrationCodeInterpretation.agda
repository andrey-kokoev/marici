{-# OPTIONS --safe --cubical --guardedness #-}
module FibrationCodeInterpretation where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence using (ua; ua-gluePt; pathToEquiv)
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv-snd; Σ-cong-equiv)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
import WholePackageSigmaPi as Old
import WholePackageResolution as Resolution
import ProofRelevantCoherenceClosure as Compatibility
import FibrationSigmaPiBridge as Bridge
import TableFibrationCycle as Table
import BoundaryGeneratedQuestions as Boundary

Pointed : (ℓ : Level) → Type (ℓ-suc ℓ)
Pointed ℓ = Σ (Type ℓ) (λ A → A)
Compatible : {ℓ : Level} → Pointed ℓ → Pointed ℓ → Type ℓ
Compatible a b = Σ (fst a ≃ fst b) (λ e → equivFun e (snd a) ≡ snd b)
compose-compatible : {ℓ : Level} {a b c : Pointed ℓ}
  → Compatible a b → Compatible b c → Compatible a c
compose-compatible (e , p) (f , q) = compEquiv e f , cong (equivFun f) p ∙ q

Compare : {ℓ : Level} (A B : Type ℓ) → A ≃ B → Type ℓ
Compare A B e = Σ A (λ x → Σ B (λ y → equivFun e x ≡ y))

-- Same complete constructor metadata, new recursive VALUE interpretation.
-- This is an annotated fiber/section interpretation, not a claim that two
-- bare regroupings have the semantics of E and Pi.
module View (ℓ : Level) where
  open Old.Universe ℓ
  mutual
    Value : Code → Type ℓ
    Value (atom A) = A
    Value (E I F) = Bridge.Family.Total I (λ i → Value (F i))
    Value (Pi I F) = Bridge.Family.Sections I (λ i → Value (F i))
    Value (paths C x y) = equivFun (code-equivalence C) x ≡ equivFun (code-equivalence C) y
    Value (maps C D) = Value C → Value D
    Value (equivalences C D) = Value C ≃ Value D
    Value (retain C x D) = Value D
    Value (comparison C D e) = Compare (Value C) (Value D)
      (transport (λ i → ua (code-equivalence C) i ≃ ua (code-equivalence D) i) e)

    code-equivalence : (C : Code) → El C ≃ Value C
    code-equivalence (atom A) = idEquiv A
    code-equivalence (E I F) = compEquiv
      (Σ-cong-equiv-snd (λ i → code-equivalence (F i)))
      (isoToEquiv (Bridge.Family.total-iso I (λ i → Value (F i))))
    code-equivalence (Pi I F) = compEquiv
      (equivΠCod (λ i → code-equivalence (F i)))
      (isoToEquiv (Bridge.Family.sections-iso I (λ i → Value (F i))))
    code-equivalence (paths C x y) = Compatibility.pathLift (code-equivalence C)
    code-equivalence (maps C D) = pathToEquiv
      (λ i → ua (code-equivalence C) i → ua (code-equivalence D) i)
    code-equivalence (equivalences C D) = pathToEquiv
      (λ i → ua (code-equivalence C) i ≃ ua (code-equivalence D) i)
    code-equivalence (retain C x D) = code-equivalence D
    code-equivalence (comparison C D e) = pathToEquiv
      (λ i → Compare (ua (code-equivalence C) i) (ua (code-equivalence D) i)
        (transport-filler (λ j → ua (code-equivalence C) j ≃ ua (code-equivalence D) j) e i))

  Package : Type (ℓ-suc ℓ)
  Package = Σ Code Value
  old-sigma : Iso Complete (Σ Code El)
  Iso.fun old-sigma q = expression q , value q
  Iso.inv old-sigma (c , v) = pack c v
  Iso.leftInv old-sigma q = refl
  Iso.rightInv old-sigma (c , v) = refl
  package-equivalence : Complete ≃ Package
  package-equivalence = compEquiv (isoToEquiv old-sigma) (Σ-cong-equiv-snd code-equivalence)
  package-iso : Iso Complete Package
  package-iso = equivToIso package-equivalence
  encode : Complete → Package
  encode = Iso.fun package-iso
  decode : Package → Complete
  decode = Iso.inv package-iso
  decode-encode : (q : Complete) → decode (encode q) ≡ q
  decode-encode = Iso.leftInv package-iso
  encode-decode : (q : Package) → encode (decode q) ≡ q
  encode-decode = Iso.rightInv package-iso
  code-retained : (q : Complete) → fst (encode q) ≡ expression q
  code-retained q = refl

  old-point : Complete → Pointed ℓ
  old-point q = El (expression q) , value q
  view-point : Package → Pointed ℓ
  view-point (c , v) = Value c , v
  pointed-path : (q : Complete) → old-point q ≡ view-point (encode q)
  pointed-path q i = ua (code-equivalence (expression q)) i ,
    ua-gluePt (code-equivalence (expression q)) i (value q)
  filler-path : (a b : Complete) → Compatible (old-point a) (old-point b)
    ≡ Compatible (view-point (encode a)) (view-point (encode b))
  filler-path a b i = Compatible (pointed-path a i) (pointed-path b i)
  filler-equivalence : (a b : Complete) → Compatible (old-point a) (old-point b)
    ≃ Compatible (view-point (encode a)) (view-point (encode b))
  filler-equivalence a b = pathToEquiv (filler-path a b)
  composition-commutes : (a b c : Complete)
    (f : Compatible (old-point a) (old-point b))
    (g : Compatible (old-point b) (old-point c))
    → equivFun (filler-equivalence a c) (compose-compatible f g)
      ≡ compose-compatible (equivFun (filler-equivalence a b) f) (equivFun (filler-equivalence b c) g)
  composition-commutes a b c f g = fromPathP (λ i → compose-compatible
    (transport-filler (filler-path a b) f i) (transport-filler (filler-path b c) g i))
  package-path-equivalence : (a b : Complete) → (a ≡ b) ≃ (encode a ≡ encode b)
  package-path-equivalence a b = Compatibility.pathLift package-equivalence

  E-computes : (I : Type ℓ) (F : I → Complete) (i : I)
    → snd (encode (E-package I F i))
      ≡ (i , (i , equivFun (code-equivalence (expression (F i))) (value (F i))) , refl)
  E-computes I F i = refl
  P-computes : (I : Type ℓ) (F : I → Complete)
    → snd (encode (Pi-package I F))
      ≡ (λ i → (i , equivFun (code-equivalence (expression (F i))) (value (F i))) , refl)
  P-computes I F = refl

  -- Every old readout transports through the proven equivalence. This is a
  -- transport theorem, not a check of an independently specified new readout.
  readout-commutes : {ℓ' : Level} {X : Type ℓ'} (f : Complete → X) (q : Complete)
    → f (decode (encode q)) ≡ f q
  readout-commutes f q = cong f (decode-encode q)

  module RuleBoundary where
    open Resolution.Generators ℓ
    input-view : (r : Rule) → Arity r → Package
    input-view r i = encode (input r i)
    output-view : Rule → Package
    output-view r = encode (output r)
    input-roundtrip : (r : Rule) (i : Arity r) → decode (input-view r i) ≡ input r i
    input-roundtrip r i = decode-encode (input r i)
    output-roundtrip : (r : Rule) → decode (output-view r) ≡ output r
    output-roundtrip r = decode-encode (output r)

    -- Transport of the EXISTING derivation theory along package-equivalence.
    -- This is not a new proof that regrouping alone implements the rules.
    ClosureView : (Complete → Type (ℓ-suc ℓ)) → Type (ℓ-suc ℓ)
    ClosureView S = Σ Package (λ v → Resolve S (decode v))
    closure-equivalence : (S : Complete → Type (ℓ-suc ℓ)) → Closure S ≃ ClosureView S
    closure-equivalence S = Σ-cong-equiv package-equivalence
      (λ q → pathToEquiv (cong (Resolve S) (sym (decode-encode q))))

-- This endpoint type is exactly the previously checked comparison question.
boundary-filler-equivalence : (a b : Old.Universe.Complete ℓ-zero)
  → Boundary.Filler a b ≃ Compatible
      (View.view-point ℓ-zero (View.encode ℓ-zero a))
      (View.view-point ℓ-zero (View.encode ℓ-zero b))
boundary-filler-equivalence = View.filler-equivalence ℓ-zero

-- Reified derivations (all twelve schemas, including higher witnesses) are
-- retained exactly. They are carried as the original atom payload, not
-- claimed to be an independently implemented graph reduction calculus.
module RetainedDerivation (ℓ : Level) where
  open Old.Universe ℓ
  open Resolution.Generators ℓ
  module Next = View (ℓ-suc ℓ)
  encoded-derivation : {S : Complete → Type (ℓ-suc ℓ)} {q : Complete}
    → Resolve S q → Next.Package
  encoded-derivation d = Next.encode (reify-history d)
  derivation-recovered : {S : Complete → Type (ℓ-suc ℓ)} {q : Complete}
    (d : Resolve S q) → snd (snd (encoded-derivation d)) ≡ d
  derivation-recovered d = refl

-- Value-only tables cannot recover the constructor code. Both a plain atom
-- of function type and a maps code have exactly the same interpreted values.
module LostMetadata where
  open Old.Universe ℓ-zero
  record BareView : Type₁ where
    constructor bare
    field
      carrier : Type
      incidence : Table.Table carrier Unit carrier
      selected : carrier
  display : Complete → BareView
  display (pack c v) = bare (El c)
    (Table.table (El c) (λ x → x) (λ _ → tt) (λ x → x)) v
  q-atom q-map : Complete
  q-atom = pack (atom (Unit → Unit)) (λ x → x)
  q-map = pack (maps (atom Unit) (atom Unit)) (λ x → x)
  same-bare-view : display q-atom ≡ display q-map
  same-bare-view = refl
  is-map : Code → Bool
  is-map (maps _ _) = true
  is-map _ = false
  different-complete : q-atom ≡ q-map → ⊥
  different-complete p = false≢true (cong (λ q → is-map (expression q)) p)
  no-bare-recovery : (recover : BareView → Complete)
    → ((q : Complete) → recover (display q) ≡ q) → ⊥
  no-bare-recovery recover law = different-complete (sym (law q-atom) ∙ law q-map)
