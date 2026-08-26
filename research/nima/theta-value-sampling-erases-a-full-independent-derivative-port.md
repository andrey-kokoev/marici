# Theta value sampling erases a full independent derivative port

## Status

Exact sampling-quotient theorem. Compression from first lattice jets to lattice
values does not discard one scalar correction. It erases an entire independent
rapidly decreasing derivative sequence.

Consequently a derivative-comb residual has no canonical sign, phase, or
orientation on the full Schwartz source. It becomes meaningful only after a
source-derived restriction couples derivative samples to value samples.

## Value and first-jet sampling

Let \(\mathcal S(\mathbb R)\) be the Schwartz space and let
\(s(\mathbb Z)\) be the rapidly decreasing sequence space. Define

\[
S_0f=(f(n))_{n\in\mathbb Z}
\]

and

\[
S_1f=((f(n),f'(n)))_{n\in\mathbb Z}.
\]

The value-forgetting projection is

\[
\pi:s(\mathbb Z)\oplus s(\mathbb Z)
\longrightarrow s(\mathbb Z),
\qquad
\pi(v,d)=v.
\]

It satisfies

\[
S_0=\pi S_1.
\]

## Surjectivity of the derivative defect

Choose a smooth compactly supported function \(\psi\) with support contained in
\((-1/3,1/3)\) and

\[
\psi(0)=0,
\qquad
\psi'(0)=1.
\]

For any rapidly decreasing sequence (d=(d_n)\), define

\[
h_d(x)=\sum_{n\in\mathbb Z}d_n\psi(x-n).
\]

The supports are disjoint, and rapid decay of (d_n\) implies

\[
h_d\in\mathcal S(\mathbb R).
\]

At every integer (m\),

\[
h_d(m)=0,
\qquad
h_d'(m)=d_m.
\]

Therefore the map

\[
D:\ker S_0\longrightarrow s(\mathbb Z),
\qquad
Dh=(h'(n))_n
\]

is surjective.

Value sampling erases the full derivative port (s(\mathbb Z)\).

## Full first-jet interpolation

Choose another compactly supported smooth function \(\varphi\), with the same
small support, satisfying

\[
\varphi(0)=1,
\qquad
\varphi'(0)=0.
\]

For arbitrary rapidly decreasing sequences (v=(v_n)\) and (d=(d_n)\), the
function

\[
f_{v,d}(x)
=\sum_n[v_n\varphi(x-n)+d_n\psi(x-n)]
\]

is Schwartz and satisfies

\[
f_{v,d}(n)=v_n,
\qquad
f_{v,d}'(n)=d_n.
\]

Hence first-jet sampling is surjective onto

\[
s(\mathbb Z)\oplus s(\mathbb Z).
\]

The derivative sequence is not constrained by the value sequence on the full
source space.

## Exact quotient picture

At the sampled boundary, forgetting derivatives gives the split sequence of
vector spaces

\[
0
\longrightarrow
s(\mathbb Z)
\overset{d\mapsto(0,d)}{\longrightarrow}
s(\mathbb Z)\oplus s(\mathbb Z)
\overset{\pi}{\longrightarrow}
s(\mathbb Z)
\longrightarrow0.
\]

Many algebraic splittings exist, such as (v\mapsto(v,0)\), but no splitting is
selected by value sampling itself. A rule (d=Kv\) is additional structure.

## Consequence for the annihilator

The sampled annihilation readout is

\[
(S_0af)_n=f'(n)+2\pi nf(n).
\]

For a fixed value sequence (v\), the derivative term can be any element of
\(s(\mathbb Z)\). Therefore the annihilation readout can be varied arbitrarily
without changing the sampled values.

No sign or norm inequality for this residual can descend through (S_0\) on the
full Schwartz source.

## Symmetry does not restore orientation

If the source is even, its derivative sequence is odd:

\[
f'(-n)=-f'(n).
\]

The full symmetric derivative sum then cancels. But on the positive half-line,
the remaining derivative sequence is still freely variable within the
corresponding rapidly decreasing odd extension.

Parity removes the total odd current; it does not select the sign of the
one-sided boundary port.

## Restricted-source escape hatch

A derivative adapter can become canonical on a strict source-generated
subspace \(\mathcal V\subset\mathcal S(\mathbb R)\) if value sampling is
injective there and the map

\[
S_0f\longmapsto(f'(n))_n
\]

is continuous in the admitted topology.

Examples might include a bandlimited space, a Gaussian shift-invariant space,
or the completed labelled theta-vacuum module. None is authorized merely by
the ambient Schwartz structure.

The required theorem is a bounded graph relation

\[
D_{\mathcal V}S_0f=(f'(n))_n
\]

derived from the source constructors. Its kernel and completion stability must
be checked explicitly.

## Finite falsifier

Take one bump (h=\psi(\,cdot-n_0)\). Then

\[
S_0h=0,
\]

while its derivative sample is the unit sequence at (n_0\). Scaling or taking
finite sums gives arbitrary finite derivative defects with identical zero value
samples.

This kills any proposed value-only derivative adapter before completion.

## Consequence

The first lossy Poisson crossing has now been measured exactly. Its defect is
too unconstrained to orient RH on the ambient source. The next admissible move
is not to assign a sign to the derivative-comb current, but to prove that the
actual labelled Gaussian/comb module carries a source-authorized continuous
jet adapter. Failure of such an adapter closes this boundary-current branch.
