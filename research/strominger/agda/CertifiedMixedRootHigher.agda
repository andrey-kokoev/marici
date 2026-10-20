{-# OPTIONS --safe --cubical --guardedness #-}
module CertifiedMixedRootHigher where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Maybe.Base using (just)
open import Cubical.Data.Sigma.Base using (_×_)
open import NativeExtensionFamilyAudit using (A; C; Seeds; pointQ)
open import SourceIndexedExtensionFamilies using (Out)
import ForwardCertifiedPrograms as P
open import InternalSourceComparisons using (Mode; package)
import FiniteComparisonTrees as F
import MixedComparisonTrees as M
import MixedHistoryCertificates as H
import CertifiedMixedHistoryOrigins as O
import MixedRootHistoryCoherence as R
import InternalComparisonInterchange as Native
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

-- Certified actual-input objects. No constructor accepts a bare mixed tree.
record Tree (m : Mode) (a b : F.Object) : Type₁ where
  constructor checked
  field
    tree : M.Tree m a b
    origins : O.Origins tree
bundle : {m : Mode} {a b : F.Object} (r : Tree m a b) → O.CertifiedTree (Tree.tree r)
bundle r = O.assemble (Tree.tree r) (Tree.origins r)

-- Finite expression grammar; no Full boundary or equivalence import.
data Boundary {m : Mode} {a b : F.Object} : Tree m a b → Tree m a b → Type₁ where
  direct : (r s : Tree m a b) → Boundary r s
  compose : {r s t : Tree m a b} → Boundary r s → Boundary s t → Boundary r t
evaluate : {m : Mode} {a b : F.Object} {r s : Tree m a b}
  → Boundary r s → H.RootBoundary (Tree.tree r) (Tree.tree s)
evaluate (direct r s) = R.root-boundary (Tree.tree r) (Tree.tree s)
evaluate (compose {r} {s} {t} u v) = R.composeBoundary
  {r = Tree.tree r} {s = Tree.tree s} {t = Tree.tree t} (evaluate u) (evaluate v)

module Pair {m : Mode} {a b : F.Object} {r s : Tree m a b} (u v : Boundary r s) where
  module Q = R.Higher (Tree.tree r) (Tree.tree s)
  path : evaluate u ≡ evaluate v
  path = Q.coherence (evaluate u) (evaluate v)
  closure : Closure Seeds
  closure = path-package Q.E.CodeE (Q.E.section (evaluate u)) (Q.E.section (evaluate v)) (Q.E.liftPath path)
    , Q.path-native (evaluate u) (evaluate v)
  recovered : cong fst (Q.E.liftPath path) ≡ path
  recovered = Q.E.path-recovery path
module Square {m : Mode} {a b : F.Object} {r s : Tree m a b} (u v w : Boundary r s) where
  module Q = R.Higher (Tree.tree r) (Tree.tree s)
  directPath : evaluate u ≡ evaluate v
  directPath = Pair.path u v
  viaPath : evaluate u ≡ evaluate v
  viaPath = Pair.path u w ∙ Pair.path w v
  square : directPath ≡ viaPath
  square = Q.square directPath viaPath
  closure : Closure Seeds
  closure = higher-package Q.E.CodeE (Q.E.section (evaluate u)) (Q.E.section (evaluate v))
    (Q.E.liftPath directPath) (Q.E.liftPath viaPath) (Q.E.liftHigher square)
    , Q.square-native directPath viaPath
  recovered : cong (cong fst) (Q.E.liftHigher square) ≡ square
  recovered = Q.E.higher-recovery square

rootClosure : {m : Mode} {a b : F.Object} (r s : Tree m a b)
  → H.RootBoundary (Tree.tree r) (Tree.tree s) → Closure Seeds
rootClosure r s w = package (R.asBody (Tree.tree r) (Tree.tree s) w) , R.native (Tree.tree r) (Tree.tree s) w

-- Families, full boundaries, paths and squares are computed from certified
-- objects and expression trees. They are not independent producer ports.
data Program : Type₁ where
  compareP : {m : Mode} {a b : F.Object} {r s : Tree m a b} → Boundary r s → Program
  envelopeP : {m : Mode} {a b : F.Object} {r s : Tree m a b} → Boundary r s → Program
  pathP : {m : Mode} {a b : F.Object} {r s : Tree m a b} → Boundary r s → Boundary r s → Program
  squareP : {m : Mode} {a b : F.Object} {r s : Tree m a b}
    → Boundary r s → Boundary r s → Boundary r s → Program
native : Program → Closure Seeds
native (compareP {r = r} {s} u) = rootClosure r s (evaluate u)
native (envelopeP {r = r} {s} u) = Q.E.encoded (evaluate u) , Q.E.native (evaluate u)
  where module Q = R.Higher (Tree.tree r) (Tree.tree s)
native (pathP u v) = Pair.closure u v
native (squareP u v w) = Square.closure u v w
operands-recovered : {m : Mode} {a b : F.Object} {r s : Tree m a b} (u : Boundary r s)
  → Native.comparisonOperands (native (compareP u))
    ≡ just (Native.closure (fst b , H.root (Tree.tree r)), Native.closure (fst b , H.root (Tree.tree s)))
operands-recovered {r = r} {s} u = R.root-operands-recovered (Tree.tree r) (Tree.tree s) (evaluate u)

-- Existing full root comparisons can be matched, but are never stored in
-- Program as free parameters. Matching retains the actual native derivation.
record Certificate (original : Closure Seeds) : Type₁ where
  constructor certificate
  field
    producer : Program
    matches : native producer ≡ original
comparison-certificate : {m : Mode} {a b : F.Object} (r s : Tree m a b)
  (w : H.RootBoundary (Tree.tree r) (Tree.tree s))
  → Certificate (package (R.asBody (Tree.tree r) (Tree.tree s) w) , R.native (Tree.tree r) (Tree.tree s) w)
comparison-certificate r s w = certificate (compareP (direct r s))
  (cong (rootClosure r s) (R.boundary-prop (Tree.tree r) (Tree.tree s) (evaluate (direct r s)) w))

triangleProgram : {m : Mode} {a b : F.Object} (r s t : Tree m a b) → Program
triangleProgram r s t = pathP (compose (direct r s) (direct s t)) (direct r t)
triangleClosure : {m : Mode} {a b : F.Object} (r s t : Tree m a b) → Closure Seeds
triangleClosure r s t = _ , R.TriangleAdmission.admitted-triangle (Tree.tree r) (Tree.tree s) (Tree.tree t)
triangle-matches : {m : Mode} {a b : F.Object} (r s t : Tree m a b)
  → native (triangleProgram r s t) ≡ triangleClosure r s t
triangle-matches r s t = refl

-- Retain the source/history evidence of every intermediate object in a
-- boundary expression, rather than reporting only its outer endpoints.
Evidence : {m : Mode} {a b : F.Object} {r s : Tree m a b} → Boundary r s → Type₁
Evidence (direct r s) = O.CertifiedTree (Tree.tree r) × O.CertifiedTree (Tree.tree s)
Evidence (compose u v) = Evidence u × Evidence v
evidence : {m : Mode} {a b : F.Object} {r s : Tree m a b} (u : Boundary r s) → Evidence u
evidence (direct r s) = bundle r , bundle s
evidence (compose u v) = evidence u , evidence v
ProgramEvidence : Program → Type₁
ProgramEvidence (compareP u) = Evidence u
ProgramEvidence (envelopeP u) = Evidence u
ProgramEvidence (pathP u v) = Evidence u × Evidence v
ProgramEvidence (squareP u v w) = Evidence u × Evidence v × Evidence w
programEvidence : (p : Program) → ProgramEvidence p
programEvidence (compareP u) = evidence u
programEvidence (envelopeP u) = evidence u
programEvidence (pathP u v) = evidence u , evidence v
programEvidence (squareP u v w) = evidence u , evidence v , evidence w

-- Actual forward-context roots of different retained syntax, not fresh roots.
module Forward (d : Resolve Seeds (pointQ A)) (c0 : P.InitialCertificate A d) (o : Out C) where
  module X = O.Forward d c0 o
  r = checked X.t X.origin
  s = checked (M.old X.core) (fst X.origin)
  t = checked (M.old (F.cell X.f)) (fst (fst X.origin))
  triangle : Program
  triangle = triangleProgram r s t
  square : Program
  square = squareP (compose (direct r s) (direct s t)) (direct r t)
    (compose (direct r r) (direct r t))
  triangle-inputs : ProgramEvidence triangle
  triangle-inputs = programEvidence triangle
  square-inputs : ProgramEvidence square
  square-inputs = programEvidence square
  actual-triangle-match : native triangle ≡ triangleClosure r s t
  actual-triangle-match = triangle-matches r s t
