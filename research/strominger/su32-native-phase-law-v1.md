# Native phase law from coefficient operations

## Frozen question

The signed-reference incidence does not select a phase action. Test the actual five-slot coefficient operations instead: PN, inverse PN, NE, P reader advance and N reader/NN advance.

Conjecture: stationary, species-indexed diagonal phase actions satisfying every native coefficient intertwiner reduce to a common circle action; the retained full packet has invariant two-dimensional sectors that support Hopf lifts without discarding context.

Rivals: multiple independent slot phases survive; no invariant doublet exists; doublets exist only for the reader operations and fail the additional geometric comparison actions.

The tests will solve all phase-weight equations exactly, determine the generated coefficient group and its invariant projectors, and add the prior four-vertex A4 coefficient action as a hostile extension. A4 is an additional prior geometric-binding hypothesis, not silently another native reader rule. Stationarity means the diagonal weight at a named species/slot is independent of occurrence. Occurrence-dependent transported actions are a separate rival.

SCC obligation: attachment transport on the supplied five-complex-coordinate grammar, preceding any signed-record encoding or global Su-32 route comparison. Neither four independent amplitudes nor a choice of four-mode sector is assigned to the signed wire by this test.

## 1. Operation-derived common phase

Read the actual row permutations from the live source modules:

```
PN       = [3,1,2,0,4]
NE       = [0,4,2,3,1]
P reader = [2,3,0,1,4]
N reader = [0,3,4,1,2]
```

For each species s let `D_s(theta)=diag(exp(i q_sj theta))`, with fixed slot weights. For every native transfer `Pi:s->t`, impose

```
D_t(theta) Pi = Pi D_s(theta).
```

This gives the exact equalities `q_ti=q_s,Pi[i]`. The 15 weights form one connected equality class; the equation matrix has rank 14 and kernel spanned by the all-ones vector. Consequently all five slots and all three species share one phase. This also holds at group level: every diagonal unitary entry is equated, not merely its infinitesimal weight.

PN/NE alone permit separately chosen phases transported between species. The reader constraints remove that freedom. A transported phase on just one slot fails the P reader equation. Uniform opposite phases on N and E fail the linear NE equation directly. Thus opposite weights on the two *derived* columns `[z,Jz]` cannot simply be assigned to independent native P/E fields.

This derives the common U(1) within the stated stationary slot-diagonal class. It selects neither an absolute integer character weight nor an electrical charge. Occurrence-dependent phase tables can instead be transported with the coefficient permutation; they are not classified by this stationary calculation.

## 2. Two invariant doublets, derived without choosing active contrasts

Use the P coefficient reference and set

```
A = P-reader
B = PN^-1 (N-reader) PN
C = A B.
```

The exact matrices satisfy

```
A^2=B^2=I, C^5=I, A C A=C^-1.
```

Their generated coefficient group has ten elements: D5. Its action on ordered slot pairs has three orbits, so the complex matrix commutant has dimension three. These algebraic compositions classify the supplied intertwiners; they do not assert that every abstract group word is an admitted geometric path.

Let `S=C+C^T`, `Q0=J5/5`, and

```
a=(sqrt(5)-1)/2,
b=-(sqrt(5)+1)/2,
Q1=(S-b I-(2-b) Q0)/(a-b),
Q2=I-Q0-Q1.
```

Exact arithmetic verifies that these are mutually orthogonal Hermitian projectors of ranks `1,2,2`, each commuting with A and B. Q0 is the **uniform five-slot coefficient mode**, not the earlier N active-triple mean `(0,1,1,1,0)/sqrt(3)` and not an identification with a physical return mode.

Transport the projectors to N by PN and to E by `NE PN`. All native intertwiners then satisfy

```
Q_t,k Pi = Pi Q_s,k.
```

The receipt contains explicit rank-two frames, their positive Hermitian metrics, decoders and induced A/B/C matrices. The latter preserve the retained metric. A and B have determinant minus one in each doublet; C has determinant one. No phase is inserted to turn the reflections into SU(2) matrices.

Unlike the old fixed active contrast, these doublets are invariant under the tested reader operations. The full decomposition retains the uniform mode and both doublets; it is lossless on all five coordinates.

## 3. What this supplies for Hopf

Each invariant doublet is a two-complex-dimensional Hermitian space. On a positive fixed-norm shell its common-phase quotient is precisely `S3 -> CP1`. The native reader matrices act unitarily and commute with that phase action. This gives two explicit reader-compatible Hopf-sector candidates inside the existing coefficient packet.

It does not permit discarding other sectors. Two independent nonzero doublets carry relative phase information: quotienting each separately loses more than quotienting the full packet by its common phase. The uniform mode is also a genuine coordinate. At fixed total norm, the unrestricted five-slot common-phase quotient is CP4, not CP1.

The doublets are not yet the operator's P/E records. The required signed-record encoding and the rule selecting which phase data may be quotiented remain separate maps.

## 4. Two hostile extensions delimit the result

### Native-slot diagonality matters

The operator

```
U=Q0+i Q1-Q2
```

is unitary and commutes with both reader generators, but is not diagonal in the native slots. Hence independent sector phases survive in the larger commutant. Its unitary group is U(1)^3, since the three independent projectors span that commutant. Common phase is unique among stationary **native-slot diagonal** actions, not among all unitary symmetries of the coefficient packet.

### The prior geometric comparison mixes the doublets

`full-field-path-coherence-v1.md` uses a four-vertex A4 coefficient action fixing the fifth context slot. Add that action to C. Exact closure has 60 elements (A5), and its ordered-pair commutant has dimension two, spanned by Q0 and I−Q0. The four-dimensional zero-sum sector then has no invariant two-dimensional summand.

An explicit three-cycle of slots 0,1,2 has nonzero commutator with both Q1 and Q2. Thus neither Hopf doublet extends as a fixed invariant sector under this additional geometric-binding hypothesis. This is not a refutation using an invented native reader: the extra hypothesis and its source are retained separately.

A frame-dependent description might transport the doublet projectors rather than keep them fixed. That requires the actual occurrence-transition maps; choosing them to preserve a desired split would not derive those maps.

## Disposition

The common stationary slot-phase law and two reader-invariant doublets are derived from the current coefficient operations. They replace the previous phase-agnostic reference-only result at this narrower, explicit source domain. The five-slot packet was not reduced to four signed amplitudes or to a single spinor.

The attempted extension to the prior A4 geometric comparisons fails with explicit projector defects. The next substantive test is the actual full-carrier occurrence transition: does it preserve these sectors, transport them as retained subspaces, or mix them? This cannot be decided by another test of the same reader permutations.

The inspected P/E coupling note offers a different candidate, `D(p)=p/conj(p)`, with phase weight two, but its retained arrow equations also admit a frozen-frame interpretation. It therefore does not select a signed-wire comparison law here. The neutral bilinear spinor vertex requires two spinorial inputs and an independently specified neutral output; it is not supplied by the present linear grammar.

## Verification

```sh
uv run --with sympy python research/strominger/checkers/check_su32_native_phase_law.py
uv run --with sympy python research/aspect/scc/scc.py validate research/strominger/scc-models/su32-native-phase-law-v1.json
uv run --with sympy python research/aspect/scc/scc.py check su32-native-phase-law-v1
```

Receipt: `results/su32-native-phase-law-v1/verification.json`. All identities are exact, with projector entries in Q(sqrt(5)). It records source hashes, all 25 slot-weight equations, induced doublet matrices and metrics, independent-phase and geometric-mixing witnesses. Initial fresh run: `structured_command_execution:e_29164_1793122400006973300_21`. No source store, routing rule or renderer was modified.
