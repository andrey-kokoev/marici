{-# OPTIONS --safe --cubical --guardedness #-}
module NativeSharedReaderJoin where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sigma.Properties using (ΣPathP)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Unit.Base using (tt)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Bool.Properties using (false≢true)
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
import NativeTableResolution as Resolution

module G = Tables.Core ℓ-zero
module N = Rules.Native ℓ-zero

-- These are native constructions from supplied operand DERIVATIONS, not
-- seeds for a desired output. The shared-reader path is explicit input.
module Derived (Admit : G.Package → Type₁) where
  module R = Resolution.Full ℓ-zero Admit

  module Join (E : Type) (a b : G.Package)
    (readA : N.Ty a → E) (readB : N.Ty b → E)
    (agree : readA (N.value a) ≡ readB (N.value b)) where

    Compatible : Type
    Compatible = Σ[ x ∈ N.Ty a ] Σ[ y ∈ N.Ty b ] (readA x ≡ readB y)

    selected : Compatible
    selected = N.value a , N.value b , agree

    operand : Bool → G.Package
    operand false = a
    operand true = b

    loop : Bool → G.Package
    loop i = N.output (N.reflexivity-kind , operand i)

    provenance : G.Package
    provenance = N.Pi-package Bool loop

    result : G.Package
    result = N.E-package Compatible (λ _ → provenance) selected

    left : N.Ty result → N.Ty a
    left z = fst (fst z)
    right : N.Ty result → N.Ty b
    right z = fst (snd (fst z))
    shared : (z : N.Ty result) → readA (left z) ≡ readB (right z)
    shared z = snd (snd (fst z))

    -- Retained loops are not assumed contractible. In a set-valued fragment
    -- they add no value choices; with higher carriers they remain witnesses.
    loop-derivation : R.Resolve a → R.Resolve b → (i : Bool) → R.Resolve (loop i)
    loop-derivation da db false = R.apply (N.reflexivity-kind , a) (λ _ → da)
    loop-derivation da db true = R.apply (N.reflexivity-kind , b) (λ _ → db)

    provenance-derivation : R.Resolve a → R.Resolve b → R.Resolve provenance
    provenance-derivation da db = R.apply (N.P-kind , Bool , loop)
      (λ { (lift i) → loop-derivation da db i })

    derive : R.Resolve a → R.Resolve b → R.Resolve result
    derive da db = R.apply (N.E-kind , Compatible , (λ _ → provenance) , selected)
      (λ _ → provenance-derivation da db)

    -- Traverse actual native premise ports, recovering the input proofs,
    -- not merely their endpoints or images under a forgetful reader.
    recover-left : (da : R.Resolve a) (db : R.Resolve b)
      → R.premise (R.premise (R.premise (result , derive da db)
          (lift selected)) (lift false)) (lift tt) ≡ (a , da)
    recover-left da db = refl
    recover-right : (da : R.Resolve a) (db : R.Resolve b)
      → R.premise (R.premise (R.premise (result , derive da db)
          (lift selected)) (lift true)) (lift tt) ≡ (b , db)
    recover-right da db = refl

    left-selected : left (N.value result) ≡ N.value a
    left-selected = refl
    right-selected : right (N.value result) ≡ N.value b
    right-selected = refl

  module Exchange (E : Type) (a b : G.Package)
    (readA : N.Ty a → E) (readB : N.Ty b → E)
    (agree : readA (N.value a) ≡ readB (N.value b)) where
    module L = Join E a b readA readB agree
    module T = Join E b a readB readA (sym agree)

    law : Iso (N.Ty L.result) (N.Ty T.result)
    Iso.fun law ((x , y , p) , w) = (y , x , sym p) , λ { false → w true ; true → w false }
    Iso.inv law ((y , x , p) , w) = (x , y , sym p) , λ { false → w true ; true → w false }
    Iso.rightInv law z = ΣPathP (refl , funExt λ { false → refl ; true → refl })
    Iso.leftInv law z = ΣPathP (refl , funExt λ { false → refl ; true → refl })

    selected-law : Iso.fun law (N.value L.result) ≡ N.value T.result
    selected-law = ΣPathP (refl , funExt λ { false → refl ; true → refl })

    rule : N.Rule
    rule = N.compare-kind , L.result , T.result , isoToEquiv law , selected-law

    derive : R.Resolve a → R.Resolve b → R.Resolve (N.output rule)
    derive da db = R.apply rule
      (λ { (lift true) → L.derive da db ; (lift false) → T.derive db da })

    left-reader : (z : N.Ty L.result) → T.right (Iso.fun law z) ≡ L.left z
    left-reader z = refl
    right-reader : (z : N.Ty L.result) → T.left (Iso.fun law z) ≡ L.right z
    right-reader z = refl

-- An actual native preparation/operand family, with only its four tagged
-- supplied records admitted as seeds. This is a typed record-interface
-- instance, NOT a proof that these tags are Su-32 geometric occurrences.
data Reference : Type where
  P+ P- E+ E- : Reference
record RecordAt (r : Reference) : Type where
  constructor record-at
  field payload : Bool

module Prepared (registry : Reference → Bool) where
  input : Reference → G.Package
  input r = N.pack (G.atom-node (RecordAt r)) (record-at (registry r))

  data Seeds : G.Package → Type₁ where
    supplied : (r : Reference) → Seeds (input r)

  module D = Derived Seeds
  module R = D.R

  preparation : G.Package
  preparation = N.Pi-package Reference input
  preparation-derivation : R.Resolve preparation
  preparation-derivation = R.apply (N.P-kind , Reference , input)
    (λ { (lift r) → R.seed (supplied r) })

  reference : Bool → Bool → Reference
  reference _ true = E+
  reference false false = P+
  reference true false = P-

  channel : Bool → G.Package
  channel side = N.Pi-package Bool (λ i → input (reference side i))
  channel-derivation : (side : Bool) → R.Resolve (channel side)
  channel-derivation side = R.apply (N.P-kind , Bool , (λ i → input (reference side i)))
    (λ { (lift i) → snd (R.premise (preparation , preparation-derivation)
      (lift (reference side i))) })

  readShared : (side : Bool) → N.Ty (channel side) → RecordAt E+
  readShared side x = x true

  module J = D.Join (RecordAt E+) (channel false) (channel true)
    (readShared false) (readShared true) refl
  module X = D.Exchange (RecordAt E+) (channel false) (channel true)
    (readShared false) (readShared true) refl

  admitted-join : R.Resolve J.result
  admitted-join = J.derive (channel-derivation false) (channel-derivation true)
  admitted-exchange : R.Resolve (N.output X.rule)
  admitted-exchange = X.derive (channel-derivation false) (channel-derivation true)

  -- Keep the complete preparation (including unused E-) alongside the join.
  full-family : Bool → G.Package
  full-family false = preparation
  full-family true = J.result
  full : G.Package
  full = N.Pi-package Bool full-family
  admitted-full : R.Resolve full
  admitted-full = R.apply (N.P-kind , Bool , full-family)
    (λ { (lift false) → preparation-derivation ; (lift true) → admitted-join })

  unused-record-retained : N.value full false E- ≡ record-at (registry E-)
  unused-record-retained = refl

-- The source-derived joint does not turn either projection into an equivalence.
module Noninjective where
  module P = Prepared (λ _ → false)
  otherRight : N.Ty (P.channel true)
  otherRight false = record-at true
  otherRight true = record-at false
  z0 z1 : N.Ty P.J.result
  z0 = N.value P.J.result
  z1 = (N.value (P.channel false) , otherRight , refl) , N.value P.J.provenance
  same-left : P.J.left z0 ≡ P.J.left z1
  same-left = refl
  distinct-joints : z0 ≡ z1 → ⊥
  distinct-joints p = false≢true (cong (λ z → RecordAt.payload (P.J.right z false)) p)
