# Triple-soft resolution branch-gluing audit

## Question

Do the soft-triangle smoothing and transport artifacts provide a resolved overlap that glues the three cyclic soft-sheet anchors into a generic `sqrt(K)` branch?

## What the artifacts establish

Within the physical `X1` soft-triangle sector, the node smoothing is first nonzero at second normal order at four positive-incidence corners. A global transport construction has contractible open base

\[
-1<\kappa<1,
\qquad -1<\xi<1,
\qquad \sigma>0,
\]

and transports all four local costalks with orientation `+1` to one positive-cut cycle. Their sum is four times that cycle. The source factor is strictly positive on the open chamber and its period has one fixed nonzero imaginary phase.

This is genuine gluing: the four corner germs inside the `X1` soft-triangle resolution share a common oriented cycle and source phase.

## Why it is not cyclic branch gluing

The resolved base parameterizes the four endpoint corners of one `X1` soft chart. It does not contain the closures of the separate `X2` and `X3` soft anchors, does not define transition maps to their strict transforms, and does not approach a generic nonsoft three-chart basepoint.

Its own scope is the pure node coefficient and local-to-generic tube/Gysin map. The node-smoothing artifact explicitly states that Picard–Lefschetz signs still require oriented local comparison and square-root normalization. The graded observer likewise does not activate the generic rank-20 soft algebraic module.

Therefore the positive-cut phase supplies an internal `X1` boundary normalization, not a global analytic branch of the original Cayley–Menger square root.

## Strongest falsification attempt

Identify the contractible `(kappa,xi,sigma)` base with a resolved triple-soft overlap. This fails its declared geometry: `p>0` remains fixed, the physical locus is `X1=0, X2=X3=p`, and neither `X2=0` nor `X3=0` belongs to the open base. The construction resolves endpoint nodes, not the intersection of cyclic soft divisors.

## Surviving branch datum

The strongest source-normalized statement is:

- one `X1` soft boundary sector has a common positive-cut cycle;
- its four physical corners transport with equal orientation;
- the scalar source factor has common positive sign and fixed phase.

This datum may serve as one boundary anchor once maps to a true cyclic overlap are constructed.

## First missing object

The first missing object is a resolved space containing the strict transforms of all three divisors `X1=0`, `X2=0`, and `X3=0`, with overlap maps to the existing `X1` soft-triangle chart and an explicit pullback of `sqrt(K)`.

## Acceptance test

1. construct the cyclic divisor resolution and its three strict-transform charts;
2. embed the existing `X1` positive-cut cycle;
3. compare orientations and root signs on pairwise overlaps;
4. verify a Čech cocycle for branch transitions;
5. continue to a generic nonsoft basepoint without crossing `K=0` or conductor support.

## Disposition

The soft-triangle artifacts canonically glue four node germs inside one `X1` boundary sector. They do not resolve the triple-soft intersection or glue the cyclic `X1/X2/X3` square-root branches.

## Evidence

- `research/benincasa/soft-triangle-node-smoothing.json`
- `research/benincasa/soft-triangle-global-vanishing-transport.json`
- `research/benincasa/soft-triangle-source-port-recovery.json`
- `research/benincasa/physical-soft-triangle-graded-observer.json`
