import Mathlib.Algebra.Group.Hom.End

/-!
Additive core of Grothendieck's selected-cocycle descent theorem. It records
only descent of one scalar readout and does not construct a homology map or a
physical chain correspondence.
-/

namespace MariciFormal

section SelectedReadout

variable {SourceHigh SourceLow TargetHigh TargetLow Scalar : Type*}
variable [AddCommGroup SourceHigh] [AddCommGroup SourceLow]
variable [AddCommGroup TargetHigh] [AddCommGroup TargetLow]
variable [AddCommGroup Scalar]

def additiveBoundaryDefect
    (targetBoundary : TargetHigh →+ TargetLow)
    (highMap : SourceHigh →+ TargetHigh)
    (lowMap : SourceLow →+ TargetLow)
    (sourceBoundary : SourceHigh →+ SourceLow) : SourceHigh →+ TargetLow :=
  targetBoundary.comp highMap - lowMap.comp sourceBoundary

def SelectedReadoutDescends
    (sourceBoundary : SourceHigh →+ SourceLow)
    (lowMap : SourceLow →+ TargetLow)
    (readout : TargetLow →+ Scalar) : Prop :=
  ∀ source, readout (lowMap (sourceBoundary source)) = 0

def ReadoutAnnihilatesDefect
    (targetBoundary : TargetHigh →+ TargetLow)
    (highMap : SourceHigh →+ TargetHigh)
    (lowMap : SourceLow →+ TargetLow)
    (sourceBoundary : SourceHigh →+ SourceLow)
    (readout : TargetLow →+ Scalar) : Prop :=
  ∀ source,
    readout (additiveBoundaryDefect targetBoundary highMap lowMap
      sourceBoundary source) = 0

/-- For a target cocycle, the selected scalar readout descends through source
boundaries exactly when it annihilates the next-degree chain defect. -/
theorem selectedReadoutDescends_iff_annihilatesDefect
    (targetBoundary : TargetHigh →+ TargetLow)
    (highMap : SourceHigh →+ TargetHigh)
    (lowMap : SourceLow →+ TargetLow)
    (sourceBoundary : SourceHigh →+ SourceLow)
    (readout : TargetLow →+ Scalar)
    (hcocycle : ∀ target, readout (targetBoundary target) = 0) :
    SelectedReadoutDescends sourceBoundary lowMap readout ↔
      ReadoutAnnihilatesDefect targetBoundary highMap lowMap
        sourceBoundary readout := by
  constructor
  · intro hdescends source
    simp [additiveBoundaryDefect, hcocycle, hdescends source]
  · intro hannihilates source
    have h := hannihilates source
    simp [additiveBoundaryDefect, hcocycle] at h
    simpa using h

end SelectedReadout

end MariciFormal
