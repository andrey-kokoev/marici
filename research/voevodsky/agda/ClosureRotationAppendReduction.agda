{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureRotationAppendReduction where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (rUnit)
import Cubical.HITs.Pushout.Base as PO
open import ClosureFiniteGluingNormalization using (module LiftSpan)
open import ClosureGeneralRotationAdmission using (module IdentitySpan)
open import ClosureGluingReassociation using (module Chain)
open import ClosureGeneralSpanCoherence using (module Naturality; module Composition)
import ClosureSubtreeRotationAdmission as Earlier

module Reduction (K : Type) (Piece : K → Type) (Boundary : K → K → Type)
  (attachL : {a b : K} → Boundary a b → Piece a)
  (attachR : {a b : K} → Boundary a b → Piece b) where
  module G = Earlier.Subtrees K Piece Boundary attachL attachR
  open G.G.A.N

  -- This remaining coherence depends ONLY on three words, not on choices
  -- of bracketings realizing them. It is an explicit proof obligation, not an axiom.
  module Words {a b c d e f : K}
    (u : Word a b) (v : Word c d) (w : Word e f) where
    association = G.appendAssociative u v w
    module Raw = Chain (Normal u) (Normal v) (Normal w)
      (Boundary b c) (Boundary d e)
      (λ s → last u (attachL s)) (λ s → first v (attachR s))
      (λ t → last v (attachL t)) (λ t → first w (attachR t))

    module Left = LiftSpan Raw.attachLeft (λ t → first w (attachR t))
      (λ t → last (u ++ v) (attachL t)) (λ t → first w (attachR t))
      (idEquiv (Boundary d e)) (appendFrame u v) (idEquiv (Normal w))
      (funExt (λ t → appendLast u v (attachL t))) refl

    module Right = LiftSpan (λ s → last u (attachL s)) Raw.attachRight
      (λ s → last u (attachL s)) (λ s → first (v ++ w) (attachR s))
      (idEquiv (Boundary b c)) (idEquiv (Normal u)) (appendFrame v w)
      refl (funExt (λ s → appendFirst v w (attachR s)))

    leftFlat : Raw.Left → Normal ((u ++ v) ++ w)
    leftFlat x = equivFun (appendFrame (u ++ v) w) (equivFun Left.equivalence x)
    rightFlat : Raw.Right → Normal (u ++ (v ++ w))
    rightFlat x = equivFun (appendFrame u (v ++ w)) (equivFun Right.equivalence x)

    returnIndex : Normal (u ++ (v ++ w)) → Normal ((u ++ v) ++ w)
    returnIndex = transport (λ i → Normal (sym association i))

    AppendSquare : Type
    AppendSquare = (x : Raw.Left) → returnIndex (rightFlat (Raw.associate x)) ≡ leftFlat x

  -- The singleton base case is proved directly, with identity-span path
  -- corrections and the actual constant-family transport retained.
  module SingleLeft (a : K) {b c d e : K} (v : Word b c) (w : Word d e) where
    module W = Words (single a) v w
    module Id = IdentitySpan W.Raw.attachLeft (λ t → first w (attachR t))

    square : W.AppendSquare
    square x = transportRefl (W.rightFlat (W.Raw.associate x))
      ∙ cong (λ z → W.rightFlat (W.Raw.associate z)) (sym (Id.unchanged x))

  -- No restriction on ANY of the three subtree arguments below.
  module Trees {a b c d e f : K}
    {u : Word a b} {v : Word c d} {w : Word e f}
    (p : Bracket u) (q : Bracket v) (r : Bracket w) where
    module W = Words u v w
    module Indexed = G.ReindexRotation p q r
    module Nat = Naturality
      (λ s → lastAt p (attachL s)) (λ s → firstAt q (attachR s))
      (λ t → lastAt q (attachL t)) (λ t → firstAt r (attachR t))
      (λ s → last u (attachL s)) (λ s → first v (attachR s))
      (λ t → last v (attachL t)) (λ t → first w (attachR t))
      (normalize p) (normalize q) (normalize r)
      (funExt (λ s → normalizeLast p (attachL s)))
      (funExt (λ s → normalizeFirst q (attachR s)))
      (funExt (λ t → normalizeLast q (attachL t)))
      (funExt (λ t → normalizeFirst r (attachR t)))

    module LC = Composition Nat.Source.attachLeft (λ t → firstAt r (attachR t))
      Nat.Target.attachLeft (λ t → first w (attachR t))
      (λ t → last (u ++ v) (attachL t)) (λ t → first w (attachR t))
      Nat.AB.equivalence (normalize r) (appendFrame u v) (idEquiv (Normal w))
      (λ i t → PO.inr (normalizeLast q (attachL t) i))
      (funExt (λ t → normalizeFirst r (attachR t)))
      (funExt (λ t → appendLast u v (attachL t))) refl

    module RC = Composition (λ s → lastAt p (attachL s)) Nat.Source.attachRight
      (λ s → last u (attachL s)) Nat.Target.attachRight
      (λ s → last u (attachL s)) (λ s → first (v ++ w) (attachR s))
      (normalize p) Nat.BC.equivalence (idEquiv (Normal u)) (appendFrame v w)
      (funExt (λ s → normalizeLast p (attachL s)))
      (λ i s → PO.inl (normalizeFirst q (attachR s) i))
      refl (funExt (λ s → appendFirst v w (attachR s)))

    rightIdentity : compEquiv (normalize r) (idEquiv (Normal w)) ≡ normalize r
    rightIdentity = equivEq refl
    leftIdentity : compEquiv (normalize p) (idEquiv (Normal u)) ≡ normalize p
    leftIdentity = equivEq refl

    leftChildren : I → Nat.Source.Left ≃ Join (u ++ v) w
    leftChildren i = LiftSpan.equivalence Nat.Source.attachLeft (λ t → firstAt r (attachR t))
      (λ t → last (u ++ v) (attachL t)) (λ t → first w (attachR t))
      (idEquiv (Boundary d e)) (normalize (fork p q)) (rightIdentity i)
      (funExt (λ t → normalizeLast (fork p q) (attachL t)))
      (funExt (λ t → sym (rUnit (normalizeFirst r (attachR t))) i))

    rightChildren : I → Nat.Source.Right ≃ Join u (v ++ w)
    rightChildren i = LiftSpan.equivalence (λ s → lastAt p (attachL s)) Nat.Source.attachRight
      (λ s → last u (attachL s)) (λ s → first (v ++ w) (attachR s))
      (idEquiv (Boundary b c)) (leftIdentity i) (normalize (fork q r))
      (funExt (λ s → sym (rUnit (normalizeLast p (attachL s))) i))
      (funExt (λ s → normalizeFirst (fork q r) (attachR s)))

    leftToForm : equivFun (normalize Indexed.leftTree) ≡
      (λ x → W.leftFlat (equivFun Nat.Left.equivalence x))
    leftToForm = sym (λ i x → equivFun (appendFrame (u ++ v) w) (equivFun (leftChildren i) x))
      ∙ funExt (λ x → cong (equivFun (appendFrame (u ++ v) w)) (sym (LC.compositionAt x)))

    rightToForm : equivFun (normalize Indexed.nativeRight) ≡
      (λ x → W.rightFlat (equivFun Nat.Right.equivalence x))
    rightToForm = sym (λ i x → equivFun (appendFrame u (v ++ w)) (equivFun (rightChildren i) x))
      ∙ funExt (λ x → cong (equivFun (appendFrame u (v ++ w))) (sym (RC.compositionAt x)))

    -- The general admission follows once the WORD-ONLY square is proved.
    -- No arbitrary-subtree normalization square is supplied as a hypothesis.
    abstract
      rotationSquare : W.AppendSquare → Indexed.NormalizationSquare
      rotationSquare appendSquare x =
        sym (fromPathP (λ i → equivFun (Indexed.normalizationPath i)
          (transport-filler Indexed.realizationPath (Nat.Source.associate x) i)))
        ∙ cong W.returnIndex (cong (λ F → F (Nat.Source.associate x)) rightToForm)
        ∙ cong (λ z → W.returnIndex (W.rightFlat z)) (sym (Nat.naturalityAt x))
        ∙ appendSquare (equivFun Nat.Left.equivalence x)
        ∙ sym (cong (λ F → F x) leftToForm)

    abstract
      blockSquareOnSource : Indexed.NormalizationSquare → (x : Nat.Source.Left) →
        W.returnIndex (W.rightFlat (Nat.Target.associate (equivFun Nat.Left.equivalence x))) ≡
        W.leftFlat (equivFun Nat.Left.equivalence x)
      blockSquareOnSource square x =
        cong (λ z → W.returnIndex (W.rightFlat z)) (Nat.naturalityAt x)
        ∙ cong W.returnIndex (sym (cong (λ F → F (Nat.Source.associate x)) rightToForm))
        ∙ fromPathP (λ i → equivFun (Indexed.normalizationPath i)
          (transport-filler Indexed.realizationPath (Nat.Source.associate x) i))
        ∙ square x ∙ cong (λ F → F x) leftToForm

      -- Conversely, any proof for this native reindexed rotation supplies
      -- the word-only square. No claim of proof irrelevance is involved.
      recoverAppendSquare : Indexed.NormalizationSquare → W.AppendSquare
      recoverAppendSquare square z =
        sym (cong (λ y → W.returnIndex (W.rightFlat (Nat.Target.associate y)))
          (secEq Nat.Left.equivalence z))
        ∙ blockSquareOnSource square (invEq Nat.Left.equivalence z)
        ∙ cong W.leftFlat (secEq Nat.Left.equivalence z)

    admit : W.AppendSquare → Indexed.E.Admitted Indexed.leftTree Indexed.rightTree
    admit square = Indexed.admit (rotationSquare square)

  -- Reconstruct the entire previously proved family from the word base
  -- case, without importing the middle-subtree admission theorem.
  module LeftLeaf (a : K) {b c d e : K}
    {v : Word b c} {w : Word d e} (q : Bracket v) (r : Bracket w) where
    module T = Trees (leaf a) q r
    module Base = SingleLeft a v w

    forward : T.Indexed.E.Admitted T.Indexed.leftTree T.Indexed.rightTree
    forward = T.admit Base.square
