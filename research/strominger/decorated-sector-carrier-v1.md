# Four sector indices with full continuous fibers

## Frozen successor contract

Replace neither the field nor the task. Test the explicit carrier

    V -> im(E11) direct-sum im(E10) direct-sum im(E01) direct-sum im(E00),
    x |-> (E11 x,E10 x,E01 x,E00 x),

where E11=LG, E10=L-LG, E01=G-LG, E00=I-L-G+LG are the actual commuting
metric-orthogonal source projectors. Retain vectors, complex phases, the source
metric and fixed reference conventions, not just four labels or four norms.
The candidate inverse is addition. This is a proposed lossless coordinate
presentation, not a new four-state physical system.

## Exact tests

Freshly replay the PN task and its full source coefficient checks. For both P
and N, check all16 projector products, self-adjointness in the actual metric,
nonzero ranks, sumI, and sum(E_i^sharp E_i)=I. These operator identities prove
both inverse laws on the declared sector ranges and exact norm preservation
for arbitrary inputs, not just sampled states.

P ranks in order11,10,01,00 are1,11,2,22. N ranks in that same order are1,2,11,22.
For the existing coarse PN isomorphism S, projector-role exchange implies
F_(b,a) S=S E_(a,b). Thus S maps sector vectors with their ranks intact when
role labels are exchanged. This is a typed map between P and N presentations,
not an arbitrary permutation of unequal-rank sectors in one fixed field.
Use the freshly verified role identities to derive this for every input; do
not claim to have checked all dense products involving S if factor identities
were the actual certificate.

For any field endomorphism A the sector block matrix is E_i A E_j, and
summing all16 blocks recovers A. This representation preserves composition
because sum E_i=I. For the checked proper P rotations and projector reflections,
all off-diagonal blocks vanish. No assumption is made that every native
operation preserves each sector.

## Task and negative controls

Full sector vectors reconstruct the full field and therefore its fixed PN
route residual and any specified readout. On aligned inputs alone, the
squared residual is3 times the relative-sector norm squared. Weights suffice
for that scalar, not for phase-sensitive residual vectors: the two normalized
states (u+v)/sqrt2 and(u-v)/sqrt2 have identical sector weights but distinct
full fields and opposite nonzero route residuals. Retain this control.

The strict geometric-PN conversion remains impossible. A reversible coordinate
decomposition does not repair the source C3 obstruction. No E transport,
external sewing, physical constructor, new graded multiplication or Monster
identification follows.

## Interpretation and next test

The proper meaning of four here is a four-element index set of continuous
subspaces; the total field dimension remains36. The next step is to classify
which index permutations lift within one fixed decorated object, separately
from P/N role exchange and transport between differently labelled presentations.
The earlier discrete-carrier branches are not silently revived.

Replay: `python research/strominger/checkers/check_decorated_sector_carrier.py`.
Receipt: `results/decorated-sector-carrier/verification.json`.
