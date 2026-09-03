# Source-derived symmetry of instrument attachments

## Question

When does an automorphism of the original system induce a lawful symmetry of its instrument attachment, coherence object, and readout?

## Claim boundary

This packet derives attachment symmetry from typed source automorphisms and equivariant attachment data. It does not promote every permutation preserving a finite constraint table to a source symmetry.

## Source automorphism and attachment lift

Fix \(S\in\mathcal S\), an attachment \(D\in\operatorname{Att}(S)\), and an automorphism

\[
g:S\to S.
\]

Reindexing gives \(g^*D\in\operatorname{Att}(S)\). The source automorphism acts on the attached object only when supplied with an attachment lift

\[
\phi_g:D\xrightarrow{\sim}g^*D.
\]

For a group \(G\leq\operatorname{Aut}_{\mathcal S}(S)\), these lifts must satisfy identity and multiplication coherence, with the reindexing coherence inserted when \(\operatorname{Att}\) is pseudofunctorial. Without this equivariant structure, \(g\) transports \(D\) to another attachment but does not define an automorphism of \((S,D)\).

## Derived chain

A valid lift must induce the chain

\[
(S,D,g,\phi_g)
\longrightarrow
\sigma_g:I_D\to I_D
\longrightarrow
q_g:B_D\to B_D
\longrightarrow
\eta_g:F_D\xrightarrow{\sim}q_g^*F_D
\longrightarrow
\widehat g:M_D\xrightarrow{\sim}M_D.
\]

Here:

- \(\sigma_g\) preserves occurrence identities and typed placement loci;
- \(q_g\) preserves the full decorated incidence category;
- \(\eta_g\) transports every constraint naturally;
- \(\widehat g\) is induced by the universal property of the matching limit.

The induced matching maps inherit the group law only when the lifts and natural transformations satisfy their coherence equations.

## Readout equivariance

For readout \(r_D:M_D\to Y_D\), a symmetry of the readout additionally requires a record action \(\rho_g:Y_D\to Y_D\) and a commuting square

\[
r_D\widehat g=\rho_g r_D.
\]

Invariance is the special case \(\rho_g=\operatorname{id}\). A matching-object symmetry may fail to preserve readout, and readout invariance may hide a nontrivial action because the record map is nonmonic.

## Rejection gate

A permutation of occurrences is source-authorized only if it lies in the image of the lift map

\[
\operatorname{Aut}(S,D)\to\operatorname{Aut}(I_D,B_D,F_D).
\]

Preserving an incidence matrix, matching set, or readout table is necessary at the corresponding layer but does not construct the missing preimage.

## Finite diagnostic

For two equally labelled loci joined by an undirected interface, source automorphisms are the identity and swap. The swap induces occurrence and boundary permutations, preserves equality constraints, squares to the identity, and acts bijectively on the matching object.

Change one source label while retaining the same abstract equality constraint. The constraint table still admits the swap, but the labelled source net admits only the identity. The algebraic swap is therefore rejected as source-unauthorized despite preserving the matching set.

## Relation to established transport results

This construction uses the existing decorated-boundary transport and induced matching-object isomorphism results as the final arrows of the chain. It adds the missing source and attachment-lift hypotheses rather than duplicating those finite transport criteria.

## Disposition

Attachment symmetry consists of a source automorphism, a coherent lift to the attachment, induced occurrence and boundary actions, natural constraint transport, and any required readout action. Algebraic symmetry at a downstream presentation is not sufficient without a preimage through this chain.
