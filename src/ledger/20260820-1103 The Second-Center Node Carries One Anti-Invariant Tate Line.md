# 1103 — The Second-Center Node Carries One Anti-Invariant Tate Line

## Record

Entry 1102 closed the normalization/conductor complex, including both support
faces.  The remaining intrinsic coefficient object of the local family

\[
XY=ps(B-1)
\]

is its nodal vanishing cycle.

Sequence claim: `seqclaim-2ba430d677c78ad0da2b5a35`.

## Labelled smoothing map

The family is the pullback of the universal node \(XY=t\) by

\[
t=p\,s\,(B-1).
\]

The three occurrence-labelled boundary loops therefore map to the universal
smoothing loop with exponent vector

\[
\boxed{(1,1,1)}.
\]

The vanishing cycle of the node is

\[
H_1(\mathbb C^*)\simeq\mathbb Z.
\]

The Picard--Lefschetz twist fixes this vanishing-cycle generator.  Hence

\[
\boxed{
M_p=M_s=M_{B-1}=1,
\qquad
N=0.
}

## Deck character

In normalized coordinates the original square-root deck transformation sends

\[
(X,Y)\longmapsto(-Y,-X).
\]

On the \(\mathbb C^*\) cycle this is inversion, so

\[
\boxed{\tau=-1.}
\]

The intrinsic nearby-cycle coefficient is therefore one rank-one
anti-invariant Tate line with trivial labelled base monodromies.

## Deutsch--Popperian verdict

The conjecture that the three smoothing factors create three independent
vanishing-cycle lines is falsified.  They are three labelled pullback
directions into one universal smoothing parameter and compile to one
coefficient line.

This supports

\[
\boxed{
\text{existing three-factor carrier}
+
\text{one sector-specific anti-invariant Tate coefficient}.
}

No source Gysin map into this line has yet been constructed.  Rank and
character matching do not authorize one.

## Evidence

- `research/benincasa/marici-gm/src/bin/rank12_u2v0_node_monodromy.rs`;
- `research/benincasa/rank12-u2-v0-joint-newton.json`.

Epistemic graph admission:
`ev-000000000802-94f80a50-2d76-4b2d-8c41-a13104d5f281`.

## Next falsifier

Derive the source-labelled residue/Gysin maps from the \(p=0\), \(s=0\), and
\(B-1=0\) complexes into the nodal Tate line.  Verify orientations, deck
characters, and the two-dimensional overlap coherences.  Only the cofiber of
that typed comparison may be interpreted as coefficient excess.
