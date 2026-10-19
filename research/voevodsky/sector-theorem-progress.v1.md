# Sector theorem: conditional progress, not admission

Executable audit: `checkers/check_sector_theorem_progress.py`.
Result: `results/sector_theorem_progress.v1.json`.

## Source operator ambiguity

The frozen comparison specifies a 100-state native pair plus vacuum, the record,
preparation, relative unit, coupling and readout time. It does not give a formula
for K. The source-bound `native-spinor-pair-adapter.md`, section 4, gives both:

- mismatch L from its two verified spectral projectors;
- the explicitly **optional** cycle-defect extension H=L+2I-T-Tdagger.

The corresponding retained pair operators are
K=H tensor I+I tensor conjugate(H). They have different scalar energies. A unit
ratio of one does not select one of them or define an extra orbital operator.
The checker therefore audits both, without silently selecting either as frozen.
The zero extension of K to vacuum is also an explicit hypothesis here, not a
newly admitted contract fact.

## Exact conditional results

For each chirality, doublet, and the two H choices, the fresh checker establishes
H=Hdagger and KJ=2eJ. With Pi=J Ps Jdagger, this gives

    KPi=2ePi=PiK.

Thus the scalar sector reduces K. The vacuum-extended carrier projector also
commutes with the hypothesized block-diagonal K, as does c-Pi. No complementary
coordinates have been removed. These statements concern the displayed pair
operators, not an arbitrary Hamiltonian with additional mixing terms.

For either projection P, the signed controls give

    (I-R+)/2+(I-R-)/2 = I-P tensor X.

At M=1 the empty-ready record energy is g, provided K has zero vacuum energy.
Subtracting the common g gives H_P=K+N-gP tensor X. On an active scalar sector
with energy epsilon=2e, the record part is

    h = [[0,-g],[-g,1]],
    U_h(t) = exp(-it/2)[cos(omega t)I
               - i sin(omega t)(h-I/2)/omega],
    omega = sqrt(g^2+1/4).

The formula follows by squaring h-I/2 to omega^2 I. The scalar energy contributes
only a common phase exp(-i epsilon t). On the same scalar input the rival's
c-Pi vanishes, so its ready record stays ready. For g=1/2 and t=1:

    p_primary = (1-cos(sqrt(2)))/4,
    p_rival = 0.

The audit uses rational alternating-series bounds (cosine terms through orders
20 and 22), not floating-point equality, to certify 0.21<p_primary<0.22.
This discriminator is conditional on the displayed K choices and absence of
additional mixing terms; it does not fix absolute joint energies or the physical
meaning of the record.

## Remaining obligations and lifecycle

No umbrella or consumer `++` is admitted. The common-resource-accounting attempt
remains active, with its original nonce. Seven of eighteen EU are now charged
(the new attempt costs two), leaving eleven. Checkpoints preserve these charges.

Next required input is an explicit source-K selection, its vacuum reference, and
whether any orbital terms belong in this 101-state matter space. Choosing the
optional extension is a constructor decision, not a theorem inferred from a
relative unit. Any clarification must preserve old receipts and ledger history.
After it is fixed, finish full joint-energy/readout accounting, the variable-phase
contract, and reviewed scoped receipts. An unidentified K is an admission blocker,
not a refutation or a reason to erase already proved rule constructions.
