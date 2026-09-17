# Catalan quarter limit and the existing analytic realization functor

## Prior structures found

Three prior constructions are relevant.

1. `Convolution degree gives the generic r-cell...` constructs the degree successor
   \[
   L_a^{(r)}:E_r\to E_{r+1},\qquad p\mapsto a*p,
   \]
   and its Mellin realization
   \[
   \mathcal M_{r+1}L_a^{(r)}=M_{m_a}\mathcal M_r.
   \]
   At endpoints the same step is the diagonal operator
   \[
   D_a^\partial=\operatorname{diag}(m_a(i/2),m_a(-i/2)).
   \]
2. The all-arity rooted-spine theorem proves that marked Catalan transfer is natural under rooted subtree substitution. A forced two-label channel is therefore a legitimate degree-lowering Catalan submodule, not an ad hoc subset.
3. The stable cone work supplies suspension as the typed target of a four-chart cycle, with a still-required comparison `Sigma R_(4,k) -> R_(1,k+1)`.

## Which limit equals one quarter

The raw analytic successor `M_(m_a)` does not tend to `1/4` as the degree grows. Its iterates are multiplication by `m_a^r`; their limit depends on the chosen observer `a` and the target topology.

The canonical quarter occurs after **normalized trace/rank observation** of the forced-channel Catalan submodule.

Let `H_n` be the facet Hilbert module of the full `n`-point associahedron:

\[
\dim H_n=C_{n-2}.
\]

Let `P_n` be the orthogonal projection onto the adjacent-swap/forced-channel submodule. Rooted-subtree contraction identifies its image with the full `(n-1)`-point module, so

\[
\operatorname{rank}P_n=C_{n-3}.
\]

For the normalized finite trace `tau_n=Tr/dim(H_n)`,

\[
\tau_n(P_n)
=\frac{C_{n-3}}{C_{n-2}}
=\frac{n-1}{2(2n-5)}
=\frac14+\frac{3}{4(2n-5)}
\longrightarrow\frac14.
\]

Thus `1/4` is the large-degree normalized realization weight of one forced-channel sector.

## Interface with the four-chart cycle

The numerical agreement with the four-chart relation `q^4=Sigma` becomes a theorem only if the analytic realization functor satisfies both:

1. it sends the rooted forced-channel projection to a chart-sector projection;
2. its completed normalized trace agrees with the Catalan normalized trace.

Under those two intertwining identities, the asymptotic chart weight is exactly `1/4`. Without them, the Catalan quarter and the order-four chart rotation are two distinct structures with the same cardinality.

`check_catalan_realization_trace_ratio.py` verifies the exact rational formula through degree 100. At `n=33` the weight is `16/61`; it approaches `1/4` monotonically from above.
