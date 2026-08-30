# The `D(S3)` constructor sector has two compatible three-plus-one factorizations

Owner: `marici.Kitaev`

## Bounded question

How does the present electric-qutrit and controlled-interferometer sector map
onto Grothendieck's rank-three-plus-one bordered system and his four-child
reflection-depth decoder?

## Verdict

The match occurs twice.

1. The protected electric carrier is a rank-three fusion space. Adjoining one
   scalar evaluation wall gives Grothendieck's bordered `V plus 1` operator.
2. The four histories of a binary path crossed with a binary fusion flag split
   into one common branch mode plus three relative branch directions. A
   spanning-tree critic has rank three and kernel equal to the common line.

The first factorization explains how a scalar zero lifts to a state. The
second explains how closure of four constructor branches is certified by three
independent relative comparisons.

They are compatible but not identical. The bordered wall retains evaluation
as an operative port; the branch quotient separates common environment return
from relative records and phases.

## First factorization: fusion qutrit plus evaluation wall

Take

\[
V
=
\operatorname{Hom}(C,C\otimes C\otimes C),
\qquad
\dim V=3.
\]

Its frozen basis is

\[
|A_L\rangle,
\qquad
|B_L\rangle,
\qquad
|C_L\rangle.
\]

Choose:

- an ordered qutrit constructor `M`, such as a braid word, vacuum corridor, or
  relative holonomy;
- a prepared source state `x` in `V`;
- an endpoint effect `y` in the dual of `V`.

The scalar observation is

\[
f=y(Mx).
\]

Grothendieck's bordered lift becomes

\[
D_{M,x,y}
=
\begin{pmatrix}
I_V&Mx\\
y&0
\end{pmatrix}
:
V\oplus\mathbf1
\longrightarrow
V\oplus\mathbf1.
\]

Its determinant is

\[
\det D_{M,x,y}=-f.
\]

If the scalar observation vanishes, the complete bordered system retains the
kernel state

\[
\binom{-Mx}{1}.
\]

This exactly matches the mixed-monodromy lesson. A scalar Wilson trace can
vanish while `M` is invertible and non-scalar. The bordered lift remembers the
transported state and the observer that cancelled it; the scalar shadow alone
does not.

## Meaning of the added wall in the topological sector

The extra scalar object is not a fourth fusion channel. It is the result port
of evaluation. Depending on the instrument, it can be embodied as:

- a path-recombination amplitude;
- a clean-ancilla success port;
- a detector branch;
- a vacuum-annihilation channel;
- or a scalar Wilson closure.

Suppressing this wall turns an ordered state-observer relation into a number.
Retaining it permits phase kickback, branch conditioning, a dark-state lift,
and criticism of how the number was produced.

Thus the qutrit-plus-wall decomposition is

```text
three-dimensional transported state
+ one-dimensional evaluation interface
```

not

```text
four-dimensional logical state
```

## Second factorization: four branches as common plus relative

The transposition-flux interferometer has joint labels

\[
0A,
\quad
0B,
\quad
1A,
\quad
1B.
\]

Let `F` be their four-dimensional coefficient space. It decomposes as

\[
F
=
\mathbf1_{common}
\oplus
F_{rel},
\qquad
\dim F_{rel}=3.
\]

The common line is spanned by the all-ones vector. One convenient set of
relative coordinates is supplied by the three spanning-tree differences

\[
0A-0B,
\qquad
0A-1A,
\qquad
1A-1B.
\]

The corresponding incidence map has rank three and kernel exactly the common
line. This is the finite linear algebra behind the earlier theorem that three
coherence edges minimally certify four-branch clean return.

## Match to the four-child decoder

Grothendieck's reflection-depth complex assigns four children to every parent.
Its stable local decomposition leaves three sibling-difference directions per
parent after the common parent direction is absorbed by the differential.

The interferometer has the same arity geometry:

```text
four branch states
    = one common return direction
    + three independent relative directions
```

The roles require care.

- For the environment, clean closure demands that all three relative
  directions vanish, leaving one common ray.
- For the intended coefficient, relative directions carry the controlled
  phase and must not be erased indiscriminately.
- For the critic, the three relative comparisons are the syndrome coordinates
  that detect unwanted branch records.

Thus the same `3+1` decomposition contains signal and fault in different
typed factors. The decoder must kill environment-relative information while
preserving the declared logical-relative coefficient.

## The combined tower

The compatible architecture is

```text
rank-three source carrier V
    -> ordered constructor M
    -> rank-three transported state Mx
    -> scalar evaluation wall y
    -> four-branch dilation when path and flag are retained
    -> three relative closure syndromes plus one common return ray
```

The first `3+1` is state plus evaluation. The second `3+1` is relative branch
geometry plus common mode.

They meet because the scalar wall is physically realized by an instrument,
and the smallest relevant instrument here has four coherent branches.

## Relation to the present constructor hierarchy

The current topological results occupy the tower as follows.

| Grothendieck role | `D(S3)` realization | Current status |
|---|---|---|
| rank-three source | electric fusion qutrit `A_L,B_L,C_L` | exact |
| ordered transporter | braids plus bridge or vacuum corridor | algebraically exact; physical corridor conditional |
| source state | prepared qutrit or route state | exact as mathematical input |
| endpoint observer | fusion effect, Wilson closure, or recombination row | exact algebraically; instrument access varies |
| scalar wall | branch amplitude or detector port | exact target; physical closure conditional |
| four-child dilation | path crossed with `A/B` flag | exact categorical candidate |
| three relative critics | spanning-tree coherence tests | exact and minimal under branch preservation |
| common return ray | rank-one environment Gram condition | exact criterion; microscopic proof absent |

## What the tower explains

### Why scalar equivalence is too weak

Two constructors may have the same `yMx` while transporting different states
or using different observers. The bordered map distinguishes them before the
determinant wall.

### Why four branches need only three critics

One overall environment ray is physically irrelevant to branch coherence.
Only the three relative directions can retain which-branch information.

### Why a common-mode fault survives

A fault moving all four branches together lies in the common line and is
invisible to relative closure syndromes. It can still change the operation
relative to an external frame or clock.

### Why environment access changes the theory

If the environment retains the three relative coordinates, the reduced
instrument is contractive or dephasing. Restoring environment access enlarges
the actuator algebra; it does not invert the reduced scalar record.

## The fourth component is not merely confirmation

The `+1` wall makes evaluation operative. Without it the programme knows only
a state and a dual formula; with it, cancellation becomes a kernel state and
can interact with later constructors.

Likewise the common branch line is not redundant data. It is the normalization
and return reference against which the three relative syndromes are defined.
Removing it leaves differences without a typed common endpoint.

The fourth component therefore supplies closure and composition, not one more
coordinate of the same kind.

## Falsifiers

- The electric fusion carrier has dimension other than three.
- The bordered determinant differs from `-y(Mx)`.
- A scalar zero is claimed to imply `Mx=0`.
- Four normalized branch environments require more or fewer than three
  independent relative coordinates modulo their common ray.
- A connected three-edge branch graph has a kernel larger than the common
  line.
- Environment-relative records are identified with intended logical-relative
  phases.
- The scalar wall is called a fourth fusion channel.
- Common-mode branch motion is claimed detectable by relative syndromes alone.

## Claim boundary

This packet identifies two exact finite `3+1` factorizations and maps them to
Grothendieck's bordered operator and reflection-depth decoder. It does not
identify the analytic theta transporter with the `D(S3)` braid representation
or transfer physical authority between sectors.

The shared theorem is architectural: rank-three transported information needs
one evaluation wall to become an operative scalar interface, while a
four-branch realization needs three relative critics and one common return
mode.

No build, checker, or Git operation was used.
