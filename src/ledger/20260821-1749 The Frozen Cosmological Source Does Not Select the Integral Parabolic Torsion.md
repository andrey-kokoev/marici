# 1749 — The Frozen Cosmological Source Does Not Select the Integral Parabolic Torsion

## Provenance question

Entry 1748 found

\[
H^1(S^1,\mathbb Z_-)=\mathbb Z/2.
\]

The physical question is not whether the source contains *some* integral
cycles. It is whether it canonically maps an integral source lattice into the
repeated-weight parabolic reference object whose extension carries this
torsion.

## Frozen-source audit

The primary one-loop construction supplies twisted relative cycles

\[
\Gamma_X\in
H_\bullet(\text{integration fiber}_X,\partial;\mathbb Z_{\rm twist})
\]

and fiberwise Gauss--Manin transport. Thus an integral Betti lattice exists
on the integration-fiber side.

Two required comparisons remain absent:

1. Entry 150 explicitly leaves integral normalization of the rank-nine
   coefficient/Gysin system open.
2. Entry 781 proves that the primary Morse system is fiberwise and does not
   define a parameter-space current, exceptional boundary, or scalar
   normalization.

Entry 791 constructs a source-oriented Cayley--Menger cycle for its local
finite-puncture monodromy test, but does not map that rank-one cycle into the
abstract two-step reference flag of Entries 1745--1748.

Consequently no frozen-source arrow

\[
H_\bullet(\text{fiber},\partial;\mathbb Z_{\rm twist})
\longrightarrow
\mathcal F_{\rm ref,\mathbb Z}
\]

has been derived.

## Narrow result

\[
\boxed{
\text{The integral parabolic }\mathbb Z/2\text{ class is mathematically
canonical but physically unselected by the frozen cosmological source.}
}
\]

This is a missing comparison/normalization in the coefficient layer. It is
not evidence for a new carrier stratum, and it must not be repaired by simply
declaring the fiber thimble lattice to be the reference lattice.

## Evidence

- arXiv:2408.16386, fiberwise twisted-period/Morse construction;
- Entry 150, explicit statement that integral lattice normalization remains
  open;
- Entry 781, fiberwise-versus-parameter-space thimble type gate;
- Entry 791, narrowly normalized Cayley--Menger cycle monodromy.
- `research/benincasa/results/integral-reference-provenance-gate.json`

## Next falsifier

Return to a source-defined coefficient object where both Betti and de Rham
integral structures already exist. Test whether a repeated-weight flag arises
inside its actual nearby-cycle lattice; do not introduce an abstract
reference frame first.
