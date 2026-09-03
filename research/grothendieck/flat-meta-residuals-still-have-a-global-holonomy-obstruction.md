# Local meta-residual data may have a global holonomy obstruction

## Question

Does zero curvature on every declared local coherence cell guarantee that one global completed normalization exists?

## Gauge change

Let `s_i` be a change of normalization at each lower-pyramid object. Replacing

\[
K_i\longmapsto K_i+s_i
\]

changes an edge residual by

\[
\Omega_f
\longmapsto
\Omega_f+s_j-f_*s_i.
\]

Thus normalization changes add a coboundary. This becomes a genuine cohomology question only when the `K_i` are local affine representatives or the coefficient transports are transition data not yet known to descend. If globally compatible `K_i` already inhabit one coefficient system, `Omega_f=K_j-f_*K_i` is the coboundary of `K` by definition and its class is tautologically zero.

## Flat but nonexact

Assume instead that `Omega_f` is given as local transition residual data before a global `K` exists. The cocycle equation

\[
\Omega_{g\circ f}=\Omega_g+g_*\Omega_f
\]

and zero curvature on listed cells establish local flatness. They do not imply that there are potentials `s_i` satisfying

\[
\Omega_f=s_j-f_*s_i.
\]

A flat cocycle may have nonzero period around a loop. Such holonomy prevents all local presentations from descending to one global completed object.

The obstruction is the class

\[
[\Omega]\in H^1(\mathcal C_{\rm obs};\mathcal M),
\]

where the coefficient system `M` contains the typed kernel residuals and their transports.

## Role of endpoint and gamma completion

Endpoint and gamma data must do more than match individual prime-to-completed edges. They must provide a global zero-cochain `s` whose coboundary equals the prescribed completion residual on every generator. Equivalently, all residual periods must agree with the endpoint--gamma trivialization.

If the prescribed class is nonzero, no observer-dependent normalization may erase it. If endpoint--gamma data trivialize it, the resulting completed object is defined independently of route.

## Meta-observer extension

The indexing category needs a generating set of loops in addition to generating arrows and local cells. For each loop `ell`, define the transported period

\[
\operatorname{Per}_\Omega(\ell)
=
\Omega_{f_m}
+f_{m*}\Omega_{f_{m-1}}
+\cdots
+(f_m\cdots f_2)_*\Omega_{f_1}.
\]

A global completion certificate must show these periods vanish, or equal a declared nonzero class when the target itself is twisted. Finite-cutoff periods carry transported tail bounds.

## Positive residual after descent

Only after the affine residual system descends to a global completed object is the cone section

\[
\mathfrak R=D^*D
\]

route-independent. Otherwise different local trivializations may produce incompatible positive forms even though each local Gram test passes.

## Disposition

When only local affine representatives or unverified coefficient transports are available, strengthen meta-coherence from local flatness to global descent: cocycle law, zero cell curvature, and trivialized loop periods. When a global compatible `K` is already constructed, skip this vacuous cohomology lane and test its ordinary route identities directly. Positivity is imposed on the descended residual section, not on unrelated local representatives.
