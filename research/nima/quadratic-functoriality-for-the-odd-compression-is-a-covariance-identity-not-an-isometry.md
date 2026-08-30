# Quadratic functoriality for the odd compression is a covariance identity, not an isometry

## Rank-one operator

The completed odd comparison is

\[
K_p
=
d_p\otimes\ell_{\mathrm{jump}},
\]

where

\[
\ell_{\mathrm{jump}}(j_\theta)=1.
\]

Let \(G_{\theta,p}\) be the positive form operator on the theta endpoint plane
and \(G_{\mathrm{win},p}\) the independently declared window Green form.

There are three different quadratic statements, and they must not be
identified.

## Pushforward covariance

The covariance induced on the window carrier by the theta form is

\[
C_{\mathrm{win},p}
=
K_pG_{\theta,p}K_p^*.
\]

Because \(K_p\) has rank one,

\[
C_{\mathrm{win},p}
=
\left\langle
G_{\theta,p}\ell_{\mathrm{jump}}^\sharp,
\ell_{\mathrm{jump}}^\sharp
\right\rangle
|d_p\rangle\langle d_p|.
\]

This is automatically positive, rank one, and trace class across primes.

It is the correct quadratic shadow of the theta source. It need not equal the
pre-existing window Green metric.

## Pullback energy

The window energy seen from the theta side is

\[
C_{\theta,p}
=
K_p^*G_{\mathrm{win},p}K_p.
\]

Again,

\[
C_{\theta,p}
=
G_{\mathrm{win},p}(d_p,d_p)\,
|\ell_{\mathrm{jump}}^\sharp\rangle
\langle\ell_{\mathrm{jump}}^\sharp|.
\]

Since \(d_p\) becomes super-polynomially soft in the raw window metric, this
pullback collapses on the odd theta line unless the window form contains the
matching inverse scale.

Therefore the identity

\[
K_p^*G_{\mathrm{win},p}K_p
=
G_{\theta,p}
\]

cannot hold uniformly in the raw source frame when \(G_{\theta,p}\) has a
fixed nonzero odd eigenvalue.

## Exact scalar criterion

Restrict to the one-dimensional odd lines. Let

\[
g_{\theta,p}
=
G_{\theta,p}(j_\theta,j_\theta),
\qquad
g_{\mathrm{win},p}
=
G_{\mathrm{win},p}(d_p,d_p).
\]

Because \(K_pj_\theta=d_p\), isometric pullback is equivalent to

\[
g_{\mathrm{win},p}=g_{\theta,p}.
\]

The established raw topology gives \(g_{\mathrm{win},p}\to0\), while the
source theta endpoint metric gives a fixed positive value. Hence raw
isometric functoriality fails.

No Schur complement or endpoint normalization can change this conclusion
without changing one of the declared metrics.

## Correct joint Green object

The completion-stable object is the graph form

\[
G_{\Gamma,p}(y)
=
G_{\theta,p}(y)
+
G_{\mathrm{win},p}(K_py).
\]

It obeys

\[
G_{\Gamma,p}(y)\ge G_{\theta,p}(y).
\]

Thus the faithful theta energy remains present, while the Stieltjes component
is retained as a positive trace-class shadow. The graph projection to the
theta coordinate is bounded and supplies the lower margin.

This is the quadratic analogue of retaining the unit counit beside scalar
theta synthesis.

## Boundary factorization

The first-order Green identity proves that the odd coupling factors through
the endpoint trace:

\[
J_p
=
\operatorname{Tr}_{-,p}^*
\Omega
\operatorname{Tr}_{+,p}.
\]

Hence zero-trace bulk directions do not contribute to the odd interaction.
The theta columns determine the finite endpoint action of \(\Omega\), and
\(K_p\) determines its Stieltjes shadow.

This proves that the joint graph form contains the entire odd interaction. It
does not prove equality between the two diagonal energies.

## Radical descent

Let \(N_{\theta,p}\) and \(N_{\mathrm{win},p}\) be the respective Green
radicals. The graph map descends if

\[
K_pN_{\theta,p}\subseteq N_{\mathrm{win},p}.
\]

On the odd source line this is automatic whenever the theta odd energy is
nondegenerate, because its radical is zero there. On larger carriers it remains
a genuine typing theorem.

After descent, the graph form remains coercive relative to the reduced theta
metric:

\[
G_{\Gamma,p}^{\mathrm{red}}
\ge
G_{\theta,p}^{\mathrm{red}}.
\]

## Completion

Since

\[
\sum_p\|K_p\|_{\mathfrak S_1}<\infty,
\]

the direct-sum graph perturbation is trace class relative to the retained theta
carrier. It therefore cannot destroy closedness or the theta lower bound.

The soft window branch may vanish asymptotically without creating a dark state,
because the faithful theta coordinate is not quotiented out.

## Hostiles

Demanding isometric pullback forces the raw window energy of \(d_p\) to equal
the fixed theta odd energy, contradicting its established decay.

Discarding the theta coordinate after pushforward leaves only a compact
window covariance and destroys uniform observability.

Renormalizing \(d_p\) to unit norm restores an isometry only by inserting the
forbidden super-polynomial inverse scale.

## Verdict

The quadratic gate is not an equality of the theta and raw Stieltjes Green
metrics. That equality is false in the declared completion topology.

The source-authorized quadratic construction is the joint graph form

\[
G_{\Gamma,p}
=
G_{\theta,p}
+
K_p^*G_{\mathrm{win},p}K_p.
\]

It preserves the theta lower margin and retains the Stieltjes disagreement as
a trace-class positive shadow. The next local gate is radical compatibility
for the full wall--jump graph, not isometric identification of its two
diagonal metrics.
