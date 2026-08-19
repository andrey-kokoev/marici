# 1001 — The Minus Recombination Restricts to a Closed Three-Edge Arc

## Question

Entry 999 finds one chamber-incidence realization of the \((--)\) recombination support, at the adjacent occurrence pair \((1,4)\).  Test whether the \((--)\)-character projection of Entry 979's exceptional chamber cochain is the local Cousin image of that single incidence vertex.

## Frozen projection

Let \(T_{24}\) and \(T_{34}\) be the two pair-sign shifts.  Apply the unnormalized projector

\[
P_{--}=1-T_{24}-T_{34}+T_{24}T_{34}
\]

to Entry 977's exact chamber cochain \(\lambda\), then form Entry 979's twisted edge differential

\[
d_k
=
(P_{--}\lambda)_{c_{k+1}}
-U_k(P_{--}\lambda)_{c_k}
\]

on the frozen cycle

\[
(c_0,\ldots,c_5)=(0,1,4,5,3,2).
\]

No edge coefficient is fitted.

## Recombination sheets

Resolve the repeated-wall intersection by

\[
B_{24}=\frac{s}{ZA_2},
\qquad
B_{34}=\frac{tZ}{A_3},
\qquad
s^2=t^2=1.
\]

For every one of the four signed sheets, the restricted edge support is

\[
\boxed{
\operatorname{supp}(d|_{--,s,t})=\{1,2,3\}.
}
\]

The exact values are

\[
\begin{array}{c|ccc}
(s,t)&d_1&d_2&d_3\\
\hline
(-1,-1)&-16&16(1+X)&16A_3/Z\\
(-1,+1)&16&-16(1+X)&16A_3/Z\\
(+1,-1)&16&-16(1+X)&-16A_3/Z\\
(+1,+1)&-16&16(1+X)&-16A_3/Z.
\end{array}
\]

All other edge components vanish.

## Closure

Transporting the three nonzero components to the base chamber with Entry 979's Pochhammer units gives

\[
\boxed{
\sum_{j=1}^{3}
\left(\prod_{k=j+1}^{5}U_k\right)d_j
=0
}
\]

on every signed sheet.  Thus the restriction remains an exact closed edge cochain.

## Result

A local Cousin image of one ordinary hexagon vertex is supported on its two incident edges.  The source-derived \((--)\) restriction instead occupies a three-edge arc:

\[
\boxed{
P_{--}\delta_{\rm KN}\lambda\big|_{Z_{--}}
\text{ is not the local vertex Cousin image of Entry 997's modification line.}
}
\]

The mismatch is support-theoretic and survives every signed sheet.  It cannot be repaired by rescaling the modification generator or changing a residue sign.

This does not trivialize either object.  Entry 997's modification remains a globally descended rank-one normal costalk, while Entry 979's \((--)\) component remains a globally closed chamber cochain.  They are distinct coefficient structures on the same frozen carrier.

## Implication

The string sector now supplies a concrete example of partial lenses inside one sector:

- normal recombination detects a local coefficient-lattice degeneration;
- chamber transport detects a nonlocal three-edge Pochhammer relation;
- matching character and cohomological degree do not collapse them into one class.

No new carrier cell is indicated.

## Next finite test

Retain both terms in a two-step supported total complex

\[
i_{Z_{--}}^!\mathcal E[1]
\oplus
C^1_{\rm chamber}(\mathcal K_{\rm KN}).
\]

Audit the source six-point regularized intersection form for an independently normalized off-diagonal comparison between the local costalk and the three-edge arc.  If absent, the two objects remain independent; do not manufacture a map from their shared character.

## Verification artifacts

- `research/benincasa/marici-gm/src/bin/string_six_point_minus_recombination_edge_restriction.rs`
- `research/benincasa/string-six-point-minus-recombination-edge-restriction.json`

The native Symbolica checker constructs the character projector, twisted differential, all four sheet restrictions, support census, and transported closure exactly.

Epistemic graph event: `ev-000000000619-6ee2a5bc-5130-4d2b-9b42-c5efb197981b`.
