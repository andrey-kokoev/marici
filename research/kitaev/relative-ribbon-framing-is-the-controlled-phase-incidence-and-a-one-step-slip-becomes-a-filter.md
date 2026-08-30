# Relative ribbon framing is the controlled phase incidence and a one-step slip becomes a filter

Owner: `marici.Kitaev`

## Bounded question

What is the smallest topological datum that can make the three-cycle dyon
twist conditional on the same route bit used by the qutrit bridge?

It is a pair of coherent framed-ribbon histories with identical typed
endpoints and relative framing number one. On a selected three-cycle dyon
whose twist is `omega`, the ratio of the two ribbon evaluations is `omega`.
Real `X` recombination then produces the exact sixth-root injection.

This also exposes an unusually sharp fault law. With the frozen cube-root
bridge holonomy, only framing class one modulo three gives reversible branch
operators. Either one-step framing slip makes the nominal success branch a
rank-deficient sector filter. A simultaneous orientation reversal of both the
dyon phase and bridge holonomy is different: it preserves the ideal
instrument and implements the conjugate logical gate.

## Claim boundary

The framed-ribbon and finite qutrit calculations are exact in the ribbon
category of untwisted `D(S3)`. They identify the topological incidence cell
that a lattice implementation must realize.

The packet does not prove that the frozen lattice Hamiltonian supports a
coherently controlled ribbon-framing operation, that physical motion has no
dynamical phase, or that framing faults satisfy a local stochastic model.

## Relative framing theorem

Let `D` be one fixed nontrivial three-cycle dyon with topological twist

\[
\theta_D=\omega.
\]

Let `Gamma_0` and `Gamma_1` be two framed-ribbon histories in the same typed
morphism space. Require:

- identical initial and final anyon types;
- identical fusion channels and endpoint multiplicity labels;
- identical unframed connectivity;
- no unreturned ancillary ribbon or environment port;
- relative self-framing number `Delta f`.

Ribbon functoriality then gives the relative scalar

\[
\mathcal Z(\Gamma_1)
=
\theta_D^{\Delta f}\mathcal Z(\Gamma_0)
=
\omega^{\Delta f}\mathcal Z(\Gamma_0).
\]

For

\[
\Delta f=1\pmod 3,
\]

the two histories supply exactly the required cube-root route coefficient.

This is the topological form of controlled phase kickback. The control is not
an abstract controlled-unitary symbol added afterward: it is the coherent
choice between two histories whose relative framed topology differs by one.

## Why identical endpoints are insufficient

Two ribbons can have identical endpoints and the correct relative framing
while still failing as an executable interference pair. If they leave
different local deformations, fusion states, clock records, or baths, the
relative coefficient is multiplied by an environment overlap.

Thus relative framing supplies the quantum coefficient, while whole-
instrument closure supplies the authority to use it as a route amplitude.
Neither statement implies the other.

## Exact route instrument

Let

\[
R=I,
\qquad
S=H,
\qquad
H=I+(\omega-1)P_A.
\]

For framing class `k` modulo three, the route phase is

\[
\lambda_k=\omega^k.
\]

After real `X` recombination, the minus branch is

\[
K_-^{(k)}
=
\frac{I-\omega^kH}{2},
\]

and the plus branch is

\[
K_+^{(k)}
=
\frac{I+\omega^kH}{2}.
\]

Both branches are proportional to unitaries exactly when the rotated
Hermitian part of `H` is scalar:

\[
-\omega^kH-\omega^{-k}H^*=cI.
\]

On the complement of `P_A`, the left side has scalar value

\[
-2\operatorname{Re}(\omega^k).
\]

On the image of `P_A`, it has scalar value

\[
-2\operatorname{Re}(\omega^{k+1}).
\]

The values agree only for

\[
k=1\pmod 3.
\]

Therefore the intended relative framing is not one convenient convention
among three. It is the unique framing class that makes both measurement
branches reversible.

## Intended framing class

For `k=1`,

\[
K_-^{(1)}=\frac{I-\omega H}{2}.
\]

This branch occurs with probability `3/4` and, after normalization, is
projectively

\[
Q_A=\exp(i\pi P_A/3).
\]

The other branch occurs with probability `1/4` and is the admitted
correctable inverse cube-root failure.

## Negative framing slip

If the relative framing slips from `k=1` to `k=0`, then

\[
K_-^{(0)}=\frac{I-H}{2}.
\]

On the complement of `P_A`, this operator vanishes. On the image of `P_A`, it
equals the nonzero scalar `(1-omega)/2`. Hence

\[
\operatorname{rank}K_-^{(0)}
=
\operatorname{rank}P_A
=
1.
\]

The nominal gate has become a vacuum-line filter.

## Positive framing slip

If the relative framing slips from `k=1` to `k=2`, then

\[
K_-^{(2)}=\frac{I-\omega^2H}{2}.
\]

On the image of `P_A`, the factor is

\[
1-\omega^3=0.
\]

On its complement the factor is nonzero. Therefore

\[
\operatorname{rank}K_-^{(2)}=2.
\]

The nominal gate has become the complementary-sector filter.

These are not small coherent overrotations. Either one-step slip changes a
full-rank unitary branch into a rank-deficient measurement and makes the
outcome probability depend on the unknown logical state.

## Local syndrome blindness and operational visibility

A framing slip need not create or move any endpoint topological charge. The
ordinary local excitation syndrome can therefore remain unchanged even
though the logical instrument has become a filter.

The fault is nevertheless visible to a constructor-level audit:

- the normalized branch loses full rank;
- success probability differs between a `P_A` input and a complementary
  input;
- the three nonorthogonal SIC survival tests fail;
- retry correction cannot restore an unknown state after information has
  been filtered.

This is a clean example of a fault that is invisible to state syndrome but
visible to process probes.

## Common orientation reversal

Now reverse the complete orientation frame rather than changing only the
framing coefficient. Complex conjugation sends

\[
\omega\longmapsto\omega^2
\]

and simultaneously sends the bridge holonomy to

\[
H^*=I+(\omega^2-1)P_A.
\]

The conjugated minus branch is

\[
\widetilde K_-
=
\frac{I-\omega^2H^*}{2}.
\]

Its two sector magnitudes are again equal, its probability is `3/4`, and its
normalized gate is projectively

\[
Q_A^*=\exp(-i\pi P_A/3).
\]

Every internally conjugated algebraic and process test passes. Only a probe
anchored to an independently preserved external orientation distinguishes
`Q_A` from `Q_A*`.

Thus two faults that both appear to reverse a phase have different types:

- phase or framing reversal alone produces a detectable rank-deficient
  filter;
- common conjugation of phase source, bridge holonomy, compiler, and internal
  probes produces a valid but externally conjugated computation.

The second is the genuine common-mode frame fault.

## Minimal command ledger

Because local endpoint syndrome does not record relative framing, an
executable constructor needs a typed command-history coordinate containing at
least:

- selected dyon species;
- relative framing class modulo three;
- orientation of the bridge holonomy;
- `X`-measurement outcome;
- whether failure correction and joint reset completed.

This ledger is not evidence that the commanded operation occurred. A
constructor-level critic must compare it with an independent process witness.
But without the typed command coordinate, one cannot even distinguish the
three finite framing classes that lead to different instruments.

## Microscopic lattice target

The next lattice calculation should exhibit two explicit ribbon sequences
`Gamma_0,Gamma_1` and prove:

1. their endpoint and fusion maps agree exactly;
2. their relative framed evaluation is `omega`;
3. their dynamical phases agree or are removed by a source-derived echo;
4. their persistent ancillary states agree up to the declared scalar;
5. their relative framing is coherently correlated with the `R/S` bridge
   route rather than selected by a classical controller;
6. local faults changing framing are either detected by an independent
   process probe or included in the logical fault model.

An abstract ribbon isotopy identity proves item two. It does not prove the
other five.

## Exact falsifiers

- Two routes with identical endpoints are assumed to have identical framed
  histories.
- A relative topological twist is inferred without matching fusion and
  environment ports.
- Any framing class other than one modulo three is claimed to give the same
  reversible phase-halving instrument.
- A one-step framing slip is modelled only as a small overrotation.
- Local excitation syndrome is claimed to detect every framing-history fault.
- Complex conjugation of the dyon phase is considered without also auditing
  the bridge holonomy.
- The internally consistent conjugate gate is called identical to the target
  relative to an external compiler frame.
- A command record is treated as evidence of physical execution.
- A framed-category coefficient is promoted to a lattice actuator without
  dynamical-phase and environment-return checks.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies coherent histories, relative framing,
endpoint matching, command records, process witnesses, local-syndrome
blindness, and common-mode frame transformations.

The quantum coefficient lens supplies topological spin, ribbon evaluation,
projector holonomy, Kraus rank, conjugate gate alphabets, and
superselection-resolved process tests.

## Disposition

The missing phase incidence has a precise topological candidate: relative
framing one between two coherent dyon ribbon histories. In the ideal ribbon
category this gives the exact `omega` coefficient and therefore the exact
sixth-root qutrit injection after real recombination.

The same calculation identifies the first dangerous logical fault. A
one-step isolated framing slip does not gently perturb the gate; it collapses
the success branch to `P_A` or its complement. A full orientation reversal is
instead an internally valid conjugate computation and requires an independent
frame reference to detect.

The physical frontier is now an explicit pair of lattice ribbon sequences
with matched dynamical phases and returned ancillary state.

No build, checker, or Git operation was run for this research-only packet.
