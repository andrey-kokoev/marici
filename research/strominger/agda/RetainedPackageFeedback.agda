{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedPackageFeedback where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (tt)
open import Cubical.Data.Maybe.Base using (Maybe; just; nothing)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Relation.Nullary.Base using (¬_)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open import NativeExtensionFamilyAudit using
  (Vertex; A; B; D; AB; AD; pointQ; Seeds; root; isB)
open import SourceIndexedExtensionFamilies using (Out)

open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

-- The initial derivation is supplied ONCE. Every extension retains the whole
-- prior chain, including that actual derivation and every chosen edge witness.
data Chain : Vertex → Type₁ where
  initial : (v : Vertex) → Resolve Seeds (pointQ v) → Chain v
  extend : {v : Vertex} (previous : Chain v) (edge : Out v) → Chain (fst edge)

package : {v : Vertex} → Chain v → Complete
package (initial v d) = pointQ v
package (extend {v} previous edge) = E-package (Out v)
  (λ _ → path-package (expression (package previous))
    (value (package previous)) (value (package previous)) refl) edge

-- The recursive premise is the retained derivation of previous, not root(v).
derivation : {v : Vertex} (c : Chain v) → Resolve Seeds (package c)
derivation (initial v d) = d
derivation (extend {v} previous edge) = apply
  (E-rule (Out v)
    (λ _ → path-package (expression (package previous))
      (value (package previous)) (value (package previous)) refl) edge)
  (λ _ → apply
    (reflexivity-rule (expression (package previous)) (value (package previous)))
    (λ _ → derivation previous))

Total : Type₁
Total = Σ Vertex Chain
boundary : Total → Vertex
boundary = fst
Questions : Total → Type
Questions c = Out (boundary c)
step : (c : Total) → Questions c → Total
step (v , c) edge = fst edge , extend c edge
previous : Total → Maybe Total
previous (v , initial _ _) = nothing
previous (_ , extend {v} c edge) = just (v , c)
step-retains : (c : Total) (edge : Questions c) → previous (step c edge) ≡ just c
step-retains c edge = refl

closure : Total → Closure Seeds
closure (v , c) = package c , derivation c
-- Read actual premise derivations from the native output, not a second copy
-- of a source seed table. Other rule forms are left unchanged by this reader.
peel : Closure Seeds → Closure Seeds
peel (_ , apply (E-rule I F i) ds) = F i , ds (lift i)
peel (_ , apply (reflexivity-rule Q x) ds) = pack Q x , ds (lift tt)
peel c = c
native-premises-retained : (c : Total) (edge : Questions c)
  → peel (peel (closure (step c edge))) ≡ closure c
native-premises-retained c edge = refl

-- A fixed next-universe code provides an explicit admission interface.
-- This is NOT a decoder for arbitrary Complete values or arbitrary syntax.
module W = Whole.Universe (ℓ-suc ℓ-zero)
record Ready : Type₂ where
  constructor ready
  field
    whole : W.Complete
    admission : W.expression whole ≡ W.atom Total
open Ready
encode : Total → Ready
encode c = ready (W.pack (W.atom Total) c) refl
decode : Ready → Total
decode r = subst W.El (admission r) (W.value (whole r))
decode-encode : (c : Total) → decode (encode c) ≡ c
decode-encode c = substRefl {B = W.El} {x = W.atom Total} c

Task : Ready → Type
Task r = Questions (decode r)
run : (r : Ready) → Task r → Ready
run r edge = encode (step (decode r) edge)
run-decodes : (r : Ready) (edge : Task r)
  → decode (run r edge) ≡ step (decode r) edge
run-decodes r edge = decode-encode (step (decode r) edge)
run-retains : (r : Ready) (edge : Task r)
  → previous (decode (run r edge)) ≡ just (decode r)
run-retains r edge = cong previous (run-decodes r edge)
run-native-premises : (r : Ready) (edge : Task r)
  → peel (peel (closure (decode (run r edge)))) ≡ closure (decode r)
run-native-premises r edge = cong (λ c → peel (peel (closure c))) (run-decodes r edge)

-- The API can be applied again to its own admitted result. It still requires
-- the actual second edge witness; closure of admission does not invent it.
run-twice : (r : Ready) (e : Task r) → Task (run r e) → Ready
run-twice r e f = run (run r e) f

-- Initial source lookup occurs only in this fixture, not the feedback law.
base : Chain A
base = initial A (root A)
left : Chain B
left = extend base (B , AB)
alternative : Chain D
alternative = extend base (D , AD)
branch-values-distinct : ¬ (value (package left) ≡ value (package alternative))
branch-values-distinct p = false≢true
  (sym (cong (λ x → isB (fst (fst x))) p))
