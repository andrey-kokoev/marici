# Theta ideles are a null boundary for additive Hilbert completion

## The tempting operator lift

The global Tate operation begins with an additive Schwartz--Bruhat source on
`A` and restricts it to the multiplicative group `A^x` before Mellin
integration.  A tempting lift would extend additive Fourier transform to a
Hilbert operator on multiplicative boundary states and then take its two norm
polarization blocks as the seam maps `B,C`.

This fails on the naive additive `L2(A)` completion because the required
restriction is singular.

## Additive measure of the ideles

Normalize additive Haar measure on each `Z_p` to one.  For an element of
`Z_p`, the probability of being a unit is

\[
 \mu_p(\mathbb Z_p^\times)=1-\frac1p.
\]

An adele is an idele only if its finite component is a unit at all but
finitely many primes.  For any fixed finite exceptional set, the additive
measure of being a unit at every remaining prime is

\[
 \prod_{p>N}\left(1-\frac1p\right)=0,
\]

because `sum_p 1/p` diverges.  Taking the countable union over finite
exceptional sets still gives measure zero.  Hence

\[
 \boxed{
 \mathbb A^\times\text{ has additive Haar measure zero inside }\mathbb A.}
\]

## Trace no-go

An additive `L2(A)` vector is an equivalence class modulo additive-null sets.
Its values on `A^x` are therefore undetermined.  Consequently there is no
canonical bounded restriction

\[
 \boxed{
 j^*:L^2(\mathbb A,dx)
 \longrightarrow L^2(\mathbb A^\times,d^\times x).}
\]

Indeed two representatives of the same additive `L2` class may differ
arbitrarily on the entire idelic locus.

Thus one cannot define the desired multiplicative seam operator by

\[
 j^*\mathcal F(j^*)^{-1}
\]

on naive Hilbert completions.  The inverse and even the first restriction are
not typed.

## Why the Tate scalar still exists

For a Schwartz--Bruhat function `phi`, pointwise restriction to the ideles is
well-defined and has the decay and local constancy needed for the Tate zeta
integral.  Poisson summation also acts before passing to additive `L2`
equivalence classes.

Therefore the source-level scalar correspondence survives while its naive
Hilbert operator lift does not.  This is a concrete instance of

\[
 \text{source correspondence}
 \not\Rightarrow
 \text{bounded operator after lossy completion}.
\]

## Required rigged trace object

The seam module must retain a trace map before Hilbert completion, schematically

\[
 \mathcal S(\mathbb A)
 \xrightarrow{j^*}
 \mathcal T(\mathbb A^\times)
 \hookrightarrow
 \mathcal T'(\mathbb A^\times),
\]

with additive Fourier transform acting on the source side and multiplicative
Mellin transport acting on the boundary side.  The completed seam maps are a
**correspondence through this trace**, not blocks of one ordinary `L2`
operator.

The topology of `T` must also accommodate the exponentially growing primitive
atomic current from packet 168.

## Compiler consequence

The joint Tate operation `A_Tate` precedes any Hilbert compression.  Seam
retention `S` must preserve the idelic trace data at the source/test-function
level:

\[
 \boxed{S_{\rm trace}\prec A_{\rm Tate}\prec D_{\rm relative}.}
\]

Applying additive `L2` completion before `S_trace` irreversibly deletes the
entire multiplicative boundary.  No post-completion repair can reconstruct it.

## Real remaining theorem

Construct a nuclear or exponential rigged trace theorem in which:

1. `j*` is continuous on the source test space;
2. Fourier--Poisson sewing and Mellin transport form a coherent
   correspondence;
3. the primitive and square atomic currents act continuously;
4. the relative Green boundary form descends without identifying idelic
   states modulo additive-null equivalence.

This trace correspondence is the missing operator-valued lift from the global
Tate integral to the seam incidence maps.
