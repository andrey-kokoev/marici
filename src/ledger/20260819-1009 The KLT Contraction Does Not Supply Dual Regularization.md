# 1009 — The KLT Contraction Does Not Supply Dual Regularization

## Question

Entry 1007 left the minus-recombination primitive cellularly exact but Betti
exactness untyped.  Entry 908 appeared to contain the missing ingredient under
the name “source intersection matrix.”  Does its exact six-point contraction
provide the required dual regularization map?

## Variance audit

The frozen matrices in Entry 908 have types

\[
M_{\rm block}:B_{\rm sparse}\times L,
\qquad
\mathcal S^T:L\times D_{\rm dense},
\]

and therefore

\[
T=M_{\rm block}\mathcal S^T:
B_{\rm sparse}\times D_{\rm dense}.
\]

Here all three labelled spaces are twisted-cycle bases.  Thus (T) is a
cycle-basis comparison.  The local Pochhammer relation from Entry 949,

\[
\partial\gamma=(M-1)e,
\]

also has chain variance.

The primitive from Entry 1002 instead lies in the chamber cochain complex.
Testing its Betti exactness requires a map of the form

\[
\operatorname{Reg}^{\vee}:
C^0_{\rm chamber}
\longrightarrow
H^{\vee}_{\rm Betti,reg}
\]

or an equivalent source-normalized chain/cochain pairing from which this
adjoint is derived.

No such pairing is serialized in the frozen six-point packets.  In particular,

\[
\boxed{
T^T\text{ is not }\operatorname{Reg}^{\vee}
\text{ without an independently fixed pairing.}
}
\]

A bare transpose would silently identify cycle bases with their duals and
would choose the missing normalization and orientation data.

## Narrow result

\[
\boxed{
\text{The KLT contraction certifies cycle-to-cycle comparison, not dual
regularization of the chamber cochain primitive.}
}
\]

Therefore Entry 1007 remains the correct frontier:

- cellular exactness is established;
- Betti exactness is neither proved nor falsified;
- the missing datum is the source-normalized twisted cycle/cochain pairing,
  including the dual local-system convention and residue orientations.

This is consistent with the primary KLT topology: the momentum kernel and the
twisted-cycle intersection matrix are inverse comparison objects, while open
string periods additionally pair twisted cycles with twisted cocycles.  Those
pairings must not be conflated.

## Next falsifier

Construct the six-point twisted period pairing in the exact occurrence-labelled
bases used by Entries 908 and 974.  Derive its adjoint regularization map and
apply it to the primitive from Entry 1002.  Betti exactness is established only
if the resulting dual class is a source-normalized boundary; a nonzero class
would establish a genuine lattice obstruction.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_dual_regularization_type_gate.rs`;
- packet:
  `research/benincasa/string-six-point-dual-regularization-type-gate.json`;
- primary references:
  Mizera, *Combinatorics and Topology of Kawai–Lewellen–Tye Relations*,
  arXiv:1706.08527; Mizera, *Inverse of the String Theory KLT Kernel*,
  arXiv:1610.04230;
- allocator claim:
  `seqclaim-d0106a9eb0997a14643d3b4c`.
- epistemic event:
  `ev-000000000628-056ccf46-885b-41c9-871f-6d0428597b7f`.
