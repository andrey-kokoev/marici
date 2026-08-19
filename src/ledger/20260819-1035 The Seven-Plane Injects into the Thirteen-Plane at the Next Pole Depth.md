# The Seven-Plane Injects into the Thirteen-Plane at the Next Pole Depth

## Transition rather than dimension comparison

Entry 1026 proves

\[
\dim E_2(C^{k\le2})=7,
\qquad
\dim E_2(C^{k\le3})=13,
\]

but leaves open whether the original seven directions survive, die, or are
replaced.  The presentations are genuinely nested: the depth-two ambient
columns and labelled relations embed into their depth-three counterparts.

The complete depth-two exact-valuation quotient basis was therefore exported
without using its family labels.  Each representative was embedded blockwise
into the three normal grades of the depth-three presentation, reduced first
by the depth-three valuation-zero/one subspace, and then expressed in the
depth-three exact-valuation-two quotient.

## Exact transition result

Over \(\mathbf F_{32003}\), the induced map has

\[
\boxed{
\operatorname{rank}
\left(
E_2(C^{k\le2})\longrightarrow E_2(C^{k\le3})
\right)=7.
}
\]

More precisely,

\[
\dim\ker=0,
\qquad
\dim\operatorname{coker}=6.
\]

All seven embedded representatives reduce with zero remainder against the
complete depth-three relation space.  Hence the calculation is a map of the
exact-valuation quotients, not a comparison of elimination witnesses.

Thus

\[
\boxed{
0\longrightarrow E_2^{(2)}
\longrightarrow E_2^{(3)}
\longrightarrow \mathbf F_{32003}^{,6}
\longrightarrow0.
}
\]

## Meaning

The original seven-plane is not killed or rotated away by the first
connection-stable pole-depth extension.  It survives as a canonical
subobject of the thirteen-plane.  The failure of stabilization in Entry 1026
comes entirely from six new exact-valuation directions.

This strengthens one part of the earlier picture while weakening another:

- the depth-two seven-plane is a persistent source-derived sector;
- it is not the whole direct-limit coefficient object;
- identifying it with the generic rank-seven algebraic kernel would require
  a canonical quotient, support condition, or grading that removes the six
  higher-pole directions.

No such removal is presently derived.  Saturation or fitted projection may
not be imposed post hoc.

## Next gate

The highest-information next calculation is not depth four immediately.  It
is to type the six-dimensional cokernel:

1. determine its family and pole-grade filtration intrinsically;
2. test occurrence transport on the short exact sequence;
3. check whether the six new directions are connection descendants of the
   old seven or an independent supported coefficient block;
4. only then decide whether another pole-depth extension is needed.

## Durable verification

- transition-capable rank engine:
  `research/benincasa/marici-gm/src/bin/triangle_wall_dual_rank.rs`;
- rank and transition packet:
  `research/nima/triangle-wall-kdepth3-rank.json`;
- allocator claim: `seqclaim-7e8d06744d42c8ecb8f7b862`.
