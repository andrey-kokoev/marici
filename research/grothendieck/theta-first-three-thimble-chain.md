# First three-thimble relative-cycle chain

## Topology mutation

After the third saddle joins on \(z=1/2+ib\) near
\(b=9.6439257771\), the old basis reconnects through source zeros

\[
u_{\star,0}\approx0.6388300536005935\,i,
\]

\[
u_{\star,1}\approx
0.2556475134765196+0.6955398322128286\,i.
\]

Both are numerically simple zeros of the analytically continued Mellin
amplitude, with derivative magnitudes approximately \(259.20\) and \(1593.82\).

At \(b=9.66\), the oriented endpoint graph is

\[
\boxed{
-\infty
\longrightarrow u_{\star,0}
\longrightarrow u_{\star,1}
\longrightarrow+\infty.
}
\]

Its edges are the first competitor, the newly admitted third thimble, and the
mutated principal thimble. The wall therefore mutates the relative-cycle
incidence graph; it does not append a term to an unchanged basis.

## Contour reconstruction

Incidence determines every sign without fitting. Downward path quadrature
gives

\[
I_{\rm chain}
\approx0.0448932771147791+0.0128040098923378\,i.
\]

Independent real-contour quadrature gives

\[
I_{\mathbb R}
\approx0.0449152174983273+0.0128139386485156\,i.
\]

Their relative difference is \(5.16\times10^{-4}\).

## Positivity after mutation

The reconstructed chain has

\[
\boxed{C_{\rm chain}\approx2.96772133898>0.}
\]

The independent real-contour value is \(2.96858813246\), differing by about
\(8.67\times10^{-4}\).

Thus coupled positivity survives the first mutation from a two-edge to a
three-edge relative-cycle graph.

The algebraic reason is now isolated: the cone numerator is a Hermitian
quadratic functional of the total relative class and is invariant under an
integral Picard--Lefschetz basis mutation. The numerical reconstruction here
tests that the proposed three-edge chain is the same physical class; it is not
an independent positivity principle for three saddles. See
`theta-relative-cycle-mutation-invariance.md`.

## Generalized conjecture

The source-derived object is an oriented path in the relative-cycle graph
whose vertices are zeros of \(G\), together with the two decaying infinities.

At each Stokes wall:

1. mutate the edge basis by Picard--Lefschetz transport;
2. preserve the endpoint incidence chain;
3. assemble the cone numerator only after mutation; and
4. prove dominance of the complete oriented chain.

The falsifier is a wall where the incidence mutation cannot reconstruct the
real contour, or a chamber point where the chain cone becomes nonpositive.

## Limitations

The zeros, flows, and integrals are numerical reconnaissance, not
interval-certified. Only the \(a=1/2\) ray has been followed.

Artifacts:

- checkers/theta_first_three_thimble_block.py
- results/theta-first-three-thimble-block.json
- checkers/theta_complex_source_zero_endpoints.py
- results/theta-complex-source-zero-endpoints.json
