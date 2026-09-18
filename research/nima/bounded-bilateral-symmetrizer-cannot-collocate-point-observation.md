# Bounded bilateral symmetrizer cannot collocate point observation

On the bilateral dilation space

$$
H=L^2(\mathbb R)\oplus L^2(\mathbb R),
$$

the lifted forcing column obtained by zero extension of the stable source profiles is an element

$$
b_{\rm dil}\in H.
$$

The endpoint observation

$$
c(f_-,f_+)=f_-(0)-f_+(0)
$$

is not a bounded functional on `H`. It is bounded on the graph/Sobolev domain

$$
H^1(\mathbb R)\oplus H^1(\mathbb R)
$$

and is represented in the anti-dual by

$$
c^*=(\delta_0,-\delta_0)
\in H^{-1}(\mathbb R)\oplus H^{-1}(\mathbb R),
$$

but `c*` does not belong to `H`.

If `K:H->H` is bounded, then

$$
Kb_{\rm dil}\in H.
$$

Therefore the colocation equation

$$
Kb_{\rm dil}=\alpha c^*
$$

cannot hold as an equality in `H` for nonzero `alpha`. This is a type obstruction, independent of positivity or spectral ratios.

Three valid repairs are possible:

1. use a rigged symmetrizer `K:H -> H^{-1}` with a declared nondegenerate pairing;
2. enlarge the state by an explicit boundary port so the observation is represented by a Hilbert coordinate;
3. smooth the observation through a source-authorized boundary kernel, changing the realization only if transfer preservation is proved.

The existing enlarged Green coordinate space follows option 2 by retaining wall/jump and seam coordinates. Consequently a conservative six-port realization cannot live on the bare bilateral history space alone.

Status: bounded bare-history colocation ruled out; boundary-enlarged or rigged conservative realization required.
