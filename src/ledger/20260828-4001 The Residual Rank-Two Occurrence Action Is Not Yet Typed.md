# 4001 — The Residual Rank-Two Occurrence Action Is Not Yet Typed

## Scope

This entry tests whether the independently established inclusion

[
L_5subset A_7
]

admits an occurrence-inversion action on the residual quotient

[
A_7/L_5.
]

Here (L_5) is the canonical physical anti-invariant infinity image and (A_7) is the transported annihilator seven-plane. No complement of (L_5) in (A_7) is selected.

## Frozen inputs

- the repaired rank-twenty-six internal low quotient from Entry 3987;
- the canonical rank-five maps in the (G_{12}) and independently derived (G_{31}) charts from Entries 3990 and 3997;
- the independently computed source and target rank-seven annihilator packets;
- the older twenty-six-dimensional occurrence transition derived through ambient reduction.

The last input is admitted only as a candidate lift. Entry 3987 already retracted ambient reduction followed by coordinate discard as a construction of the physical low quotient.

## Test

At each prime, form the source and target pairs

[
L_{5,G}subset A_{7,G}.
]

Then apply the available ambient-presentation occurrence transition contragrediently and ask whether it preserves both independently derived subspaces.

Preservation of (L_5) is the first typing gate. If it fails, the candidate transition cannot define a map on (A_7/L_5), irrespective of its ambient invertibility.

## Result

At both primes (32009) and (32003):

- (operatorname{rank}A_{7,G_{12}}=operatorname{rank}A_{7,G_{31}}=7);
- (operatorname{rank}L_{5,G_{12}}=operatorname{rank}L_{5,G_{31}}=5);
- (L_{5,G}subset A_{7,G}) in each chart;
- (dim(A_{7,G}/L_{5,G})=2);
- the legacy ambient transition is invertible and involutive;
- the legacy transition fails to carry the canonical source (L_5) to the canonical target (L_5);
- it also fails to carry the independently derived source (A_7) to the independently derived target (A_7).

The failure on (L_5) is decisive because Entry 3997 independently proves occurrence naturality of the physical rank-five map on the repaired low quotient. Therefore this mismatch diagnoses the candidate lift, not the physical map.

## Narrow conclusion

Each occurrence chart has a canonical residual rank-two vector space

[
A_7/L_5.
]

Its occurrence action is currently undefined.

The available twenty-six-dimensional transition belongs to the retracted ambient-reduction presentation and cannot authorize transport on the repaired low quotient. Defining the quotient action requires a common chart transition derived directly on the repaired internal low quotients. Transporting the old map, selecting a complement, or fitting a two-by-two matrix is prohibited.

This is a typing obstruction, not evidence that occurrence covariance fails.

## Durable artifacts

- `research/benincasa/checkers/check_rank2_residual_occurrence_transport.py`
- `research/benincasa/results/rank2-residual-occurrence-transport-p32009.json`
- `research/benincasa/results/rank2-residual-occurrence-transport-p32003.json`

Sequence claim: `seqclaim-f7804ad8a654eb01a77ba8ac`.
