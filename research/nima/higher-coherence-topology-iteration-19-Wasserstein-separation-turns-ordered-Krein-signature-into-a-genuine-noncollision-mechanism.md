# Higher-coherence topology iteration 19: Wasserstein separation turns ordered Krein signature into a genuine noncollision mechanism

## Candidate topology

Represent an indefinite boundary transfer by the Jordan decomposition of its
spectral measure:

\[
F(z)=\int\frac{d\mu(t)}{t-z},
\qquad
\mu=\mu_+-\mu_-.
\]

For `z=x+iy`, `y!=0`, weight both sectors by the positive Cauchy window

\[
p_{x,y}(t)=\frac1{(t-x)^2+y^2}.
\]

When their weighted masses agree, normalize them to probability measures
`nu_+(x,y)` and `nu_-(x,y)` and compare them in Wasserstein topology.

## Zero as a moment collision

The equation `F(z)=0` implies both

\[
\int p_{x,y}\,d\mu_+
=
\int p_{x,y}\,d\mu_-
\]

and equality of weighted barycenters

\[
\int t\,d\nu_+(x,y)
=
\int t\,d\nu_-(x,y).
\]

Thus an off-axis zero requires a mass-and-first-moment collision between the
two signature sectors.

## Ordered-support transport gap

Assume a source-derived spectral ordering

\[
\operatorname{supp}\mu_+\subset(-\infty,\tau],
\qquad
\operatorname{supp}\mu_-\subset[\tau+\delta,\infty)
\]

with `delta>0`. Positive Cauchy weighting preserves these supports. Every
transport plan from `nu_+` to `nu_-` moves all mass by at least `delta`, so

\[
W_1(\nu_+,
u_-)
\ge\delta.
\]

In particular their barycenters differ by at least `delta`. Therefore no
nonreal zero can occur.

Unlike previous topology changes, this is a genuine exclusion mechanism: it
uses geometric separation of independently positive sectors rather than trying
to quotient or complete away a residual.

## Relation to higher cones

A repeated simplex/prism/cone tower could preserve the transport gap if every
higher attachment is sign-ordered and does not interlace the two supports.
Wasserstein completion is stable under weak convergence plus uniform first
moments, so a uniform gap survives the limit.

Conversely, a higher system whose new positive and negative atoms interlace can
close the gap and create a moment collision. Higher coherence is therefore not
automatically benign; it needs an order-preserving attachment law.

## Prime two-ray model

For a reciprocal pair supported at logarithmic positions `-log p` and
`+log p`, equality of route masses makes the barycenter neutral only when the
two weights agree. With weights proportional to `1` and `p^(-2a)`, this gives

\[
1=p^{-2a},
\qquad a=0.
\]

The transport picture recovers the Haar criterion as equality of two ordered
atomic masses.

## Actual open source test

Prior work proves the ordered-signature theorem abstractly but does not prove
that the finite theta/Tate endpoint-cyclic spectral weights have only one sign
transition. A three-atom `+,-,+` interlacing already permits a nonreal hostile
collision.

The executable source test is finite:

1. diagonalize each finite carrier `A_X`;
2. compute typed weights
   `⟨P_j b_X,K_XP_j b_X⟩`;
3. order them by carrier eigenvalue;
4. count signature transitions;
5. seek a cutoff-uniform support gap or prove its failure.

## Verdict for topology 19

Wasserstein topology does not absorb the Haar residual. It reveals a potentially
new unlock: uniformly ordered positive and negative spectral supports forbid
the collision required by an off-seam zero, and this exclusion survives
transport completion.

This route depends on a concrete source theorem—single-transition ordered
Krein signature—not on RH itself. It is the strongest genuinely new topology
candidate found so far.

The next nonredundant topology to test is a variation-diminishing/total-
positivity topology, which may enforce the required one-transition signature
law under higher attachments.