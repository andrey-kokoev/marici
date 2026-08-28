# The toric ordered tower closes at the central commutator

## Question

Does balanced-word interferometry reveal an unbounded hierarchy of new ordered invariants in the toric logical Pauli sector?

Let \(\mathcal P_{\mathrm{log}}\) be the logical Pauli group on the two encoded toric qubits, including scalar phases.

## Claim boundary

The quotient by scalar phase is

\[
\mathcal P_{\mathrm{log}}/Z(\mathcal P_{\mathrm{log}})
\simeq
V\simeq\mathbf F_2^4.
\]

For Weyl representatives \(W_v\),

\[
[W_v,W_w]
=
W_vW_wW_v^{-1}W_w^{-1}
=
(-1)^{\omega(v,w)}I.
\]

Every commutator is central. Hence the lower central series satisfies

\[
\Gamma_1=\mathcal P_{\mathrm{log}},
\qquad
\Gamma_2=[\mathcal P_{\mathrm{log}},\mathcal P_{\mathrm{log}}]
=\{\pm I\},
\qquad
\Gamma_3=[\mathcal P_{\mathrm{log}},\Gamma_2]=\{I\}.
\]

The logical Pauli group is nilpotent of class two. In particular,

\[
[[W_u,W_v],W_w]=I
\]

for every triple.

Choose a section with multiplication cocycle

\[
W_vW_w=c(v,w)W_{v+w}.
\]

Associativity is exactly the cocycle identity

\[
c(u,v)c(u+v,w)=c(v,w)c(u,v+w).
\]

For a word \(W_{v_1}\cdots W_{v_n}\), the final projective label is \(\sum_i v_i\). Reordering adjacent factors changes only the central sign

\[
(-1)^{\omega(v_i,v_j)}.
\]

Therefore the relative phase between two permutations of the same factors is determined by the sum of pairwise intersection parities over the inversions connecting the permutations. No independent triple-order invariant remains.

This gives a finite closure of the ideal toric logical data:

1. additive labels \(V\);
2. bilinear intersection form \(\omega\);
3. the associated central phase.

Higher balanced-word experiments can retest these data or expose implementation faults, but they cannot reveal another invariant of the ideal logical Pauli group.

This closure is specific to the abelian toric-code anyon sector and its Pauli representation. It does not transfer to nonabelian braid representations, nonassociative effective models, leakage dynamics, or higher-order physical process constraints.

## Disposition

The ordered coefficient tower self-closes at nilpotency class two. The scalar lens supplies the abelianized labels; the quantum lens restores one central commutator layer; associativity and centrality eliminate a further nested layer.

The first falsifier is one of:

1. a logical commutator is noncentral;
2. a nested commutator acts nontrivially on the code space;
3. the multiplication cocycle violates associativity;
4. two word permutations with the same factors differ by more than the predicted pairwise intersection phase;
5. leakage or non-Pauli dynamics is included while the Pauli closure theorem is claimed;
6. the class-two result is generalized to nonabelian anyons without a separate braid-algebra audit.

The finite completeness test for this sector is therefore not an unbounded word search. It is verification that the logical label group is \(V\), the intersection form is nondegenerate, the Weyl cocycle has the stated commutator, and the represented multiplication is associative.
