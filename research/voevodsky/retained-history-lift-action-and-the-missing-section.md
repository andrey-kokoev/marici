# Retained history, signed lift, action: no multiplicative lift selector

## Selection and independent audit

The operator chose Nima's new concrete Clifford example before further abstract
three-profile coherence. Fresh resume still selected that generic coherence
leaf; its associativity theorem is not claimed solved by this experiment.

I read `research/nima/clifford-retained-order-recursion.md` and its checker,
then reran the COMPLETE checker in an isolated sandbox. Its source file was
copied, and its receipt write redirected; the original checker, source and
receipt hashes were unchanged. This reproduces the source-sector intertwiner,
64 cocycle cases, 512 signed associativity cases, reversal/inverse controls,
and 127 words / 3239 parenthesizations through length six.

The owner's restrictions remain important: this is a declared Cl(2,0) lift of
an active four-dimensional source-product sector, not the entire sixteen-
dimensional source product, not an isometry, and not a selected physical theory.
The linear intertwiner does not derive Clifford multiplication from source
multiplication. No independent rerun of the separate square-reversal Agda root
is claimed here.

## The retained observation chain

The concrete object is a full construction tree, not its normal form:

    History -> SignedLift -> AdjointAction.

Our syntax includes unit, either generator, binary multiplication and explicit
reversal nodes. Thus parenthesizations and reversal operations remain recorded.
The signed lift is (epsilon,a,b), where epsilon records the sign and (a,b) the
Clifford grade. The action forgets epsilon. Exact matrix checks show that these
four action labels classify the adjoint maps of the eight signed basis units.

`agda/RetainedCliffordProfiles.agda` instantiates the actual native retained-
profile and coarsening interfaces on this history type. It also attaches the
owner's actual retained source swap comparison and an explicit restricted-sector
scope tag. Every modeled history remains recoverable. Action-level regrouping
retains BOTH its signed-lift index and the entire construction tree.

This is the complete history of the DECLARED WORD PROTOTYPE, not a replacement
for all higher witnesses or histories of the owner's full source calculus.

## Two different losses that normalization must not hide

- e1 e2 and e2 e1 have the same action but lifts J and -J.
- The empty history and e1 e1 have the same signed lift but different histories.

Both distinctions are proved in Agda. The finite audit additionally retains all
3239 distinct multiplication trees and checks exact recovery after composition
and reversal. A double reversal node has the original lift reading but remains
a different construction record. A change of bracketing also remains recorded.

This does not prohibit separately supplied comparisons between routes. It
prohibits silently treating equality of their readings as equality of their
retained construction records.

## New structural obstruction: the action quotient has no multiplicative section

For the declared signed Clifford group, multiplication is

    (epsilon,a,b)*(delta,c,d)
      = (epsilon XOR delta XOR (b AND c), a XOR c, b XOR d).

Projection to the action bits preserves multiplication. However there is NO
choice of one lift per action that preserves multiplication.

Proof: the two generator actions commute. Any of their possible lifts are
+/-e1 and +/-e2, which still anticommute. A multiplicative section would therefore
force those chosen lifts to commute, a contradiction. Agda proves this for every
section and every choice of signs; the independent finite check tests all 16
set-theoretic sections and finds zero multiplicative ones.

This is stronger than showing that a particular representative convention fails.
The obstruction is inside THIS declared Clifford extension. It is not a theorem
that every source realization must use this extension or exhibit a physical phase.

Composition therefore needs the central sign/cocycle information. Keeping it
restores the signed multiplication law. Keeping the signed normal form still
does not retain the original history, so the full tree remains separate data.

This does not contradict the retained-family recovery theorem. That theorem
recovers from the coarse TOTAL, which still contains the histories and lifts,
not from an action LABEL alone. Set-theoretic lift selectors do exist here (all
16 were tested); what fails is choosing one that preserves multiplication.

## Composition and reversal checks

The signed group multiplication, cocycle and reversal laws are exhaustively
checked on their complete finite domains. The formal module proves action
composition, the native history/lift recovery laws, the distinctness controls
and the no-section theorem. Reversal reads the same declared signed reverse
while retaining its input subtree; composition retains its input trees.

General word-level associativity follows algebraically from the finite group
law. Enumeration of parenthesizations is explicitly bounded at length six;
this is not a formal construction of arbitrary higher source-coherence cells.

The owner's nonzero quantity is the lift DIFFERENCE J-(-J)=2J. The nested
commutator [J,-J] remains zero. Positive norm does not recover every phase or
history, and ordinary squaring fails on the owner's nonzero nilpotent control.
These distinctions survive the independent audit; no new universal residue or
physical scalar recurrence is inferred.

## Verification and next structural use

    python research/voevodsky/check_native_radar_formal.py --clifford-profiles --fresh
    python research/voevodsky/check_retained_clifford_profiles.py

Fresh safe/cubical closure passes. Direct negative controls reject lift-phase
erasure and identification of distinct histories with the same normal form. All 21 audit checks pass, including the full isolated owner rerun,
complete finite-group tests, all 16 sections, and recovery of 3239 history trees.
Receipts: `retained-clifford-profiles-formal.json` and
`retained-clifford-profiles.json`.

This supplies a concrete stress test for the pending three-profile coherence
work: gluing/reordering the history, lift and action organizations must retain
central signs and histories and must not introduce a multiplicative section of
the action quotient. Return to that existing leaf with these controls, rather
than add another disconnected physical model or claim its general theorem done.
