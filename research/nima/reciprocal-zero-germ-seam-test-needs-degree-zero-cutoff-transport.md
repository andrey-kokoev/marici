# The Reciprocal Zero-Germ Test Needs Degree-Zero Cutoff Transport

## Exact comparator

The direct and reciprocal Euler–Maclaurin boundary germs at a common cutoff
are

\[
C_s(N)=\frac{N^{1-s}}{1-s},
\qquad
C_{1-s}(N)=\frac{N^s}{s}.
\]

Their forced comparator has logarithmic growth rate

\[
\chi(s)=1-2\operatorname{Re}s.
\]

Uniform invertibility therefore selects the critical seam.

## Regrading falsifier

The conclusion is not invariant under arbitrary identification of cutoff
scales. If the reciprocal germ is evaluated at \(M=N^\alpha\), then

\[
\frac{C_s(N)}{C_{1-s}(M)}
=
\frac{s}{1-s}N^{1-s-\alpha s},
\]

and its modulus has growth rate

\[
\chi_\alpha(s)=1-(1+\alpha)\operatorname{Re}s.
\]

For every \(0<\operatorname{Re}s<1\), choosing

\[
\alpha=\frac{1-\operatorname{Re}s}{\operatorname{Re}s}
\]

makes the comparator neutral. Thus an unrestricted change of filtration can
manufacture reversible sewing at any horizontal position.

The seam theorem survives bounded multiplicative cutoff distortion
\(M/N\asymp1\), because such distortion changes only the bounded prefactor.
It does not survive a power regrading.

## Categorical statement

The boundary germs form filtered objects. The required sewing is not merely
an isomorphism of their unfiltered completions. It must be a degree-zero
filtered isomorphism whose inverse is also degree zero, and it must preserve
the nonzero leading Euler class.

Equivalently, the source square must compare the two germs over one common
scale object. Allowing an independent endofunctor on either scale leg changes
the theorem.

## Source audit

Poisson reciprocity exchanges a scale with its reciprocal. That alone does
not yet prove the needed condition. The audit must identify one source scale
parameter before Mellin projection and show that both Euler boundary germs
are induced from it with the same filtration degree. A scalar functional
equation, equality of finite parts, or an unfiltered determinant-line
isomorphism is insufficient.

The exact pass conditions are:

1. one common cutoff object is constructed from the source;
2. direct and reciprocal boundary maps are degree-one in that object;
3. sewing is natural over the identity of the cutoff object, up to bounded
   multiplicative distortion;
4. the leading Euler class survives completion;
5. the sewing and its inverse are uniformly bounded in the boundary topology.

## Decisive interpretation

The current construction has found a valid conditional confinement
mechanism. Its content is reversible comparison at fixed filtration, not
reciprocity by itself. The remaining theorem is exactly the source authority
for that fixed filtration.

