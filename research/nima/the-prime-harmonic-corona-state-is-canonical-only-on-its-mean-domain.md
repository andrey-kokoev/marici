# The Prime-Harmonic Corona State Is Canonical Only on Its Mean Domain

## Source-derived cutoff states

Let

\[
H_X=\sum_{p\le X}\frac1p
\]

and define the normalized prime-harmonic functional

\[
\omega_X(f)=\frac1{H_X}\sum_{p\le X}\frac{f(p)}p
\]

for bounded labelled observables \(f\). Each \(\omega_X\) is positive, unital,
and has norm one. It is exactly the state carried by the normalized Euler
cutoff from the two-port completion audit.

Define the mean domain

\[
\mathcal A_{\mathrm{ph}}
=
\{f\in\ell^\infty(\mathbb P):
\exists L\in\mathbb C,\ \lim_X\omega_X(f)=L\}.
\]

This domain is a norm-closed unital self-adjoint linear subspace of
\(\ell^\infty(\mathbb P)\). On this operator system,

\[
\omega_\infty(f)=\lim_X\omega_X(f)
\]

is a canonical positive unital functional. It is source-derived because both
the weights and cutoff order come from the Euler labels.

Every finitely supported observable has value zero at the corona. More
generally, every observable vanishing at infinity belongs to the kernel:

\[
c_0(\mathbb P)\subseteq\ker\omega_\infty.
\]

Thus the state factors through the prime-label corona operator system on its
admitted domain. It retains the trace-one mass that every fixed finite label
port loses.

## The mean domain is not a multiplication algebra

Multiplicative closure does not follow from convergence of individual means.
This can be seen for the prime weights themselves.

Choose consecutive prime blocks whose harmonic weights alternately dominate
all preceding weight. Let \(h\) equal \(+1\) and \(-1\) on alternating blocks.
Its normalized means oscillate, so \(h\notin\mathcal A_{\mathrm{ph}}\).

Now choose a rapidly alternating sign sequence \(f\). Block boundaries may be
placed far enough apart that the reciprocal of the first prime in block \(k\)
is at most \(2^{-k}\). The alternating-series estimate then bounds the signed
harmonic sum of \(f\) on each block by \(2^{-k}\). It follows that both \(f\)
and \(g=hf\) have prime-harmonic mean zero. Nevertheless,

\[
fg=h,
\]

whose mean does not exist. Therefore

\[
f,g\in\mathcal A_{\mathrm{ph}},
\qquad
fg\notin\mathcal A_{\mathrm{ph}}.
\]

Calling the domain an algebra would silently authorize a multiplication
constructor that the cutoff limit does not preserve.

## Why the domain cannot be all bounded observables

The prime harmonic series diverges. This permits consecutive prime blocks
whose harmonic weight is arbitrarily larger than the total weight of all
earlier blocks.

Choose alternating blocks and let \(f\) equal one on odd blocks and zero on
even blocks. If the new block has weight at least \(k\) times all preceding
weight, then at the end of an odd block,

\[
\omega_X(f)\ge\frac{k}{k+1},
\]

while at the end of an even block,

\[
\omega_X(f)\le\frac1{k+1}.
\]

Taking \(k\) successively larger makes the cutoff means oscillate between
values approaching one and zero. Hence \(f\) is bounded but does not belong to
\(\mathcal A_{\mathrm{ph}}\).

There is no canonical state on all of \(\ell^\infty(\mathbb P)\) determined
by the cutoff net alone. A global extension exists by functional-analytic
choice, but selecting one amounts to choosing a generalized limit or
ultrafilter. Transporting that choice into the source would manufacture
boundary authority.

## Categorical consequence

The corona port is a partial observer on an operator system, not a total
scalar readout or a multiplicative character:

\[
\omega_\infty:
\mathcal A_{\mathrm{ph}}
\longrightarrow
\mathbb C.
\]

Its domain is part of its type. Forgetting the domain and retaining only the
codomain falsely turns a source-defined filtered state into an arbitrary
state on the full Stone--Čech corona.

The completion architecture now has three distinct layers:

1. finite labelled diagonal and Mellin off-diagonal tomography;
2. \(B^2\) completion for square-summable packets;
3. the prime-harmonic corona state on its mean domain for the Euler vacuum.

The third layer repairs escaped total mass but does not recover arbitrary
label-sensitive boundary data. Any further boundary orientation must be
defined on an explicitly admitted subalgebra and shown independent of
unauthorized generalized-limit choices.

## Falsifier

The alternating-block observable is the finite-construction falsifier for any
claim that normalized prime-harmonic cutoff evaluation converges on every
bounded label observable. At dominance factor \(k\), its two endpoint bounds
are \(k/(k+1)\) and \(1/(k+1)\); their gap tends to one.
