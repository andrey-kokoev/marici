# Krylov Cyclicity Is Weaker Than Witness Equivalence

## Question

Which transformations of a three-dimensional cyclic pair \((A,x)\) preserve
only its Krylov rank, and which preserve the full Marici witness consisting of
the staged history, ordered ports, volume reference, and lineage?

Write

\[
K(A,x)=[x,Ax,A^2x],
\qquad
\Omega_A(x)=\det K(A,x).
\]

## Algebraic transformation census

Simultaneous similarity gives

\[
(A,x)\mapsto(SAS^{-1},Sx),
\qquad
K\mapsto SK,
\qquad
\Omega\mapsto\det(S)\Omega.
\]

It preserves cyclicity. It preserves a signed readout only when the volume
reference is transported by the inverse determinant character, or when the
admitted subgroup has determinant one.

Seed rescaling gives

\[
x\mapsto\lambda x,
\qquad
\Omega\mapsto\lambda^3\Omega.
\]

Thus cyclicity descends to the seed ray, while an unreferenced phase or sign
does not. A reference \(\rho\) of weight minus three makes
\(\rho\Omega\) invariant under the simultaneous transformation
\(\rho\mapsto\lambda^{-3}\rho\).

For an affine reparameterization of the evolution,

\[
A\mapsto \alpha A+\beta I,
\qquad \alpha\ne0,
\]

the new Krylov columns are obtained from the old ones by an upper-triangular
matrix with diagonal \((1,\alpha,\alpha^2)\). Hence

\[
\Omega_{\alpha A+\beta I}(x)=\alpha^3\Omega_A(x).
\]

This preserves the Krylov flag, but it does not by itself preserve the
physical evolution agent. Implementing the affine transformation requires an
identity bypass, weighted addition, and a new lineage declaration.

The genuinely control-theoretic symmetry is single-input state feedback:

\[
A\mapsto A+xf,
\]

where \(f\) is a covector. The new Krylov columns differ by a unit
upper-triangular recombination, so

\[
\Omega_{A+xf}(x)=\Omega_A(x).
\]

This is exact controllability equivalence. It is still not automatically a
Marici witness equivalence: a physical implementation must supply the
feedback evaluation, retain or regenerate the seed channel, and record the
new closed-loop lineage.

Finally, replacing the seed by \(q(A)x\) gives

\[
K(A,q(A)x)=q(A)K(A,x),
\qquad
\Omega_A(q(A)x)=\det(q(A))\Omega_A(x).
\]

It preserves cyclicity exactly when \(q(A)\) is invertible on the cyclic
module. A polynomial reparameterization \(A\mapsto p(A)\) is not generally
safe: it can merge distinct spectral responses. On a simple-spectrum
diagonalizable carrier, cyclicity requires \(p\) to remain injective on the
three spectral points. Affine maps with nonzero slope satisfy this
universally; a nonlinear polynomial need not.

## Preservation lattice

The transformations therefore fall through five increasingly strict gates:

1. **rank gate** — the transformed pair remains cyclic;
2. **history gate** — one seed, two admitted evolution steps, and two retained
   snapshots still construct the three ordered ports;
3. **projective gate** — the descended magnitude is unchanged or transported
   with its declared normalization;
4. **reference gate** — the volume wire transforms contragrediently, making
   the signed comparison invariant;
5. **lineage gate** — early and late records still map to the same preparation,
   epoch, and messenger path.

Passing an earlier gate does not imply passing a later one. In particular,
controllability equivalence is weaker than capability-witness equivalence.

## Observer interpretation

Nima's signed-character rank is the discrete analogue of observability rank
for a dynamically constructed output family. An output character contributes
only after its frame exists. The surviving indistinguishability is the
intersection of the kernels of the admitted stage outputs, restricted to one
lineage fiber. Rank computed after erasing construction stage or lineage is
not an observability theorem for the physical process.

Terminal reconciliation is therefore data association before estimation. The
pullback over lineage removes cross-run pairings; no estimator can reconstruct
an intermediate sign or association that the record constructor deleted.

## Exact hostile and status

The checker verifies similarity covariance, cubic seed and affine weights,
exact feedback invariance, polynomial spectral collapse, seed-filter
invertibility, referenced phase cancellation, and the difference between a
Cartesian join and a lineage pullback.

This is a finite exact control classification. It does not establish that a
Flavor source supplies the feedback channel, affine bypass, history store, or
volume reference. Those are Carrier constructors and must be derived rather
than inferred from preservation of Krylov rank.

