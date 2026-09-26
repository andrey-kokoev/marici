{-# OPTIONS --safe --cubical --guardedness #-}
module ThreeProfileCoherence where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sigma.Base using (_×_)
import NativeRetainedProfiles as Profiles
import RetainedCliffordProfiles as C

-- Three retained profiles on the common Clifford/History source.
-- Key theorem: the left-first and right-first nested pullbacks are canonically
-- equivalent through the triple pullback. All constructions are phase-independent
-- because the readings r1, r2, r3 are defined on History identically for both
-- Clifford and trivial phase models.

module Triple where
  module N = Profiles.Native ℓ-zero

  Source = C.History
  a0 = C.unit

  r1 : Source -> C.Signed
  r1 = C.lift-reading

  r2 : Source -> C.Grade
  r2 = C.action-reading

  r3 : Source -> C.Signed × C.Grade
  r3 h = (C.lift-reading h , C.action-reading h)

  module J12 = N.Two (C.source-node) a0 r1 r2
  module J23 = N.Two (C.source-node) a0 r2 r3
  module J123 = N.Two (C.source-node) a0 r1 (λ a -> r2 a , r3 a)

  -- Use the Reassemble isomorphism directly: a -> (reading, a, refl).
  -- This gives definitional recover(Iso.fun reassemble a) = a.
  reassemble12 = J12.Joint.R.reassemble
  reassemble23 = J23.Joint.R.reassemble

  -- Left-first: glue J12 with r3.
  module Left = N.Two J12.Joint.node
    (Iso.fun reassemble12 a0)
    (λ j -> r1 (J12.Joint.recover j))
    (λ j -> r3 (J12.Joint.recover j))

  -- Right-first: glue J23 with r1.
  module Right = N.Two J23.Joint.node
    (Iso.fun reassemble23 a0)
    (λ j -> r1 (J23.Joint.recover j))
    (λ j -> r2 (J23.Joint.recover j) , r3 (J23.Joint.recover j))

  -- Canonical maps using the stored fiber proof p.
  triple-to-left : J123.Joint.R.Total -> Left.Joint.R.Total
  triple-to-left ((v1 , (v2 , v3)) , a , p) =
    (v1 , v3) , Iso.fun reassemble12 a ,
    cong (λ { (u1 , (u2 , u3)) -> (u1 , u3) }) p

  triple-to-right : J123.Joint.R.Total -> Right.Joint.R.Total
  triple-to-right ((v1 , (v2 , v3)) , a , p) =
    (v1 , (v2 , v3)) , Iso.fun reassemble23 a , p
    -- p already has type (r1 a, (r2 a, r3 a)) ≡ (v1, (v2, v3)),
    -- which matches Right's r1(recover j), (r2(recover j), r3(recover j))
    -- since recover(Iso.fun reassemble23 a) = a definitionally.

  left-to-triple : Left.Joint.R.Total -> J123.Joint.R.Total
  left-to-triple ((v1 , v3) , j , p) =
    (v1 , (r2 (J12.Joint.recover j) , v3)) , J12.Joint.recover j ,
    cong (λ { (u1 , u3) -> u1 , (r2 (J12.Joint.recover j) , u3) }) p

  right-to-triple : Right.Joint.R.Total -> J123.Joint.R.Total
  right-to-triple ((v1 , (v2 , v3)) , j , p) =
    (v1 , (v2 , v3)) , J23.Joint.recover j , p

  left-to-right : Left.Joint.R.Total -> Right.Joint.R.Total
  left-to-right t = triple-to-right (left-to-triple t)

  right-to-left : Right.Joint.R.Total -> Left.Joint.R.Total
  right-to-left t = triple-to-left (right-to-triple t)

compiled : Type
compiled = C.History