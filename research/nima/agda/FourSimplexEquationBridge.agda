{-# OPTIONS --safe --cubical --guardedness #-}
module FourSimplexEquationBridge where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_; equivFun; invEq; retEq; secEq; compEquiv)
open import Cubical.Foundations.Isomorphism using (iso; isoToEquiv)
open import Cubical.Foundations.Path using (congPathEquiv)
open import Cubical.Foundations.Univalence using (pathToEquiv)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv)
import FourSimplexHorn as Cube
import TetrahedronPresentationBridge as Tetra
import MarkedTetrahedronCoherence as Marked
import RetainedTetrahedralPackage as Retained

-- This is the induced equation-family presentation of a four-cell, NOT an
-- identification with an independently defined old pentagon equation.
module Bridge {ℓ : Level} (A : Type ℓ)
  (v : Cube.Simplex.Vertices A)
  (e : Cube.Simplex.At.Edges A v)
  (a : Cube.Simplex.At.WithEdges.Faces A v e) where
  module C = Cube.Simplex A
  module E = C.At.WithEdges v e
  module F = E.WithFaces a
  module M = Marked.Tetrahedra A
  open C.Vertices v
  open C.At.Edges e
  open E.Faces a

  module B0123 = Tetra.FixedBoundaryTarget A E.edges0123
  module B0124 = Tetra.FixedBoundaryTarget A E.edges0124
  module B0134 = Tetra.FixedBoundaryTarget A E.edges0134
  module B0234 = Tetra.FixedBoundaryTarget A E.edges0234
  module B1234 = Tetra.FixedBoundaryTarget A E.edges1234

  O0123 = B0123.old-filler F.s0123
  O0124 = B0124.old-filler F.s0124
  O0134 = B0134.old-filler F.s0134
  O0234 = B0234.old-filler F.s0234
  O1234 = B1234.old-filler F.s1234

  e0123 : F.T0123 ≃ O0123
  e0123 = B0123.equivalence F.s0123
  e0124 : F.T0124 ≃ O0124
  e0124 = B0124.equivalence F.s0124
  e0134 : F.T0134 ≃ O0134
  e0134 = B0134.equivalence F.s0134
  e0234 : F.T0234 ≃ O0234
  e0234 = B0234.equivalence F.s0234
  e1234 : F.T1234 ≃ O1234
  e1234 = B1234.equivalence F.s1234

  -- The ten triangle translations are fixed globally through a, so every
  -- shared face has the same equation witness on both incident tetrahedra.
  record EquationHorn : Type ℓ where
    constructor equation-horn
    field
      t0123 : O0123
      t0124 : O0124
      t0134 : O0134
      t0234 : O0234

  to-equation-horn : F.Horn → EquationHorn
  to-equation-horn h = equation-horn
    (equivFun e0123 (F.Horn.t0123 h)) (equivFun e0124 (F.Horn.t0124 h))
    (equivFun e0134 (F.Horn.t0134 h)) (equivFun e0234 (F.Horn.t0234 h))
  from-equation-horn : EquationHorn → F.Horn
  from-equation-horn h = F.horn
    (invEq e0123 (EquationHorn.t0123 h)) (invEq e0124 (EquationHorn.t0124 h))
    (invEq e0134 (EquationHorn.t0134 h)) (invEq e0234 (EquationHorn.t0234 h))
  equation-horn-recovered : (h : EquationHorn)
    → to-equation-horn (from-equation-horn h) ≡ h
  equation-horn-recovered h i = equation-horn
    (secEq e0123 (EquationHorn.t0123 h) i) (secEq e0124 (EquationHorn.t0124 h) i)
    (secEq e0134 (EquationHorn.t0134 h) i) (secEq e0234 (EquationHorn.t0234 h) i)
  cubical-horn-recovered : (h : F.Horn)
    → from-equation-horn (to-equation-horn h) ≡ h
  cubical-horn-recovered h i = F.horn
    (retEq e0123 (F.Horn.t0123 h) i) (retEq e0124 (F.Horn.t0124 h) i)
    (retEq e0134 (F.Horn.t0134 h) i) (retEq e0234 (F.Horn.t0234 h) i)
  horn-equivalence : F.Horn ≃ EquationHorn
  horn-equivalence = isoToEquiv
    (iso to-equation-horn from-equation-horn equation-horn-recovered cubical-horn-recovered)

  CubicalBoundary EquationBoundary : Type ℓ
  CubicalBoundary = F.Horn × F.T1234
  EquationBoundary = EquationHorn × O1234
  boundary-equivalence : CubicalBoundary ≃ EquationBoundary
  boundary-equivalence = Σ-cong-equiv horn-equivalence (λ _ → e1234)

  cubical-boundary-recovered : (b : CubicalBoundary)
    → invEq boundary-equivalence (equivFun boundary-equivalence b) ≡ b
  cubical-boundary-recovered = retEq boundary-equivalence
  equation-boundary-recovered : (b : EquationBoundary)
    → equivFun boundary-equivalence (invEq boundary-equivalence b) ≡ b
  equation-boundary-recovered = secEq boundary-equivalence

  -- Each slice of the Cubical four-cell is itself a tetrahedron. Apply the
  -- fixed-boundary tetrahedron equivalence to that moving marked slice.
  moving-edges : (i : I) → M.Edges (e01 i) x2 x3 x4
  moving-edges i = record
    { e01 = a012 i ; e12 = e23 ; e02 = a013 i
    ; e23 = e34 ; e13 = e24 ; e03 = a014 i }
  moving-surface : (h : F.Horn) (i : I) → C.OnEdges.Surface (moving-edges i)
  moving-surface h i = C.OnEdges.surface
    (F.Horn.t0123 h i) a234 (F.Horn.t0124 h i) (F.Horn.t0134 h i)

  EquationFamily : F.Horn → I → Type ℓ
  EquationFamily h i = Tetra.FixedBoundaryTarget.old-filler A
    (moving-edges i) (moving-surface h i)
  slice-equivalence : (h : F.Horn) (i : I) → F.Family h i ≃ EquationFamily h i
  slice-equivalence h i = Tetra.FixedBoundaryTarget.equivalence A
    (moving-edges i) (moving-surface h i)

  -- The endpoint maps are exactly the independently chosen tetrahedron
  -- maps; no horn-derived replacement of the fifth tetrahedron is used.
  slice-start : (h : F.Horn) → slice-equivalence h i0 ≡ e0234
  slice-start h = refl
  slice-end : (h : F.Horn) → slice-equivalence h i1 ≡ e1234
  slice-end h = refl

  EquationFourCell : (h : F.Horn) → O1234 → Type ℓ
  EquationFourCell h t = PathP (EquationFamily h)
    (equivFun e0234 (F.Horn.t0234 h)) t
  fourcell-equivalence : (h : F.Horn) (t : F.T1234)
    → F.FourCell h t ≃ EquationFourCell h (equivFun e1234 t)
  fourcell-equivalence h t = congPathEquiv (slice-equivalence h)

  fourcell-map : (h : F.Horn) (t : F.T1234) (u : F.FourCell h t)
    → equivFun (fourcell-equivalence h t) u
      ≡ (λ i → equivFun (slice-equivalence h i) (u i))
  fourcell-map h t u = refl

  EquationMissing : F.Horn → Type ℓ
  EquationMissing h = Σ[ t ∈ O1234 ] EquationFourCell h t
  completion-equivalence : (h : F.Horn) → F.Missing h ≃ EquationMissing h
  completion-equivalence h = Σ-cong-equiv e1234 (fourcell-equivalence h)
  to-equations : (h : F.Horn) → F.Missing h → EquationMissing h
  to-equations h = equivFun (completion-equivalence h)
  to-cubical : (h : F.Horn) → EquationMissing h → F.Missing h
  to-cubical h = invEq (completion-equivalence h)
  cubical-completion-recovered : (h : F.Horn) (p : F.Missing h)
    → to-cubical h (to-equations h p) ≡ p
  cubical-completion-recovered h = retEq (completion-equivalence h)
  equation-completion-recovered : (h : F.Horn) (p : EquationMissing h)
    → to-equations h (to-cubical h p) ≡ p
  equation-completion-recovered h = secEq (completion-equivalence h)

  fifth-tetrahedron-preserved : (h : F.Horn) (p : F.Missing h)
    → fst (to-equations h p) ≡ equivFun e1234 (fst p)
  fifth-tetrahedron-preserved h p = refl

  equation-unique : (h : F.Horn) → isContr (EquationMissing h)
  equation-unique h = isContrSinglP (EquationFamily h)
    (equivFun e0234 (F.Horn.t0234 h))
  complete-then-translate : (h : F.Horn)
    → to-equations h (fst (F.unique h)) ≡ fst (equation-unique h)
  complete-then-translate h = isContr→isProp (equation-unique h) _ _

  -- An old-horn-indexed version, with no Cubical witness supplied by the
  -- caller. Its family is still induced by decoding the first three old
  -- tetrahedra; this is not an independently authored pentagon relation.
  OldFourCell : EquationHorn → O1234 → Type ℓ
  OldFourCell h t = PathP (EquationFamily (from-equation-horn h))
    (EquationHorn.t0234 h) t
  OldMissing : EquationHorn → Type ℓ
  OldMissing h = Σ[ t ∈ O1234 ] OldFourCell h t

  correct-start-fiber : (h : EquationHorn) (t : O1234)
    → EquationFourCell (from-equation-horn h) t ≃ OldFourCell h t
  correct-start-fiber h t = pathToEquiv
    (λ i → PathP (EquationFamily (from-equation-horn h))
      (secEq e0234 (EquationHorn.t0234 h) i) t)

  -- Reindex while holding the fifth tetrahedron fixed, then correct the
  -- initial endpoint by the section law. All five boundary maps are now
  -- exactly the independent tetrahedron equivalences, not derived choices.
  old-fourcell-equivalence : (h : F.Horn) (t : F.T1234)
    → F.FourCell h t ≃ OldFourCell (to-equation-horn h) (equivFun e1234 t)
  old-fourcell-equivalence h t = compEquiv (fourcell-equivalence h t)
    (compEquiv
      (pathToEquiv (λ i → EquationFourCell
        (cubical-horn-recovered h (~ i)) (equivFun e1234 t)))
      (correct-start-fiber (to-equation-horn h) (equivFun e1234 t)))

  old-completion-equivalence : (h : F.Horn)
    → F.Missing h ≃ OldMissing (to-equation-horn h)
  old-completion-equivalence h = Σ-cong-equiv e1234 (old-fourcell-equivalence h)

  old-fifth-tetrahedron-preserved : (h : F.Horn) (p : F.Missing h)
    → fst (equivFun (old-completion-equivalence h) p) ≡ equivFun e1234 (fst p)
  old-fifth-tetrahedron-preserved h p = refl

  OldFilled : Type ℓ
  OldFilled = Σ[ h ∈ EquationHorn ] OldMissing h
  filled-equivalence : F.Filled ≃ OldFilled
  filled-equivalence = Σ-cong-equiv horn-equivalence old-completion-equivalence
  old-filled-recovered : (p : OldFilled)
    → equivFun filled-equivalence (invEq filled-equivalence p) ≡ p
  old-filled-recovered = secEq filled-equivalence
  cubical-filled-recovered : (p : F.Filled)
    → invEq filled-equivalence (equivFun filled-equivalence p) ≡ p
  cubical-filled-recovered = retEq filled-equivalence
  supplied-horn-preserved : (p : F.Filled)
    → fst (equivFun filled-equivalence p) ≡ to-equation-horn (fst p)
  supplied-horn-preserved p = refl

  cubical-boundary : F.Filled → CubicalBoundary
  cubical-boundary (h , t , u) = h , t
  old-boundary : OldFilled → EquationBoundary
  old-boundary (h , t , u) = h , t
  boundary-square : (p : F.Filled)
    → old-boundary (equivFun filled-equivalence p)
      ≡ equivFun boundary-equivalence (cubical-boundary p)
  boundary-square (h , p) i = to-equation-horn h , old-fifth-tetrahedron-preserved h p i

  old-unique : (h : EquationHorn) → isContr (OldMissing h)
  old-unique h = isContrSinglP (EquationFamily (from-equation-horn h))
    (EquationHorn.t0234 h)
  old-completion-square : (h : F.Horn)
    → equivFun (old-completion-equivalence h) (fst (F.unique h))
      ≡ fst (old-unique (to-equation-horn h))
  old-completion-square h = isContr→isProp (old-unique (to-equation-horn h)) _ _

module TypedFixture where
  module F = Cube.TypedFixture
  module B = Bridge (Retained.TypedValue ℓ-zero) F.v F.e F.faces
  translated : B.EquationMissing F.horn
  translated = B.to-equations F.horn F.explicit
  recovered : B.to-cubical F.horn translated ≡ F.explicit
  recovered = B.cubical-completion-recovered F.horn F.explicit
  completion-square : B.to-equations F.horn (fst (F.H.unique F.horn))
    ≡ fst (B.equation-unique F.horn)
  completion-square = B.complete-then-translate F.horn
  old-filled : B.OldFilled
  old-filled = equivFun B.filled-equivalence (F.horn , F.explicit)
  full-roundtrip : invEq B.filled-equivalence old-filled ≡ (F.horn , F.explicit)
  full-roundtrip = B.cubical-filled-recovered (F.horn , F.explicit)
  old-completion-square : equivFun (B.old-completion-equivalence F.horn)
    (fst (F.H.unique F.horn)) ≡ fst (B.old-unique (B.to-equation-horn F.horn))
  old-completion-square = B.old-completion-square F.horn
