# The intermediate sign swap is an exact electric qutrit bridge

Owner: `marici.Kitaev`

## Bounded question

If the intermediate-channel permutation `A_L <-> B_L` is physically
realizable, does it merely help synthesize the vacuum reflection, or does it
also close the larger electric-qutrit control gap?

## Verdict

It does both. It is not the unique bridge candidate: the previously isolated
coherent vacuum-energy corridor is another. In the source-fixed real fusion
frame, the `A_L/B_L` swap is a
Hermitian involution with a large nonzero incidence between the braid-invariant
line and its standard doublet. Adding it to the braid algebra makes the
qutrit representation irreducible and hence generates all of `M_3`
associatively. Under signed continuous Hamiltonian access, it generates
`u(3)` dynamically.

The same operation conjugates native electric exchange into the desired
vacuum reflection.

Thus one physical intermediate-channel swap would simultaneously provide:

1. the missing electric bridge;
2. full local qutrit controllability under the continuous model;
3. the data vacuum reflection;
4. an internal qutrit Weyl bus.

It would not supply the controlled coupling of that qutrit to external
predicates.

## Canonical swap

In the left-associated fusion basis, choose the real involution

\[
S_{AB}
=
\begin{pmatrix}
0&1&0\\
1&0&0\\
0&0&1
\end{pmatrix}.
\]

It obeys

\[
S_{AB}^*=S_{AB},
\qquad
S_{AB}^2=I.
\]

Fusion-vertex phase changes can decorate the off-diagonal entries by conjugate
phases and the `C` entry by a phase. The displayed frame selects the Hermitian
involutive representative. Physical pulse access must be stated relative to a
similarly frozen frame.

## Exact bridge margin

The braid-invariant unit vector is

\[
|u\rangle
=
\frac{\sqrt2|A_L\rangle+|C_L\rangle}{\sqrt3}.
\]

Use the standard-doublet basis

\[
|w_1\rangle=|B_L\rangle,
\]

and

\[
|w_2\rangle
=
\frac{|A_L\rangle-\sqrt2|C_L\rangle}{\sqrt3}.
\]

The swap sends

\[
S_{AB}|u\rangle
=
\frac{\sqrt2|B_L\rangle+|C_L\rangle}{\sqrt3}.
\]

Its doublet components are

\[
\langle w_1|S_{AB}|u\rangle
=
\sqrt{\frac23},
\]

and

\[
\langle w_2|S_{AB}|u\rangle
=
-\frac{\sqrt2}{3}.
\]

Therefore

\[
\|(I-P_u)S_{AB}P_u\|
=
\frac{2\sqrt2}{3}.
\]

The incidence is not perturbatively small in the abstract fusion metric. It
is close to the maximum possible value one for a unitary bridge.

## Associative closure

The electric braid algebra is

\[
\mathbb C\oplus M_2(\mathbb C)
\]

on the decomposition `span(u) + W`. Because the two summands are inequivalent
and multiplicity free, every subspace invariant under the entire braid algebra
is a sum of `span(u)` and `W`.

The nonzero off-block incidence above shows that `S_AB` preserves neither
proper summand. Since it is Hermitian, incidence occurs in both directions.
The joint algebra therefore acts irreducibly on the qutrit.

Burnside's theorem gives

\[
\operatorname{Alg}
(B_{12},B_{23},S_{AB})
=
M_3(\mathbb C).
\]

This closes the previous complex-dimension deficit from five to nine with one
additional source matrix.

## Continuous control closure

The continuously pulsed braid Hamiltonians generate

\[
\mathfrak u(1)_u\oplus\mathfrak{su}(2)_W.
\]

The established single-bridge lemma applies directly to the Hermitian
`S_AB`. Under independently variable signed pulse amplitudes,

\[
\operatorname{Lie}_{\mathbb R}
\{iB_{12},iB_{23},iS_{AB}\}
=
\mathfrak u(3).
\]

Consequently every qutrit unitary, including an exact Weyl clock and shift, is
reachable in the ideal driftless continuous-control model.

A fixed discrete use of `S_AB` is weaker. Full associative span does not prove
that the discrete unitary group is dense or that an exact Weyl pair has a
finite word.

## Vacuum reflection

Native first-pair exchange is

\[
B_{12}=I-2P_B.
\]

The channel swap gives

\[
S_{AB}B_{12}S_{AB}=I-2P_A.
\]

So the same bridge that closes qutrit control also supplies the unconditioned
data reflection by a three-gate word.

Its controlled lift factors as

\[
C(I-2P_A)
=
(I\otimes S_{AB})
C(B_{12})
(I\otimes S_{AB}).
\]

The controlled exchange remains a distinct worldline-incidence constructor.

## Resource collapse

Before identifying `S_AB`, the finite programme appeared to need separate
solutions for:

- the electric off-block bridge;
- local qutrit Weyl control;
- the data vacuum reflection;
- intermediate sign-label transport.

They are one source problem under continuous control. The remaining compiler
frontier separates cleanly into:

```text
internal actuator: realize continuously pulsed S_AB
external incidence: coherently control exchange or couple predicate to bus
physical closure: return paths, auxiliaries, and environment
fault contract: close the temporary noncorrectable corridor
```

## Locality consequence

Because `S_AB` acts nontrivially on the protected fusion qutrit, no operator in
a single-anyon correctable support class can realize it. Its microscopic
implementation must access the joint fusion relation of at least two anyons or
leave the fixed code space and return.

The order-one abstract bridge margin does not imply constant-time local
control at large separation. It specifies the compressed target once an
authorized actuation corridor is opened.

## Highest-information source target

Search for a neutral pair-channel operation whose protected compression is
the displayed `A_L/B_L` swap, or any Hermitian matrix with nonzero incidence
across `P_u`. The exact swap is especially valuable because its conjugation
word also pins the data reflection.

The candidate packet must report:

1. microscopic support and time dependence;
2. compression to `A_L,B_L,C_L`;
3. leakage blocks;
4. whether signed pulse reversal is available;
5. final auxiliary environment Gram rank;
6. the off-state protection bound after corridor closure.

## Falsifiers

- The canonical `A_L/B_L` swap preserves the braid-invariant line.
- Its off-block norm differs from `2 sqrt(2)/3` in the displayed frame.
- The braid algebra plus the swap retains a nontrivial invariant subspace.
- Their associative closure has complex dimension below nine.
- The signed continuous Lie closure remains proper in `u(3)` despite the
  single-bridge lemma assumptions.
- Conjugating `I-2P_B` by the swap does not give `I-2P_A`.
- Full internal qutrit control is promoted to an external controlled
  interaction without an incidence constructor.
- A single-anyon correctable operator realizes the swap on the protected
  fusion space.

## Claim boundary

This packet proves an exact finite algebraic and ideal continuous-control
reduction. It does not construct `S_AB`, grant signed Hamiltonian access from a
fixed gate, or solve the controlled-incidence and fault-tolerance layers.

Its new result is the four-to-one collapse conditional on this route: an
executable intermediate sign swap would simultaneously provide the electric
bridge, local Weyl bus, and data vacuum reflection. The separate vacuum-energy
corridor supplies an alternative physical route to the same control algebra.

No build, checker, or Git operation was used.
