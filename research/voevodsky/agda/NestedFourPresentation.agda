{-# OPTIONS --safe --cubical --guardedness #-}
module NestedFourPresentation where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Fin.Base using (Fin)
open import Cubical.Data.Nat.Order using (_≤_; ≤-refl; ≤-trans; isProp≤)
open import Cubical.Categories.Category
open import Cubical.Categories.Functor.Base
open import Cubical.Categories.NaturalTransformation.Base
open import Cubical.Categories.Constructions.BinProduct
open import Cubical.Categories.Instances.Functors
open import Cubical.Categories.Instances.Functors.Currying

-- The ordinal category [3]: four vertices, six nonidentity arrows.
-- Its nerve is Delta^3. It models a tetrahedral system with forced coherence,
-- not a freely specified system of independent higher homotopies.
Four : Category ℓ-zero ℓ-zero
Category.ob Four = Fin 4
Category.Hom[_,_] Four a b = fst a ≤ fst b
Category.id Four = ≤-refl
Category._⋆_ Four = ≤-trans
Category.⋆IdL Four _ = isProp≤ _ _
Category.⋆IdR Four _ = isProp≤ _ _
Category.⋆Assoc Four _ _ _ = isProp≤ _ _
Category.isSetHom Four = isProp→isSet isProp≤

Grid : Category ℓ-zero ℓ-zero
Grid = Four ×C Four

module FirstNesting {ℓ ℓ' : Level} (C : Category ℓ ℓ') where
  Nested : Type _
  Nested = Functor Four (FUNCTOR Four C)

  Expanded : Type _
  Expanded = Functor Grid C

  expand : Nested → Expanded
  expand = λF⁻ Four C Four

  nest : Expanded → Nested
  nest = λF Four C Four

  -- Full functor records, not just arrays of sixteen objects, round-trip.
  nest-expand : (D : Nested) → nest (expand D) ≡ D
  nest-expand = Iso.rightInv (isoλF Four C Four)

  expand-nest : (D : Expanded) → expand (nest D) ≡ D
  expand-nest = Iso.leftInv (isoλF Four C Four)

  expandedVertex : (D : Nested) (a i : Fin 4) →
    Functor.F-ob (expand D) (a , i) ≡
    Functor.F-ob (Functor.F-ob D a) i
  expandedVertex D a i = refl

  module _ (D : Nested) where
    X : Fin 4 → Fin 4 → Category.ob C
    X a i = Functor.F-ob (Functor.F-ob D a) i

    inner : (a : Fin 4) {i j : Fin 4} → Four [ i , j ] →
      C [ X a i , X a j ]
    inner a = Functor.F-hom (Functor.F-ob D a)

    outer : {a b : Fin 4} → Four [ a , b ] → (i : Fin 4) →
      C [ X a i , X b i ]
    outer p = NatTrans.N-ob (Functor.F-hom D p)

    -- The mixed square has a common source X a i and target X b j.
    -- It is exactly naturality of the outer comparison between inner systems.
    mixedSquare : {a b i j : Fin 4}
      (p : Four [ a , b ]) (q : Four [ i , j ]) →
      seq' C (inner a q) (outer p j) ≡
      seq' C (outer p i) (inner b q)
    mixedSquare p q = NatTrans.N-hom (Functor.F-hom D p) q

-- Nonterminal regression: the target itself has all sixteen ordered pairs.
-- No physical maps or identity of analytical presentations are asserted.
module Test = FirstNesting Grid

expandedGrid : Test.Expanded
expandedGrid = 𝟙⟨ Grid ⟩

nestedGrid : Test.Nested
nestedGrid = Test.nest expandedGrid

gridRoundTrip : Test.expand nestedGrid ≡ expandedGrid
gridRoundTrip = Test.expand-nest expandedGrid

-- Critical scope: Category has hom-SETS. Its equation witnesses have no
-- independent higher choices. Hence this test cannot certify the conjectured
-- infinite homotopy-coherence tower, or an analytic instantiation of it.
