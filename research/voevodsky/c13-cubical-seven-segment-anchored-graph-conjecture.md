# C13 cubical seven-segment anchored-graph conjecture

## Question

Can the source-to-spectral comparison be represented by seven consecutive universe paths with segmentwise inverses?

## Claim boundary

The following construction gives a typed candidate by replacing every intermediate presentation with a cumulative graph over the source observer pair. It proves algebraic inversion on each graph image. It does not prove that the unanchored shadows are equivalent, that the graph topologies agree with pre-existing target topologies, or that the candidate terminal graph is the intended intrinsic definition of the spectral vertex.

Fix a semilocal place stage \(S\). Let

$$
X_0=\{(g_1,g_2):g_i\in\mathsf{Obs}_S\}.
$$

Define successively

$$
h_{12}=g_1*g_2^*,
$$

$$
m_i=\mathcal F_\mu w(g_i),
$$

$$
\xi_i^+=A_S^+m_i,
$$

$$
\xi_i^-=\mathcal H_S\xi_i^+,
$$

$$
b_{12}=B_S(\xi_1^+,\xi_2^-),
$$

$$
J_{\mathrm{loc},S}=\prod_{v\in S}\frac{L_v(1/2-is)}{L_v(1/2+is)},
$$

$$
V_{\mathrm{loc},S}=\frac{1}{2i}\frac{d}{ds}\log J_{\mathrm{loc},S}.
$$

Let \(X_r\) be the graph retaining \((g_1,g_2)\) and the first \(r\) displayed coordinates. Thus \(X_7\) retains the complete source anchor, transformed observer vectors, pairing value, phase, and connection.

For \(r=0,\ldots,6\), let \(f_r:X_r\to X_{r+1}\) append the next displayed coordinate, and let \(g_r:X_{r+1}\to X_r\) forget that last coordinate. Since \(X_{r+1}\) is defined as the graph of that coordinate constructor,

$$
g_rf_r=\operatorname{id}_{X_r},
$$

$$
f_rg_r=\operatorname{id}_{X_{r+1}}.
$$

Hence each pair \((f_r,g_r)\) is an algebraic equivalence and determines a universe path by univalence. The forward comparison is the concatenation

$$
f_6f_5f_4f_3f_2f_1f_0:X_0\longrightarrow X_7,
$$

and its reverse is

$$
g_0g_1g_2g_3g_4g_5g_6:X_7\longrightarrow X_0.
$$

## Falsifiers

The construction fails as the intended intrinsic source-to-spectral path if any appended coordinate is not defined on the common source carrier, if its graph is not admitted in the declared topology, or if the intended spectral endpoint is required to forget the source anchor. It also fails to include completed endpoint data unless an eighth coordinate is unnecessary because that row belongs to a different edge or dependent boundary fiber.

## Disposition

The candidate is rejected as a factorization of the declared C13 comparison. Its initial and terminal objects are cumulative graph sets of observer pairs, whereas the independently declared vertices are Hermitian-form presentation functors. Therefore the claimed universe path has the wrong endpoint type, and none of its fourteen graph maps counts as a certified C13 segment constructor. The first missing object is a universe of Hermitian-form presentations in which both endpoint functors and every intermediate presentation are objects.