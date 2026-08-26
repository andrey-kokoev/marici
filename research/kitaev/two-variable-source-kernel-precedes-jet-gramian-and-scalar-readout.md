# Two-variable source kernel precedes jet Gramian and scalar readout

## Bounded question

What is the minimal operator object that simultaneously generates analytic jet
Gramians, diagonal observation energy, and a comparison between direct and
reciprocal feature carriers without being reverse-engineered from a desired
scalar function?

## Source-first kernel

Let \(X\) be the labelled state carrier, \(E\) a feature carrier, and

\[
J(w):X\longrightarrow E
\]

an operator-valued analytic germ constructed from source atoms and incidence
maps. Define the sesquianalytic operator kernel

\[
K(z,w)=J(z)^*J(w)\in\operatorname{End}(X).
\]

For finite points \(w_i\) and states \(x_i\),

\[
\sum_{i,j}\langle x_i,K(w_i,w_j)x_j\rangle
=\left\|\sum_jJ(w_j)x_j\right\|^2\ge0.
\]

Thus positivity is derived from the source feature map. It is not imposed on a
scalar section after the fact.

## Mixed coefficient extraction

Write

\[
J(w)=\sum_{n\ge0}J_nw^n.
\]

Then

\[
K(z,w)=\sum_{m,n\ge0}G_{mn}\overline z^{,m}w^n,
\qquad
G_{mn}=J_m^*J_n.
\]

Mixed coefficient extraction from the two-variable kernel therefore recovers
every jet Gram block. Every finite block matrix

\[
(G_{mn})_{0\le m,n\le r}
\]

is positive semidefinite. The diagonal

\[
K(w,w)=J(w)^*J(w)
\]

is the pointwise feature Gramian, but the full kernel additionally retains
cross-point and cross-jet coherence.

The analytic-germ topology of milestone 2646 is sufficient when the operator
series converges on one common radius and coefficient extraction is continuous
in operator norm or a declared weaker topology.

## Direct and reciprocal factorizations

Suppose source constructions give

\[
K(z,w)=J_+(z)^*J_+(w)=J_-(z)^*J_-(w)
\]

through distinct carriers \(E_+,E_-\). If each factorization is minimal—the
closed span of all \(J_\pm(w)X\) is its whole carrier—then there is a unique
unitary

\[
U_K:E_+\longrightarrow E_-
\]

satisfying

\[
U_KJ_+(w)=J_-(w).
\]

The isometry is first defined on finite source-generated sums; equality of
kernels makes it well-defined and norm-preserving, and minimality extends it
onto the full carriers.

This is mathematical unitary equivalence of labelled minimal factorizations.
It does not identify their source objects or authorize physical Fourier–Tate
sewing. That further claim requires the unitary to agree with the independently
derived source transport.

## Dark-summand hostile

Without minimality, the same kernel admits

\[
J_-(w)=\binom{J_+(w)}{0}
\]

on a larger carrier. The extra summand is invisible to \(K\). Kernel equality
therefore determines only the source-generated feature subspace, not arbitrary
ambient carrier structure.

## Scalar diagonal compression is insufficient

A selected state or scalar functional sees only

\[
k_x(z,w)=\langle x,K(z,w)x\rangle.
\]

Two distinct operator kernels can have the same selected scalar diagonal and
different action on the orthogonal state direction. Scalar agreement cannot
establish operator-kernel equality, jet-block closure, or reciprocal sewing.

For a genuinely sesquianalytic scalar kernel, the complete diagonal on an open
set may determine the scalar polarization. That does not repair compression:
the missing operator and source labels have already been discarded.

## Noncircularity gate

Given any scalar analytic function \(\Xi(w)\), one may define

\[
K_\Xi(z,w)=\overline{\Xi(z)}\Xi(w).
\]

This kernel is automatically positive semidefinite, whatever the zero set of
\(\Xi\). Choosing \(\Xi\) with an off-target zero changes nothing about that
positivity. Therefore a rank-one \(\Xi\)-polarized kernel cannot explain or
constrain the zeros it was built from.

An RH-bearing kernel is admissible only if the same \(K\) is constructed before
scalar readout from independently specified source atoms, carrier maps,
boundary currents, and cutoff-natural incidence. The scalar completed section
may then be derived as a compression or determinant. It may not be used as the
feature map that retroactively certifies itself.

## Required typing packet

A candidate two-variable theta kernel must declare:

1. state carrier \(X\) and feature carriers \(E_+,E_-\);
2. source atoms and analytic maps \(J_\pm(w)\);
3. common germ radius and coefficient topology;
4. all mixed blocks \(J_{\pm,m}^*J_{\pm,n}\);
5. minimal generated subspaces and any dark complements;
6. the mathematical comparison \(U_K\) and the independent Fourier–Tate map;
7. the scalar readout as a downstream compression;
8. uniform cutoff bounds needed for completion.

## Exact audit and falsifiers

The checker verifies an operator polynomial kernel, all mixed jet blocks, finite
kernel positivity, equality under a unitary reciprocal factorization, failure
of ambient uniqueness with a dark summand, scalar-compression blindness, and a
positive rank-one polarization with an explicit off-target zero.

The construction is rejected if source atoms are absent, the kernel appears
only after scalar completion, mixed coefficient blocks disagree, a claimed
unitary includes dark summands without minimality, or cutoff convergence holds
only after scalar compression.

## Claim boundary

This is a finite/operator-analytic compiler theorem. It does not construct the
theta source kernel, prove its completion bounds, identify Fourier–Tate sewing,
derive a signed arithmetic current, orient zeros, or prove RH.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The alternatives were source-first kernel organization and sufficiency
of scalar polarization. Mixed blocks, positivity, minimal unitary, dark summand,
compression, and an off-target \(\Xi\) hostile were frozen measurements.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Scalar polarization was eliminated as explanatory evidence; the source
kernel generated every jet Gram block; minimal reciprocal factorizations gained
a unique mathematical unitary; and source identity remained explicitly
stronger than factorization equivalence. Theta kernel authority is unresolved.
