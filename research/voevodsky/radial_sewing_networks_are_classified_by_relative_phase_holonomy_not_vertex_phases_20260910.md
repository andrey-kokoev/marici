# Radial sewing networks are classified by relative-phase holonomy, not vertex phases

## Question

How does the two-wall relative phase extend to a network of radial sewings with independently chosen channel frames?

## Claim boundary

Once connecting transports are declared, the phase data form a \(U(1)\)-valued graph connection. Vertex rephasings are gauge transformations; products around cycles are invariant. For a connected graph, gauge classes are classified by \(\operatorname{Hom}(H_1(\Gamma;\mathbb Z),U(1))\). A tree has no intrinsic phase invariant. This classifies only the phase layer, not the full Green operator network or observer stability.

## Problem

An isolated radial wall phase is removable by a channel gauge. Two walls in one frame produce the relative transport

\[
H_{v,u}=\operatorname{diag}(u/v,v/u).
\]

For several walls, absolute phase assignments depend on local frames. The invariant content should be stated without choosing a global trivialization.

## Bold conjecture

A network with \(n\) wall phases contains \(n\) independent phase observables.

## Named rivals

1. Vertex phases are gauge and only cycle holonomies survive.
2. Every relative edge phase is invariant.
3. A tree still carries endpoint-relative phases without an external frame.
4. Real conjugation identifies a holonomy with its inverse only after passing to a Real scalar readout.

## Typed sewing graph

Let \(\Gamma=(V,E)\) be a connected finite graph. Each vertex \(i\) carries a radial double \(X_i\) with a chosen local second-channel frame. Each oriented edge \(e:i\to j\) carries a unitary relative-phase transport

\[
z_e\in U(1),
\qquad
z_{\bar e}=z_e^{-1}.
\]

On the doubled carrier, the corresponding orientation-preserving comparison is

\[
H_e=\operatorname{diag}(z_e^{-1},z_e).
\]

This is a Green isometry.

## Gauge action

A vertex rephasing is a family

\[
g=(g_i)_{i\in V}\in U(1)^V.
\]

It acts on edge phases by

\[
z_e\longmapsto z'_e=g_jz_eg_i^{-1}
\qquad(e:i\to j).
\]

This is the usual coboundary action. Individual edge phases are not invariant when endpoint frames may vary independently, rejecting rival 2.

## Cycle holonomy

For an oriented cycle

\[
\gamma=e_1e_2\cdots e_m,
\]

define

\[
\operatorname{Hol}(\gamma)
=
\prod_{r=1}^m z_{e_r}.
\]

Under vertex gauge, all intermediate factors cancel, so

\[
\operatorname{Hol}'(\gamma)=\operatorname{Hol}(\gamma).
\]

Reversing orientation gives

\[
\operatorname{Hol}(\bar\gamma)
=
\operatorname{Hol}(\gamma)^{-1}.
\]

## Classification theorem

Gauge-equivalence classes of \(U(1)\)-valued edge phases are naturally

\[
H^1(\Gamma;U(1))
\cong
\operatorname{Hom}(H_1(\Gamma;\mathbb Z),U(1)).
\]

### Proof

Choose a spanning tree \(T\subset\Gamma\) and a root. Successively choose vertex gauges to set every tree-edge phase to \(1\). Each non-tree edge then closes a fundamental cycle, and its remaining phase is exactly that cycle's holonomy. No residual based gauge changes these phases. Different spanning trees change the cycle basis but not the induced homomorphism on \(H_1\).

Thus the number of independent \(U(1)\) parameters is the first Betti number

\[
b_1(\Gamma)=|E|-|V|+1,
\]

not \(|V|\). The bold conjecture fails.

## Tree corollary

If \(\Gamma\) is a tree, then

\[
H_1(\Gamma;\mathbb Z)=0.
\]

Every edge phase can be gauged to \(1\). No intrinsic relative phase remains without an external endpoint frame or additional coupling. Rival 3 fails.

## Two-wall recovery

The two-sewing loop is the first graph with one independent cycle. Its holonomy is

\[
z=v/u
\]

in a common frame, and the radial carrier transport is

\[
\operatorname{diag}(z^{-1},z).
\]

This recovers the previous two-wall invariant.

## Real structure

Fiberwise twisted Real maps transport consistently along the edges. Complex conjugation sends

\[
z_e\longmapsto\bar z_e=z_e^{-1}
\]

and therefore

\[
\operatorname{Hol}(\gamma)
\longmapsto
\operatorname{Hol}(\gamma)^{-1}.
\]

An oriented complex phase observer distinguishes these values. A Real scalar observer such as the trace retains only

\[
2\operatorname{Re}\operatorname{Hol}(\gamma).
\]

Therefore Real compatibility does not identify a holonomy with its inverse as a typed oriented transport; identification occurs only under a readout that forgets orientation. Rival 4 survives.

## Green structure

Each edge matrix satisfies

\[
H_e^*J_\partial H_e=J_\partial.
\]

Cycle transport is therefore a Green isometry. Wall swaps remain Green anti-isometries; an even composition produces the orientation-preserving edge transport used here. Networks with unmatched odd swap parity require a separately typed orientation-reversing endpoint, not an ordinary cycle holonomy.

## Observer layer

A cycle-holonomy observer needs coherent comparison around a loop. It cannot be assembled from independent intensity readouts at vertices. Its role signature includes:

- graph and cycle;
- oriented connecting transports;
- common Green/Real compatibility;
- coherent phase readout;
- gauge-invariance proof.

The target is finite-dimensional for a finite graph. Hence cycle-phase observation may repair finite relational ambiguities but cannot supply an essential lower margin on an infinite-dimensional source.

## Symmetry-descent interpretation

Passing from vertex phases and edge trivializations to cycle holonomies is a genuine gauge quotient: the vertex-gauge group acts on connections, and the quotient is \(H^1(\Gamma;U(1))\). This is distinct from the earlier subgroup restriction

\[
C_4\rightsquigarrow\langle F^2\rangle.
\]

The worked example now contains both operations with separate types:

- subgroup restriction for Fourier-to-reciprocal sewing;
- gauge quotient for phase-network classification.

## Constructor-role consequence

The roles are:

- `vertex_trivialization`: local frame choice;
- `edge_comparison`: relative channel transport;
- `gauge_transformation`: change of vertex trivialization;
- `cycle_holonomy`: gauge-invariant composite;
- `relative_phase_observer`: readout of a chosen holonomy;
- `essential_observer`: independent completed-source stability role.

Only `cycle_holonomy` descends to the gauge quotient. Copying a vertex phase into that slot is rejected because it is not gauge invariant.

## Strongest falsification attempt

Endpoint-relative phases on a tree appear meaningful in a fixed laboratory frame. They are meaningful relative to that external frame, but the frame is an additional vertex object not transformed by the internal gauge group. Without it, spanning-tree gauge fixing removes every phase. This locates rather than suppresses the missing datum.

## Disposition

Radial sewing phases on a network are classified by cycle holonomy. Absolute wall phases and tree-edge phases are trivialization data; loops carry the intrinsic relative classes. This supplies the programme's first genuine quotient descent and separates it sharply from Fourier subgroup restriction and from complementary-observer stability.
