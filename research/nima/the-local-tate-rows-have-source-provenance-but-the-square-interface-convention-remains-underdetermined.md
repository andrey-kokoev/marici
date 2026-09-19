# The local Tate rows have source provenance but the square interface convention remains underdetermined

## Primitive normalization

For the translated source atom

\[
c_a(q)=\Phi(q-a),
\qquad a=\log p,
\]

the primitive synthesis column carries the Euler half-density `p^{-1/2}`.
The centered first-position moment is normalized so that

\[
L_{\mathrm{prim}}(c_a)=a.
\]

Therefore its transpose row is exactly

\[
(K'L_{\mathrm{prim}})_p
=(\log p)p^{-1/2}.
\]

This identifies the primitive Tate coefficient with a continuous graph-dual
coordinate of the saturated ordered carrier. It is a covector, not a Hilbert
state.

## Square normalization family

Define exponentially twisted moments

\[
M_j^-(f)=\int q^j e^{-q/2}f(q)\,dq.
\]

Translation gives

\[
M_j^-(c_a)
=e^{-a/2}
\sum_{r=0}^j\binom jr a^{j-r}\mu_r^-.
\]

Since `mu_0^-` is nonzero for the positive Gaussian source, this triangular
moment system realizes every row

\[
P(\log p)p^{-1}
\]

for a fixed polynomial `P`. In particular it realizes both retained square
conventions:

\[
\frac12p^{-1}
\qquad\text{and}\qquad
(\log p)p^{-1}.
\]

These are source-generated members of one finite twisted-moment module; no
primewise interpolation is needed.

## Compatibility with the ordered graph

Position moments and exponentially twisted moments are continuous on the
metaplectic graph core after passing to their declared graph-dual rungs.
The generic labelled incidence theorem therefore applies with the physical
rows

\[
b_p^{(P)}=(\log p)p^{-1/2},
\qquad
b_p^{(2)}=P(\log p)p^{-1}.
\]

Their translated graph sums, Fourier images, endpoint coordinates, and
ordered principal-value currents are continuous and cutoff-independent on the
mixed rapid carrier.

The connected `k>=3` tail is smoother and absolutely convergent; the
archimedean attachment is a separate Mellin-line functional. Neither should
be collapsed into the primitive or square dual rows.

## Exact obstruction

Source provenance does not choose between the constant square endpoint
coefficient and the logarithmic square-current coefficient. Both satisfy the
internal continuity and transpose tests. Selecting one requires the declared
external Fourier--Poisson/G4 interface and its determinant-line convention.

Consequently local coefficient identification is complete up to a finite
interface choice:

1. the primitive row is fixed as `(log p)p^{-1/2}`;
2. the square row lies in the explicit family `P(log p)p^{-1}`;
3. the external comparison must specify `P` and the archimedean completion
   normalization;
4. only then can equality of the complete five-wall polarized rows be tested.

No scalar functional equation distinguishes the two square conventions,
because it is evaluated after this typed boundary choice has already been
compressed.
