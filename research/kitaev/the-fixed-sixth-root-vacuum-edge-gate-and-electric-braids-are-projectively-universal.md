# The fixed sixth-root vacuum-edge gate and electric braids are projectively universal

Owner: `marici.Kitaev`

## Bounded question

Does the exact fixed gate

\[
Q_A=e^{i\pi P_A/3}
\]

obtained from coherent cube-root phase halving generate only another finite
complex-reflection group, or does its electric-braid orbit give dense qutrit
control?

It gives dense projective control. Two adjacent edge gates already have an
infinite-order product with eigenangle `theta` satisfying

\[
\cos\theta=\frac78.
\]

The three braid-conjugate edge projectors act irreducibly, preserve no system
of three orthogonal lines, and are incompatible with the irreducible real
`SO(3)` form. The connected component of the compact closure is therefore
`SU(3)`. The full closure has six determinant components and projects onto all
of `PU(3)`.

## Claim boundary

The matrix and compact-group argument is exact, conditional on the frozen
qutrit basis, electric braid permutations, and exact injected gate `Q_A`.

The last classification step uses the standard classification of connected
compact subgroups acting irreducibly in complex dimension three: a proper
nonabelian connected irreducible subgroup has the three-dimensional real
`SU(2)` representation, projectively `SO(3)`. Reducible and toral cases are
handled separately in the proof below.

This is a qualitative density theorem. It does not provide an efficient word
compiler, a spectral gap for random walks, or a physical fault threshold. The
measurement-assisted construction of `Q_A` remains conditional on coherent
route and reference primitives.

## Three edge reflections

Use the monomial basis

\[
|q_0\rangle,
\qquad
|q_1\rangle,
\qquad
|q_2\rangle.
\]

For each unordered pair `i,j`, define

\[
|u_{ij}\rangle
=
\frac{|q_i\rangle+|q_j\rangle}{\sqrt2}
\]

and

\[
P_{ij}=|u_{ij}\rangle\langle u_{ij}|.
\]

The native vacuum projector is one `P_ij`, and completed electric braids
permute the three coordinate axes. Hence the fixed injected gate supplies all
three conjugates

\[
Q_{ij}
=
e^{i\pi P_{ij}/3}.
\]

Let

\[
\zeta=e^{i\pi/3},
\qquad
\omega=e^{2\pi i/3}.
\]

Since

\[
\zeta-1=\omega,
\]

projector functional calculus gives

\[
Q_{ij}=I+\omega P_{ij}.
\]

Each gate has eigenvalues

\[
\zeta,
\qquad
1,
\qquad
1
\]

and determinant `zeta`.

## Infinite-order adjacent product

Take two distinct edge lines, for example `u_01` and `u_02`. Their overlap has
magnitude

\[
|\langle u_{01}|u_{02}\rangle|=\frac12.
\]

Let

\[
T=Q_{01}Q_{02}.
\]

The vector orthogonal to both edge lines is fixed by `T`, so one eigenvalue is
one. The trace is

\[
\operatorname{Tr}T
=
3+2\omega
+
\omega^2
\operatorname{Tr}(P_{01}P_{02})
=
3+2\omega+\frac{\omega^2}{4}.
\]

Using

\[
1+\omega=\zeta,
\qquad
\omega^2=-\zeta,
\]

the sum of the remaining two eigenvalues is

\[
\operatorname{Tr}T-1
=
\frac{7\zeta}{4}.
\]

Their product is

\[
\det T=\zeta^2.
\]

Therefore they have the form

\[
\zeta e^{i\theta},
\qquad
\zeta e^{-i\theta},
\]

where

\[
2\zeta\cos\theta
=
\frac{7\zeta}{4}.
\]

Hence

\[
\cos\theta=\frac78.
\]

## Irrationality of the eigenangle

If `theta` were a rational multiple of `2 pi`, then

\[
e^{i\theta}
\]

would be a root of unity. The number

\[
e^{i\theta}+e^{-i\theta}
=
2\cos\theta
=
\frac74
\]

would then be an algebraic integer. A rational algebraic integer is an
integer, but `7/4` is not an integer. This is impossible.

Thus `theta/(2 pi)` is irrational. The adjacent product `T` has infinite
projective order, and the generated compact closure has a nontrivial connected
component.

## Irreducibility

Let `L` be a subspace invariant under all three `Q_ij`. Since

\[
P_{ij}=\omega^{-1}(Q_{ij}-I),
\]

the subspace is invariant under every edge projector. Because the projectors
are Hermitian, its orthogonal complement is also invariant.

Equivalently, inspect the common commutant. If `X` commutes with all three
projectors, each `u_ij` is an eigenvector of `X`. Any two edge states have
nonzero overlap. Commutation with their rank-one projectors forces the
corresponding eigenvalues to agree. Since the three edge states span the
qutrit, `X` is scalar.

The common commutant is therefore

\[
\mathbb C I.
\]

The generated unitary representation is irreducible.

## Excluding an imprimitive torus normalizer

An irreducible disconnected compact group can have a reducible identity
component by permuting a system of orthogonal one-dimensional weight spaces.
That would make the qutrit representation imprimitive.

Suppose three orthogonal lines were permuted by every generator. A unitary
that nontrivially permutes those lines has, on each nontrivial permutation
cycle, eigenvalue ratios forced by a transposition or three-cycle. A
transposition produces a ratio `-1`; a three-cycle produces three distinct
cube-related eigenvalues.

But each `Q_ij` has only the eigenvalue ratio `zeta`, with multiplicities one
and two, and

\[
\zeta\neq-1.
\]

Therefore every `Q_ij` would have to fix all three imprimitivity lines
individually. The three gates would then be simultaneously diagonal and their
rank-one projectors would commute. They do not, because the edge lines have
overlap `1/2`.

Hence the closure preserves no system of three orthogonal lines. Its connected
component is not merely a torus with a finite permutation extension.

## The identity component acts irreducibly

Let `K_0` be the identity component of the closure. It is a normal subgroup of
`K`. If its qutrit representation were reducible, decompose into `K_0`
isotypic components. Normality makes the full group permute components of the
same dimension.

In dimension three, an unequal `1 plus 2` decomposition would be preserved by
the full group, contradicting irreducibility. Three equal one-dimensional
components would define the orthogonal imprimitivity system already excluded.
If `K_0` acted only by scalars, the projective component group would be finite,
contradicting the infinite projective order of `T`.

Therefore `K_0` acts irreducibly. Since the determinant image of the generated
group is finite, connectedness also gives

\[
K_0\subseteq SU(3).
\]

## Excluding the projectively real subgroup

The only proper connected irreducible compact possibility in complex
dimension three is the spin-one `SU(2)` image, projectively `SO(3)`.

Every projective `SO(3)` element has eigenvalues, up to a common scalar,

\[
1,
\qquad
e^{i\varphi},
\qquad
e^{-i\varphi}.
\]

If two eigenvalues coincide, the only nontrivial projective ratio is `-1`,
corresponding to a rotation through `pi`.

The edge gate `Q_ij` has a repeated eigenvalue one and distinct ratio `zeta`,
which is not `-1`. It cannot lie in a scalar multiple of `SO(3)`.

Nor can a disconnected normalizer enlarge the projective `SO(3)` image to
contain it: the irreducible real subgroup is self-normalizing projectively.

Thus the connected component is not the real spin-one subgroup.

## Closure theorem

Let `K` be the closure in `U(3)` of the electric braid permutations and the
three gates `Q_ij`.

We have shown:

1. `K` is infinite and has a nontrivial identity component;
2. its qutrit action is irreducible;
3. it is not imprimitive;
4. its connected irreducible component is not projectively `SO(3)`.

The connected-subgroup classification therefore forces

\[
SU(3)\subseteq K.
\]

Every generator has determinant in the sixth roots of unity. Electric
transpositions have determinant minus one, which is `zeta` cubed, and every
edge gate has determinant `zeta`. Hence

\[
\det K=\langle\zeta\rangle\cong C_6.
\]

Since `K` contains `SU(3)`, it follows that

\[
K
=
\{U\in U(3):\det U\in\langle\zeta\rangle\}.
\]

Projectivization removes the finite determinant coordinate, so

\[
\overline{\langle S_3,Q_A\rangle}^{\,\mathrm{proj}}
=
PU(3).
\]

The fixed gate set is projectively universal.

## Why this is stronger than the irrational-wait theorem

The earlier sufficient theorem used one fixed phase with irrational angle so
that its powers densely recovered a continuous one-parameter subgroup. The
present gate has finite order six. No individual generator has irrational
phase.

Density arises from noncommuting finite-order edge reflections. Their product
creates the irrational eigenangle with cosine `7/8`.

Thus the continuous resource has been fully compiled out of the algebraic
gate alphabet:

- electric braids are finite-order topological routes;
- the injected vacuum-edge gate has order six;
- all commands come from a finite discrete alphabet;
- arbitrarily accurate qutrit gates arise from longer words.

This is the desired discrete replacement for analog vacuum waiting at the
logical group level.

## Compilation boundary

Projective density proves existence of approximating words. It does not give
their length or a constructive search algorithm.

An executable compiler still needs:

- an inverse-closed finite generator presentation;
- a quantitative approximation algorithm;
- word-length bounds as a function of target accuracy;
- calibration and fault error below the required per-word budget;
- handling of the probabilistic phase-halving attempts;
- reference and environment reset between generator uses.

A Solovay--Kitaev theorem may become applicable after these hypotheses are
frozen, but it is not part of the current density proof.

## Physical-authority boundary

The density theorem starts only after `Q_A` is an admitted logical gate. Its
measurement-assisted construction still requires:

1. two coherent charged routes with relative holonomy
   `exp(2 pi i P_A/3)`;
2. the relational `B`-charge reference;
3. the oriented `C3` measurement phase `-omega`;
4. rank-one environment return across routes;
5. exact correction of the failure branch;
6. branch labels and retry control;
7. microscopic leakage and fault-spread bounds.

The algebraic universality result makes this one constructor especially
valuable. It does not manufacture it.

## Fault implications

### Generator overrotation

A systematic error in the injected sixth-root angle changes every long word
coherently. Projective density of the ideal generators does not syndrome that
fault.

### Route-coherence loss

If the two phase-halving routes leave distinguishable environments, `Q_A`
becomes a noisy branch channel and the exact reflection-group proof no longer
applies.

### Outcome correction fault

An incorrect minus-branch recovery changes the distribution of subsequent
words and can create a logical error before retry.

### Common complex-frame conjugation

Conjugating `omega`, the injected gate, and all internal testers preserves the
abstract density theorem while reversing the external phase convention.

### Long-word accumulation

Even a small one-gate diamond residual can grow with synthesis length unless
fault-tolerant correction intervenes.

## Exact falsifiers

- The edge gate fails to equal `I plus omega P_ij`.
- Two adjacent edge states have overlap magnitude other than `1/2`.
- The product trace differs from `3 plus 2 omega plus omega squared over 4`.
- The nontrivial product eigenangle fails to satisfy `cos theta=7/8`.
- `7/4` is treated as a rational algebraic integer.
- The three edge projectors have a nonscalar common commutant.
- The generators preserve a system of three orthogonal lines.
- The sixth-root reflection is placed inside projective `SO(3)` despite its
  repeated-eigenvalue ratio differing from `-1`.
- The connected-subgroup classification is invoked before infinite order,
  irreducibility, and imprimitivity have been checked.
- The full closure is called `U(3)` despite its determinant being restricted
  to sixth roots.
- Finite determinant components are claimed to obstruct projective
  universality.
- Qualitative density is promoted to efficient or fault-tolerant compilation.
- The conditional measurement gadget is treated as a physically admitted
  gate without its route and reference constructors.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies finite generator alphabets, conjugation
orbits, compact closure, connected components, imprimitivity, compilation
length, and separation of qualitative reachability from executable synthesis.

The quantum coefficient lens supplies complex reflections, projector
functional calculus, projective unitary groups, determinant sectors,
irreducible compact subgroup classification, and coherent gate-error
accumulation.

## Disposition

The fixed nonmonomial sixth-root vacuum-edge gate is projectively universal
with electric braiding. Its adjacent-edge product has irrational eigenangle
even though every generator has finite order. Irreducibility and the exclusion
of toral and real proper closures force `SU(3)` as the identity component.

The algebraic control question is therefore settled conditionally: arbitrary
analog waiting is unnecessary, and one exact measurement-injected gate
`Q_A` suffices. The research frontier moves entirely to physical compilation,
quantitative word synthesis, and fault tolerance of that discrete constructor.

No build, checker, or Git operation was run for this research-only packet.
