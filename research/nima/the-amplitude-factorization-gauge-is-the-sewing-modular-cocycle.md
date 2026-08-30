# The amplitude-factorization gauge is the sewing modular cocycle

The paired pole condition leaves

\[
c_P(a)=c_0(a)e^{\phi(a)},
\qquad
c_Q(1-a)=c_0(a)e^{-\phi(a)}.
\]

This relative gauge is not an arbitrary new parameter once the reciprocal
sewing arrow is included.

Let

\[
S_a:P_a\longrightarrow Q_{1-a}
\]

be the source-authorized sewing map between the one-dimensional amplitude
lines, and let its positive metric modulus be \(s(a)>0\). Compatibility of
the represented endpoint amplitudes requires

\[
c_Q(1-a)=s(a)c_P(a).
\]

Combining this with the pole product gives

\[
c_P(a)=c_0(a)s(a)^{-1/2},
\qquad
c_Q(1-a)=c_0(a)s(a)^{1/2}.
\]

Therefore

\[
\phi(a)=-\frac12\log s(a).
\]

The factorization gauge is exactly half the logarithmic modular cocycle of
reciprocal sewing.

## Involution and dagger gates

If reciprocal sewing is involutive,

\[
S_{1-a}S_a=I,
\]

then its modulus satisfies

\[
s(1-a)s(a)=1.
\]

Hence

\[
\log s(1-a)=-\log s(a),
\]

so the relative gauge has the required reciprocal parity. Involution alone
does not imply \(s=1\).

If sewing is unitary in the source metric, then

\[
s(a)=1
\]

and the reciprocal-even square-root frame is forced:

\[
c_P(a)=c_Q(1-a)=c_0(a).
\]

Thus the missing authority condition from event 10272 is not merely
“reflection symmetry.” It is source metric unitarity of the sewing line.

## Completion criterion

The individual amplitudes are uniformly bi-bounded exactly when the sewing
modulus is:

\[
0<\inf_a s(a)\le\sup_a s(a)<\infty.
\]

Equivalently,

\[
\sup_a|\log s(a)|<\infty.
\]

A cutoff family can satisfy the involution law at every finite stage while
failing completion: choose \(s_X(a_X)\to\infty\) and enforce
\(s_X(1-a_X)=s_X(a_X)^{-1}\). The paired pole remains exact, but one endpoint
amplitude blows up and the other collapses.

The connection splitting is likewise sourced:

\[
d\log c_P=d\log c_0-\frac12d\log s,
\]

\[
d\log c_Q=d\log c_0+\frac12d\log s
\]

after reciprocal pullback. The common connection is fixed by the pole metric;
the relative connection is the sewing modular connection.

## Consequence

The next source audit has become a one-dimensional metric test:

1. construct the reciprocal sewing arrow \(S_a\);
2. compute its modulus \(s(a)\) in the source-fixed endpoint metrics;
3. prove involution and dagger compatibility;
4. determine whether \(s=1\), or at least whether \(s\) is uniformly
   bi-bounded.

This is the determinant modular cocycle from the earlier holonomy programme,
now appearing concretely on the first Euler–theta amplitude line.
