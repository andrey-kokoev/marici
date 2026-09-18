# Tail-seam stabilized Xi pencil

Let

$$
C_a:\mathcal H\longrightarrow
\mathcal H_{\rm tail,a}\oplus\mathcal H_{\rm seam,a}
$$

be the complete cut unitary, with `C_a^{-1}=C_a^*`. On the two-history state space set

$$
\mathbf C_a=C_a\oplus C_a,
$$

and retain the scalar source/endpoint port unchanged.

Define the stabilized pencil by unitary conjugation:

$$
\widehat{\mathcal R}_{\Xi,a}(z)
=
(\mathbf C_a\oplus1)
\mathcal R_{\Xi,0}(z)
(\mathbf C_a^*\oplus1).
$$

This is not the tail-only translated pencil. Its seam blocks contain exactly the interval data removed from the tail.

## Exact invariants

Unitary equivalence gives

$$
\ker\widehat{\mathcal R}_{\Xi,a}(z)
=(\mathbf C_a\oplus1)
\ker\mathcal R_{\Xi,0}(z).
$$

Because `C_a` is independent of `z`, parameter differentiation commutes with the conjugacy. Therefore every root chain and its length are preserved. The transfer and bordered determinant are unchanged in the transported source/endpoint frame:

$$
\widehat E_{\Xi,a}(z)=E_{\Xi,0}(z)=\tau(z),
$$

so the Xi divisor and multiplicities are exactly retained.

## Translation-groupoid coherence

Complete cuts compose by seam resegmentation:

$$
C_{a+b}
=\mathfrak a_{a,b}(C_b\oplus I)C_a.
$$

Consequently the stabilized pencils satisfy the corresponding conjugacy cocycle. Associativity is inherited from interval concatenation and the resegmentation maps. Thus `a -> Rhat_(Xi,a)` is a representation of the cut/translation groupoid on the stabilized Rosenbrock family.

## Six-port consequence

The fixed-endpoint pencil failed bare translation covariance because it discarded the moving seam. The stabilized pencil restores realization coherence without changing the Xi transfer. Hence the Xi realization is a module object over the complete cut groupoid, although not over the tail-only translation representation.

The remaining gate is conservative symmetrization on this stabilized carrier: transport a source-derived nondegenerate metric through `C_a` and verify the source/endpoint port colocation equations.

Status: divisor-preserving tail-plus-seam Xi realization and groupoid coherence constructed by exact unitary stabilization.
