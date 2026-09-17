# Convolution successor and observation have a common joint graph domain

## Fixed-observer theorem

Fix a source observer `a` and let its Mellin multiplier be `M_a`. Let

\[
\mathcal O:G\supset\operatorname{Dom}(\mathcal O)\to B
\]

be the retained endpoint/readout operator on the declared analytic graph carrier. On the finite Mellin packet core `D_0`, the exact source identity is

\[
\mathcal O M_a=D_a^\partial\mathcal O,
\]

where `D_a^partial` is the finite-dimensional endpoint multiplier.

Define the combined graph map

\[
J_{a,O}x=(x,M_ax,\mathcal Ox,\mathcal OM_ax)
\]

and the common domain

\[
D_{a,O}=\overline{J_{a,O}(D_0)}
\subset G\times G\times B\times B.
\]

Equivalently, use the graph seminorms

\[
\|x\|_G,
\quad
\|M_ax\|_G,
\quad
\|\mathcal Ox\|_B,
\quad
\|\mathcal OM_ax\|_B.
\]

## Closability

Mellin multiplication by a measurable symbol is closed on its maximal multiplication domain. The retained observation is a closed coordinate of the declared joint graph carrier; it is not raw point evaluation on bare `L2`. The composite coordinate on the core satisfies

\[
\mathcal OM_a=D_a^\partial\mathcal O.
\]

Since `D_a^partial` is bounded on the finite endpoint fiber, the composite is closable wherever `O` is closable. For a finite family of closed or closable coordinates, the diagonal graph map is closable: a source-null sequence whose coordinates converge has zero limit in each coordinate. Thus `D_{a,O}` is a faithful complete graph domain over `G`.

Both operators extend continuously as graph-coordinate maps:

\[
M_a:D_{a,O}\to G,
\qquad
\mathcal O:D_{a,O}\to B,
\]

and endpoint naturality persists by density:

\[
\widehat{\mathcal O}\,\widehat M_a
=D_a^\partial\widehat{\mathcal O}.
\]

This simultaneously supplies the generic completion faces `R x L` and `R x O` for each admitted observer.

## Families of observers

For a finite observer family, include all multiplier and observed-multiplier coordinates in one diagonal graph. Separate closability implies joint closability in the ordinary finite product topology.

For an infinite or pro-family, use the projective product of the finite-family graph domains. This gives coordinatewise continuity and faithfulness. A stronger uniform record norm requires additional uniform multiplier estimates and is not claimed.

## Exact boundary

This constructs the analytic `L/O` common domain. It does not prove that the labelled arithmetic synthesis lands in it. The remaining incidence gate is

\[
U_4(\mathcal A_{\exp})\subset D_{a,O}
\]

continuously, uniformly for the observer family required by the full cube.

It also does not place endpoint evaluation on bare `L2`; retaining the graph coordinate is essential. A sequence converging in `L2` while its point values remain nonzero is the standard falsifier of that stronger claim.
