# One scalar common-mode anchor does not complete the three-plus-one certificate

Owner: `marici.Kitaev`

## Bounded question

Does the proposed certificate of three relative branch coherences plus one
independent scalar anchor determine the full branch-preserving qutrit
instrument?

## Verdict

No. A common nontrivial qutrit operation can postcompose every branch, preserve
all three relative coherence tests exactly, and fix one anchored state or
scalar expectation. The original prediction is falsified if `+1 anchor` means
one scalar datum.

The repaired theorem is:

> Three connected relative coherence tests certify branch closure, while one
> separately typed common-mode port must be tomographically faithful on the
> admitted common actuator algebra.

A maximally entangled Choi preparation with a spanning output effect family is
one such port. It counts as one interface, not one number.

## Hostile branch-preserving model

Let the data carrier be the electric fusion qutrit

\[
V=\operatorname{span}\{|A_L\rangle,|B_L\rangle,|C_L\rangle\}.
\]

Let `T` be the ideal operation on data and the four path-by-flag branches. Pick

\[
G_\theta
=
\operatorname{diag}(1,e^{i\theta},e^{-i\theta}),
\qquad
0<\theta<\pi.
\]

Define the hostile implementation by common postcomposition:

\[
\widetilde T
=
(G_\theta\otimes I_{branch})T.
\]

Assume the same returned environment ray in all four branches. Then:

- branch labels are preserved;
- there is no leakage;
- all three spanning-tree coherence visibilities and phases agree with the
  ideal branch-relative values;
- the environment Gram matrix has rank one;
- `G_theta` has determinant one;
- the anchored state `A_L` is fixed exactly.

Nevertheless `T` and `T_tilde` differ on the admitted qutrit. For example,

\[
\frac{|B_L\rangle+|C_L\rangle}{\sqrt2}
\]

acquires a relative phase `2 theta` under the hostile common operation.

Thus three relative tests plus survival of `A_L`, vacuum probability, one
diagonal expectation, determinant, or any other similarly weak scalar anchor
do not determine the common-mode action.

## Why the relative critic cannot see it

The branch incidence map acts on the four-dimensional branch factor and has
kernel equal to the common branch line. A common data operator has the form

\[
G\otimes I_{branch}.
\]

It lies entirely outside the relative branch coordinate being tested. No
number of repetitions of the same branch-only spanning tree can identify `G`.

This is not a defect in the rank-three relative critic. It is a type boundary:
branch closure and data-plane process correctness are different claims.

## Stabilizer of one state anchor

Fixing one pure qutrit state leaves a large common-mode ambiguity. The unitary
stabilizer of its ray contains `U(2)` acting on the orthogonal complement.

Even checking all three fusion-basis projectors leaves independent diagonal
phases. Population tomography sees

\[
\operatorname{diag}(1,e^{i\alpha},e^{i\beta})
\]

as the identity channel on those basis populations.

Therefore `one anchor` cannot mean one input state, one effect, one
expectation, one determinant, or one central readout.

## A sufficient one-port repair

Let `R` be a qutrit reference and prepare a maximally entangled state

\[
|\Omega\rangle
=
\frac1{\sqrt3}
\sum_{e=A,B,C}|e_L\rangle_V|e_L\rangle_R.
\]

For a common unitary `G`,

\[
(G\otimes I_R)|\Omega\rangle
\]

equals `Omega` up to global phase exactly when `G` is scalar. Thus an anchored
Choi comparison kills every nontrivial common qutrit unitary at once.

For a general channel, its Choi state determines the channel completely.
Operational certification still requires a spanning effect family on the
joint output. The port is singular as an interface but internally
tomographically rich.

The repaired resource count is therefore

```text
three scalar relative coherence coordinates
+ one complete-order common-process port
```

not

```text
three scalar relative coordinates
+ one scalar common coordinate
```

## Minimal unentangled alternative

If reference entanglement is unavailable, exact unitary verification can use
a spanning family of data inputs plus coherence-fixing superpositions. Three
basis rays alone leave diagonal phase freedom. Adding one full-support
superposition fixes their relative phases once each output ray is verified.

This is already more than one scalar anchor. It is another realization of one
typed common-mode tester family.

## Common channel contraction hostile

The unitary hostile is not the only one. Let `E` be a qutrit dephasing or
depolarizing channel that fixes the chosen anchor state. Applying `E` after
every branch preserves relative branch closure while contracting future data
contexts.

Retained environment access may dilate `E` to a unitary on a larger system,
but that enlarges the admitted actuator algebra. It does not make the reduced
qutrit channel equal to the target.

Hence the common-mode anchor must distinguish all admitted channels, not only
unitaries, if the claimed instrument class includes noise.

## Revised falsifiable prediction

Under branch preservation and no leakage:

1. three connected branch-coherence tests are necessary and sufficient for
   rank-one relative environment return;
2. a common-mode tester faithful on the admitted data-plane channel class is
   independently necessary and sufficient for process correctness;
3. the two certificates compose because they act on different factors;
4. neither certificate supplies microscopic implementation authority.

The new falsifier is stronger:

> Exhibit two branch-preserving implementations that agree on the three
> relative coherences and on a complete Choi tester for the common data channel,
> yet differ as admitted instruments.

Such a pair would show an additional cross-factor correlation omitted by the
product model.

## Consequence for the bordered wall

Grothendieck's `+1` wall should likewise be read as one typed evaluation
interface, not one scalar observation. Its context family must be faithful on
the ambiguity that survives transport.

The wall's dimension counts compositional ports. It does not bound the number
of experiments needed to characterize the map attached to that port.

This distinction repairs the overly literal resource prediction while
preserving the `3+1` architecture.

## Falsifiers

- `G_theta` changes any of the four branch-relative environment overlaps.
- One fixed qutrit ray has only scalar unitary stabilizer.
- Three fusion-basis populations determine all diagonal phases.
- A maximally entangled Choi vector is fixed by a non-scalar qutrit unitary up
  to global phase.
- Two channels with the same complete Choi state differ.
- Branch-relative closure alone determines a common data-plane operation.
- One typed port is equated with one scalar datum.

## Claim boundary

This packet falsifies the scalar-anchor version of the prediction and repairs
it with a complete-order anchor. It assumes a product separation between
common data action and relative branch environment; cross-factor correlated
errors remain the next hostile class.

It does not construct a Choi tester physically or reduce its fault-tolerant
cost.

No build, checker, or Git operation was used.
