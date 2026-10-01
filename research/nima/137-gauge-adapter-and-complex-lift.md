# Gauge adapter boundary and a complex comparison lift

## Real comparison model

Each labelled comparison is a real reflection H_i=I-2d_i d_i^T on the
153-dimensional joint carrier-record space. The137 normals are independent;
their orthogonal complement is the16-dimensional common fixed space.

Consider a linear norm-preserving continuous internal symmetry that leaves
every labelled operation unchanged. Its skew generator J must commute with
every H_i. Commutation preserves the one-dimensional -1 eigenspace span(d_i).
Thus J d_i is proportional to d_i, and real skewness forces J d_i=0. It follows
that J vanishes on the entire active comparison space. Continuous rotations
may still act within the common fixed space, where they do not act on the
mismatch observable.

This obstructs a nontrivial global phase action on active real comparisons
under the stated fixed-operation condition. It does not exclude nonlinear
adapters, symmetries that transform the operators, or local gauge fields.
It also does not prove any general physical no-go.

## Complex lift

Promote the real joint vector to z in C^153, equivalently two real copies.
Use the same real matrices H_i on both components. Global phase z->exp(i chi)z
then commutes with every comparison and preserves norm. With the canonical
complex symplectic structure, the norm generates a global phase action up to
sign convention.

Each comparison now has an explicit Hamiltonian interpolation:

    P_i=d_i d_i^T,
    h_i(z)=(pi/tau) z^dagger P_i z,
    i dot(z)=(pi/tau) P_i z,
    exp(-i*pi*P_i)=I-2P_i=H_i.

The pulse coefficient and Hamiltonian here are in action-normalized model
units; physical energy requires the action scale. Duration tau remains free.
This introduces complex/canonical structure as an explicit extension rather
than finding it inside the original odd-dimensional real model. It constructs
a global conserved phase quantity, not local electromagnetic charge assignment.

## Product-state adapter test

The carrier comparison block is a4-by4 tensor feature. A simple adapter would
represent it by a product of two four-state amplitude vectors. Such matrices
have rank1. The allowed arrow feature v=(e2-e0) tensor (e2-e0), with the fixed
metric K=G4 tensor G4, projects

    x=e0 tensor e0
    to y=x-v*(v^T K x)/(v^T K v).

The matrix of y has rank2. Thus product tensors are not closed under even one
comparison. The full comparison state cannot be represented by that simple
two-vector adapter. Using a general tensor state or additional retained degrees
of freedom is a different candidate requiring its own dynamical correspondence.

## Current conclusion

The attempted direct identification with the earlier four-site matter/link
Hamiltonian is incomplete. We now know two necessary design decisions: how
complex phase structure enters, and which state representation is closed under
comparison updates. The complex lift provides a working option for the first;
the product-state trial fails the second.

The next useful adapter should retain the full tensor state, define local
endpoint phase actions on it and its records, and test covariance of each
comparison while allowing link/operation data to transform. A common global
phase alone does not fix field stiffness, charge coupling, or alpha.

## Verification

    uv run research/nima/checkers/check_137_gauge_adapter_boundary.py

NumPy checks normal independence, all137 complex norm/phase symmetries and pulse
endpoints, the rank-changing product-state counterexample, and free pulse duration.
The real skew-generator obstruction is the linear argument above; the checker
does not solve a separate symbolic commutant system. No physical values enter.
