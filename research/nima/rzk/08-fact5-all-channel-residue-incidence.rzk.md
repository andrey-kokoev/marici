# All-channel five-point biadjoint residue incidence

This module extends the channel-13 result to every planar channel.  The ten
nondegenerate two-spines are exactly the ten incidences between five channels
and the two cubic diagrams containing each channel.

```rzk
#lang rzk-1

#data MariciFact5Channel
  := marici-channel-13
  | marici-channel-14
  | marici-channel-24
  | marici-channel-25
  | marici-channel-35

#data MariciResiduePresence
  := marici-residue-absent
  | marici-residue-present
```

The complete incidence table is computed on channel-term pairs.

```rzk
#define marici-fact5-residue-presence
  ( channel : MariciFact5Channel)
  : MariciFact5PlanarCubicTerm → MariciResiduePresence
  := match channel
      ( marici-channel-13 ⇒ \ term → match term
          ( marici-cubic-term-13-14 ⇒ marici-residue-present
          | marici-cubic-term-13-35 ⇒ marici-residue-present
          | marici-cubic-term-14-24 ⇒ marici-residue-absent
          | marici-cubic-term-24-25 ⇒ marici-residue-absent
          | marici-cubic-term-25-35 ⇒ marici-residue-absent)
      | marici-channel-14 ⇒ \ term → match term
          ( marici-cubic-term-13-14 ⇒ marici-residue-present
          | marici-cubic-term-13-35 ⇒ marici-residue-absent
          | marici-cubic-term-14-24 ⇒ marici-residue-present
          | marici-cubic-term-24-25 ⇒ marici-residue-absent
          | marici-cubic-term-25-35 ⇒ marici-residue-absent)
      | marici-channel-24 ⇒ \ term → match term
          ( marici-cubic-term-13-14 ⇒ marici-residue-absent
          | marici-cubic-term-13-35 ⇒ marici-residue-absent
          | marici-cubic-term-14-24 ⇒ marici-residue-present
          | marici-cubic-term-24-25 ⇒ marici-residue-present
          | marici-cubic-term-25-35 ⇒ marici-residue-absent)
      | marici-channel-25 ⇒ \ term → match term
          ( marici-cubic-term-13-14 ⇒ marici-residue-absent
          | marici-cubic-term-13-35 ⇒ marici-residue-absent
          | marici-cubic-term-14-24 ⇒ marici-residue-absent
          | marici-cubic-term-24-25 ⇒ marici-residue-present
          | marici-cubic-term-25-35 ⇒ marici-residue-present)
      | marici-channel-35 ⇒ \ term → match term
          ( marici-cubic-term-13-14 ⇒ marici-residue-absent
          | marici-cubic-term-13-35 ⇒ marici-residue-present
          | marici-cubic-term-14-24 ⇒ marici-residue-absent
          | marici-cubic-term-24-25 ⇒ marici-residue-absent
          | marici-cubic-term-25-35 ⇒ marici-residue-present))
```

Each nondegenerate refinement spine determines its middle channel and terminal
cubic diagram.

```rzk
#define marici-fact5-spine-channel
  ( spine : MariciFact5TwoSpine)
  : MariciFact5Channel
  := match spine
      ( marici-spine-13-1314 ⇒ marici-channel-13
      | marici-spine-13-1335 ⇒ marici-channel-13
      | marici-spine-14-1314 ⇒ marici-channel-14
      | marici-spine-14-1424 ⇒ marici-channel-14
      | marici-spine-24-1424 ⇒ marici-channel-24
      | marici-spine-24-2425 ⇒ marici-channel-24
      | marici-spine-25-2425 ⇒ marici-channel-25
      | marici-spine-25-2535 ⇒ marici-channel-25
      | marici-spine-35-1335 ⇒ marici-channel-35
      | marici-spine-35-2535 ⇒ marici-channel-35)

#define marici-fact5-spine-cubic-term
  ( spine : MariciFact5TwoSpine)
  : MariciFact5PlanarCubicTerm
  := match spine
      ( marici-spine-13-1314 ⇒ marici-cubic-term-13-14
      | marici-spine-13-1335 ⇒ marici-cubic-term-13-35
      | marici-spine-14-1314 ⇒ marici-cubic-term-13-14
      | marici-spine-14-1424 ⇒ marici-cubic-term-14-24
      | marici-spine-24-1424 ⇒ marici-cubic-term-14-24
      | marici-spine-24-2425 ⇒ marici-cubic-term-24-25
      | marici-spine-25-2425 ⇒ marici-cubic-term-24-25
      | marici-spine-25-2535 ⇒ marici-cubic-term-25-35
      | marici-spine-35-1335 ⇒ marici-cubic-term-13-35
      | marici-spine-35-2535 ⇒ marici-cubic-term-25-35)
```

Every refinement incidence gives a present residue term.

```rzk
#define marici-fact5-spine-is-residue-incidence
  ( spine : MariciFact5TwoSpine)
  : marici-fact5-residue-presence
      (marici-fact5-spine-channel spine)
      (marici-fact5-spine-cubic-term spine)
    =_{MariciResiduePresence} marici-residue-present
  := match spine
      ( marici-spine-13-1314 ⇒ refl
      | marici-spine-13-1335 ⇒ refl
      | marici-spine-14-1314 ⇒ refl
      | marici-spine-14-1424 ⇒ refl
      | marici-spine-24-1424 ⇒ refl
      | marici-spine-24-2425 ⇒ refl
      | marici-spine-25-2425 ⇒ refl
      | marici-spine-25-2535 ⇒ refl
      | marici-spine-35-1335 ⇒ refl
      | marici-spine-35-2535 ⇒ refl)
```

## Interpretation boundary

The table classifies all 25 channel-term pairs: ten are present and fifteen are
absent.  It proves that the nondegenerate two-spines index every supported
five-point cubic residue incidence.  Numerical propagator values and linearity
of residue remain outside this finite support model.
