import Mathlib.Data.Set.Basic
import Mathlib.Order.Hom.Basic

/-! The set-theoretic core of polygon face factorization. -/

namespace Marici.FaceProduct

universe u v w

/-- Subsets containing the already chosen cuts. -/
def Face {α : Type u} (D : Set α) := {E : Set α // D ⊆ E}

/-- Removing the fixed cuts identifies their upper interval with arbitrary
subsets of the complement. -/
def faceEquivComplement {α : Type u} (D : Set α) :
    Face D ≃ Set {x : α // x ∉ D} where
  toFun E := {x | x.1 ∈ E.1}
  invFun A := ⟨D ∪ Subtype.val '' A, fun x hx => Or.inl hx⟩
  left_inv E := by
    apply Subtype.ext
    ext x
    constructor
    · rintro (hD | ⟨y, hy, hval⟩)
      · exact E.2 hD
      · simpa [← hval] using hy
    · intro hx
      by_cases hD : x ∈ D
      · exact Or.inl hD
      · exact Or.inr ⟨⟨x, hD⟩, hx, rfl⟩
  right_inv A := by
    ext x
    constructor
    · rintro (hD | ⟨y, hy, hval⟩)
      · exact False.elim (x.property hD)
      · have hyx : y = x := Subtype.ext hval
        simpa [hyx] using hy
    · intro hx
      exact Or.inr ⟨x, hx, rfl⟩

/-- An equivalence of underlying types induces an equivalence of powersets. -/
def powersetCongr {α : Type u} {β : Type v} (e : α ≃ β) : Set α ≃ Set β where
  toFun A := e '' A
  invFun B := e.symm '' B
  left_inv A := by
    ext x
    simp
  right_inv B := by
    ext y
    simp

/-- A subset of a dependent sum is exactly a family of subsets of its fibers. -/
def sigmaPowersetEquiv {ι : Type v} (β : ι → Type w) :
    Set (Sigma β) ≃ ((i : ι) → Set (β i)) where
  toFun A i := {x | Sigma.mk i x ∈ A}
  invFun B := {z | z.2 ∈ B z.1}
  left_inv A := by ext z; rfl
  right_inv B := by funext i; ext x; rfl

/-- A unique regional address decomposes subsets of admissible optional
diagonals into one subset per region. In polygon applications the source must
exclude diagonals crossing the fixed cuts; using the raw complement is too
large. -/
def regionalPowersetEquiv {α : Type u} {ι : Type v} (β : ι → Type w)
    (address : α ≃ Sigma β) : Set α ≃ ((i : ι) → Set (β i)) :=
  (powersetCongr address).trans (sigmaPowersetEquiv β)

/-- A unique regional address for every diagonal outside `D` implies the
unrestricted powerset equivalence below. Polygon dissections use
`regionalPowersetEquiv` with their smaller admissible-diagonal type. -/
def faceProductEquiv {α : Type u} {ι : Type v} (D : Set α)
    (β : ι → Type w) (address : {x : α // x ∉ D} ≃ Sigma β) :
    Face D ≃ ((i : ι) → Set (β i)) :=
  (faceEquivComplement D).trans ((powersetCongr address).trans (sigmaPowersetEquiv β))

/-- Nested regional addressing composes by ordinary equivalence composition;
this is the formal naturality mechanism for successive cuts. -/
def nestedAddress {α : Type u} {ι : Type v} {κ : Type w}
    (first : α ≃ ι) (second : ι ≃ κ) : α ≃ κ := first.trans second

@[simp] theorem nestedAddress_apply {α : Type u} {ι : Type v} {κ : Type w}
    (first : α ≃ ι) (second : ι ≃ κ) (x : α) :
    nestedAddress first second x = second (first x) := rfl

/-- Restrict an equivalence to predicates that it preserves and reflects. -/
def restrictEquiv {A : Type u} {B : Type v} (e : A ≃ B)
    (P : A → Prop) (Q : B → Prop) (compatible : ∀ a, P a ↔ Q (e a)) :
    {a : A // P a} ≃ {b : B // Q b} where
  toFun a := ⟨e a.1, (compatible a.1).mp a.2⟩
  invFun b := ⟨e.symm b.1, (compatible (e.symm b.1)).mpr (by simpa using b.2)⟩
  left_inv a := by
    apply Subtype.ext
    exact e.symm_apply_apply a.1
  right_inv b := by
    apply Subtype.ext
    exact e.apply_symm_apply b.1

/-- The face product restricted to noncrossing families. Geometry enters through
one exact compatibility theorem: a global refinement is noncrossing iff all of
its regional restrictions are noncrossing. -/
def dissectionFaceProductEquiv {α : Type u} {ι : Type v} (D : Set α)
    (β : ι → Type w) (address : {x : α // x ∉ D} ≃ Sigma β)
    (GlobalNoncrossing : Face D → Prop)
    (RegionalNoncrossing : ((i : ι) → Set (β i)) → Prop)
    (noncrossing_iff : ∀ E,
      GlobalNoncrossing E ↔ RegionalNoncrossing (faceProductEquiv D β address E)) :
    {E : Face D // GlobalNoncrossing E} ≃
      {A : (i : ι) → Set (β i) // RegionalNoncrossing A} :=
  restrictEquiv (faceProductEquiv D β address)
    GlobalNoncrossing RegionalNoncrossing noncrossing_iff

/-- When regional noncrossing is defined componentwise, the required geometric
statement has the exact form below. -/
def componentwiseNoncrossing {ι : Type v} (β : ι → Type w)
    (NC : (i : ι) → Set (β i) → Prop) (A : (i : ι) → Set (β i)) : Prop :=
  ∀ i, NC i (A i)

/-- Predicate-relative maximality in an ordered type. -/
def IsMaximalFor {A : Type u} [Preorder A] (P : A → Prop) (a : A) : Prop :=
  P a ∧ ∀ b, P b → a ≤ b → b ≤ a

/-- Build an order isomorphism from an equivalence that preserves and reflects
the order. -/
def orderIsoOfEquiv {A : Type u} {B : Type v} [Preorder A] [Preorder B]
    (e : A ≃ B) (order_iff : ∀ a b, a ≤ b ↔ e a ≤ e b) : A ≃o B where
  toEquiv := e
  map_rel_iff' := fun {a b} => (order_iff a b).symm

/-- Relabelling elements by an equivalence is an order isomorphism of
powersets ordered by inclusion. -/
def powersetOrderIso {A : Type u} {B : Type v} (e : A ≃ B) : Set A ≃o Set B :=
  orderIsoOfEquiv (powersetCongr e) (by
    intro X Y
    constructor
    · intro h z hz
      rcases hz with ⟨x, hx, rfl⟩
      exact ⟨x, h hx, rfl⟩
    · intro h x hx
      have hex : e x ∈ e '' X := ⟨x, hx, rfl⟩
      rcases h hex with ⟨y, hy, hey⟩
      have hyx : y = x := e.injective hey
      simpa [hyx] using hy)

/-- Splitting a dependent sum into its fibers preserves and reflects inclusion. -/
def sigmaPowersetOrderIso {ι : Type v} (β : ι → Type w) :
    Set (Sigma β) ≃o ((i : ι) → Set (β i)) :=
  orderIsoOfEquiv (sigmaPowersetEquiv β) (by
    intro X Y
    constructor
    · intro h i x hx
      exact h hx
    · intro h z hz
      exact h z.1 hz)

/-- The regional-address equivalence is canonically an order isomorphism. -/
def regionalPowersetOrderIso {A : Type u} {ι : Type v} (β : ι → Type w)
    (address : A ≃ Sigma β) : Set A ≃o ((i : ι) → Set (β i)) :=
  (powersetOrderIso address).trans (sigmaPowersetOrderIso β)

/-- Relative maximality is invariant under an order isomorphism when its
admissibility predicate is preserved and reflected. -/
theorem isMaximalFor_orderIso_iff {A : Type u} {B : Type v}
    [Preorder A] [Preorder B] (e : A ≃o B)
    (P : A → Prop) (Q : B → Prop) (compatible : ∀ a, P a ↔ Q (e a))
    (a : A) : IsMaximalFor P a ↔ IsMaximalFor Q (e a) := by
  constructor
  · rintro ⟨hPa, hmax⟩
    refine ⟨(compatible a).mp hPa, ?_⟩
    intro b hQb hab
    let a' := e.symm b
    have hPa' : P a' := (compatible a').mpr (by simpa [a'] using hQb)
    have haa' : a ≤ a' := by
      simpa [a'] using e.symm.monotone hab
    have ha'a := hmax a' hPa' haa'
    simpa [a'] using e.monotone ha'a
  · rintro ⟨hQa, hmax⟩
    refine ⟨(compatible a).mpr hQa, ?_⟩
    intro b hPb hab
    have hQb : Q (e b) := (compatible b).mp hPb
    have heb : e a ≤ e b := e.le_iff_le.mpr hab
    simpa using e.symm.monotone (hmax (e b) hQb heb)

end Marici.FaceProduct
