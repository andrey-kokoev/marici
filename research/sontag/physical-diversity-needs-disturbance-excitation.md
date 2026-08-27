# Physical diversity needs disturbance excitation

## Question

What observation distinguishes two separately stored record copies from two copies that actually expose an additional disturbance direction?

## Frozen model

Take two binary record errors, two candidate binary disturbance inputs, and a static linear response over the field with two elements:

`e = B d`.

Compare

```text
B_common  = [1 0]    B_diverse = [1 0]
            [1 0]                [1 1]
```

The first matrix has rank one. The second has rank two. Both copies in both models occupy distinct registers; register multiplicity says nothing about the response matrix.

## Attack

A baseline and the first excitation `d1 = (1,0)` do not distinguish the models. Both return `(1,1)`. Thus one active probe can still mistake rank two for rank one.

The second independent excitation `d2 = (0,1)` breaks the alias:

```text
                 d1       d2
B_common       (1,1)    (0,0)
B_diverse      (1,1)    (0,1)
```

With an unknown static output offset, the baseline removes the offset; the two independent excitations then recover the two columns of `B`. In this frozen model, baseline plus two probes identifies the response matrix, and its rank establishes whether the apparatus exposes a differential disturbance mode.

## What rank does not prove

Rank two is not absence of common cause. `B_diverse` still maps `d1` to the diagonal error `(1,1)`. It proves that a second, differential direction exists; it does not prove stochastic independence, bound the probability of the diagonal direction, or justify a majority-vote error rate.

So a physical-diversity certificate needs more than copy lineage. At minimum it carries:

- declared disturbance ports and admissible probes;
- baseline and response matrix;
- rank and response subspace;
- explicit identification of diagonal common-mode responses;
- a joint law or robust bounds on disturbances if reliability probabilities are claimed;
- lineage from response channels to the record copies.

The control-theoretic distinction is between state duplication and input-channel diversity. The former is a storage fact. The latter is an identified input-output property.

## Relation to Marici objects

A closed Marici packet that claims diversity cannot close merely over two record identities. It must close over the experiment that identified their disturbance coupling, plus the assumptions under which that identification transports. Otherwise the packet transports multiplicity while leaving the relevant joint failure carrier open.

This also explains the temporal analogue: separated time bins can remain coupled through a hidden memory state. An active reset is evidence about the state transition; passive spacing is not.

## Reproduction

Run:

```text
python research/sontag/checkers/physical_diversity_disturbance_excitation.py
```

Expected result: 8 of 8 exact checks pass. The checker writes `research/sontag/results/physical_diversity_disturbance_excitation.json`.

Verified locally: 8 of 8 checks passed. The result and reply to the detector-memory analogue were admitted to the epistemic graph at event `ev-000000006155-5607c64d-610a-40cf-9036-32c52969064c`. Graph admission records review and coordination, not truth certification.
