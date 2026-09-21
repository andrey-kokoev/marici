{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureAllDimensionalCutCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.HLevels using (isContr→isContrPath)
open import Cubical.Data.Unit
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import Cubical.Data.Sigma.Base using (_×_)

-- All finite GLOBULAR dimensions: boundaries are pairs of parallel cells.
-- This does not assert that an arbitrary unframed realization is contractible.
module ContractibleTower (T : Type) (contract : isContr T) where
  mutual
    Boundary : ℕ → Type
    Boundary zero = Unit
    Boundary (suc n) = Σ[ b ∈ Boundary n ] (Cell n b × Cell n b)

    Cell : (n : ℕ) → Boundary n → Type
    Cell zero _ = T
    Cell (suc n) (b , (x , y)) = x ≡ y

  allCellsContractible : (n : ℕ) (b : Boundary n) → isContr (Cell n b)
  allCellsContractible zero _ = contract
  allCellsContractible (suc n) (b , (x , y)) =
    isContr→isContrPath (allCellsContractible n b) x y

  fillCell : (n : ℕ) (b : Boundary n) → Cell n b
  fillCell n b = fst (allCellsContractible n b)

-- Frames identify each cut's input/output with common realizations A and B.
-- Their existence is an explicit hypothesis, not a consequence of dimension.
module FramedCuts (K : Type) (X Y : K → Type) (A B : Type)
  (inputFrame : (k : K) → X k ≃ A)
  (outputFrame : (k : K) → Y k ≃ B)
  (operation : A → B) where

  Map : K → Type
  Map k = X k → Y k

  post : (k : K) → Map k → (X k → B)
  post k F x = equivFun (outputFrame k) (F x)

  target : (k : K) → X k → B
  target k x = operation (equivFun (inputFrame k) x)

  -- A cut presentation includes its square identifying the common operation.
  Compatible : K → Type
  Compatible k = Σ[ F ∈ Map k ] (post k F ≡ target k)

  abstract
    postIsEquiv : (k : K) → isEquiv (post k)
    postIsEquiv k = snd (equivΠCod (λ (_ : X k) → outputFrame k))

    compatibleIsContr : (k : K) → isContr (Compatible k)
    compatibleIsContr k =
      equivCtr (post k , postIsEquiv k) (target k) ,
      equivCtrPath (post k , postIsEquiv k) (target k)

  canonical : (k : K) → Compatible k
  fst (canonical k) x = invEq (outputFrame k) (target k x)
  snd (canonical k) = funExt (λ x → secEq (outputFrame k) (target k x))

  -- Actual transport of the given map through input and output frames.
  -- The square witness is assembled from the old witness and inverse laws.
  change : (i j : K) → Compatible i → Compatible j
  fst (change i j p) x = invEq (outputFrame j)
    (equivFun (outputFrame i)
      (fst p (invEq (inputFrame i) (equivFun (inputFrame j) x))))
  snd (change i j p) = funExt λ x →
    secEq (outputFrame j)
      (equivFun (outputFrame i)
        (fst p (invEq (inputFrame i) (equivFun (inputFrame j) x))))
    ∙ cong (λ F → F (invEq (inputFrame i) (equivFun (inputFrame j) x))) (snd p)
    ∙ cong operation (secEq (inputFrame i) (equivFun (inputFrame j) x))

  -- The underlying function spaces are themselves equivalent, before fixing
  -- the common operation or passing to its compatible-presentation fiber.
  mapSpaceEquiv : (i j : K) → Map i ≃ Map j
  mapSpaceEquiv i j = compEquiv
    (equiv→ (inputFrame i) (outputFrame i))
    (invEquiv (equiv→ (inputFrame j) (outputFrame j)))

  changeUnderlying : (i j : K) (p : Compatible i) →
    equivFun (mapSpaceEquiv i j) (fst p) ≡ fst (change i j p)
  changeUnderlying i j p = refl

  compare : (k : K) (p q : Compatible k) → p ≡ q
  compare k = isContr→isProp (compatibleIsContr k)

  changeIdentity : (k : K) (p : Compatible k) → change k k p ≡ p
  changeIdentity k p = compare k (change k k p) p

  changeComposition : (i j k : K) (p : Compatible i) →
    change j k (change i j p) ≡ change i k p
  changeComposition i j k p = compare k _ _

  -- No bound on the number of intermediate cuts. These are finite routes,
  -- not an infinite limit or an assertion of convergence of a completion.
  data Route : K → K → Type where
    stay : (k : K) → Route k k
    step : {i j : K} (k : K) → Route i j → Route i k

  run : {i j : K} → Route i j → Compatible i → Compatible j
  run (stay k) p = p
  run (step {j = j} k r) p = change j k (run r p)

  routeComparison : {i j : K} (r s : Route i j) (p : Compatible i) →
    run r p ≡ run s p
  routeComparison {j = j} r s p = compare j _ _

  cycleLaw : {k : K} (r : Route k k) (p : Compatible k) → run r p ≡ p
  cycleLaw {k = k} r p = routeComparison r (stay k) p

  -- All finite-dimensional parallel-boundary fillers at EACH framed cut.
  module Higher (k : K) = ContractibleTower (Compatible k) (compatibleIsContr k)

  -- In particular, independently supplied route-comparison paths agree;
  -- their equalities have higher comparisons as well, recursively.
  routeComparisonCoherence : {i j : K} (r s : Route i j) (p : Compatible i)
    (α β : run r p ≡ run s p) → α ≡ β
  routeComparisonCoherence {j = j} r s p α β =
    Higher.fillCell j 2 ((tt , (run r p , run s p)) , (α , β))

-- Only the fibers of COMPATIBLE PRESENTATIONS are contractible. X k, Y k,
-- and their full function spaces are not truncated. Independent cut maps or
-- previously chosen higher cells must first be equipped with compatibility
-- in these fibers; this theorem does not silently certify that extra step.
