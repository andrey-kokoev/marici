# Theta nontrivial divisor is created only at restricted-product completion

## Finite Euler charts

Fix a finite set of primes `S` and retain the standard unramified local
source at every `p in S`.  Its multiplicative Tate integral is

\[
 Z_p(s)
 =\int_{\mathbb Q_p^\times}{\bf1}_{\mathbb Z_p}(x)|x|_p^s\,d^\times x
 ={1\over1-p^{-s}}
\]

in the convergence chamber.  Therefore the finite Euler chart is

\[
 E_S(s)=\prod_{p\in S}{1\over1-p^{-s}}.
\]

For `p notin S`, tensor-product functoriality gives the exact transition

\[
 \boxed{
 E_{S\cup\{p\}}(s)=Z_p(s)E_S(s).}
\]

This is the scalar shadow of the line transition.  On every domain avoiding
the local pole lattice, `Z_p(s)` is invertible and has no zeros.

## Finite descent residual

Let `I_S` denote the source incidence written in the `S`-Euler chart, and let
the target line be transported by `Z_p`.  With the covariant typing

\[
 I_{S\cup\{p\}}=I_S\circ Z_p^{-1},
\]

the typed residual is exactly

\[
 \boxed{
 \mathfrak D_{S,p}
 =I_{S\cup\{p\}}Z_p-I_S=0.}
\]

Nothing analytic is being estimated here.  It is associativity of the local
tensor product and Fubini in the common convergence chamber.  The equality
continues meromorphically because both sides are the same source-derived local
zeta functional.

Thus the finite-cutoff braid closes.  Primitive and square currents are the
first two logarithmic coordinates of this exact transition, not residual
failures of it.

## No finite nontrivial divisor

Include the archimedean gamma factor and the standard elementary completion
units, but do not form an answer-fitted symmetric sum.  A finite product of
these local Tate factors is meromorphic and has no nontrivial zero divisor:

- every finite Euler factor is zero-free;
- the gamma function is zero-free;
- elementary exponential and power normalizations are zero-free;
- the explicit completion polynomial contributes only its declared boundary
  zeros.

Consequently a nontrivial Riemann zero cannot be a kernel already present in
one of these finite tensor products.

\[
 \boxed{
 \text{the nontrivial divisor is created only by the completed
 restricted-product operation}.}
\]

This is not a claim that arbitrary finite symmetrizations are zero-free.  A
sum such as `F_S(s)+F_S(1-s)` may have accidental zeros, but it is not the
finite tensor-product transition and has no authority unless derived as the
exact Poisson incidence of a finite source object.

## Completion-created transversality

The situation is therefore structurally identical to

\[
 \mathbb C\xrightarrow{\varepsilon_X}\mathbb C,
 \qquad \varepsilon_X\ne0,
 \qquad \varepsilon_X\to0.
\]

Every finite map is invertible, yet its inverse can escape and the limit can
acquire a kernel.  Here the finite Euler transitions and reciprocal pairings
remain exact, while the infinite restricted-product completion may fail to
preserve strict invertibility of the distinguished Poisson-sewn section.

This explains why a finite-cutoff residual census cannot prove RH even when
every typed residual vanishes:

\[
 \boxed{
 \text{finite coherence controls provenance;}
 \quad
 \text{uniform completion controls the divisor}.}
\]

## Exact remaining theorems

Let `sigma_S(s)` be the distinguished, source-derived section in its finite
boundary-bearing normal form, and let `sigma(s)` be the restricted-product
completion.  The required open-sector transport theorem is not merely

\[
 \sigma_S(s)\ne0
 \quad\text{for every finite }S.
\]

It is local uniform strictness on every compact `K` in either open half-plane:

\[
 \boxed{
 \inf_{s\in K}\|\sigma_S(s)^{-1}\|^{-1}
 \not\longrightarrow0}
\]

in the source-derived relative line/graph topology, or an equivalent
completion-stable contracting homotopy.

The pointwise scalar modulus of a chosen Euler trivialization is not an
invariant substitute for this statement.

This transport theorem is necessary but not sufficient for the scalar
readout. Even an injective or unitary correspondence can have a vanishing
matrix coefficient:

\[
 T=1_{\mathbb C^2},
 \qquad
 \psi=e_1,
 \qquad
 \ell=e_2^*,
 \qquad
 \ell(T\psi)=0.
\]

Therefore the remaining gate is irreducibly two-part:

1. completion-stable injectivity/no escape for the operator correspondence;
2. source-derived transversality of the distinguished detector pairing.

Only a separately proved determinant--kernel bridge can collapse these into
one theorem.

## Falsifier and scope

A compatible sequence of normalized finite source states `v_S` satisfying

\[
 \|v_S\|=1,
 \qquad
 \|\sigma_S(s)v_S\|\longrightarrow0
\]

at one fixed off-seam `s` is the completion falsifier.  High spectral height
without fixed `s`, or decay caused only by changing scalar trivializations,
does not suffice.

The packet proves exact finite tensor descent and absence of a nontrivial
finite-product divisor. It proves neither uniform strictness of the completed
operator correspondence nor transversality of its distinguished scalar
detector. These are the two RH-bearing gates.
