# Higher-coherence topology iteration 02: strict LF/bornological totalization cannot send a fixed-prime residual to infinity

## Candidate topology

Let `C_N` be the finite coherence system through rung or support depth `N`, and
use injective structure maps

\[
i_N:C_N\hookrightarrow C_{N+1}.
\]

Form the strict locally convex inductive limit

\[
C_{\rm LF}=\underset{N}{\operatorname{ind\,lim}}\,C_N.
\]

Equivalently, use the associated regular bornology: a set is bounded only if
it is contained and bounded in some finite stage. This is the natural topology
for compact-support form cores and finite cone packages.

## What “escape to infinity” can mean

A sequence `x_N in C_N` whose support or coherence degree tends to infinity may
converge weakly to zero under observers supported in fixed finite regions. This
is genuine escape to infinity.

But an element `x in C_N` already living in one fixed stage does not move when
viewed in later stages. Strictness means every inclusion is a topological
embedding. Hence

\[
i_{N,\infty}(x)=0
\quad\Longleftrightarrow\quad
x=0.
\]

A fixed-prime residual is of this second kind, not the first.

## Haar residual

Choose `N_p` containing prime `p` and the required endpoint/reciprocal packet.
Then

\[
r_p(z)
=
\bigl(1-p^{-2\operatorname{Re}z}\bigr)E_p(b_z)
\in C_{N_p}.
\]

Every later simplex/prism/cone stage contains its unchanged image. Therefore
it cannot escape by increasing coherence degree:

\[
i_{N_p,\infty}(r_p(z))=0
\quad\Longleftrightarrow\quad
r_p(z)=0.
\]

The same conclusion holds for a continuous scalar readout. By the universal
property of the strict inductive limit, a compatible family
`ell_N:C_N->C` defines a continuous `ell:C_LF->C`, and

\[
\ell(i_{N_p,\infty}r_p)=\ell_{N_p}(r_p).
\]

## Compact-support arithmetic clue

The strict support limit has an additional rigidity: for a vector supported in
`[-L,L]`, only prime powers with `log n<=2L` contribute. Arithmetic cutoff
convergence is eventual equality, not asymptotic cancellation. Once a
fixed-support residual is present, adding farther prime shells cannot alter it
on that test vector.

Thus the topology preserves precisely the signed finite arithmetic information
that the confinement argument needs; it does not wash it into a tail.

## Bornological alternatives

One could choose a nonregular bornology in which bounded sets spread through
infinitely many stages, or nonembedding transition maps that shrink old
coordinates. Then a finite residual could approach zero. But this has one of
two costs:

1. the fixed endpoint/Haar observer is no longer continuous; or
2. a nonzero finite source coordinate is identified with zero.

Either destroys the faithful retained graph and cannot support the required
positive noncollapse theorem.

## Verdict for topology 2

Strict LF/bornological completion is useful for:

- finite-support arithmetic stabilization;
- local cone packages of unbounded coherence degree;
- avoiding unnecessary absolute prime majorants;
- preserving every sourced finite packet faithfully.

It cannot absorb a residual already detected at one fixed prime. “Escape to
infinity” applies only to moving-support families, not to the persistent image
of a fixed-stage class.

The next nonredundant topology to test is a quotient or derived-limit topology
in which residuals are killed modulo an asymptotic/null ideal. Such a topology
might absorb finite representatives, but must be checked against positivity and
faithfulness.