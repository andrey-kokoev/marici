# Toric-code constructor access and three disappearances

Status: finite-cutoff theorem for the frozen toric/annular protocol model.
This packet covers WP11--WP13.

## One class, three different losses

Fix the annular outer circumference `gamma`.  In the absolute complex it is
a residue-free non-boundary and the marked seam cocycle reads it as one.
Hold that upstream class fixed and compare:

| mechanism | current class | constructor | record on `gamma` | successor class |
|---|---|---|---|---|
| access denial | nonzero | forbidden | no legal record | not changed |
| projection loss | nonzero | Wilson constructor retained | coarse map sends both bits to `0` | not changed |
| constitutive collapse | zero after migration | old port invalid | not defined on new quotient | zero in `H1(K,Rrough)` |

Access denial changes the admitted operational algebra, not homology.
Projection loss composes a valid Wilson record `w in F2` with the constant
map `q(w)=0`; the class and constructor survive while the record kernel grows.
Constitutive collapse changes the physical relation: the relative projection
sends `gamma` into the face-repair span.  These mechanisms cannot substitute
for one another.

## Source-defined loop constructors

The admitted Wilson protocol is phase kickback:

1. prepare an ancilla in `|+>`;
2. apply controlled `P_e` from that ancilla along every edge of a marked
   noncontractible string, with `P=Z` or `X` as appropriate;
3. preserve the accumulated correlation until the path closes;
4. measure ancilla `X`, producing the loop eigenvalue record.

The support union is the declared string.  A single `Z1` constructor induces
the projective label algebra `{I,Z1}` of size two.  Independent commuting
`Z1,Z2` constructors give size four and separate their marked joint basis.
An intersecting `X1,Z1` pair also generates four labels but is
noncommutative; its two effects require separate settings/repeated
preparations rather than a simultaneous sharp measurement.  The four
constructors `X1,X2,Z1,Z2` generate all 16 phase-free logical Pauli labels.
Full state reconstruction still requires expectation estimation over an
informationally complete set; operator generation is not a single-shot
tomography protocol.

Constructor access also does not select a recovery.  The reproduced `L=3`
decoder gate separates four source data:

1. the noise/cost model ranks candidate histories;
2. the logical recovery objective chooses which homology class counts as
   success;
3. the optimizer/tie-break chooses a representative inside that class;
4. the physical instrument implements the selected operation and record.

Uniform cost leaves two tied representatives in one repair class.  Two local
cost models uniquely choose different representatives of that same class.  A
hostile nonlocal cost chooses a different logical class with the identical
syndrome.  Thus syndrome plus cost is not a recovery certificate, and an
accessible constructor is not authorization to invoke it as a decoder.

## Locality and resource cost

For torus sizes `L=2,3,4`, exact enumeration finds no residue-free
non-boundary below weight `L` and exactly `2L` minimum straight cycles at
weight `L`.  Therefore no constructor whose total data support remains below
the code distance acts nontrivially on the protected quotient.

A mobile ancilla uses `L` controlled gates and sequential depth `L`.  Although
its instantaneous footprint may be local, its retained spacetime worldline
has noncontractible length `L`.  An already prepared cat ancilla can couple
to all `L` data edges at depth one, but its spatial extent is `L`; preparation
and verification cost are not erased, merely moved upstream.  Thus spatially
extended support and time-like transported correlation are alternative
resources, not subdistance counterexamples.

## Assumptions and falsifiers

The constructor model admits controlled single-edge Pauli gates, ancilla
preparation/measurement, a retained marked path, and noiseless correlation
transport.  It does not claim fault-tolerant laboratory scheduling.  The
result is falsified by a subdistance admitted protocol with nontrivial logical
action, by a generated-algebra size other than `1,2,4,4,16`, or by treating
an intersecting pair as simultaneously sharp.  A decoder claim is further
falsified when an admissible cost/prior/tie-break variation changes its
logical class or implemented representative.
