# Raw Sobolev Completion Admits a Homogeneous Zero Forger That the Source Infinity Trace Excludes

## The missing domain condition

The reciprocal tail equation

\[
(\partial_q+z)G_+=-f

\]

has the source-normalized solution

\[
G_+^{\rm src}(q)
=
\int_q^\infty f(v)e^{z(v-q)}\,dv.
\]

When `a=Re z>0`, every function

\[
G_+^{\rm src}(q)+Ce^{-zq}
\]

solves the same differential equation and belongs to `H^1(0,infinity)`. Plain
decay and Sobolev regularity therefore do not select the source tail.

The source integral carries the stronger asymptotic normalization

\[
\lim_{q\to\infty}e^{zq}G_+^{\rm src}(q)=0.
\]

The homogeneous addition changes this limit to `C`. Thus the source remembers
one infinity trace that raw Sobolev completion forgets.

For `a<0`, the reciprocal equation has the corresponding ambiguity

\[
G_-^{\rm src}(q)+Ce^{zq},
\]

excluded by

\[
\lim_{q\to\infty}e^{-zq}G_-^{\rm src}(q)=0.
\]

On the seam `a=0`, neither homogeneous mode lies in `L^2`; ordinary Hilbert
typing restores uniqueness. The hidden degree of freedom therefore changes
sheet exactly across the critical line.

## Exact zero forger

In the right half-plane, let

\[
C=-X(z).
\]

Adding `C exp(-zq)` to `G_+` changes its endpoint by `C` while leaving the
differential equation, `H^1` membership, and decay intact. It forces

\[
G_+(0)+G_-(0)=0
\]

at every `z` in that half-plane. Hence the Dirichlet condition from the parity
rotation is not equivalent to a source zero on the raw Sobolev domain.

The forged state is rejected only by the infinity normalization, because its
weighted asymptotic trace is `-X(z)` rather than zero.

## The source-normalized subspace is not raw-graph closed

Let `a>0` and consider the homogeneous mode

\[
h(q)=e^{-zq}.
\]

Choose smooth cutoffs `chi_R` equal to one before `R` and zero after `R+1`.
Then

\[
h_R=\chi_Rh
\]

has compact support and hence zero weighted infinity trace, while

\[
h_R\longrightarrow h
\]

in the ordinary `H^1` graph norm. But the weighted infinity trace of `h` is
one. Therefore the source-normalized domain is not closed in the raw Sobolev
graph topology.

This corrects the scope of the previous weighted Sobolev result. That result
constructs the closed local generator and retains the finite seam trace. It
does not retain the Volterra normalization at infinity.

## Corrected boundary object

The faithful reciprocal state must include an independent asymptotic port:

\[
\mathcal B_z^+(G)=\lim_{q\to\infty}e^{zq}G(q)
\]

in the right half-plane, and

\[
\mathcal B_z^-(G)=\lim_{q\to\infty}e^{-zq}G(q)
\]

in the left half-plane. The source tail is the kernel of the appropriate port.

This port cannot be recovered continuously from the raw `H^1` graph state.
It must be retained as boundary data or built into a stronger weighted graph
topology. The two choices must be compared for reciprocal sewing at the seam,
where the exponential weights lose decay.

## Multi-tower meaning

The input and output towers plus the finite seam comparison are insufficient.
The control tower has two boundary faces:

- the finite seam trace at `q=0`;
- the source normalization trace at `q=infinity`.

The latter is sheet-dependent and becomes singular at the unitary seam. This
is the genuine next coherence wall. Without it, the completed operator admits
off-seam punctures manufactured by a legal Hilbert-space homogeneous mode.

## Result

Raw Sobolev completion is too coarse for the zero-to-state bridge. It admits a
one-dimensional homogeneous zero-forging torsor in each open half-plane. The
source integral is selected by an additional weighted infinity trace, and
that trace is not closed in the raw graph topology. Any RH construction must
retain this asymptotic port explicitly through reciprocal completion.

