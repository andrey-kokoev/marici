# The response graph does not discharge Evans membership without the missing polarized prime cell

## Question

Does construction of the canonical maximal-isotropic Fourier response graph prove the remaining Evans prime-shell residual automatically?

## Claim boundary

No. It proves the target relation and source-generated membership, but the unchanged Evans trace is not yet identified as a source response vector. Attempting to define its source preimage by first-coordinate projection makes the missing outgoing equality exactly the original residual. The earliest noncircular executable input remains one full polarized two-output Green cell per prime.

## Constructed relation

The complete response sewing relation is

$$
\Lambda_{\mathbb T}
=\{(x,\mathbb Tx):x\in\mathcal H_{\rm resp}\}.
$$

Every declared source vector \(g\) gives

$$
(\mathscr R(g),\mathscr R(\mathcal Fg))
\in\Lambda_{\mathbb T}.
$$

This closes existence, unitarity, and maximal isotropy of the target relation.

## Evans membership equation

Write the unchanged Evans boundary data as

$$
(e_-,e_+).
$$

Membership means

$$
e_+=\mathbb T e_-.
$$

Because response recovery is projection to all-seam flux, one can set

$$
g_e=C_{41}^{\rm resp}e_-.
$$

But this only identifies the incoming record if

$$
e_-=\mathscr R(g_e),
$$

and it identifies the outgoing record only if

$$
e_+=\mathscr R(\mathcal Fg_e).
$$

The second equation is precisely \(e_+=\mathbb Te_-\). Thus defining \(g_e\) from the incoming coordinate does not prove sewing; it restates the missing membership condition.

## Prime-shell projection

After projection to a consecutive-prime shell and differentiation through a Xi zero, the same equality becomes

$$
B_\Sigma^\dagger\partial_z^ju(\cdot;z_0)=0,
\qquad 0\le j<m(z_0).
$$

Hence the newly constructed response graph supplies the codomain of the residual but does not annihilate it.

## Fresh locator reduction

Current sourced shell information is:

1. the ordinary term is explicit and eventually nonzero;
2. the regular-derivative plus wall term is the explicit endpoint difference
   $$
   \Phi(b)u_z(b)-\Phi(a)u_z(a)
   $$
   in the analytic-transpose lane;
3. reciprocal Fourier transport is now explicit on the complete source-response carrier;
4. the ordered linking form and its scalar coefficient \(\lambda_p\) are continuous and fixed;
5. the full two-output Green metric comparison is absent.

The missing primewise datum is still

$$
G_S=T_p^*G_WT_p,
\qquad
T_p=\operatorname{diag}(\alpha_p,\lambda_p),
$$

including the source-derived even coefficient \(\alpha_p\), both diagonal energies, and the complex mixed entry.

## Why scalar sewing cannot supply it

The Fourier/Tate calculation determines reciprocal transport and character phases. It does not determine an arbitrary positive two-output Green metric. Unitarity fixes the metric only after the source and target embeddings are declared. Choosing \(G_W\) or \(\alpha_p\) to force the equality would fit the G4 adjoint to the desired cancellation.

Likewise, determinant equality checks only

$$
\det G_S=|\det T_p|^2\det G_W
$$

and cannot recover the mixed real-even and oriented-odd entries independently.

## Earliest admissible continuation

A noncircular next calculation requires, for one prime block:

- the declared ordered source and G4 output bases;
- the explicit matrices \(G_S,G_W\);
- the source-derived \(\alpha_p\);
- the already fixed \(\lambda_p\).

Then the matrix identity can be tested mechanically before any Xi-zero specialization. Without these data there is no complete shell scalar to evaluate and no symbolic cancellation claim to falsify.

## Disposition

The maximal-isotropic response relation is constructed, but unchanged-Evans membership in it remains exactly the prime-shell adjoint residual. The remaining obstruction is no longer Fourier response transport; it is the missing polarized G4 prime-cell metric and even comparison coefficient. No further source-derived residual calculation is executable until that cell is exposed.