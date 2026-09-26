{-# OPTIONS --safe --cubical --guardedness #-}
module RecursiveConstructorTables where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence using (pathToEquiv)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop; Σ-cong-equiv)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
import WholePackageSigmaPi as Legacy
import TableFibrationCycle as Table

-- Independent recursive typed tables for the atom/E/P CODE fragment.
-- No Legacy.Code or Complete occurs in the stored Header/Graph datatype.
module Core (ℓ : Level) where
  data Header : Type (ℓ-suc ℓ) where
    atom-header : Type ℓ → Header
    E-header P-header : Type ℓ → Header
  Arity : Header → Type ℓ
  Arity (atom-header A) = Lift ⊥
  Arity (E-header I) = I
  Arity (P-header I) = I
  data Graph : Type (ℓ-suc ℓ) where
    vertex : (h : Header) → (Arity h → Graph) → Graph

  -- A vertex IS a canonical table: a declaration row and one child row for
  -- every declared port. The declaration survives when the index is empty.
  data Port (I : Type ℓ) : Type ℓ where
    declaration : Port I
    child : I → Port I
  record Row (h : Header) : Type (ℓ-suc ℓ) where
    constructor row
    field
      label : Header ⊎ Graph
      from : Lift {j = ℓ} Unit
      to : Port (Arity h)
  rows : (h : Header) → (Arity h → Graph) → Port (Arity h) → Row h
  rows h children declaration = row (inl h) (lift tt) declaration
  rows h children (child i) = row (inr (children i)) (lift tt) (child i)
  row-target : (h : Header) (children : Arity h → Graph) (p : Port (Arity h))
    → Row.to (rows h children p) ≡ p
  row-target h children declaration = refl
  row-target h children (child i) = refl
  endpoints-unique : (h : Header) (children : Arity h → Graph) (p q : Port (Arity h))
    → Row.to (rows h children p) ≡ Row.to (rows h children q) → p ≡ q
  endpoints-unique h children p q eq = sym (row-target h children p) ∙ eq ∙ row-target h children q

  -- An actual instance of the original three-column kernel, now level
  -- polymorphic. Only row/endpoint universes are lifted; labels are unchanged.
  kernel-table : (h : Header) → (Arity h → Graph)
    → Table.Table (Header ⊎ Graph) (Lift {j = ℓ-suc ℓ} Unit)
        (Lift {j = ℓ-suc ℓ} (Port (Arity h)))
  kernel-table h children = Table.table (Lift (Port (Arity h)))
    (λ { (lift p) → Row.label (rows h children p) }) (λ _ → lift tt) (λ p → p)
  kernel-unique : (h : Header) (children : Arity h → Graph)
    → Table.UniqueEndpoints (kernel-table h children)
  kernel-unique h children p q from-eq to-eq = to-eq
  kernel-four-return : (h : Header) (children : Arity h → Graph)
    → Table.four (kernel-table h children) ≡ kernel-table h children
  kernel-four-return h children = Table.four-path (kernel-table h children)

  atom-table : Type ℓ → Graph
  atom-table A = vertex (atom-header A) (λ { (lift ()) })
  E-table : (I : Type ℓ) → (I → Graph) → Graph
  E-table I F = vertex (E-header I) F
  P-table : (I : Type ℓ) → (I → Graph) → Graph
  P-table I F = vertex (P-header I) F

  -- Independent interpreter: reads the declaration and child tables.
  -- It does not call the old interpreter or decode an old Code first.
  Value : Graph → Type ℓ
  Value (vertex (atom-header A) children) = A
  Value (vertex (E-header I) children) = Σ I (λ i → Value (children i))
  Value (vertex (P-header I) children) = (i : I) → Value (children i)
  Package : Type (ℓ-suc ℓ)
  Package = Σ Graph Value
  E-value : (I : Type ℓ) → (I → Package) → I → Package
  E-value I F i = E-table I (λ j → fst (F j)) , (i , snd (F i))
  P-value : (I : Type ℓ) → (I → Package) → Package
  P-value I F = P-table I (λ i → fst (F i)) , (λ i → snd (F i))

  -- Decoder and equivalence proof are separate from the implementation above.
  module O = Legacy.Universe ℓ
  decode : Graph → O.Code
  decode (vertex (atom-header A) children) = O.atom A
  decode (vertex (E-header I) children) = O.E I (λ i → decode (children i))
  decode (vertex (P-header I) children) = O.Pi I (λ i → decode (children i))
  value-path : (g : Graph) → O.El (decode g) ≡ Value g
  value-path (vertex (atom-header A) children) = refl
  value-path (vertex (E-header I) children) k = Σ I (λ i → value-path (children i) k)
  value-path (vertex (P-header I) children) k = (i : I) → value-path (children i) k
  value-equivalence : (g : Graph) → O.El (decode g) ≃ Value g
  value-equivalence g = pathToEquiv (value-path g)

  -- Explicitly delimit the legacy fragment. The remaining five constructor
  -- forms are NOT silently packed as opaque original Code labels.
  data Supported : O.Code → Type (ℓ-suc ℓ) where
    atom-supported : {A : Type ℓ} → Supported (O.atom A)
    E-supported : {I : Type ℓ} {F : I → O.Code}
      → ((i : I) → Supported (F i)) → Supported (O.E I F)
    P-supported : {I : Type ℓ} {F : I → O.Code}
      → ((i : I) → Supported (F i)) → Supported (O.Pi I F)
  supported-prop : (c : O.Code) → isProp (Supported c)
  supported-prop (O.atom A) atom-supported atom-supported = refl
  supported-prop (O.E I F) (E-supported p) (E-supported q) =
    cong E-supported (funExt (λ i → supported-prop (F i) (p i) (q i)))
  supported-prop (O.Pi I F) (P-supported p) (P-supported q) =
    cong P-supported (funExt (λ i → supported-prop (F i) (p i) (q i)))
  supported-prop (O.paths c x y) ()
  supported-prop (O.maps c d) ()
  supported-prop (O.equivalences c d) ()
  supported-prop (O.retain c v d) ()
  supported-prop (O.comparison c d e) ()

  encode : {c : O.Code} → Supported c → Graph
  encode (atom-supported {A}) = atom-table A
  encode (E-supported {I} p) = E-table I (λ i → encode (p i))
  encode (P-supported {I} p) = P-table I (λ i → encode (p i))
  decoded-supported : (g : Graph) → Supported (decode g)
  decoded-supported (vertex (atom-header A) children) = atom-supported
  decoded-supported (vertex (E-header I) children) = E-supported (λ i → decoded-supported (children i))
  decoded-supported (vertex (P-header I) children) = P-supported (λ i → decoded-supported (children i))
  decode-encode : {c : O.Code} (p : Supported c) → decode (encode p) ≡ c
  decode-encode atom-supported = refl
  decode-encode (E-supported {I} p) = cong (O.E I) (funExt (λ i → decode-encode (p i)))
  decode-encode (P-supported {I} p) = cong (O.Pi I) (funExt (λ i → decode-encode (p i)))
  encode-decode : (g : Graph) → encode (decoded-supported g) ≡ g
  encode-decode (vertex (atom-header A) children) =
    cong (vertex (atom-header A)) (funExt (λ { (lift ()) }))
  encode-decode (vertex (E-header I) children) =
    cong (vertex (E-header I)) (funExt (λ i → encode-decode (children i)))
  encode-decode (vertex (P-header I) children) =
    cong (vertex (P-header I)) (funExt (λ i → encode-decode (children i)))
  Fragment : Type (ℓ-suc ℓ)
  Fragment = Σ O.Code Supported
  syntax-iso : Iso Fragment Graph
  Iso.fun syntax-iso (c , p) = encode p
  Iso.inv syntax-iso g = decode g , decoded-supported g
  Iso.leftInv syntax-iso (c , p) = Σ≡Prop supported-prop (decode-encode p)
  Iso.rightInv syntax-iso = encode-decode
  package-equivalence : (Σ Fragment (λ cp → O.El (fst cp))) ≃ Package
  package-equivalence = Σ-cong-equiv (isoToEquiv syntax-iso)
    (λ { (c , p) → pathToEquiv (sym (cong O.El (decode-encode p)) ∙ value-path (encode p)) })
