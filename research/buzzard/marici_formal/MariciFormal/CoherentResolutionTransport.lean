import MariciFormal.CoherentResolution
import Mathlib.FieldTheory.RatFunc.Defs
import Mathlib.Tactic

/-! Stable rank-one transport and holonomy obstructions for coherent resolutions. -/

namespace MariciFormal

/-- An unoriented polygon diagonal. Boundary-edge exclusion is deliberately
separate: this predicate records only distinct, non-neighbouring endpoints. -/
def PolygonDiagonal (n : ℕ) (a b : Fin n) : Prop :=
  a ≠ b ∧ a.val + 1 ≠ b.val ∧ b.val + 1 ≠ a.val

/-- Strict interlacing in the declared linear vertex order. This is the exact
crossing convention used below; cyclic wrap-around is handled by reordering the
four endpoints before applying it. -/
def DiagonalsCross {n : ℕ} (a b c d : Fin n) : Prop :=
  (a.val < c.val ∧ c.val < b.val ∧ b.val < d.val) ∨
  (c.val < a.val ∧ a.val < d.val ∧ d.val < b.val)

/-- A finite type-A partial triangulation: a finite set of diagonals with no
strictly interlacing pair. -/
structure PartialTriangulation (m : ℕ) where
  diagonals : Finset (Fin (m + 3) × Fin (m + 3))
  valid : ∀ e ∈ diagonals, PolygonDiagonal (m + 3) e.1 e.2
  noncrossing : ∀ e ∈ diagonals, ∀ f ∈ diagonals,
    ¬ DiagonalsCross e.1 e.2 f.1 f.2

instance (m : ℕ) : LE (PartialTriangulation m) :=
  ⟨fun P Q => P.diagonals ⊆ Q.diagonals⟩

/-- The empty partial triangulation, the cone point of the inclusion poset. -/
def emptyPartialTriangulation (m : ℕ) : PartialTriangulation m where
  diagonals := ∅
  valid := by simp
  noncrossing := by simp

@[simp] theorem emptyPartialTriangulation_le (m : ℕ) (P : PartialTriangulation m) :
    emptyPartialTriangulation m ≤ P := by
  intro e he
  change e ∈ (∅ : Finset (Fin (m + 3) × Fin (m + 3))) at he
  simp at he

section RankOne

variable {K V : Type*} [Field K]

/-- The rank-one weighted coboundary attached to an oriented edge. -/
def weightedCoboundary (rho : V → V → K) (f : V → K) (u v : V) : K :=
  f v - rho u v * f u

/-- Ratios produced by a nowhere-zero vertex weight. -/
def vertexRatio (w : V → K) (u v : V) : K := w v / w u

/-- Diagonal rescaling converts a vertex-ratio coboundary to the ordinary
coboundary. This is the componentwise chain-isomorphism identity. -/
theorem vertexRatio_diagonal_transport (w f : V → K)
    (hw : ∀ v, w v ≠ 0) (u v : V) :
    weightedCoboundary (vertexRatio w) (fun x => w x * f x) u v =
      w v * (f v - f u) := by
  simp only [weightedCoboundary, vertexRatio]
  field_simp [hw u]

/-- Vertex ratios have unit holonomy around every finite closed walk. -/
theorem vertexRatio_closed_holonomy (w : V → K) (hw : ∀ v, w v ≠ 0)
    (a b c d : V) :
    vertexRatio w a b * vertexRatio w b c *
      vertexRatio w c d * vertexRatio w d a = 1 := by
  simp only [vertexRatio]
  field_simp [hw a, hw b, hw c, hw d]

/-- The exact two-step face residual. It vanishes precisely when direct and
composite rank-one transports agree (for a nonzero coefficient). -/
def triangleTransportResidual (rho : V → V → K) (a b c : V) (x : K) : K :=
  (rho b c * rho a b - rho a c) * x

@[simp] theorem triangleTransportResidual_formula
    (rho : V → V → K) (a b c : V) (x : K) :
    triangleTransportResidual rho a b c x =
      (rho b c * rho a b - rho a c) * x := rfl

/-- Non-flat triangular transport obstructs square-zero of the corresponding
rank-one twisted boundary; the residual is retained rather than discarded. -/
theorem triangle_holonomy_obstructs_square_zero
    (rho : V → V → K) (a b c : V) (x : K)
    (hx : x ≠ 0) (hface : rho b c * rho a b ≠ rho a c) :
    triangleTransportResidual rho a b c x ≠ 0 := by
  exact mul_ne_zero (sub_ne_zero.mpr hface) hx

/-- Exact residual around a declared square. -/
def squareHolonomyResidual (rho : V → V → K) (a b c d : V) (x : K) : K :=
  (rho a b * rho b c * rho c d * rho d a - 1) * x

/-- Exact residual around a declared pentagon. -/
def pentagonHolonomyResidual (rho : V → V → K)
    (a b c d e : V) (x : K) : K :=
  (rho a b * rho b c * rho c d * rho d e * rho e a - 1) * x

/-- Non-unit square holonomy forces a nonzero boundary-square residual. -/
theorem nonunit_square_holonomy_obstruction
    (rho : V → V → K) (a b c d : V) (x : K) (hx : x ≠ 0)
    (hhol : rho a b * rho b c * rho c d * rho d a ≠ 1) :
    squareHolonomyResidual rho a b c d x ≠ 0 := by
  exact mul_ne_zero (sub_ne_zero.mpr hhol) hx

/-- Non-unit pentagon holonomy forces a nonzero boundary-square residual. -/
theorem nonunit_pentagon_holonomy_obstruction
    (rho : V → V → K) (a b c d e : V) (x : K) (hx : x ≠ 0)
    (hhol : rho a b * rho b c * rho c d * rho d e * rho e a ≠ 1) :
    pentagonHolonomyResidual rho a b c d e x ≠ 0 := by
  exact mul_ne_zero (sub_ne_zero.mpr hhol) hx

/-- Consequently, a vertex-coboundary system cannot carry non-unit square
holonomy. -/
theorem nonunit_square_not_vertexRatio
    (rho : V → V → K) (a b c d : V)
    (hhol : rho a b * rho b c * rho c d * rho d a ≠ 1) :
    ¬ ∃ w : V → K, (∀ v, w v ≠ 0) ∧ rho = vertexRatio w := by
  rintro ⟨w, hw, rfl⟩
  exact hhol (vertexRatio_closed_holonomy w hw a b c d)

end RankOne

end MariciFormal
