# Retained prime diagonality survives on the labelled graph core; cross-prime terms can only factor through global boundary rows

## Question

Does completion create unrestricted cross-prime blocks in the retained Green
packet?

## Labelled graph core

At finite cutoff the valuation/Fock incidence is a direct sum over `(p,k)`, so
its mixed Green operator is exactly prime diagonal. The retained graph
completion is formed with valuation-labelled direct sums of the bilateral
histories, endpoint columns, and Green coordinates. On the labelled bulk core,
the prime projections are bounded coordinate projections and commute with the
closed graph operators.

Consequently the completed bulk form remains decomposable:

\[
G_{\rm bulk}=\bigoplus_p G_p,
\]

and

\[
\widehat Q_qG_{\rm bulk}\widehat P_p=0
\qquad(p\ne q).
\]

This uses retention of the prime label in the graph norm. It would fail for a
completion that first aggregated all translated shells into one absolute
radial coordinate.

## Boundary qualification

Global endpoint, seam, or archimedean observation may aggregate local
coordinates into a common finite-dimensional row. Squaring such an aggregate
can create a finite-rank cross-prime Gram block. This is not bulk mixing; it
factors through the declared boundary map

\[
B_\partial:
\bigoplus_p D_{{\rm ret},p}
\longrightarrow E_\partial.
\]

Thus the general retained form has the constrained shape

\[
G_{\rm ret}
=
\bigoplus_pG_p
+B_\partial^*H_\partial B_\partial.
\]

The independent Tate current has the same distinction: its local logarithmic
terms are place diagonal, while `E_end` is a separately declared finite-rank
endpoint row.

## Interface residual

Packet sewing does not require every cross-prime matrix entry to vanish. It
requires:

1. no off-diagonal block in the labelled bulk;
2. every surviving cross-prime term to factor through the common boundary
   packet;
3. equality of that finite-rank factorization with the Tate endpoint row.

A cross-prime term orthogonal to the range of `B_partial^*` is an immediate
falsifier.

## Disposition

The unrestricted cross-prime bulk residual is closed on the retained labelled
core. The remaining finite-rank boundary comparison is already typed by the
weighted Hadamard endpoint sewing; its metric equality belongs to the final
Hermitian packet comparison.