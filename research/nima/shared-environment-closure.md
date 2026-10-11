# Shared-environment closure generates a quartic interaction

## Question

The operator points to the Machian response/back-reaction calculation as a proposed organizing principle for proton-versus-hydrogen composition. Test whether allowing one common surrounding system to readjust generates a pair correction, instead of inserting that correction into a readout.

## Conjecture and named rivals

Conjecture: joint environmental closure produces a nonadditive term even when neither isolated source contains an explicit pair interaction. Rival 1 freezes the environment and treats its effect as an additive external potential. Rival 2 inserts a quartic coefficient directly without deriving it from a response. The test distinguishes these mechanisms at fixed input geometry, not their physical identifications.

## Declared source and environment

Reconstruct the existing tetrahedral collective mode from the two seed rotations and the triangle coefficients. Normalize its squared norm 80 to one. The proposed dual witness has identical block intensities. Retain the five previous partitions: whole mode, four parent faces, twelve triangles, three axes, and thirty-six ports.

Let a and b be the two intensity profiles, s and t the squared source amplitudes, and x the real environment response. Choose a positive quadratic stiffness D and a density coupling of strength g:

    E(s,t,x) = E_p(s) + E_e(t) + x^T D x/2 - J^T x,
    J = g(s a + t b).

This functional is a new declared model, not a deduction from the arrow count. Both baselines cancel in the comparison below. Sources are held fixed while the environment is minimized; global stability under arbitrary source-amplitude variation is not asserted.

Two frozen environment choices are tested: D=I, and D=I-eta A where A is complete-graph adjacency and eta=1/[2(m-1)] for m>1 blocks. The latter has uniform eigenvalue 1/2 and contrast eigenvalue 1+eta, hence is positive. Its feedback row sum is 1/2. For one block, use D=I. These choices do not use a mass target.

## Exact closure and induced interaction

Stationarity gives

    D x = J,
    x = D^-1 J,
    E_closed = E_p + E_e - J^T D^-1 J/2.

The same D is used for proton alone, witness alone, their pair, and neither. Inclusion-exclusion therefore gives

    Delta = -g^2 s t a^T D^-1 b.

Because s and t are squared amplitudes, this term is quartic in the source amplitudes. It is produced by eliminating the shared response variable; no explicit quartic term was inserted. For this model's same-sign, equal intensity profiles and positive inverse response, Delta is negative. Changing one source coupling sign reverses it.

The inverse D^-1 is also the convergent repeated-return series sum_k (eta A)^k. This supplies an operator-level analogue of a scalar response denominator such as the proposed Machian Z factor. It does not derive that factor's numerical coefficients.

## Risky tests and disposition

The checker verifies stationarity, exact square completion and the unique environmental minimum. Eight feedback iterations satisfy the contraction error bound against the exact inverse solution. Changing either source amplitude gives the required quartic scaling. Doubling g multiplies the cross-term by four.

The frozen-environment rival gives exactly zero mixed term, even when frozen at the proton-only response. Joint readjustment instead gives a nonzero negative term. Thus environmental readjustment, rather than a fixed external offset, supplies the interaction in this model. An opposite-sign source control reverses the interaction, demonstrating that its sign is not fixed by the tetrahedral count alone.

No value of g, energy conversion, or stiffness has been selected by WG. The next missing object is that source-derived coupling law. The calculation establishes a self-consistent mechanism for quartic binding, not a numerical hydrogen mass.

## Verification

Dependency-free exact rational checker:

```text
python research/nima/checkers/check_shared_environment_closure.py
```

Results: `research/nima/results/shared-environment-closure.json`. The result file contains all ten partition/environment combinations and exact fractions. Invocation: structured-command execution `structured_command_execution:e_32876_1791216576344108800_8`. No graph admission, ledger publication, commit or push is claimed here.
