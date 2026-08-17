---
id: 406
date: 2026-08-17
title: The Primitive Cousin Normalization Selects the Nonzero Mobius Atlas Class
---

# The Primitive Cousin Normalization Selects the Nonzero Möbius Atlas Class

Entry 405 proved that endpoint parity alone cannot distinguish the zero atlas
cocycle from the primitive Möbius cocycle. The missing datum was the
crosscap comparison
\[
\Psi_{\rm crosscap}:
\operatorname{Fib}_{\partial,Q}\longrightarrow L_{\rm or}.
\]
The required map is already determined when the later geometric
construction is combined with the earlier primitive Cousin normalization.

## The two primitive lines

Entry 142 computes the only homology of the unsplit endpoint pullback:
\[
H_1(C_{\partial}^{\rm coeff})\cong\mathbb Z_{\rm or}.
\]
Entries 91--92 compute the primitive Möbius quotient:
\[
L_{\rm or}\cong\mathbb Z_{\rm or}.
\]
On both lines, rotations act by \(+1\) and reflections by \(-1\). Therefore
every equivariant homomorphism is multiplication by an integer \(n\).
Character matching alone leaves \(n\) undetermined, exactly as Entry 92
warned.

Entry 94 supplies the missing nonordinary map. Its
normalization--conductor Cousin/Gysin symbol lands in the tag resolution
before road incidence, and its Verdier-dual primitive branch has unit value
on every retained polarized occurrence. It is integral and primitive, so
\[
|n|=1.
\]
The positive Cousin, polarity, and coaction convention fixes the sign
\[
n=+1.
\]
Entries 392--400 subsequently construct the spatial connector and endpoint
mapping fiber with that same retained positive normalization; Entry 404
provides the faithful \(D_8\)-equivariant square-sector identification.
Thus the associated crosscap comparison is
\[
\boxed{\Psi_{\rm crosscap}=+1:
\mathbb Z_{\rm or}\xrightarrow{\sim}\mathbb Z_{\rm or}.}
\]

## Atlas value

Let \(\gamma\) be the primitive Möbius core and \(\omega\) its primitive
dual cocycle. The geometrically normalized endpoint generator maps to
\(\gamma\) with coefficient one:
\[
\langle\Theta,\gamma\rangle=1.
\]
Hence the selected additive atlas class is
\[
\boxed{\Theta=\omega,}
\]
not the zero solution. Since the outer octagon is twice the core,
\[
\langle\Theta,\partial O\rangle=2.
\]
This is fully compatible with Entry 400:
\[
2\bmod2=0=p_{\partial,Q}.
\]
The even endpoint parity records only the capped mod-two shadow and therefore
did not reveal that the integral crosscap weight is primitive and nonzero.

## Scope

This selects the additive Möbius/Jordan atlas class at the primitive
associated-grade and spatially normalized connector level. It does not turn
the noninvertible residue/Gysin cospans into transition automorphisms, and it
does not construct multiplicative holonomy. The result is a nonzero additive
higher-coherence class, not an obstruction to the already proved polarity
homotopy or square comparison.

The next question is interpretive and structural: determine whether the
primitive class \(\omega\) is exactly the capped rectangular Jordan
fundamental-formula cell, or whether their equality requires one further
top-dimensional comparison homotopy.

The executable audit is
\`research/voevodsky/check_endpoint_to_mobius_crosscap_comparison.py\`.
