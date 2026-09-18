# Conservative/cyclic naturality reduces to three bordered generators

The bordered response packet

$$
\beta=(\rho_0,E,W,R)
$$

satisfies the exact Stokes relation

$$
zR-\rho_0=E-\frac12W.
$$

For `z!=0`, one has

$$
R=z^{-1}\left(\rho_0+E-\frac12W\right).
$$

Hence the bordered response module has three independent coordinates. Let `Lambda_cons` be the independently constructed conservative functional and `Lambda_cyc` the cyclic trace functional. If

$$
\Lambda_{\rm cons}(\rho_0)
=\Lambda_{\rm cyc}(\rho_0),
$$

$$
\Lambda_{\rm cons}(E)
=\Lambda_{\rm cyc}(E),
$$

and

$$
\Lambda_{\rm cons}(W)
=\Lambda_{\rm cyc}(W)
$$

on every source generator, then equality on `R` follows from the Stokes relation for `z!=0`. The removable continuation at `z=0` extends the equality there. Continuity and density then extend equality from finite source packets to the completed source-generated trace ideal.

The three tests have distinct roles:

1. `rho_0`: ordinary source normalization;
2. `E`: even endpoint/wall normalization;
3. `W`: oriented odd linking normalization.

Reciprocal transport generates the opposite-orientation tests contragrediently once these forward tests and the declared pairings are fixed.

Thus the naturality gate is not four unrelated identities. It is a three-generator comparison, with the ordinary generator already explicit. The genuinely unresolved source comparisons are the even endpoint functional and the oriented Wronskian functional for the independent conservative trace.

Status: conservative/cyclic comparison reduced to two new source equalities after the ordinary normalization; owner construction of the conservative functional remains required.
