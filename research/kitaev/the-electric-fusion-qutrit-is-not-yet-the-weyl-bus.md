# The electric fusion qutrit is not yet the Weyl bus

Owner: `marici.Kitaev`

## Bounded question

Can the already pinned three-dimensional electric fusion space be used as the
minimal qutrit bus that compiles the joint phase from two marginal controlled
couplings?

## Verdict

Not with the presently authorized electric braid operations.

The abstract bus requires a Weyl pair `X,Z` satisfying

\[
ZX=\omega XZ,
\qquad
\omega^3=1,
\qquad
\omega\ne1.
\]

Such a pair acts irreducibly on a three-dimensional space and generates the
whole matrix algebra `M_3`. The pinned electric braid representation instead
decomposes as `1 + 2`, preserves an explicit rank-one projector, and generates
only `C + M_2`. Therefore its existing braid words cannot be the Weyl bus.

This is an actuator obstruction, not a dimension obstruction. The physical
qutrit is present; the required complementary clock-and-shift incidence is not.

## Irreducibility of a qutrit Weyl pair

Suppose `X` and `Z` are unitary and satisfy the Weyl relation above. If `v` is
a `Z` eigenvector with eigenvalue `lambda`, then

\[
Z X^jv=\lambda\omega^jX^jv.
\]

The three eigenvalues are distinct. Hence `v,Xv,X^2v` span the qutrit. Any
nonzero common invariant subspace containing a `Z` eigenvector is therefore the
whole space. Since a unitary invariant subspace has an invariant orthogonal
complement, the pair is irreducible.

Burnside's theorem then gives

\[
\operatorname{Alg}(X,Z)=M_3(\mathbb C).
\]

Equivalently, the common commutant of `X` and `Z` consists only of scalars.

## Conflict with the pinned electric braid qutrit

On the established `C,C,C` to `C` multiplicity space, the elementary braid
operators preserve

\[
P_u=|u\rangle\langle u|,
\qquad
|u\rangle=
\frac{\sqrt2|A_L\rangle+|C_L\rangle}{\sqrt3}.
\]

Their representation is `1 + 2`, their associative algebra has complex
dimension five, and their commutant contains the nonscalar projector `P_u`.
Every pair of operators formed solely from electric braid words also commutes
with `P_u`.

Consequently no two existing electric braid words can satisfy the irreducible
qutrit Weyl relation. If they did, their common commutant would be scalar, in
contradiction with the conserved `P_u`.

The order-three braid rotation does not rescue the construction. It can supply
an order-three spectral operation on the standard doublet plus the invariant
line, but every other braid-generated candidate remains block diagonal in the
same `1 + 2` decomposition. A clock without a constructor crossing that
decomposition is not a Weyl bus.

## Exact missing incidence

Let `Z_0` be any authorized order-three unitary with three distinct eigenvalues
on the fusion qutrit. A complementary unitary `X_0` is sufficient when

\[
Z_0X_0=\omega X_0Z_0.
\]

Necessarily `X_0` cyclically permutes the three eigenspaces of `Z_0`. In
particular it cannot preserve `P_u` when `P_u` is one of those eigenspaces.
Thus the previously isolated off-block bridge condition

\[
(I-P_u)X_0P_u\ne0
\]

is necessary. For the exact Weyl compiler it is not sufficient: the three
transition amplitudes must close as one cyclic permutation with compatible
phases. The bridge problem has therefore sharpened from arbitrary qutrit
controllability to one typed cyclic-incidence constructor.

## Two routes, with different authority

### Internalize the bus

Derive a localized fusion-space operation `X_0` which cycles the three
eigenlines of an authorized `Z_0`. Then the existing physical fusion qutrit can
serve as the catalytic bus. The two required controlled marginal couplings
still have to be compiled and fault-audited.

### Adjoin a bus

Supply an independent three-level ancilla with physical clock and shift
operations. This realizes the abstract commutator identity, but it expands the
hardware model. The ancilla must couple separately to the anyonic charge
predicate and the flag predicate, return exactly, and expose leakage and
common-mode faults.

The first route is source-minimal. The second is constructor-minimal once a
qutrit ancilla is admitted. Neither follows from endpoint algebraic rank.

## Controlled coupling remains a separate gate

Even an executable Weyl pair on the bus does not provide

\[
U_P=(I-P)\otimes I+P\otimes Z,
\qquad
V_Q=(I-Q)\otimes I+Q\otimes X.
\]

These are charge-conditioned interactions between different subsystems. Their
existence is stronger than independent access to `P`, `Q`, `X`, and `Z`.

The realization ladder is now:

```text
three-dimensional fusion space
    -> irreducible Weyl pair on that space
    -> two source-conditioned bus couplings
    -> exact bus return under the group commutator
    -> fault-contained joint phase constructor
```

The present source reaches the first line. Abstract algebra proves the third
line would imply the fourth, but does not manufacture the second or third.

## Highest-information next experiment

Search the microscopic ribbon and fusion operations for a single localized
constructor whose compression has nonzero incidence across `P_u` and whose
conjugates by the order-three operation form a closed three-cycle. This one
test distinguishes:

- a native anyonic qutrit bus;
- a merely controllable qutrit needing pulse synthesis;
- a permanently reducible electric actuator;
- or the need for an external typed qutrit ancilla.

Measuring more scalar braid invariants has lower information gain because all
such invariants remain compatible with the conserved projector.

## Falsifiers

- Two electric braid words have scalar common commutant.
- The pinned braid algebra has complex dimension nine rather than five.
- The projector `P_u` fails to commute with an existing authorized braid
  generator.
- A pinned localized constructor already cycles all three eigenlines of an
  authorized order-three clock.
- Controlled marginal bus couplings have already been source-derived with
  exact bus return and bounded fault spread.

## Claim boundary

This packet proves a no-renaming theorem for the existing electric braid
qutrit. It does not exclude a native bus from the larger `D(S3)` ribbon
algebra, nor does it prove that an external qutrit ancilla is necessary.

The new reduction is exact: realizing the catalytic bus internally requires
one source-authorized cyclic incidence that destroys the conserved `1 + 2`
decomposition. After that, controlled coupling and fault containment remain
independent obligations.

No build, checker, or Git operation was used.
