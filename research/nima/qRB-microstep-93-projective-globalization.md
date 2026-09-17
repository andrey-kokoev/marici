# qRB microstep 93: projective globalization

Because the fixed-support constants `C_L` need not be uniformly bounded, globalize the observer through the projective family of support domains rather than one bare Hilbert norm.

Let `p_L` be the logarithmic graph seminorm on the support rung `[-L,L]`. The required continuity is

$$
|Q(f,g)|\le C_Lp_L(f)p_L(g)
$$

for every finite rung, with compatibility under restriction and endpoint graph maps.

This defines a continuous bilinear observation on the projective limit whenever the rung restrictions agree. No uniform bound in `L` is required.

The projective construction preserves the relative qRB semantics: finite stages are positive carriers, while the global observation is signed and endpoint-relative.

Status: projective globalization is the correct non-uniform completion target; restriction compatibility remains to be checked for the explicit source identity.
