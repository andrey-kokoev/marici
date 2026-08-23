# Split self-modeling objects: exact criterion and first saturated witness

## Correction of interpretation

The prior smallest witness has no strict retraction
\(\mathsf U(X)\to X\). That disproves a universal split, but it does not prove
that every act of self-modeling leaves an ineradicable residue. Part of the
failure is structural but elementary: the base object contains no targets of
the new meta-level types and roles.

## Reflection-witness criterion

For each node \(x\in X\), call a pair \((M_x,R_x)\) a reflection witness when

- \(M_x\) is a meta-level object;
- \(R_x\) is a meta-level record;
- \(M_x\xrightarrow{\rm models}x\) is an edge of \(X\);
- \(R_x\xrightarrow{\rm classifies}M_x\) is an edge of \(X\).

For the finite operator used here, a strict map

\[
a_X:\mathsf U(X)\longrightarrow X,
\qquad a_X\eta_X=1_X,
\]

exists if and only if every node of \(X\) has at least one reflection witness.
Indeed, necessity follows by applying \(a_X\) to the two new edges over each
node. Conversely, chosen witnesses define

\[
a_X(m_x)=M_x,\qquad a_X(r_x)=R_x,
\]

while fixing \(X\), and all typed edges are preserved.

## Saturated witness

The checker constructs a finite object containing a meta-model node \(M\), a
meta-record node \(R\), the edge \(R\to M\), and `models` edges from \(M\) to
every node, including \(M\) and \(R\). The same pair \((M,R)\) witnesses every
node. Its self-modeling extension therefore retracts strictly.

Thus

\[
\boxed{
X\text{ splits under self-modeling}
\iff
X\text{ is internally reflection-witness complete}
}
\]

for this finite construction.

## Revised metaphysical reading

Self-modeling is irreversible for an object that lacks the internal capacity
to represent the newly created representation relations. It need not remain
irreversible in a sufficiently reflection-complete object.

This is closer to the operator's original conjecture:

\[
X_\infty\simeq\mathsf U(X_\infty).
\]

The finite saturated witness is not such an isomorphism and does not prove a
limit exists. But it shows that splitting can emerge from internal recursive
closure rather than from weakening the morphisms or erasing types.

## New frontier

The sharp question is no longer whether all self-modeling extensions split.
They do not. It is whether iterating a source-derived completion process can
produce reflection-witness completeness coherently, and whether its limit is
universal rather than an ad hoc saturated graph.

