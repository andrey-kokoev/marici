# Mixed-boundary surface codes lose exactly one absolute logical rank

Owner: `marici.Kitaev`

## Bounded question

For a connected orientable genus-\(g\) surface with \(b\) boundary components,
how does an arbitrary nontrivial partition into rough and smooth boundary
components change the primal and dual logical ranks?

## Relative groups

Let \(R\) be the union of \(r\) rough boundary circles and \(S\) the union of
\(s=b-r\) smooth boundary circles. Assume \(r,s>0\). The primal and dual
logical spaces are

\[
H_1(\Sigma,R;\mathbf F_2),
\qquad
H_1(\Sigma,S;\mathbf F_2).
\]

The absolute group has dimension

\[
\dim H_1(\Sigma;\mathbf F_2)=2g+b-1.
\]

## Long-exact-sequence calculation

For a proper nonempty union \(R\) of boundary components, the map

\[
H_1(R)\longrightarrow H_1(\Sigma)
\]

has rank \(r\). The boundary components have one global relation, but because
at least one smooth component is omitted, no relation is supported entirely
on \(R\).

The kernel of

\[
H_0(R)\longrightarrow H_0(\Sigma)
\]

has dimension \(r-1\). Exactness therefore gives

\[
\dim H_1(\Sigma,R)
=(2g+b-1)-r+(r-1)
=2g+b-2.
\]

Exchanging \(R\) and \(S\) gives the same dual rank. Poincare--Lefschetz
duality supplies a perfect mod-two intersection pairing

\[
H_1(\Sigma,R)\times H_1(\Sigma,S)\longrightarrow\mathbf F_2.
\]

Thus the code encodes

\[
k=2g+b-2
\]

qubits whenever both boundary types occur.

## The compensating relative arcs

It is incorrect to subtract one logical generator for every rough boundary.
After the first rough component kills one absolute boundary-loop direction,
each additional rough component contributes a new relative arc class through
the \((r-1)\)-dimensional reduced \(H_0(R)\) term. The rank is therefore
independent of the size of the nontrivial partition.

For a planar pair of pants, \(g=0,b=3\), either a one-versus-two or a
two-versus-one partition encodes one qubit. The representatives change from
loop-like to arc-like under boundary exchange, but the paired logical rank
does not.

For the mixed annulus, \(g=0,b=2,r=s=1\), the rank is zero, recovering the
earlier hostile-boundary result.

## Endpoint cases

If \(R=\varnothing\), the primal group is absolute and has rank \(2g+b-1\).
If \(R=\partial\Sigma\), the inclusion rank drops to \(b-1\), while the
reduced \(H_0\) contribution has rank \(b-1\); the relative group again has
rank \(2g+b-1\). Hence the one-rank loss occurs only for a genuinely mixed
partition.

## Shared versus quantum structure

Carrier geometry supplies the relative quotient, long exact sequence,
boundary-component relation, and intersection pairing. The quantum
coefficient lens converts odd intersection into Pauli anticommutation and
identifies the paired relative groups as logical \(Z\)- and \(X\)-operator
spaces. Boundary labels remain source data; topology alone does not decide
which components condense which excitation.

## Falsifiers

- a proper boundary subset whose circle classes have inclusion rank below its
  number of components;
- failure of the reduced \(H_0(R)\) term to restore \(r-1\) arc classes;
- unequal primal and dual ranks for a complementary partition;
- a degenerate relative intersection pairing;
- applying the mixed formula when one boundary type is absent.

## Disposition

The general mixed-boundary family is classified at finite topological
strength. Boundary condensation removes exactly one absolute logical rank,
not one rank per condensing component. Additional components replace killed
loop coordinates by relative arc coordinates.

## Claim strength

Exact finite topological theorem over \(\mathbf F_2\). No lattice-distance,
Hamiltonian-gap, or perturbative-stability claim is made.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_mixed_boundary_relative_rank.py`.
The result is written to
`research/kitaev/results/mixed-boundary-relative-rank.json`.

