# Pentachoron parent and inward/outward direction trial

Date: 2026-10-09
Status: First constructive test; electron and charge identifications unresolved

## Operator question

Could the electron be represented by a pentachoron, and could outward versus inward construction account for negative versus positive charge?

This first test separates geometric existence, traversal reversal, and cyclic-mode reversal. It does not silently equate them.

## A four-dimensional parent of the current hydrogen-1 picture

Retain A=(1,1,1), B=(1,-1,-1), C=(-1,1,-1), D=(-1,-1,1). With F=(A+B+C)/3, the reflected apex is E=2F-D=(5/3,5/3,-5/3).

Lift A,B,C,D to fourth coordinate zero and E to fourth coordinate one. The five points are affinely independent in R4. Dropping the fourth coordinate recovers exactly the two face-sharing regular tetrahedra ABCD and ABCE, including the opposite-side apex condition.

The parent itself is **not regular**. The hidden height one is supplied; replacing it by any nonzero height still gives a nondegenerate parent with the same zero-shear projection. Thus this construction does not select a fourth-dimensional metric or scale.

Its five boundary tetrahedra split into:

- the displayed pair ABCD, ABCE;
- the complementary three ABDE, ACDE, BCDE, sharing DE.

The signed simplicial boundary has boundary zero. Under the zero-shear projection these give the familiar two alternative triangulations of the bipyramid. The complete projected boundary should not be interpreted as five disjoint spatial volumes.

**Interpretive distinction:** this constructs a parent containing both current tetrahedra as boundary cells. It does not establish that the electron alone is the complete pentachoron. That stronger reading would require deciding how the proton relates to the electron's full boundary and what the other cells represent. No five-cell spinor encoding has been derived here.

## What direction reversal actually does

The full 4-simplex has 120 maximal flags and 75 immediate incidence arrows among its nonempty cells. A selected outward flag is:

ABCDE → ABCD → ABC → AB → A.

Reversing it gives an inward traversal with the same cells and the same locations. Reversal is involutive. It does not, by itself, change their orientations or ordered cyclic-mode inputs. The displayed path is one flag out of 120, not the whole branching construction.

For a retained oriented triangle mode,

v = F + ωa + ω²b = r + i√3 s,
r = F − (a+b)/2, s = (a−b)/2.

Two distinct tests give different results:

1. Reverse only the incidence traversal. The ordered tuple (F,a,b) stays fixed, so v and its nonzero bivector r×s stay fixed. This supplies a counterexample to the claim that traversal reversal alone necessarily reverses the signed flux.
2. Reverse the cyclic order a↔b. Then r stays fixed, s changes sign, v is conjugated, and r×s changes sign. This is the known geometric flux-reversal mechanism.

Consequently an outward/inward charge rule needs a constructor relating traversal direction to cyclic order or to another signed coupling. It cannot be obtained just by playing a growth sequence backward. Neither operation in this test derives electromagnetic charge.

## Viewer

The existing `papers/witness-generators/proton-neutron-assembly.html` now has a switchable **Pentachoron / direction trial**.

It shows the original pair, complementary three, or all five boundary cells. A projection shear adds λw to the displayed horizontal coordinate, revealing dependence on the hidden coordinate. This is a declared linear projection, not a four-dimensional rotation. At λ=0 the original face-attached geometry is recovered.

A direction selector and path-reveal slider show the selected flag in either direction. No positive/negative charge labels are assigned by the animation. Switching the trial off restores the existing tetrahedral constructions; it does not replace their stored operators.

## Verification and next missing operation

`python research/voevodsky/checkers/check_pentachoron_direction_trial.py`

Exact rational checks cover nondegeneracy, projection, face attachment, complementary incidence, boundary cancellation, flag reversal and the two distinct mode-reversal tests. Result: `results/pentachoron_direction_trial.json`.

The next missing operation is a source-defined map from construction direction to cyclic orientation or spinorial phase action. The geometric parent exists; the physical identifications do not yet follow.
