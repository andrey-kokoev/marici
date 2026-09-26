{-# OPTIONS --safe --cubical --guardedness #-}
module TableFibrationCycle where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence using (ua; ua→)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)

-- The same kernel at every universe level, so typed recursive constructor
-- labels can themselves be table data. Existing small instances are unchanged.
private
  variable
    ℓ : Level

-- One generic grouping operation. Unpacking uses the dependent-sum former.
fibrate : {E B : Type ℓ} → (E → B) → B → Type ℓ
fibrate {E = E} p b = Σ E (λ e → p e ≡ b)
total : {B : Type ℓ} → (B → Type ℓ) → Type ℓ
total {B = B} F = Σ B F
unpack-fibers : {E B : Type ℓ} (p : E → B) → Iso (total (fibrate p)) E
Iso.fun (unpack-fibers p) (b , e , witness) = e
Iso.inv (unpack-fibers p) e = p e , e , refl
Iso.rightInv (unpack-fibers p) e = refl
Iso.leftInv (unpack-fibers p) (b , e , witness) i =
  witness i , e , (λ j → witness (i ∧ j))

record Table (L S T : Type ℓ) : Type (ℓ-suc ℓ) where
  constructor table
  field
    Rows : Type ℓ
    label : Rows → L
    from : Rows → S
    to : Rows → T
open Table

data Column : Type where
  label-column from-column to-column : Column
ColumnType : (L S T : Type ℓ) → Column → Type ℓ
ColumnType L S T label-column = L
ColumnType L S T from-column = S
ColumnType L S T to-column = T
select : {L S T : Type ℓ} (q : Table L S T) (k : Column) → Rows q → ColumnType L S T k
select q label-column = label q
select q from-column = from q
select q to-column = to q
fibrate-column : {L S T : Type ℓ} (q : Table L S T) (k : Column) → ColumnType L S T k → Type ℓ
fibrate-column q k = fibrate (select q k)

record Grouped (B L T : Type ℓ) : Type (ℓ-suc ℓ) where
  field
    Family : B → Type ℓ
    enclosed-label : (b : B) → Family b → L
    enclosed-endpoint : (b : B) → Family b → T
open Grouped

group-from : {L S T : Type ℓ} → Table L S T → Grouped S L T
Family (group-from q) = fibrate (from q)
enclosed-label (group-from q) b (r , p) = label q r
enclosed-endpoint (group-from q) b (r , p) = to q r

group-to : {L S T : Type ℓ} → Table L S T → Grouped T L S
Family (group-to q) = fibrate (to q)
enclosed-label (group-to q) b (r , p) = label q r
enclosed-endpoint (group-to q) b (r , p) = from q r

group-label : {L S T : Type ℓ} → Table L S T → Grouped L S T
Family (group-label q) = fibrate (label q)
enclosed-label (group-label q) b (r , p) = from q r
enclosed-endpoint (group-label q) b (r , p) = to q r

column-recovery : {L S T : Type ℓ} (q : Table L S T) (k : Column)
  → Iso (total (fibrate-column q k)) (Rows q)
column-recovery q k = unpack-fibers (select q k)

-- Two different wiring conventions use the SAME total family.
unpack : {B L T : Type ℓ} → Grouped B L T → Table L B T
Rows (unpack g) = total (Family g)
label (unpack g) (b , r) = enclosed-label g b r
from (unpack g) (b , r) = b
to (unpack g) (b , r) = enclosed-endpoint g b r

unpack-reversed : {B L T : Type ℓ} → Grouped B L T → Table L T B
Rows (unpack-reversed g) = total (Family g)
label (unpack-reversed g) (b , r) = enclosed-label g b r
from (unpack-reversed g) (b , r) = enclosed-endpoint g b r
to (unpack-reversed g) (b , r) = b

unpack-label : {L S T : Type ℓ} → Grouped L S T → Table L S T
Rows (unpack-label g) = total (Family g)
label (unpack-label g) (b , r) = b
from (unpack-label g) (b , r) = enclosed-label g b r
to (unpack-label g) (b , r) = enclosed-endpoint g b r

GroupedAt : (L S T : Type ℓ) → Column → Type (ℓ-suc ℓ)
GroupedAt L S T label-column = Grouped L S T
GroupedAt L S T from-column = Grouped S L T
GroupedAt L S T to-column = Grouped T L S
fibrate-table : {L S T : Type ℓ} (q : Table L S T) (k : Column) → GroupedAt L S T k
fibrate-table q label-column = group-label q
fibrate-table q from-column = group-from q
fibrate-table q to-column = group-to q
restore-table : {L S T : Type ℓ} (k : Column) → GroupedAt L S T k → Table L S T
restore-table label-column = unpack-label
restore-table from-column = unpack
restore-table to-column = unpack-reversed

-- Transposition is used to STATE what two steps do, not as a primitive in
-- the construction twice. That construction uses fibers, total, and wiring.
transpose : {L S T : Type ℓ} → Table L S T → Table L T S
transpose q = table (Rows q) (label q) (to q) (from q)
twice : {L S T : Type ℓ} → Table L S T → Table L T S
twice q = unpack-reversed (group-from q)
four : {L S T : Type ℓ} → Table L S T → Table L S T
four q = twice (twice q)

record TableIso {L S T : Type ℓ} (a b : Table L S T) : Type ℓ where
  field
    rows : Iso (Rows a) (Rows b)
    preserves-label : (r : Rows a) → label b (Iso.fun rows r) ≡ label a r
    preserves-from : (r : Rows a) → from b (Iso.fun rows r) ≡ from a r
    preserves-to : (r : Rows a) → to b (Iso.fun rows r) ≡ to a r
open TableIso

unpack-correct : {L S T : Type ℓ} (q : Table L S T) → TableIso (unpack (group-from q)) q
rows (unpack-correct q) = unpack-fibers (from q)
preserves-label (unpack-correct q) (b , r , p) = refl
preserves-from (unpack-correct q) (b , r , p) = p
preserves-to (unpack-correct q) (b , r , p) = refl

twice-correct : {L S T : Type ℓ} (q : Table L S T) → TableIso (twice q) (transpose q)
rows (twice-correct q) = unpack-fibers (from q)
preserves-label (twice-correct q) (b , r , p) = refl
preserves-from (twice-correct q) (b , r , p) = refl
preserves-to (twice-correct q) (b , r , p) = p

transpose-iso : {L S T : Type ℓ} {a b : Table L S T} → TableIso a b → TableIso (transpose a) (transpose b)
rows (transpose-iso e) = rows e
preserves-label (transpose-iso e) = preserves-label e
preserves-from (transpose-iso e) = preserves-to e
preserves-to (transpose-iso e) = preserves-from e
compose : {L S T : Type ℓ} {a b c : Table L S T} → TableIso a b → TableIso b c → TableIso a c
rows (compose e f) = compIso (rows e) (rows f)
preserves-label (compose e f) r = preserves-label f (Iso.fun (rows e) r) ∙ preserves-label e r
preserves-from (compose e f) r = preserves-from f (Iso.fun (rows e) r) ∙ preserves-from e r
preserves-to (compose e f) r = preserves-to f (Iso.fun (rows e) r) ∙ preserves-to e r
four-correct : {L S T : Type ℓ} (q : Table L S T) → TableIso (four q) q
four-correct q = compose (twice-correct (twice q)) (transpose-iso (twice-correct q))

restore-correct : {L S T : Type ℓ} (q : Table L S T) (k : Column)
  → TableIso (restore-table {L = L} {S = S} {T = T} k (fibrate-table q k)) q
rows (restore-correct q label-column) = unpack-fibers (label q)
preserves-label (restore-correct q label-column) (b , r , p) = p
preserves-from (restore-correct q label-column) (b , r , p) = refl
preserves-to (restore-correct q label-column) (b , r , p) = refl
restore-correct q from-column = unpack-correct q
restore-correct q to-column = twice-correct (transpose q)

-- Univalence upgrades the structured equivalence to equality of TABLE DATA.
-- It does not identify separately retained operation syntax or derivations.
table-path : {L S T : Type ℓ} {a b : Table L S T} → TableIso a b → a ≡ b
Rows (table-path e i) = ua (isoToEquiv (rows e)) i
label (table-path {L = L} {a = a} {b = b} e i) = ua→ {e = isoToEquiv (rows e)} {B = λ _ → L}
  {f₀ = label a} {f₁ = label b} (λ r → sym (preserves-label e r)) i
from (table-path {S = S} {a = a} {b = b} e i) = ua→ {e = isoToEquiv (rows e)} {B = λ _ → S}
  {f₀ = from a} {f₁ = from b} (λ r → sym (preserves-from e r)) i
to (table-path {T = T} {a = a} {b = b} e i) = ua→ {e = isoToEquiv (rows e)} {B = λ _ → T}
  {f₀ = to a} {f₁ = to b} (λ r → sym (preserves-to e r)) i
four-path : {L S T : Type ℓ} (q : Table L S T) → four q ≡ q
four-path q = table-path (four-correct q)

MarkedGrouping : (L S T : Type ℓ) → Type (ℓ-suc ℓ)
MarkedGrouping L S T = Σ Column (GroupedAt L S T)
marked-fibrate : {L S T : Type ℓ} → Table L S T → Column → MarkedGrouping L S T
marked-fibrate q k = k , fibrate-table q k
restore-marked : {L S T : Type ℓ} → MarkedGrouping L S T → Table L S T
restore-marked (k , g) = restore-table k g
marked-recovery : {L S T : Type ℓ} (q : Table L S T) (k : Column)
  → restore-marked (marked-fibrate q k) ≡ q
marked-recovery q k = table-path (restore-correct q k)

-- The user's endpoint uniqueness condition is transported by these maps.
-- The recovery theorem itself does not need this restriction.
UniqueEndpoints : {L S T : Type ℓ} → Table L S T → Type ℓ
UniqueEndpoints q = (x y : Rows q) → from q x ≡ from q y → to q x ≡ to q y → x ≡ y
transpose-unique : {L S T : Type ℓ} (q : Table L S T)
  → UniqueEndpoints q → UniqueEndpoints (transpose q)
transpose-unique q unique x y ps pt = unique x y pt ps
preserve-uniqueness : {L S T : Type ℓ} {a b : Table L S T}
  → TableIso a b → UniqueEndpoints b → UniqueEndpoints a
preserve-uniqueness e unique x y ps pt =
  sym (Iso.leftInv (rows e) x)
  ∙ cong (Iso.inv (rows e))
      (unique (Iso.fun (rows e) x) (Iso.fun (rows e) y)
        (preserves-from e x ∙ ps ∙ sym (preserves-from e y))
        (preserves-to e x ∙ pt ∙ sym (preserves-to e y)))
  ∙ Iso.leftInv (rows e) y
four-preserves-uniqueness : {L S T : Type ℓ} (q : Table L S T)
  → UniqueEndpoints q → UniqueEndpoints (four q)
four-preserves-uniqueness q = preserve-uniqueness (four-correct q)

-- Fibers alone do not choose which endpoint becomes the outer coordinate.
example : Table Bool Bool Bool
example = table Unit (λ _ → false) (λ _ → false) (λ _ → true)
example-unique : UniqueEndpoints example
example-unique tt tt ps pt = refl
endpoint-exchange-is-not-identity : TableIso example (transpose example) → ⊥
endpoint-exchange-is-not-identity e = true≢false (preserves-from e tt)

-- In a self-labelled space, dropping the selected coordinate is ambiguous.
-- This is definitional equality of the complete grouped records.
grouping-ambiguous : group-from example ≡ group-to (transpose example)
grouping-ambiguous = refl
identity-iso : {L S T : Type ℓ} (q : Table L S T) → TableIso q q
rows (identity-iso q) = idIso
preserves-label (identity-iso q) r = refl
preserves-from (identity-iso q) r = refl
preserves-to (identity-iso q) r = refl
path-to-table-iso : {L S T : Type ℓ} {a b : Table L S T} → a ≡ b → TableIso a b
path-to-table-iso {a = a} p = transport (λ i → TableIso a (p i)) (identity-iso a)
no-unmarked-recovery : (recover : Grouped Bool Bool Bool → Table Bool Bool Bool)
  → ((q : Table Bool Bool Bool) → UniqueEndpoints q → recover (group-from q) ≡ q)
  → ((q : Table Bool Bool Bool) → UniqueEndpoints q → recover (group-to q) ≡ q) → ⊥
no-unmarked-recovery recover from-law to-law = endpoint-exchange-is-not-identity
  (path-to-table-iso (sym (from-law example example-unique)
    ∙ to-law (transpose example) (transpose-unique example example-unique)))
