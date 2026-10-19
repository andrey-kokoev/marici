{-# OPTIONS --safe --cubical --guardedness #-}
module TickOperationalWholeReturnKernel where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool)
open import Cubical.Data.Sigma.Base using (_×_; _,_)
open import CauchyMetricEquivalence using (MetricCompletionCandidate)
open import CauchyCompletionCommRing using (oneCompletion)
import TickCompletionMetricInterval as I
import TickCompletionClippedTime as Time
import TickSpectralLocalOperators as L
import TickSpectralLocalDynamics as D
import TickSpectralRetainedReturn as R
import TickSpectralOpenPieces as O
import TickSpectralPiecewiseDerivative as PD
import TickSpectralHamiltonian as H
import TickSpectralGlobalPath as Path
import TickSpectralFactorOperators as F
import TickSpectralLocalInverse as Inv
import TickSpectralLocalNorm as N
import TickSpectralCovariance as Cov
import TickSpectralWitnessCorrespondence as W
import TickComplexNativeBasis as B
import TickRetainedStructure as S
module V = L.V
module G = R.G

-- Explicit public theorem types. Every field is about the same fixed
-- operational spectral operators and the same actual interval return.
LocalLaws : Type
LocalLaws = D.Operational.LocalDynamics L.leftLocal D.leftGenerator ×
  D.Operational.LocalDynamics L.rightLocal D.rightGenerator

ReturnLaws : Type
ReturnLaws =
  ((r : G.Schedule) (s : V.Label) → R.returnPath r s I.start ≡ R.nativeTarget s) ×
  ((r : G.Schedule) (s : V.Label) → R.returnPath r s I.finish ≡ B.basis s) ×
  ((r : G.Schedule) (s : V.Label) → Path.IntervalPathContinuous (R.returnPath r s)) ×
  ((r : G.Schedule) (s : V.Label) (t : I.ReturnInterval) → N.vectorNormSquared (R.returnPath r s t) ≡ oneCompletion)

GeneratorLaws : Type
GeneratorLaws =
  ((r : G.Schedule) (s : V.Label) (u : O.FirstOpenPiece) →
    D.HasVectorMetricDerivative (PD.returnCurve r s) (fst (fst u))
      (V.scale H.minusI (H.hamiltonian (Path.permute (PD.firstIndex r)) (PD.returnCurve r s (fst (fst u)))))) ×
  ((r : G.Schedule) (s : V.Label) (u : O.SecondOpenPiece) →
    D.HasVectorMetricDerivative (PD.returnCurve r s) (fst (fst u))
      (V.scale H.minusI (H.hamiltonian (Path.permute (PD.secondIndex r)) (PD.returnCurve r s (fst (fst u))))))

CoherenceLaws : Type
CoherenceLaws =
  ((s : V.Label) (t : S.AtSource.A.Tick s) → R.AtSource.realize s t ≡ R.AtSource.realize s (S.AtSource.rebuild s (S.AtSource.tags s t))) ×
  ((s : V.Label) (r q : G.Schedule) → R.AtSource.realize s (S.AtSource.rebuild s (q , r)) ≡
    R.AtSource.swap s (R.AtSource.realize s (S.AtSource.rebuild s (r , q)))) ×
  ((s : V.Label) (t u : S.AtSource.A.Tick s) → R.AtSource.realize s t ≡ R.AtSource.realize s u → t ≡ u)

FactorLaws : Type
FactorLaws =
  ((t : MetricCompletionCandidate) (A : F.F.Matrix) (v : V.Vector) →
    L.leftLocal t (F.F.left A (Inv.leftInverse t v)) ≡ F.F.left (F.F.compose (F.localMatrix t) (F.F.compose A (F.inverseMatrix t))) v) ×
  ((t : MetricCompletionCandidate) (A : F.F.Matrix) (v : V.Vector) →
    L.rightLocal t (F.F.right A (Inv.rightInverse t v)) ≡ F.F.right (F.F.compose (F.localMatrix t) (F.F.compose A (F.inverseMatrix t))) v) ×
  ((t : MetricCompletionCandidate) (A : F.F.Matrix) (v : V.Vector) → L.leftLocal t (F.F.right A (Inv.leftInverse t v)) ≡ F.F.right A v) ×
  ((t : MetricCompletionCandidate) (A : F.F.Matrix) (v : V.Vector) → L.rightLocal t (F.F.left A (Inv.rightInverse t v)) ≡ F.F.left A v) ×
  ((s t : MetricCompletionCandidate) (v : V.Vector) → L.leftLocal s (L.rightLocal t v) ≡ L.rightLocal t (L.leftLocal s v))

CovarianceLaws : Type
CovarianceLaws =
  ((r : G.Schedule) (s : V.Label) (t : I.ReturnInterval) → V.exchange (R.returnPath r s t) ≡ R.returnPath (Cov.swapSchedule r) (Cov.exchangeIndex s) t) ×
  ((p q : Bool) (r : G.Schedule) (s : V.Label) (t : I.ReturnInterval) →
    Cov.reindex (Cov.renameIndex p q) (R.returnPath r s t) ≡ R.returnPath r (Cov.renameIndex p q s) t) ×
  ((t : MetricCompletionCandidate) (v : V.Vector) → V.exchange (L.leftLocal t v) ≡ L.rightLocal t (V.exchange v)) ×
  ((v : V.Vector) → V.exchange (H.hamiltonian V.left v) ≡ H.hamiltonian V.right (V.exchange v))

StructuralLaws : Type
StructuralLaws =
  ((t : MetricCompletionCandidate) → W.adjoint (F.localMatrix t) ≡ F.inverseMatrix t) ×
  (W.adjoint F.hamiltonianMatrix ≡ F.hamiltonianMatrix) ×
  ((t : MetricCompletionCandidate) → F.localMatrix t ≡ W.referenceLocalMatrix t) ×
  (F.hamiltonianMatrix ≡ W.referenceHamiltonian) ×
  ((s : V.Label) → R.nativeTarget s ≡ B.basis (G.run G.leftFirst s)) ×
  ((r : G.Schedule) (s : V.Label) (t : I.LeftPiece) → R.returnPath r s (fst t) ≡
    L.local (Path.permute (W.first r)) (fst (fst t)) (R.nativeTarget s)) ×
  ((r : G.Schedule) (s : V.Label) (t : I.RightPiece) → R.returnPath r s (fst t) ≡
    L.local (Path.permute (W.second r)) (Time.afterOne (fst (fst t))) (Path.permute (W.first r) (R.nativeTarget s)))

-- Generic syntax avoids traversing operational schedules in positivity checks.
record KernelBundle (Local Return Generator Coherence Factor Covariance Structural : Type) : Type where
  field
    local : Local
    returns : Return
    generators : Generator
    coherence : Coherence
    factors : Factor
    covariance : Covariance
    structural : Structural

OperationalWholeReturnKernel : Type
OperationalWholeReturnKernel = KernelBundle LocalLaws ReturnLaws GeneratorLaws CoherenceLaws FactorLaws CovarianceLaws StructuralLaws

abstract
  operational-whole-return-kernel : OperationalWholeReturnKernel
  operational-whole-return-kernel .KernelBundle.local = D.left-local-dynamics , D.right-local-dynamics
  operational-whole-return-kernel .KernelBundle.returns = R.return-start , R.return-finish , R.return-continuous , R.return-unit-norm
  operational-whole-return-kernel .KernelBundle.generators = O.return-first-open-generator , O.return-second-open-generator
  operational-whole-return-kernel .KernelBundle.coherence = R.AtSource.reconstruction-coherence , R.AtSource.schedule-swap , R.AtSource.fixed-source-faithful
  operational-whole-return-kernel .KernelBundle.factors = F.left-conjugates-own-factor , F.right-conjugates-own-factor , F.left-fixes-other-factor , F.right-fixes-other-factor , F.local-legs-commute
  operational-whole-return-kernel .KernelBundle.covariance = Cov.exchange-return , Cov.relabel-return , Cov.exchange-left-local , Cov.exchange-left-hamiltonian
  operational-whole-return-kernel .KernelBundle.structural = W.local-adjoint-is-inverse , W.hamiltonian-self-adjoint , W.local-matrix-specification , W.hamiltonian-matrix-specification , R.native-target-correspondence , W.return-first-piece-specification , W.return-second-piece-specification

-- No standard-real interpretation law is assumed or claimed. Full net target
-- admission requires that remaining semantic obligation in addition to this
-- unconditional operational kernel bundle.
