# The causal large-parameter asymptotic proves the relative return determinant is nonconstant

On the positive-real causal chart, let `A` be the history semigroup generator
and

\[
R(s)=B^\dagger(s-A)^{-1}B.
\]

The standard resolvent approximation gives

\[
s(s-A)^{-1}\longrightarrow I
\]

strongly as `s -> +infinity`, uniformly bounded on that ray.  Since `B` is
Hilbert--Schmidt, sandwiching upgrades this to trace-norm convergence:

\[
sR(s)\longrightarrow B^\dagger B
\qquad\text{in }\mathcal S_1.
\]

The diagonal Euler loop satisfies `L(s)->0`, so

\[
(I-L(s))^{-1}\longrightarrow I
\]

in operator norm. Hence

\[
sK(s)=s(I-L(s))^{-1}R(s)
\longrightarrow B^\dagger B
\qquad\text{in }\mathcal S_1.
\]

Fredholm determinant expansion at the identity yields

\[
\det_F(I-K(s))
=1-\frac{\operatorname{Tr}(B^\dagger B)}s+o(s^{-1})
=1-\frac{\|B\|_2^2}s+o(s^{-1}).
\]

The completed incidence is nonzero, so `||B||_2^2>0`. Therefore the relative
return determinant is not identically one and cannot be discarded as a
trivial normalization.

This does not decide whether the determinant is nowhere zero on a chosen open
chart, nor whether another independently sourced factor cancels it. It rules
out the simplest proposed comparison in which the coupled determinant equals
the already matched bare Euler target with no additional factor.
