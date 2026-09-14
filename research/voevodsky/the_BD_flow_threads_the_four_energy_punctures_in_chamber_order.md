# The Bunch–Davies flow threads the four energy punctures in chamber order

## Question

Given the four total-energy discriminant values, what based path is selected by the physical lower-half-plane prescription before any comparison with conductor wall monodromy?

## Claim boundary

This packet determines the path in the punctured \(E\)-plane from the declared physical base value. It does not compute its braid-to-Picard lift or identify its braid factors with conductor wall swaps.

## Triangle chamber

Let

\[
E_{\rm phys}=x+y+z
\]

with positive \(x,y,z\) satisfying the strict triangle inequalities. Then

\[
\max(2x,2y)<E_{\rm phys}<2(x+y).
\]

If \(x<y\), the real order is

\[
0<2x<2y<E_{\rm phys}<2(x+y).
\]

The Bunch–Davies continuation toward \(E=0\) through the lower half-plane therefore threads the punctures in the order

\[
E_{\rm phys}
\longrightarrow
\text{below }2y
\longrightarrow
\text{below }2x
\longrightarrow
0.
\]

If \(y<x\), the middle order reverses:

\[
E_{\rm phys}
\longrightarrow
\text{below }2x
\longrightarrow
\text{below }2y
\longrightarrow
0.
\]

The puncture \(2(x+y)\) lies to the right of the basepoint and is not crossed by this continuation.

## Role in the coherence pyramid

The flow is not a fork from \(0\) through two middle vertices followed by endpoint equalization. It is one chamber-dependent based path from the physical basepoint to the \(E=0\) boundary, with an ordered pair of lower detours around the middle punctures.

The information carried by this path consists of:

- the order of the two middle punctures;
- lower rather than upper detours;
- the resulting braid word on the four roots;
- the Bunch–Davies orientation of the terminal collision arcs at \(E=0\).

Root permutations cannot retain all of this information because every puncture has the same double-transposition shadow. The required next arrow is the integral lift of this ordered braid word to Picard–Lefschetz transport on the del Pezzo lattice.

Only after that lift may one compare the resulting action with \(T_1\), \(T_2\), or their product in the separate conductor monodromy module.

## Other chambers

If one triangle inequality fails, the physical basepoint lies in a different interval and the list of punctures passed on the route to zero changes. Therefore a universal path word independent of the kinematic chamber is unavailable.

## Disposition

In the triangle chamber, information should flow from the physical basepoint under both middle punctures, in decreasing real order, and terminate at the oriented \(E=0\) collision. The missing thing plays the role of a braid-to-integral-Picard lift: it converts that retained path information into the lattice action needed by the physical detector.

Verification:

- `research/voevodsky/checkers/check_BD_four_puncture_path_order.py`
- `research/voevodsky/results/BD_four_puncture_path_order.json`
