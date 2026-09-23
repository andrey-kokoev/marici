# Sparse cyclic Farkas proofs need source-dependent supports

The seven admitted whole-fibre packets used just two cyclic inequalities per noncyclic inequality. Two particular supports happened to be identical across all seven packets:

- minor 27 from cyclic edges 12 and 23;
- minor 37 from cyclic edges 23 and 34.

It would be tempting to promote those support choices to a universal symbolic formula. Two **strictly positive** exact source targets falsify that promotion. The independent verifier checks every one of their 21 source minors strictly positive, reconstructs the complete affine coefficient identities, and finds a negative multiplier in each formerly stable support:

- for minor 27, the 12/23 coefficient of minor 12 is `-135991738877/97044484259840`;
- for minor 37, the 23/34 coefficient of minor 34 is `-12097266115057/967681985478656`.

Neither failure refutes cyclic sufficiency. On the SAME respective targets, cyclic edges 67 and 17 provide exact two-edge certificates with both coefficients positive and constant zero. Thus the correct certificate system must switch support as the admitted source moves between chambers; exact source binding is essential.

This is a useful narrowing of the universal proof task. One cannot simply prove fourteen fixed algebraic identities using two preselected cyclic edges each. Instead, one must cover the admitted positive-source parameter space by **support chambers** and prove that for every chamber at least one nonnegative two-edge representation exists for each of the fourteen noncyclic minors. The already established compact cyclic fibre ensures such a certificate, when valid, proves the entire fibre inequality. Finite checked supports are not a parameter-space cover.

Run:

    python research/nima/checkers/check_seven_point_farkas_support_chambers.py
    python research/nima/checkers/verify_seven_point_farkas_support_chambers.py

Artifacts: `research/nima/results/seven-point-farkas-support-chambers*.json`.
