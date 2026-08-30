# Controlization boundary for the finite `D(S3)` sector instrument

Owner: `marici.Kitaev`

Status: exact finite source-typing theorem; timed synthesis of the central
generator remains open.

## Bounded question

Does uncontrolled reachability of the central unitary

\[
U=\exp(-2\pi i Z/8)
\]

supply the controlled powers `U1,U2,U4` required by the three-qubit sector
record?

No.  A black-box unitary is operationally unchanged by `U -> exp(i phi) U`.
Every circuit making a fixed number `n` of unconditional calls changes only
by the global phase `exp(i n phi)`.  But

\[
\operatorname{ctrl}(e^{i\phi}U)
=|0\rangle\!\langle0|\otimes I
 +e^{i\phi}|1\rangle\!\langle1|\otimes U
\]

is not globally phase-equivalent to `ctrl(U)` for generic `phi`: the phase is
now relative between the control branches.  Therefore no fixed-query circuit
built only from uncontrolled calls to an otherwise unknown `U` and
`U`-independent gates can uniformly implement `ctrl(U)`.  Uncontrolled Lie
reachability does not close the phase-estimation source obligation.

## Exact constructive repair

There are two source-honest repairs.

1. If the apparatus supplies the conditional Hamiltonian

   \[
   P_1\otimes Z,
   \qquad P_1=|1\rangle\!\langle1|,
   \]

   then one pulse of duration/pulse-area `j*pi/4` implements

   \[
   \exp(-2\pi i j P_1\otimes Z/8)
   =P_0\otimes I+P_1\otimes U^j
   \]

   for `j=1,2,4`.  This is one conditional pulse per phase-estimation bit.

2. If a named exact word `U=G_m ... G_1` is known and the apparatus supplies
   each `ctrl(G_r)`, then

   \[
   \operatorname{ctrl}(G_m)\cdots\operatorname{ctrl}(G_1)
   =\operatorname{ctrl}(U).
   \]

   Repeating or separately synthesizing the word gives the required powers.
   This repair cannot be invoked yet because the previous audit established
   Lie reachability but did not derive finite timed primitive words.

Both repairs add an explicit record-qubit conditional interface.  If `Z` has
data support `s`, `P1 tensor Z` has data support `s` and total support `s+1`;
controlization does not enlarge the data footprint, but it does increase the
interaction arity by one.  Calling this automatic would erase the principal
apparatus datum.

## Exact residue action

On the eight sectors `(A,B,C,D,E,F,G,H)`, use the integer lifts

\[
(-8,1,2,3,6,7,20,5),
\]

whose residues are `(0,1,2,3,6,7,4,5)`.  The three controlled powers imprint
the binary Fourier phases for weights `1,2,4`; inverse `F_8` therefore records
the eight distinct residues exactly.  A common additive shift of all lifts
only conjugates the record register by a known diagonal phase and does not
merge sectors.

## Assumptions, falsifiers, and remaining typing

The theorem assumes coherent control qubits and exact finite-dimensional
unitaries.  It does not assume the conditional coupling exists.  It is
falsified by a uniform black-box controlization circuit insensitive to the
global-phase ambiguity, failure of the conditional-Hamiltonian exponential
identity, failure of controlled-word composition, or a residue collision.

Still unresolved are a source-derived timed word for `Z`, hardware locality
of the added record-qubit coupling, its calibration/noise law, and
fault-tolerant scheduling.  The result upgrades the former vague blocker to
an impossibility theorem for black-box controlization plus a minimal typed
apparatus alternative.

Run:

```text
uv run --with sympy python research/kitaev/checkers/check_s3_controlization_boundary.py
```

Saved output: `research/kitaev/results/s3-controlization-boundary.json`.

