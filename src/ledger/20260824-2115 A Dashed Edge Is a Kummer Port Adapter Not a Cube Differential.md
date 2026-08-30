# 2115 — A Dashed Edge Is a Kummer Port Adapter, Not a Cube Differential

## Hard-to-vary claim

The source-defined dashed-edge operation has a canonical coefficient-level typing as an affine endpoint-energy pullback followed by the rank-one Kummer twist `y_e^{-1}`.

It is a port adapter from an edge-deleted sector into the common correlator base. It is not a differential from one deletion grade to the next.

## Construction

For an edge `e=(s,t)`, define

\[
(T_e f)(x_s,x_t,y_e)
=
\frac1{y_e}
f(x_s+y_e,x_t+y_e).
\]

The source formula in arXiv:2401.05207, equations (2.27)--(2.30), fixes both parts of this operation: endpoint translation and inverse two-point factor.

Its exact Weyl-algebra identities are

\[
\partial_{x_s}T_e=T_e\partial_{u_s},
\qquad
\partial_{x_t}T_e=T_e\partial_{u_t},
\]

and

\[
\boxed{
\left(\partial_{y_e}+\frac1{y_e}\right)T_e
=T_e(\partial_{u_s}+\partial_{u_t}).
}
\]

Thus the `y_e` connection is not the naive pullback connection: it includes the Kummer residue `+1` forced by `1/y_e`.

## Typing consequence

Each deleted sector can be transported into the common base by a source-defined functor

\[
\text{affine pullback}
\quad+\quad
\mathcal K_{y_e^{-1}}.
\]

But this does not provide a boundary operator

\[
\mathcal M_S\to\mathcal M_{S\cup\{e\}}.
\]

The correlator therefore has a canonical family of source-indexed ports into one readout, while a deletion-cube totalization still requires independently derived coherence maps.

## Test

The dependency-free exact-integer checker

`research/benincasa/checkers/dashed_edge_kummer_adapter.rs`

verifies the cleared intertwining identity on a nontrivial polynomial and three signed rational-integer loci. The identity itself follows symbolically from the chain rule.

## Consequence for the common architecture

This is a concrete cosmological instance of

\[
\boxed{
\text{shared labelled Carrier}
+
\text{sector-specific port adapters}
+
\text{physical sum/readout}.
}
\]

The missing object after Entry 2113 is now narrower: not the individual port maps, which exist, but coherence or extension data among their images.

## Next falsifier

For two deleted edges, compare the two orders of applying the Kummer port adapters. Test whether they commute strictly on disjoint labels and whether adjacent edges acquire any source-derived correction at their shared endpoint.

A nonzero commutator would supply the first candidate coherence cell. Strict commutation would show that even the multi-edge adapter remains a tensor product of independent ports and creates no extension class.

