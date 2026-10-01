# Embedding comparison coordinates into the fixed carrier tower

Choose seven of the twelve stabilizer probes, labelled f0,...,f6. The two
four-state carriers use {f0,f1,f2,f3} and {f0,f4,f5,f6}. They share f0.
Define b_i=f_i-f0 for i=1,...,6, and map a comparison coordinate vector q to
sum_i q_i b_i. This is an explicit coefficient interpretation of the prototype
potentials. It is a bridge choice; the earlier prototype did not specify this
interpretation or a preferred selection of seven carrier probes.

The ambient normalized Gram is G12=10I+J. Therefore

    <b_i,b_j> = 10(delta_ij+1),
    M = 10(I6+J6),
    M^-1 = I6/10 - J6/70.

This embeds the comparison space injectively into V7 inside V12, provided the
retained ordering places these seven probes first. The six contrast vectors
are independent. Their span cannot fit injectively into V4; descent below V7
requires restriction and records. A pair of four-state carriers sharing one
state has seven distinct labels, so the comparison state is not simply one
four-coordinate carrier state.

## Induced update rule

For a comparison row r, let d=M^-1 r and n=r^T M^-1 r. Projection onto
r^T q=0 using the induced Gram metric is

    q_next = q - d (r^T q)/n.

The lost budget is (r^T q)^2/n. With record z, define a=(r^T q)/n and

    q_next = q + d(z-a),
    z_next = a.

This preserves q^T M q+n z^2 and is an involution. An empty record reproduces
the metric projection. Thus the restriction geometry and comparison updates
can use the same quadratic form under this embedding.

## Changes from the previous dynamics

The prototype used the Euclidean metric I6. The bridge induces 10(I6+J6),
which is not a scalar multiple of I6. The projection operators therefore change.
For the test seed, 82 of 153 projected outputs differ. Previous numerical
sweep spectra and decay rates belong to the Euclidean prototype and must be
recomputed for the induced metric.

The broad structural results survive: metric-orthogonal record exchange is
reversible; record attenuation exports a nonnegative budget; full-rank comparison
constraints with strict attenuation settle to zero without driving. Physical
energy normalization, particle labels, and the preferred embedding/order remain
unestablished. The identification is a concrete shared geometry, not yet a
physical Hamiltonian or a unique carrier law.

Verification:

    python research/nima/checkers/check_comparison_tower_embedding.py

Exact rational arithmetic checks the induced norm against the ambient norm,
inverse metric, all comparison projections, their budget identities, populated
record exchange and reversal, and disagreement with the old Euclidean updates.
