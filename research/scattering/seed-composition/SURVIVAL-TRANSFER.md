# Exact survival decay and a nonconstant algebraic conditioning profile

**New batch, iteration 9 of 10.**

**Strength:** rational decay certificate, exact class/period analysis and algebraic backward Perron profile. Not a physical lifetime, probability law or source-authorized conditioned controller.

[Previous weight comparison](CONDITIONED-HISTORY-WEIGHTS.md) · [Checker](check_survival_transfer.py) · [Receipt](results/survival-transfer.v1.json)

## 1. Fresh transfer and uniform decay

Use the exact rational backward survival transfer from the preceding turn:

    q_0=1,
    q_(n+1)(s)=sum_t K(s,t)q_n(t),
    K(s,t)=1/(m(s)d(s)) for each allowed controller target t.

All row sums are at most one. Direct exact multiplication gives maximum row sum of K^3 equal to **1/2**. Therefore, at every finite depth,

    0<q_n(s)<=2^(-floor(n/3)).

Survival weight tends to zero uniformly; the total first-reject counting weight tends to one. Forced contexts may retain survival one at short horizons, as the previous turn observed, but there is no indefinitely surviving class with full weight.

This is decay with controller-event depth, not physical elapsed time or an emitted-particle rate.

## 2. Reducibility and periodicity checked before convergence

The eighteen states form two closed strongly connected classes:

    (0,1,2,3,4,5,12,13,14),
    (6,7,8,9,10,11,15,16,17).

Graph reflection exchanges them. Each nine-state block has a strictly positive nineteenth power, checked through integer adjacency products. Thus both blocks are primitive (period one). There is no unique global class; mixtures of the two remain possible.

For either block, exact characteristic calculation gives

    lambda^4*(lambda^5-lambda/32-1/16).

Its Perron root rho is the unique positive solution of

    32*rho^5-rho-2=0,
    3/5 < rho < 5/8.

The rational endpoints have opposite polynomial signs. The polynomial decreases to its sole positive critical minimum and then increases, so it has exactly one positive root. Block primitivity ensures all other eigenvalues have strictly smaller modulus.

## 3. Exact positive backward profile

Normalize h(0)=1. In the first-class order above,

    h=(1, 2*rho, 1/(4*rho^2), 1/(2*rho^3),
       1/rho, 1, 1/(2*rho), 1/rho^2, 2*rho).

The second class is its reflection, with h(9)=1. Every entry is positive. The checker verifies Kh=rho*h algebraically modulo the quintic, including the exact reciprocal identity

    1/rho = 16*rho^4-1/2.

This is an explicit nonconstant profile, not a numerical eigenvector fit.

Perron-Frobenius applied to each primitive block gives, for the all-ones terminal seed used by survival accounting,

    q_n/rho^n -> c*h, c>0,
    q_n(s)/q_n(0) -> h(s).

Reflection makes the two coefficients equal for this symmetric seed. General terminal weights may give different positive coefficients in the two closed classes. The result is a **backward survival profile**, not an assertion of a unique global forward stationary distribution.

## 4. Long-horizon conditioning changes target weights

The finite-horizon next-state counting weights conditioned on acceptance for N steps are

    K(s,t)*q_(N-1)(t)/q_N(s).

Their limit is the Doob reweighting

    Khat(s,t)=K(s,t)*h(t)/(rho*h(s)).

Kh=rho*h makes every row sum one. The reweighting preserves allowed support and reflection, but generally differs from normalizing only the local available primitive count. It favors targets with different future survival profiles.

For instance, context 1 has two allowed targets, 2 and 3. The controller-only split weights them equally. The limiting conditioned ratio is

    Khat(1,3)/Khat(1,2)=h(3)/h(2)=2/rho != 1.

Thus local controller-only reset and conditioning on long future acceptance are distinct constructions. Neither is derived physical control. These rational/algebraic counting weights are not promoted to emission probabilities or a physical preparation law.

## 5. Next test and retained boundary

Pull this nonconstant profile back through the selected initial mode frame. Test whether its induced metric can be removed by one scalar or by a normalization preserving the reference mode step. That checks the surviving mode distortion in the asymptotic limit rather than relying on the depth-three finite scalar exception.

All original path and first-reject records remain retained; the profile is an observer of that accounting. No conditioned record erasure is admitted. The scientific root stays null, and formal work-net/downstream contracts are unchanged.

## Reproduce

```sh
python research/scattering/seed-composition/check_survival_transfer.py
python research/scattering/seed-composition/check_survival_transfer.py --check
python research/scattering/seed-composition/check_conditioned_history_weights.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

The checker uses exact rational matrix arithmetic and polynomial remainder identities. The convergence claim uses the stated classical Perron-Frobenius theorem with explicitly checked hypotheses, not a new machine-formal admission. Prerequisites are recomputed; only the new receipt is written and `--check` is read-only.
