# Finite Prime Translations Commute on the Mellin Wall Jet

## Bounded question

Does retaining the regular-plus-polar Mellin carrier reveal a finite
two-prime commutator hidden by scalar Euler multiplication?

The answer is no. The intermediate boundary packets depend on route order,
but canonical resegmentation identifies them. The full wall Taylor jet obeys
the same exact cocycle at every order.

## Translation and wall jet

Let $T_\ell$ translate an analytic source germ:

\[
(T_\ell f)(y)=f(y+\ell).
\]

For every nonnegative integer $n$, define the wall-jet increment

\[
\Delta_\ell^{(n)}f
=f^{(n)}(\ell)-f^{(n)}(0).
\]

These increments record the change in the residue coordinate associated with
the $n$th wall Taylor coefficient.

## Two-prime square

For prime lengths $u=\log p$ and $v=\log q$, the route through $u$ then $v$
has wall-jet increment

\[
\Delta_u^{(n)}f
+\Delta_v^{(n)}(T_uf)
=f^{(n)}(u+v)-f^{(n)}(0).
\]

The route through $v$ then $u$ gives the same expression:

\[
\Delta_v^{(n)}f
+\Delta_u^{(n)}(T_vf)
=f^{(n)}(u+v)-f^{(n)}(0).
\]

Therefore the route commutator vanishes for every wall-jet order.

The raw segment decompositions are not equal term by term. One route cuts at
$u$ and the other at $v$. Their equality is mediated by the canonical common
refinement of the interval from $0$ to $u+v$. This refinement is the required
coherence map; scalar endpoint agreement alone would not establish it.

## Mellin interpretation

The residue at the pole $q=-n-1$ is proportional to $f^{(n)}(0)$. Hence the
identity above proves finite two-prime commutation on the complete polar
Taylor tower, not only on the first wall current.

The regular boundary integrals satisfy the same translation cocycle. Thus the
finite regular-plus-polar carrier commutes after source-derived resegmentation.
There is no finite prime-order anomaly to exploit.

## Consequence

The proposed continuation-level commutator attack closes at finite prime
cutoff. A genuine obstruction can occur only if one of the following happens
during completion:

1. the common-refinement maps cease to be continuous;
2. the primitive or square currents leave the admitted topology;
3. the infinite collection of individually trivial squares acquires a
   derived-limit obstruction;
4. regularization forgets the polar tower needed to implement the coherence.

The next useful test is therefore not another finite prime pair. It is whether
the finite resegmentation homotopies are equicontinuous in the completed
regular-plus-polar topology.

## Verification

The checker
`research/grothendieck/checkers/mellin_wall_jet_prime_cocycle.py` verifies the
two-route cancellation independently for jet orders zero through twelve. A
hostile route that omits the transported second segment leaves a nonzero
residual.

