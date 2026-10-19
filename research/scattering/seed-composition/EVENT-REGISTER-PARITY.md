# Joint event-register parity does not imply an odd conditional system state

**New batch, iteration 4 of 10.**

**Strength:** exact labelled output, parity recombination and coefficient second-moment tests. Not a physical instrument, Born rule or authorized event-record erasure.

[Previous controller audit](CONTROLLER-REFLECTION.md) · [Checker](check_event_register_parity.py) · [Receipt](results/event-register-parity.v1.json)

## 1. Fresh labelled carrier

The supplied eighteen-state controller is reflection-covariant, but its individual primitive branches leak parity. This turn retains the complete event label

    (displayed pair, owner-labelled primitive ID, macro completion flag).

There are sixteen distinct labels. Let T_l be the exact matrix for label l. The event-bearing output is

    Vx = direct sum_l T_l x.

It has 288 coordinates (sixteen labels times eighteen system coordinates). This redundant full register is convenient for checking symmetry; it is not a claim that all coordinates are reachable.

If J reflects controller states and r reflects event labels, then joint reflection acts on both indices:

    (l,s) -> (r(l),J(s)).

The checker verifies VJ=J_joint V exactly. Hence an odd input yields a joint odd output. This preserves the statement of covariance without confusing the register transformation with the system transformation alone.

## 2. What each fixed-label record contains

Each event label fixes a displayed pair, so T_l x is supported in that pair's system coordinates. Reflection takes that support to the other pair. Thus any nonzero conditional record has both even and odd system components, with equal squared ordinary counting norms:

    ||E_even T_l x||^2 = ||E_odd T_l x||^2 = ||T_l x||^2/2.

The checker verifies this as a Gram-matrix identity for every label restricted to arbitrary odd inputs. Each conditional map has rank one on the odd input subspace; both projected components also have rank one. Nonzero odd inputs can yield zero in a particular branch, so the statement concerns nonzero conditional outputs, not every input in every branch.

The factor one-half is a coordinate-counting identity, **not** a derived emission probability. Joint oddness is compatible with these conditional system records because reflection exchanges labels as well as system coordinates.

## 3. Retain both reflected-label recombination records

For an odd input and one reflected label pair, put

    y=T_l x, y_ref=T_r(l) x=-J y.

Define

    s=(y+y_ref)/2, d=(y-y_ref)/2.

Then s is system odd and d is system even. They reconstruct both labelled outputs by

    y=s+d, y_ref=s-d.

Their counting norms obey

    ||y||^2+||y_ref||^2 = 2(||s||^2+||d||^2).

The factor two reflects the unnormalized mean/detail convention; the code does not claim that merely stacking s and d is an isometry without this weight. On odd inputs, s and d have equal counting weight. Both channels are nonzero on the tested domain.

In system/register language, the system-odd channel accompanies register-even recombination; the system-even channel accompanies register-odd recombination. Selecting only the first requires an additional operation and leaves the other record to be accounted for. Joint parity conservation does not itself perform that selection.

## 4. Distinguishable-label discard is not coherent summation

The aggregate controller is P=sum_l T_l. Coherently summing the coefficient records yields Px, which remains odd for odd x.

Compare instead the formal second-moment record

    B=sum_l (T_l x)(T_l x)^t.

This is a coefficient-level analogue of forgetting distinguishable labels, not an assertion that V is a physical measurement instrument. For the exact witness x=e_0-e_J(0), the checker finds:

- B commutes with J;
- B has nonzero even and odd system blocks of equal trace;
- B is not (Px)(Px)^t.

Thus invariant second moments do not mean support exclusively in the odd sector. In addition, V^t V is not the identity, and P^t P differs from V^t V. Neither labelled output nor coherent aggregate is promoted to a normalized physical channel in the counting metric.

## 5. Keep source history, not just event summaries

The labelled endpoint map V has rank sixteen, not eighteen. It still loses the same two predecessor-difference directions as the predictive quotient. Appending the existing residual rows for contexts (1,14) and (10,16) gives rank eighteen; V kills both residual directions.

Accordingly the original retained paths and difference records remain required. An event register alone is not the full assembly ledger, even though it keeps more information than aggregate P. This turn neither drops rejected controller histories nor replaces the source ledger with V.

## 6. Result and next test

Aggregate odd continuation requires a recombination of distinguishable label records. Joint covariance supplies no authority for coherent erasure, selecting register parity or independently preparing a physical odd system state.

Next test whether any common positive controller metric can make the distinguishable event branches isometric or scalar-weighted isometric on the selected sector. Exact rank restrictions must be checked before fitting a metric. Retain event labels and provenance, and distinguish possible normalization of the full labelled map from an invariant metric for its coherent aggregate.

The scientific root remains null; physical metric, measurement and preparation gates stay open. Existing formal contracts are unchanged.

## Reproduce

```sh
python research/scattering/seed-composition/check_event_register_parity.py
python research/scattering/seed-composition/check_event_register_parity.py --check
python research/scattering/seed-composition/check_controller_reflection.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

All matrices, ranks, Gram identities and witnesses are exact rational calculations. Prerequisites are recomputed; the checker writes only its own receipt and compares read-only under `--check`.
