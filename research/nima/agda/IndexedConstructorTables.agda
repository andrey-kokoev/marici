{-# OPTIONS --safe --cubical --guardedness #-}
module IndexedConstructorTables where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence using (pathToEquiv)
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
import WholePackageSigmaPi as Legacy
import TableFibrationCycle as Table

-- Indexing nodes by their native carrier keeps witness attachments typed.
-- This is an independent indexed datatype, not a stored old Code annotation.
module Core (ℓ : Level) where
  Compare : (A B : Type ℓ) → A ≃ B → Type ℓ
  Compare A B e = Σ A (λ x → Σ B (λ y → equivFun e x ≡ y))
  -- One table constructor: its declaration gives the active ports and the
  -- expected carrier at every attachment. Child rows must satisfy that schema.
  data Header : Type (ℓ-suc ℓ) where
    atom-header : Type ℓ → Header
    E-header P-header : (I : Type ℓ) → (I → Type ℓ) → Header
    paths-header : (A : Type ℓ) → A → A → Header
    maps-header equivalences-header : Type ℓ → Type ℓ → Header
    retain-header : (A : Type ℓ) → A → Type ℓ → Header
    comparison-header : (A B : Type ℓ) → A ≃ B → Header
  Arity : Header → Type ℓ
  Arity (atom-header A) = Lift ⊥
  Arity (E-header I F) = I
  Arity (P-header I F) = I
  Arity (paths-header A x y) = Lift Unit
  Arity (maps-header A B) = Lift Bool
  Arity (equivalences-header A B) = Lift Bool
  Arity (retain-header A x B) = Lift Bool
  Arity (comparison-header A B e) = Lift Bool
  Inputs : (h : Header) → Arity h → Type ℓ
  Inputs (atom-header A) (lift ())
  Inputs (E-header I F) i = F i
  Inputs (P-header I F) i = F i
  Inputs (paths-header A x y) _ = A
  Inputs (maps-header A B) (lift false) = A
  Inputs (maps-header A B) (lift true) = B
  Inputs (equivalences-header A B) (lift false) = A
  Inputs (equivalences-header A B) (lift true) = B
  Inputs (retain-header A x B) (lift false) = A
  Inputs (retain-header A x B) (lift true) = B
  Inputs (comparison-header A B e) (lift false) = A
  Inputs (comparison-header A B e) (lift true) = B
  Result : Header → Type ℓ
  Result (atom-header A) = A
  Result (E-header I F) = Σ I F
  Result (P-header I F) = (i : I) → F i
  Result (paths-header A x y) = x ≡ y
  Result (maps-header A B) = A → B
  Result (equivalences-header A B) = A ≃ B
  Result (retain-header A x B) = B
  Result (comparison-header A B e) = Compare A B e
  data Node : Type ℓ → Type (ℓ-suc ℓ) where
    table-node : (h : Header) → ((i : Arity h) → Node (Inputs h i)) → Node (Result h)
  atom-node : (A : Type ℓ) → Node A
  atom-node A = table-node (atom-header A) (λ { (lift ()) })
  E-node : (I : Type ℓ) {F : I → Type ℓ} → ((i : I) → Node (F i)) → Node (Σ I F)
  E-node I {F} = table-node (E-header I F)
  P-node : (I : Type ℓ) {F : I → Type ℓ} → ((i : I) → Node (F i)) → Node ((i : I) → F i)
  P-node I {F} = table-node (P-header I F)
  paths-node : {A : Type ℓ} → Node A → (x y : A) → Node (x ≡ y)
  paths-node {A} c x y = table-node (paths-header A x y) (λ _ → c)
  maps-node : {A B : Type ℓ} → Node A → Node B → Node (A → B)
  maps-node {A} {B} c d = table-node (maps-header A B) (λ { (lift false) → c ; (lift true) → d })
  equivalences-node : {A B : Type ℓ} → Node A → Node B → Node (A ≃ B)
  equivalences-node {A} {B} c d = table-node (equivalences-header A B) (λ { (lift false) → c ; (lift true) → d })
  retain-node : {A B : Type ℓ} → Node A → A → Node B → Node B
  retain-node {A} {B} c x d = table-node (retain-header A x B) (λ { (lift false) → c ; (lift true) → d })
  comparison-node : {A B : Type ℓ} → Node A → Node B → (e : A ≃ B) → Node (Compare A B e)
  comparison-node {A} {B} c d e = table-node (comparison-header A B e) (λ { (lift false) → c ; (lift true) → d })
  Graph : Type (ℓ-suc ℓ)
  Graph = Σ (Type ℓ) Node
  Value : Graph → Type ℓ
  Value = fst
  Package : Type (ℓ-suc ℓ)
  Package = Σ Graph Value
  RowData : Type (ℓ-suc ℓ)
  RowData = Σ Header (λ h → (i : Arity h) → Node (Inputs h i))
  row-data-iso : Iso Graph RowData
  Iso.fun row-data-iso (A , table-node h children) = h , children
  Iso.inv row-data-iso (h , children) = Result h , table-node h children
  Iso.leftInv row-data-iso (A , table-node h children) = refl
  Iso.rightInv row-data-iso (h , children) = refl
  atom-table : Type ℓ → Graph
  atom-table A = A , atom-node A
  E-table : (I : Type ℓ) → (I → Graph) → Graph
  E-table I F = Σ I (λ i → Value (F i)) , E-node I (λ i → snd (F i))
  P-table : (I : Type ℓ) → (I → Graph) → Graph
  P-table I F = ((i : I) → Value (F i)) , P-node I (λ i → snd (F i))

  header : {A : Type ℓ} → Node A → Header
  header (table-node h children) = h
  child : {A : Type ℓ} (g : Node A) → Arity (header g) → Graph
  child (table-node h children) i = Inputs h i , children i
  data Port (I : Type ℓ) : Type ℓ where
    declaration : Port I
    argument : I → Port I
  label : {A : Type ℓ} (g : Node A) → Port (Arity (header g)) → Header ⊎ Graph
  label g declaration = inl (header g)
  label g (argument i) = inr (child g i)
  kernel-table : {A : Type ℓ} (g : Node A)
    → Table.Table (Header ⊎ Graph) (Lift {j = ℓ-suc ℓ} Unit)
        (Lift {j = ℓ-suc ℓ} (Port (Arity (header g))))
  kernel-table g = Table.table (Lift (Port (Arity (header g))))
    (λ { (lift p) → label g p }) (λ _ → lift tt) (λ p → p)
  kernel-unique : {A : Type ℓ} (g : Node A) → Table.UniqueEndpoints (kernel-table g)
  kernel-unique g p q from-eq to-eq = to-eq
  kernel-four-return : {A : Type ℓ} (g : Node A) → Table.four (kernel-table g) ≡ kernel-table g
  kernel-four-return g = Table.four-path (kernel-table g)

  -- A complete package is a two-row envelope: its recursive code table and
  -- its actual typed value. The schema requires their carriers to agree.
  TypedValue : Type (ℓ-suc ℓ)
  TypedValue = Σ (Type ℓ) (λ A → A)
  package-label : Package → Bool → Graph ⊎ TypedValue
  package-label (g , v) false = inl g
  package-label (g , v) true = inr (Value g , v)
  package-table : Package → Table.Table (Graph ⊎ TypedValue)
    (Lift {j = ℓ-suc ℓ} Unit) (Lift {j = ℓ-suc ℓ} Bool)
  package-table q = Table.table (Lift Bool)
    (λ { (lift b) → package-label q b }) (λ _ → lift tt) (λ b → b)
  package-unique : (q : Package) → Table.UniqueEndpoints (package-table q)
  package-unique q a b from-eq to-eq = to-eq

  -- Decoder-only semantic fibers. These old Code/path pairs are NOT fields
  -- of the independent Node or its row labels.
  module O = Legacy.Universe ℓ
  At : Type ℓ → Type (ℓ-suc ℓ)
  At A = Σ O.Code (λ c → O.El c ≡ A)
  backfill : {A : Type ℓ} (c : At A) (x : A)
    → PathP (λ i → snd c i) (transport (sym (snd c)) x) x
  backfill c x i = transport-filler (sym (snd c)) x (~ i)
  equiv-backfill : {A B : Type ℓ} (c : At A) (d : At B) (e : A ≃ B)
    → PathP (λ i → snd c i ≃ snd d i)
        (transport (λ i → snd c (~ i) ≃ snd d (~ i)) e) e
  equiv-backfill c d e i = transport-filler (λ j → snd c (~ j) ≃ snd d (~ j)) e (~ i)
  atom-at : (A : Type ℓ) → At A
  atom-at A = O.atom A , refl
  E-at : (I : Type ℓ) {F : I → Type ℓ} → ((i : I) → At (F i)) → At (Σ I F)
  E-at I F = O.E I (λ i → fst (F i)) , (λ j → Σ I (λ i → snd (F i) j))
  P-at : (I : Type ℓ) {F : I → Type ℓ} → ((i : I) → At (F i)) → At ((i : I) → F i)
  P-at I F = O.Pi I (λ i → fst (F i)) , (λ j → (i : I) → snd (F i) j)
  paths-at : {A : Type ℓ} → At A → (x y : A) → At (x ≡ y)
  paths-at c x y = O.paths (fst c) (backfill c x i0) (backfill c y i0) ,
    (λ i → backfill c x i ≡ backfill c y i)
  maps-at : {A B : Type ℓ} → At A → At B → At (A → B)
  maps-at c d = O.maps (fst c) (fst d) , (λ i → snd c i → snd d i)
  equivalences-at : {A B : Type ℓ} → At A → At B → At (A ≃ B)
  equivalences-at c d = O.equivalences (fst c) (fst d) , (λ i → snd c i ≃ snd d i)
  retain-at : {A B : Type ℓ} → At A → A → At B → At B
  retain-at c x d = O.retain (fst c) (backfill c x i0) (fst d) , snd d
  comparison-at : {A B : Type ℓ} → At A → At B → (e : A ≃ B) → At (Compare A B e)
  comparison-at c d e = O.comparison (fst c) (fst d) (equiv-backfill c d e i0) ,
    (λ i → Compare (snd c i) (snd d i) (equiv-backfill c d e i))

  quote-node : (c : O.Code) → Node (O.El c)
  quote-node (O.atom A) = atom-node A
  quote-node (O.E I F) = E-node I (λ i → quote-node (F i))
  quote-node (O.Pi I F) = P-node I (λ i → quote-node (F i))
  quote-node (O.paths c x y) = paths-node (quote-node c) x y
  quote-node (O.maps c d) = maps-node (quote-node c) (quote-node d)
  quote-node (O.equivalences c d) = equivalences-node (quote-node c) (quote-node d)
  quote-node (O.retain c x d) = retain-node (quote-node c) x (quote-node d)
  quote-node (O.comparison c d e) = comparison-node (quote-node c) (quote-node d) e
  decode-at : {A : Type ℓ} → Node A → At A
  decode-at (table-node (atom-header A) children) = atom-at A
  decode-at (table-node (E-header I F) children) = E-at I (λ i → decode-at (children i))
  decode-at (table-node (P-header I F) children) = P-at I (λ i → decode-at (children i))
  decode-at (table-node (paths-header A x y) children) = paths-at (decode-at (children (lift tt))) x y
  decode-at (table-node (maps-header A B) children) = maps-at (decode-at (children (lift false))) (decode-at (children (lift true)))
  decode-at (table-node (equivalences-header A B) children) = equivalences-at (decode-at (children (lift false))) (decode-at (children (lift true)))
  decode-at (table-node (retain-header A x B) children) = retain-at (decode-at (children (lift false))) x (decode-at (children (lift true)))
  decode-at (table-node (comparison-header A B e) children) = comparison-at (decode-at (children (lift false))) (decode-at (children (lift true))) e
  quote-at : {A : Type ℓ} → At A → Node A
  quote-at (c , p) = transport (λ i → Node (p i)) (quote-node c)
  quoted-fill : {A : Type ℓ} (c : At A)
    → PathP (λ i → Node (snd c i)) (quote-node (fst c)) (quote-at c)
  quoted-fill (c , p) = transport-filler (λ i → Node (p i)) (quote-node c)

  -- Naturality retains the carrier path jointly with each decoded code.
  quote-E : (I : Type ℓ) {F : I → Type ℓ} (f : (i : I) → At (F i))
    → quote-at (E-at I f) ≡ E-node I (λ i → quote-at (f i))
  quote-E I f = fromPathP (λ k → E-node I (λ i → quoted-fill (f i) k))
  quote-P : (I : Type ℓ) {F : I → Type ℓ} (f : (i : I) → At (F i))
    → quote-at (P-at I f) ≡ P-node I (λ i → quote-at (f i))
  quote-P I f = fromPathP (λ k → P-node I (λ i → quoted-fill (f i) k))
  quote-paths : {A : Type ℓ} (c : At A) (x y : A)
    → quote-at (paths-at c x y) ≡ paths-node (quote-at c) x y
  quote-paths c x y = fromPathP (λ i → paths-node (quoted-fill c i) (backfill c x i) (backfill c y i))
  quote-maps : {A B : Type ℓ} (c : At A) (d : At B)
    → quote-at (maps-at c d) ≡ maps-node (quote-at c) (quote-at d)
  quote-maps c d = fromPathP (λ i → maps-node (quoted-fill c i) (quoted-fill d i))
  quote-equivalences : {A B : Type ℓ} (c : At A) (d : At B)
    → quote-at (equivalences-at c d) ≡ equivalences-node (quote-at c) (quote-at d)
  quote-equivalences c d = fromPathP (λ i → equivalences-node (quoted-fill c i) (quoted-fill d i))
  quote-retain : {A B : Type ℓ} (c : At A) (x : A) (d : At B)
    → quote-at (retain-at c x d) ≡ retain-node (quote-at c) x (quote-at d)
  quote-retain c x d = fromPathP (λ i → retain-node (quoted-fill c i) (backfill c x i) (quoted-fill d i))
  quote-comparison : {A B : Type ℓ} (c : At A) (d : At B) (e : A ≃ B)
    → quote-at (comparison-at c d e) ≡ comparison-node (quote-at c) (quote-at d) e
  quote-comparison c d e = fromPathP (λ i → comparison-node (quoted-fill c i) (quoted-fill d i) (equiv-backfill c d e i))

  paths-normal : (c : O.Code) (x y : O.El c)
    → paths-at (c , refl) x y ≡ (O.paths c x y , refl)
  paths-normal c x y i = O.paths c (backfill (c , refl) x i) (backfill (c , refl) y i) ,
    (λ j → backfill (c , refl) x (i ∨ j) ≡ backfill (c , refl) y (i ∨ j))
  retain-normal : (c d : O.Code) (x : O.El c)
    → retain-at (c , refl) x (d , refl) ≡ (O.retain c x d , refl)
  retain-normal c d x i = O.retain c (backfill (c , refl) x i) d , refl
  comparison-normal : (c d : O.Code) (e : O.El c ≃ O.El d)
    → comparison-at (c , refl) (d , refl) e ≡ (O.comparison c d e , refl)
  comparison-normal c d e i = O.comparison c d (equiv-backfill (c , refl) (d , refl) e i) ,
    (λ j → Compare (O.El c) (O.El d) (equiv-backfill (c , refl) (d , refl) e (i ∨ j)))
  decode-quote : (c : O.Code) → decode-at (quote-node c) ≡ (c , refl)
  decode-quote (O.atom A) = refl
  decode-quote (O.E I F) = cong (E-at I) (funExt (λ i → decode-quote (F i)))
  decode-quote (O.Pi I F) = cong (P-at I) (funExt (λ i → decode-quote (F i)))
  decode-quote (O.paths c x y) = cong (λ a → paths-at a x y) (decode-quote c) ∙ paths-normal c x y
  decode-quote (O.maps c d) = cong₂ maps-at (decode-quote c) (decode-quote d)
  decode-quote (O.equivalences c d) = cong₂ equivalences-at (decode-quote c) (decode-quote d)
  decode-quote (O.retain c x d) = cong₂ (λ a b → retain-at a x b) (decode-quote c) (decode-quote d) ∙ retain-normal c d x
  decode-quote (O.comparison c d e) = cong₂ (λ a b → comparison-at a b e) (decode-quote c) (decode-quote d) ∙ comparison-normal c d e
  decode-quote-at : {A : Type ℓ} (c : At A) → decode-at (quote-at c) ≡ c
  decode-quote-at (c , p) =
    sym (fromPathP (λ i → decode-at (quoted-fill (c , p) i)))
    ∙ cong (transport (λ i → At (p i))) (decode-quote c)
    ∙ fromPathP (λ i → c , (λ j → p (i ∧ j)))
  quote-decode : {A : Type ℓ} (g : Node A) → quote-at (decode-at g) ≡ g
  quote-decode (table-node (atom-header A) f) = transportRefl (atom-node A)
    ∙ cong (table-node (atom-header A)) (funExt (λ { (lift ()) }))
  quote-decode (table-node (E-header I F) f) = quote-E I (λ i → decode-at (f i))
    ∙ cong (E-node I) (funExt (λ i → quote-decode (f i)))
  quote-decode (table-node (P-header I F) f) = quote-P I (λ i → decode-at (f i))
    ∙ cong (P-node I) (funExt (λ i → quote-decode (f i)))
  quote-decode (table-node (paths-header A x y) f) = quote-paths (decode-at (f (lift tt))) x y
    ∙ cong (table-node (paths-header A x y)) (funExt (λ { (lift tt) → quote-decode (f (lift tt)) }))
  quote-decode (table-node (maps-header A B) f) = quote-maps (decode-at (f (lift false))) (decode-at (f (lift true)))
    ∙ cong (table-node (maps-header A B)) (funExt (λ { (lift false) → quote-decode (f (lift false)) ; (lift true) → quote-decode (f (lift true)) }))
  quote-decode (table-node (equivalences-header A B) f) = quote-equivalences (decode-at (f (lift false))) (decode-at (f (lift true)))
    ∙ cong (table-node (equivalences-header A B)) (funExt (λ { (lift false) → quote-decode (f (lift false)) ; (lift true) → quote-decode (f (lift true)) }))
  quote-decode (table-node (retain-header A x B) f) = quote-retain (decode-at (f (lift false))) x (decode-at (f (lift true)))
    ∙ cong (table-node (retain-header A x B)) (funExt (λ { (lift false) → quote-decode (f (lift false)) ; (lift true) → quote-decode (f (lift true)) }))
  quote-decode (table-node (comparison-header A B e) f) = quote-comparison (decode-at (f (lift false))) (decode-at (f (lift true))) e
    ∙ cong (table-node (comparison-header A B e)) (funExt (λ { (lift false) → quote-decode (f (lift false)) ; (lift true) → quote-decode (f (lift true)) }))

  fiber-iso : (A : Type ℓ) → Iso (At A) (Node A)
  Iso.fun (fiber-iso A) = quote-at
  Iso.inv (fiber-iso A) = decode-at
  Iso.leftInv (fiber-iso A) = decode-quote-at
  Iso.rightInv (fiber-iso A) = quote-decode
  syntax-iso : Iso O.Code Graph
  Iso.fun syntax-iso c = O.El c , quote-node c
  Iso.inv syntax-iso (A , g) = fst (decode-at g)
  Iso.leftInv syntax-iso c = cong fst (decode-quote c)
  Iso.rightInv syntax-iso (A , g) =
    (λ i → snd (decode-at g) i , quoted-fill (decode-at g) i)
    ∙ cong (λ n → A , n) (quote-decode g)
  sigma-package-equivalence : (Σ O.Code O.El) ≃ Package
  sigma-package-equivalence = Σ-cong-equiv (isoToEquiv syntax-iso) (λ c → idEquiv (O.El c))
  old-sigma : Iso O.Complete (Σ O.Code O.El)
  Iso.fun old-sigma q = O.expression q , O.value q
  Iso.inv old-sigma (c , v) = O.pack c v
  Iso.leftInv old-sigma q = refl
  Iso.rightInv old-sigma (c , v) = refl
  complete-equivalence : O.Complete ≃ Package
  complete-equivalence = compEquiv (isoToEquiv old-sigma) sigma-package-equivalence
  encode-package : O.Complete → Package
  encode-package = equivFun complete-equivalence
  selected-unchanged : (q : O.Complete) → snd (encode-package q) ≡ O.value q
  selected-unchanged q = refl
  decode : Graph → O.Code
  decode (A , g) = fst (decode-at g)
  value-equivalence : (g : Graph) → O.El (decode g) ≃ Value g
  value-equivalence (A , g) = pathToEquiv (snd (decode-at g))
