{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidBoundary where

open import Cubical.Foundations.Prelude hiding (J)

-- A bounded fragment of a dg category at exactly the degrees used by the
-- conductor–Morse boundary. Superscripts are written in names for portability.
-- J, Q and F are object labels; the six Hom-degree types are kept distinct.
record DGPyramidBoundary {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    SourceObj GenericObj SupportedObj : Type ℓ

    JQminus1 JQzero : Type ℓ
    QFtwo QFthree : Type ℓ
    JFone JFtwo : Type ℓ

    zeroQFthree : QFthree
    zeroJFtwo : JFtwo
    addJFone : JFone → JFone → JFone
    negJFone : JFone → JFone
    addJFtwo : JFtwo → JFtwo → JFtwo
    negJFtwo : JFtwo → JFtwo

    deltaJQ : JQminus1 → JQzero
    deltaQF : QFtwo → QFthree
    deltaJF : JFone → JFtwo

    -- Composition at the three degree pairs needed by Leibniz.
    compose20 : QFtwo → JQzero → JFtwo
    compose2minus1 : QFtwo → JQminus1 → JFone
    compose3minus1 : QFthree → JQminus1 → JFtwo

    q : JQzero
    e : QFtwo
    hM : JQminus1
    HC : JFone

    morseFace : deltaJQ hM ≡ q
    eClosed : deltaQF e ≡ zeroQFthree
    conductorFace : deltaJF HC ≡ compose20 e q

    -- Degree(e)=2 is even, hence the positive second Leibniz term.
    compositionBoundary :
      deltaJF (compose2minus1 e hM) ≡
      addJFtwo (compose3minus1 (deltaQF e) hM)
        (compose20 e (deltaJQ hM))

    deltaDifference : (x y : JFone) →
      deltaJF (addJFone x (negJFone y)) ≡
      addJFtwo (deltaJF x) (negJFtwo (deltaJF y))

    composeZero : compose3minus1 zeroQFthree hM ≡ zeroJFtwo
    zeroPlus : (x : JFtwo) → addJFtwo zeroJFtwo x ≡ x
    differenceSelf : (x : JFtwo) → addJFtwo x (negJFtwo x) ≡ zeroJFtwo

open DGPyramidBoundary public

-- Mathematical-name accessors for packets stated directly with J, Q, F,
-- h_M and H_C. The descriptive record fields remain stable for existing code.
J : {ℓ : Level} (P : DGPyramidBoundary {ℓ}) → Type ℓ
J = SourceObj

Q : {ℓ : Level} (P : DGPyramidBoundary {ℓ}) → Type ℓ
Q = GenericObj

F : {ℓ : Level} (P : DGPyramidBoundary {ℓ}) → Type ℓ
F = SupportedObj

h_M : {ℓ : Level} (P : DGPyramidBoundary {ℓ}) → JQminus1 P
h_M = hM

H_C : {ℓ : Level} (P : DGPyramidBoundary {ℓ}) → JFone P
H_C = HC

-- The face discrepancy. This is defined before any filler or framing claim.
pyramidDiscrepancy : {ℓ : Level} (P : DGPyramidBoundary {ℓ}) → JFone P
pyramidDiscrepancy P =
  addJFone P (HC P) (negJFone P (compose2minus1 P (e P) (hM P)))

-- The public mathematical spelling is judgmentally the same discrepancy.
namedDiscrepancyEquation : {ℓ : Level} (P : DGPyramidBoundary {ℓ}) →
  pyramidDiscrepancy P ≡
  addJFone P (H_C P)
    (negJFone P (compose2minus1 P (e P) (h_M P)))
namedDiscrepancyEquation P = refl

-- Closure is derived from the two face equations, closedness of e, and the
-- graded composition law. It is not an additional field of the record.
pyramidDiscrepancyClosed : {ℓ : Level} (P : DGPyramidBoundary {ℓ}) →
  deltaJF P (pyramidDiscrepancy P) ≡ zeroJFtwo P
pyramidDiscrepancyClosed P =
  deltaDifference P (HC P) (compose2minus1 P (e P) (hM P))
  ∙ cong₂ (addJFtwo P)
      (conductorFace P)
      (cong (negJFtwo P) (compositionBoundary P))
  ∙ cong (λ t → addJFtwo P (compose20 P (e P) (q P))
      (negJFtwo P t))
      (cong₂ (addJFtwo P)
        (cong (λ d → compose3minus1 P d (hM P)) (eClosed P)
          ∙ composeZero P)
        (cong (compose20 P (e P)) (morseFace P))
        ∙ zeroPlus P (compose20 P (e P) (q P)))
  ∙ differenceSelf P (compose20 P (e P) (q P))

-- Directly exported statement δ(H_C - e ∘ h_M) = 0.
namedPyramidDiscrepancyClosed : {ℓ : Level} (P : DGPyramidBoundary {ℓ}) →
  deltaJF P
    (addJFone P (H_C P)
      (negJFone P (compose2minus1 P (e P) (h_M P))))
  ≡ zeroJFtwo P
namedPyramidDiscrepancyClosed P = pyramidDiscrepancyClosed P

-- Deliberately absent: a filler, frame predicates, source comparison adapters,
-- or claims that any current Marici packet instantiates all fields.
