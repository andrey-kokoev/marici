# Seven admitted fibres have sparse whole-polygon cyclic certificates

The possible reduction from 21 source-minor inequalities to seven cyclic ones has moved from pointwise polygon comparison to **exact whole-fibre proofs for seven independently frozen admitted targets**, one in each of seven source sign gauges.

On a fixed target fibre write every minor as `L_ij(a,b)=c_ij+a*A_ij+b*B_ij`. For each of the fourteen NONCYCLIC minors, the constructor supplies two cyclic edges `p,q` and exact nonnegative rational numbers `alpha,beta,gamma` satisfying the full affine identity

    L_ij(a,b)=alpha*L_p(a,b)+beta*L_q(a,b)+gamma.

Therefore cyclic nonnegativity implies that noncyclic inequality at **every point of the entire fibre polygon**, without checking samples or vertices. Each of the seven admitted target packets has fourteen such proofs: 98 independently replayed identities. This is a sparse exact Farkas certificate (two cyclic normals plus a constant), not an asymptotic or numerical claim.

The separate verifier reconstructs the moment-curve kernel from alternating binomial coefficients, checks that all 21 source minors at every bound source are STRICTLY positive, checks each of the three affine coefficients for all 98 identities, confirms the full fourteen-minor inventory, and rejects four controls: corrupted multiplier, negative constant, missing minor and changed source. It also independently checks that an UNADMITTED target has a feasible cyclic-only fibre point `(-1/20,1/20)` with noncyclic minor 16 equal to `-43/20`. Admission remains a necessary precondition.

This is still not a uniform seven-cyclic-minor theorem for every admitted target. The seven certificate supports and coefficients can vary with target; neither the 98 identities nor the 14,000 adversarial exact passes replace a parameter-uniform sign proof. A productive next mathematical step is to classify which two-edge Farkas supports can certify each noncyclic minor and prove their nonnegative constants throughout the corresponding admitted-target chambers. The already proved cyclic-polygon boundedness makes that an exact finite-active-set problem.

Reproduce:

    python research/nima/checkers/check_seven_point_cyclic_farkas_packets.py
    python research/nima/checkers/verify_seven_point_cyclic_farkas_packets.py

Packets: `research/nima/results/seven-point-cyclic-farkas-packets.json` and `seven-point-cyclic-farkas-verification.json`.
