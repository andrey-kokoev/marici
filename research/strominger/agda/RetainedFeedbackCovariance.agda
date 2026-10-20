{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedFeedbackCovariance where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence using (ua; ua-gluePath)
open import Cubical.Foundations.Transport using (subst⁻Subst; substSubst⁻)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open Resolution.Generators ℓ-zero
open import NativeExtensionFamilyAudit using
  (Vertex; A; B; C; D; AB; BC; CA; BA; AD; DB;
   pointQ; graphQ; Seeds; sigma; sigma²; sigmaEquiv)
open import SourceIndexedExtensionFamilies using (Out; moveOut)
open import RetainedPackageFeedback

-- Do not collapse indexed source proofs to literal seed nodes. Their index
-- contains type-valued Code, and Cubical transport must remain present.
-- Univalence supplies a path of complete endpoint packages. The graph
-- provenance remains retained, while the selected vertex carrier is moved.
module Small = Whole.Universe ℓ-zero
pointPath : (v : Vertex) → pointQ v ≡ pointQ (sigma v)
pointPath v i = Small.remember graphQ
  (Small.pack (Small.atom (ua sigmaEquiv i))
    (ua-gluePath sigmaEquiv {x = v} {y = sigma v} refl i))
moveInitial : (v : Vertex) → Resolve Seeds (pointQ v) → Resolve Seeds (pointQ (sigma v))
moveInitial v = subst (Resolve Seeds) (pointPath v)
backInitial : (v : Vertex) → Resolve Seeds (pointQ v) → Resolve Seeds (pointQ (sigma v))
backInitial A = subst (Resolve Seeds) (sym (pointPath B))
backInitial B = subst (Resolve Seeds) (sym (pointPath A))
backInitial C = subst (Resolve Seeds) (sym (pointPath D))
backInitial D = subst (Resolve Seeds) (sym (pointPath C))
back-moveInitial : (v : Vertex) (d : Resolve Seeds (pointQ v))
  → PathP (λ i → Resolve Seeds (pointQ (sigma² v i)))
      (backInitial (sigma v) (moveInitial v d)) d
back-moveInitial A d = subst⁻Subst (Resolve Seeds) (pointPath A) d
back-moveInitial B d = subst⁻Subst (Resolve Seeds) (pointPath B) d
back-moveInitial C d = subst⁻Subst (Resolve Seeds) (pointPath C) d
back-moveInitial D d = subst⁻Subst (Resolve Seeds) (pointPath D) d
move-backInitial : (v : Vertex) (d : Resolve Seeds (pointQ v))
  → PathP (λ i → Resolve Seeds (pointQ (sigma² v i)))
      (moveInitial (sigma v) (backInitial v d)) d
move-backInitial A d = substSubst⁻ (Resolve Seeds) (pointPath B) d
move-backInitial B d = substSubst⁻ (Resolve Seeds) (pointPath A) d
move-backInitial C d = substSubst⁻ (Resolve Seeds) (pointPath D) d
move-backInitial D d = substSubst⁻ (Resolve Seeds) (pointPath C) d

-- Every retained edge and every native initial witness is transported.
moveChain : {v : Vertex} → Chain v → Chain (sigma v)
moveChain (initial v d) = initial (sigma v) (moveInitial v d)
moveChain (extend previous edge) = extend (moveChain previous) (moveOut edge)

backChain : {v : Vertex} → Chain v → Chain (sigma v)
backChain (initial v d) = initial (sigma v) (backInitial v d)
backChain (extend previous edge) = extend (backChain previous) (moveOut edge)

back-moveChain : (v : Vertex) (c : Chain v)
  → PathP (λ i → Chain (sigma² v i)) (backChain (moveChain c)) c
back-moveChain v (initial .v d) i = initial (sigma² v i) (back-moveInitial v d i)
back-moveChain _ (extend c (_ , AB)) i = extend (back-moveChain A c i) (B , AB)
back-moveChain _ (extend c (_ , BC)) i = extend (back-moveChain B c i) (C , BC)
back-moveChain _ (extend c (_ , CA)) i = extend (back-moveChain C c i) (A , CA)
back-moveChain _ (extend c (_ , BA)) i = extend (back-moveChain B c i) (A , BA)
back-moveChain _ (extend c (_ , AD)) i = extend (back-moveChain A c i) (D , AD)
back-moveChain _ (extend c (_ , DB)) i = extend (back-moveChain D c i) (B , DB)
move-backChain : (v : Vertex) (c : Chain v)
  → PathP (λ i → Chain (sigma² v i)) (moveChain (backChain c)) c
move-backChain v (initial .v d) i = initial (sigma² v i) (move-backInitial v d i)
move-backChain _ (extend c (_ , AB)) i = extend (move-backChain A c i) (B , AB)
move-backChain _ (extend c (_ , BC)) i = extend (move-backChain B c i) (C , BC)
move-backChain _ (extend c (_ , CA)) i = extend (move-backChain C c i) (A , CA)
move-backChain _ (extend c (_ , BA)) i = extend (move-backChain B c i) (A , BA)
move-backChain _ (extend c (_ , AD)) i = extend (move-backChain A c i) (D , AD)
move-backChain _ (extend c (_ , DB)) i = extend (move-backChain D c i) (B , DB)

move back : Total → Total
move (v , c) = sigma v , moveChain c
back (v , c) = sigma v , backChain c
back-move : (c : Total) → back (move c) ≡ c
back-move (v , c) i = sigma² v i , back-moveChain v c i
move-back : (c : Total) → move (back c) ≡ c
move-back (v , c) i = sigma² v i , move-backChain v c i
wholeEquiv : Total ≃ Total
wholeEquiv = isoToEquiv (iso move back move-back back-move)

-- The fundamental square includes the complete chain, not just its endpoint.
extension-square : (c : Total) (e : Questions c)
  → move (step c e) ≡ step (move c) (moveOut e)
extension-square c e = refl

-- The composed task fiber is dependent: the second question belongs to the
-- actual first output. Transport preserves both witnesses and their seam.
TwoTasks : Total → Type
TwoTasks c = Σ (Questions c) (λ e → Questions (step c e))
moveTwo : (c : Total) → TwoTasks c → TwoTasks (move c)
moveTwo c (e , f) = moveOut e , moveOut f
two-extension-square : (c : Total) (e : Questions c) (f : Questions (step c e))
  → move (step (step c e) f)
    ≡ step (step (move c) (moveOut e)) (moveOut f)
two-extension-square c e f = refl

-- Applying the actual native interpreter gives equality of complete native
-- endpoints AND their retained Resolve derivations. No new seed lookup occurs.
native-history-square : (c : Total) (e : Questions c)
  → closure (move (step c e)) ≡ closure (step (move c) (moveOut e))
native-history-square c e = cong closure (extension-square c e)
transported-parent-retained : (c : Total) (e : Questions c)
  → peel (peel (closure (move (step c e)))) ≡ closure (move c)
transported-parent-retained c e = refl

-- Arbitrary admitted inputs may require code transport to decode. Normalize
-- into the canonical admitted presentation without discarding decoded content.
moveReady : Ready → Ready
moveReady r = encode (move (decode r))
normalization : (r : Ready) → move (decode r) ≡ decode (moveReady r)
normalization r = sym (decode-encode (move (decode r)))
moveTask : (r : Ready) → Task r → Task (moveReady r)
moveTask r e = subst Questions (normalization r) (moveOut e)

step-along : {c d : Total} (p : c ≡ d) (e : Questions c)
  → step c e ≡ step d (subst Questions p e)
step-along p e i = step (p i) (subst-filler Questions p e i)

-- Equality of the actual admitted output packages, including their canonical
-- admission certificates. This does not assert proof irrelevance of arbitrary
-- input admission paths or literal equality of serialized presentations.
ready-square : (r : Ready) (e : Task r)
  → moveReady (run r e) ≡ run (moveReady r) (moveTask r e)
ready-square r e = cong encode
  (cong move (run-decodes r e)
   ∙ extension-square (decode r) e
   ∙ step-along (normalization r) (moveOut e))

-- A second application has the same typed square, with the first output as
-- its actual input. The statement is uniform over arbitrary finite chains.
ready-next-square : (r : Ready) (e : Task r) (f : Task (run r e))
  → moveReady (run (run r e) f)
    ≡ run (moveReady (run r e)) (moveTask (run r e) f)
ready-next-square r e f = ready-square (run r e) f
