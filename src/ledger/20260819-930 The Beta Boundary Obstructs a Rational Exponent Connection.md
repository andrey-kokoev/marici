# 930 — The Beta Boundary Obstructs a Rational Exponent Connection

## Finite falsifier

Entry 929 identified the logarithmic insertion missing from the frozen
six-word packet. Before enlarging the full six-point system, restrict to the
source-normalized Euler boundary already present in Entry 891. One factor of
that period is

\[
B(a,e)=\frac{\Gamma(a)\Gamma(e)}{\Gamma(a+e)}.
\]

If its rank-one line carried a rational connection in the exponent direction,
then

\[
\partial_a B(a,e)=\omega_a(a,e)B(a,e)
\]

for some \(\omega_a\in\mathbf Q(a,e)\). Necessarily,

\[
\omega_a=\partial_a\log B
=\psi(a)-\psi(a+e).
\]

## Pole obstruction

Specialize to the generic nonintegral slice \(e=\tfrac12\). The first
digamma term has poles at

\[
a=0,-1,-2,\ldots,
\]

while the second has poles at

\[
a=-\tfrac12,-\tfrac32,-\tfrac52,\ldots.
\]

The two infinite progressions are disjoint, so they cannot cancel. A rational
function of \(a\) has only finitely many poles. Therefore

\[
\boxed{
\psi(a)-\psi(a+\tfrac12)\notin\mathbf Q(a)
}
\]

and the canonical beta boundary line has no rational exponent connection.

## Consequence for six points

Any source-derived six-point connection compatible with boundary residue
would induce the boundary connection above. Hence the missing six-point
parameter transport cannot be a rational \(6\times6\) correction within
the existing word frame alone.

The obstruction is coefficient-theoretic:

\[
\boxed{
\text{Koba--Nielsen exponent transport}
\text{ requires a digamma/logarithmic parameter extension}.
}
\]

It does not require a new carrier cell. It also does not say that all
finite-dimensional descriptions are impossible after adjoining the correct
parameter-difference or unipotent structure; it excludes the proposed
rational differential connection in the frozen frame.

## Surviving hypothesis

The rank-two normal-symbol module of Entries 925--928 is an associated-grade
object over monodromy coordinates. Promoting it to a horizontal object
requires a coefficient category that remembers exponent variation, rather
than an ambient rational connection inferred from KLT transition matrices.

## Next falsifier

Replace differential transport in the exponent by the source gamma-shift
operation

\[
B(a+1,e)=\frac{a}{a+e}B(a,e).
\]

Test whether the six-point normal-symbol line is preserved by the corresponding
integer monodromy-coordinate shift. This is rational and source-derived, so it
is the smallest admissible transport structure after the differential no-go.

## Durable verification

- checker:
  research/benincasa/marici-gm/src/bin/string_beta_parameter_connection_gate.rs;
- packet:
  research/benincasa/string-beta-parameter-connection-gate.json;
- allocator claim:
  seqclaim-dd46d12abb827e72b16e1268.
- epistemic event:
  ev-000000000547-8f87d83a-eb58-40c4-8ea1-68f46667a281.
