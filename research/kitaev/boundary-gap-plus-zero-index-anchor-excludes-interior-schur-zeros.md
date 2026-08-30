# Boundary gap plus a zero-index anchor excludes interior Schur zeros

## Question

What operator-valued Hardy certificate excludes zeros inside a parameter
domain, rather than merely detecting their germs?

## Boundary invertibility is not enough

Let \(\Omega\) be a bounded parameter domain with positively oriented
boundary \(\Gamma\), and let \(S(z)\) be an analytic finite-dimensional
Schur-complement family.

Even if \(S(z)\) is uniformly invertible on \(\Gamma\), it may be singular
inside. The scalar family

\[
S(z)=z
\]

is invertible with unit boundary margin on the unit circle and has one
interior zero.

Thus neither a boundary Hardy norm nor a boundary inverse bound determines
interior invertibility by itself.

## Exact finite-dimensional index

Assume \(S(z)\) is invertible on \(\Gamma\). The number of interior zeros of
\(\det S\), counted with algebraic multiplicity, is

\[
\nu_\Omega(S)
=
\frac{1}{2\pi i}
\int_\Gamma
\operatorname{tr}\bigl(S(z)^{-1}S'(z)\bigr)\,dz.
\]

Equivalently, \(\nu_\Omega(S)\) is the winding number of
\(\det S(\Gamma)\) around zero.

Since \(\det S\) is holomorphic and has no poles, \(S(z)\) is invertible for
every \(z\in\Omega\) exactly when \(\nu_\Omega(S)=0\).

The boundary gap makes the index well-defined and stable. The index decides
whether zeros lie inside.

## Anchor–homotopy theorem

Let \(S_\tau(z)\), \(0\le\tau\le1\), be continuous in \(\tau\), analytic in
\(z\), and invertible on \(\Gamma\) for every \(\tau\). Then

\[
\nu_\Omega(S_\tau)
\]

is constant in \(\tau\).

Consequently, if:

1. \(S_0\) is a source-authorized anchor with no interior zero;
2. \(S_\tau\) is a source-authorized deformation to \(S_1\);
3. the boundary gap never closes along the deformation;

then \(S_1\) has no interior zero.

This is the exact topological route from a known open system to the completed
sewn system.

## Boundary-feedback homotopy

For the theta boundary colligation, the natural candidate is

\[
S_\tau(z)
=
D_z-\tau C_z(I-K_z)^{-1}B_z.
\]

At \(\tau=0\), the boundary feedback is disconnected:

\[
S_0(z)=D_z.
\]

At \(\tau=1\), the physical feedback is closed. If \(D_z\) is zero-free in
\(\Omega\) and the entire homotopy remains invertible on \(\Gamma\), then the
closed system has zero index and hence no zero in \(\Omega\).

Small gain is one sufficient way to preserve the boundary gap:

\[
\left\|
D_z^{-1}C_z(I-K_z)^{-1}B_z
\right\|<1
\]

on \(\Gamma\). It is not necessary. Any source-derived coercive, passive,
or direct spectral certificate preventing a boundary unit loop eigenvalue
for all \(\tau\) suffices.

This makes the topological theorem strictly broader than small gain.

## Why reciprocity is insufficient

Reciprocal covariance may pair zeros or force a symmetry of the index. It
does not force the index to vanish. A reciprocal domain may contain a pair
of zeros and have nonzero even count.

The zero-free anchor supplies the missing absolute reference. Symmetry alone
only relates sectors.

## Completion-stable form

For cutoff families \(S_{\tau,N}\), finite zero indices stabilize only if the
operator families converge in a topology preserving the contour gap.
A sufficient packet on every compact domain is:

1. one fixed contour \(\Gamma\);
2. compact-open operator convergence on \(\Gamma\);
3. a uniform bound

   \[
   \sup_{\tau,N,z\in\Gamma}
   \|S_{\tau,N}(z)^{-1}\|<\infty;
   \]

4. convergence in an operator ideal strong enough to pass the selected
   regularized determinant or Fredholm index;
5. a fixed source-authorized homotopy, not cutoff-dependent repairs.

Without the uniform gap, zeros can cross the contour or appear through
singular completion even when every finite stage has the same index.

## Analytic Fredholm extension

For an analytic Fredholm family with determinant-class perturbation, the
finite winding number is replaced by the analytic Fredholm multiplicity or
the winding of the appropriate regularized determinant. The same architecture
survives:

- invertibility on the contour;
- a stable Fredholm index;
- homotopy to a zero-free anchor;
- operator-ideal continuity through completion.

A regularized scalar determinant may compute the index only after the
operator family and its ideal class have been independently established.

## Three distinct thresholds

The boundary programme now has three logically independent gates:

1. observation: the operator jet changes when the realization changes;
2. robustness: the contour has a uniform least-singular-value margin;
3. exclusion: the enclosed analytic Fredholm index is zero.

Aspect's optical hierarchy has the same form: nonzero relational visibility
is weaker than crossing the quantitative nonlocality threshold. Here,
operator sensitivity is weaker than a gap, and a gap is weaker than a
zero-index conclusion unless an anchor fixes the enclosed count.

## Hostile fixtures

### Gap with nonzero winding

\[
S(z)=z
\]

on the unit disk has boundary gap one and index one.

### Zero index without a gap

A contour passing through a zero has no defined winding certificate, even if
a formal signed count cancels elsewhere.

### Cutoffwise homotopies with collapsing gaps

Each cutoff can remain invertible on its contour while the smallest boundary
singular value tends to zero. The limiting index is then not protected.

### Unauthorized anchor

Choosing a convenient \(D_z\) or feedback scaling not derived from the source
does not transport authority to the physical colligation.

### Symmetric nonzero count

A reciprocal pair of interior zeros obeys the symmetry while falsifying
zero exclusion.

## Disposition

The strongest current abstract route is no longer a pointwise inequality.
It is an anchor–homotopy–gap certificate:

1. derive the decoupled boundary anchor;
2. derive the physical feedback homotopy;
3. prove a uniform contour gap;
4. transport the zero index from the anchor;
5. pass the index through operator-ideal completion.

This localizes the remaining hard theorem to the contour behavior of the
source-derived boundary loop. Interior scalar zeros need not be attacked one
at a time.

## Claim boundary

This packet proves the finite analytic theorem and states its Fredholm
extension requirements. It does not derive the theta boundary homotopy,
establish a contour gap, or identify the completed operator ideal.
