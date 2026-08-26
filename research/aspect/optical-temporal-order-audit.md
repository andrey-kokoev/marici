# Optical audit of physical and removable order

## Question

How can an experiment distinguish physically meaningful order from an ordering introduced only by description or coordinate choice?

## Criterion

Swapping two constructors is operationally removable only when their continuation maps commute on the admitted state family. Comparing one endpoint intensity is insufficient: equal scalar records can hide different continuation states.

The finite audit uses three familiar polarization experiments.

## Crossed-polarizer insertion

Prepare horizontal polarization. The word horizontal--diagonal--vertical transmits one quarter of the prepared intensity. The word horizontal--vertical--diagonal is extinguished at the crossed pair and remains zero. These are different constructor words, and their order is physically observable at the endpoint.

## Equal transmission, different continuation

Apply horizontal then diagonal filtering to a maximally mixed input, and compare it with diagonal then horizontal filtering. Both selective words have total probability one quarter. Their surviving polarization states differ: one is diagonal and the other horizontal. A final horizontal analyzer transmits them with conditional probabilities one half and one, respectively.

This is the crucial hostile against classifying order from endpoint intensity alone. The continuation, not merely its trace, must be compared.

## Sequential same-carrier forgetting

Use nonselective polarization measurements along horizontal/vertical and along the linear-polarization axis whose Bloch vector is three-fifths X plus four-fifths Z. On a horizontal input, applying the two dephasing channels in opposite orders gives a nonzero off-diagonal residual of minus six twenty-fifths. The deletion square therefore fails.

This is the optical realization of Nima's exact ordered-forgetting gate in `research/nima/boolean-forgetting-requires-authorized-instrument-commutation.md`.

## Independent-port forgetting

Lift the same channels to different photons. One acts on the first tensor factor and the other on the second. They commute on all sixteen matrix units of the two-photon operator space. Different inertial descriptions may order spacelike records differently without changing the continuation or any joint record probability.

## Interpretation

The audit does not decide whether time is fundamental or emergent. It establishes a narrower operational distinction:

- noncommuting continuation maps make order physical;
- commuting independent-port maps make that pairwise ordering removable;
- equality of one scalar record never proves commutation.

The mixed delayed-choice case then becomes transparent. Remote signal and marker instruments commute, but their stable records must exist before a later classical join can condition them.

## Claim boundary

This is an exact finite ideal-polarization theorem. It does not include loss, detector thresholds, finite extinction, depolarization, relativistic detector dynamics, or a metaphysical theory of time.

## Verification

Run:

```text
python research/aspect/checkers/check_optical_temporal_order_audit.py
```

The checker is dependency-free and uses exact rational matrices.
