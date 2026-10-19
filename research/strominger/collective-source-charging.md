# Collective occupation does not rescue the source Gauss charging branch

## Test

The October 11 Gauss-response model failed in the single-occupation sector. Test its symmetric many-occupation extension, retaining the same source kinetic operators K, inverse grounded Laplacians C, boundary ports and common empty reference:

    H_s = dGamma(K_s) + (beta/2) sum_ij C_s,ij n_i n_j + (eta/2) M_s².

Here M_s=sum_i n_i is fixed within each tested sector. The vacuum has M=0 and energy zero. All sectors share beta>0 and eta>=0. The frozen fixture is the prior beta=3/5, eta=1/5.

This is a specific symmetric-occupation model. It introduces no fitted offsets or arrow multiplier. It does not derive occupation number or particle statistics.

Contract: `contracts/collective-source-charging.json`.

## Retain occupation variance

For M particles in a kinetic-zero-mode condensate with site probabilities rho,

    <n_i n_j> = M(M-1) rho_i rho_j + M rho_i delta_ij,
    <n^T C n> = M(M-1) rho^T C rho + M sum_i rho_i C_ii.

Replacing this by M² rho^T C rho would lose variance. The checker verifies the formula against every two-particle occupation configuration on all three actual source graphs.

Positivity of K makes any lower bound on the diagonal charging operator a ground-energy lower bound. A condensate in a zero mode gives a variational upper bound including the full kinetic operator, without discarding modes or diagonalizing a truncated subspace.

For any sharp occupation, Cauchy-Schwarz in the C metric gives

    n^T C n >= M² / (1^T C^-1 1) = M² / number_of_exterior_ports.

The source ground weights and ports are retained from the existing matter/link adapter. The elementary zero-mode condensate is constructed from the first column of (I+Q)/2; its site probabilities are (1/2,1/6,1/6,1/6).

## Result 1: equal occupation fails for every M

The actual proton graph has C_ii=29/105, row sums one and a uniform kinetic zero mode. Its condensate gives

    proton charging upper bound = M²/12 + 27M/140.

For the elementary graph C=(I+ones)/5, exact sharp occupations give

    elementary charging lower bound = (M² + min sum_i n_i²)/5.

The integer minimum distributes M as evenly as possible over four modes. For M>=2 it is at least M²/4, and

    M²/4 - (M²/12 + 27M/140) = M(70M-81)/420 > 0.

For M=1, 29/105 < 2/5. The common eta*M²/2 term cancels. Consequently

    E_proton(M) < E_elementary(M)

for EVERY M>=1 and EVERY common beta>0, eta>=0. Merely adding equal collective occupation cannot reverse the failed hierarchy.

## Result 2: source-size occupation also fails

As a separately declared alternative, take one total occupation per native source mode: M_p=12, M_b=18, M_e=4. The occupation distribution remains dynamical; this does not impose one occupied particle at each site.

At the existing fixture, certified full-sector bounds are:

| Sector | Ground-energy lower bound | Ground-energy upper bound |
|---|---:|---:|
| Proton | 18 | 6543/350 |
| Belt | 81/2 | 5981608400077/137051733000 |
| Elementary | 14/5 | 76/25 |

These are model-unit bounds, not approximated exact eigenvalues. They require no finite boson cutoff because the fixed occupation sectors are finite and the inequalities apply to their entire Hilbert spaces.

For all common positive coefficients,

    E_p/E_e <= max[(501/35)/4, 12²/4²] = 9.

The separately loaded reference is 1836.152673. Thus this alternative also cannot explain the joint mass comparison, irrespective of the neutron splitting. Its occupation ratios were fixed from mode dimensions, not chosen to match the reference.

## Consequence

This extends the earlier single-occupation exclusion: neither equal collective occupation nor the source-mode-size prescription repairs the same electrostatic branch. A different sourced occupation rule, kinetic/charging form or boundary interaction is needed. Choosing occupation numbers backward from 1836 would not supply that rule.

## Verification

```sh
python research/strominger/checkers/check_collective_source_charging.py
```

Six checks passed. They cover exact two-particle quantum variance on three graphs, integer elementary minima through M=12, the algebraic all-M bound and the source-size ratio exclusion. The all-M proof is the displayed inequality, not extrapolation from the finite checks.

Receipt: `results/collective-source-charging.json`, including source hashes and rational bounds. Prior source hashes were checked, benchmark data opened after constructing the bounds, and shared stores left unchanged.
