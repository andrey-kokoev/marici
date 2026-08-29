# Three-polarizer interaction net

This diagram models each polarizer as a state-changing instrument rather than a scalar intensity map. Its visible output is transmitted intensity; its continuation residue is the outgoing polarization state required by the next instrument.

```mermaid
flowchart LR
    classDef carrier fill:#e8f1ff,stroke:#315a8a,stroke-width:1.5px,color:#10243d
    classDef instrument fill:#fff3cf,stroke:#9a6b00,stroke-width:1.5px,color:#3d2a00
    classDef observation fill:#e9f8ea,stroke:#377a3d,stroke-width:1.5px,color:#173619
    classDef residue fill:#f5eaff,stroke:#74409a,stroke-width:1.5px,color:#321743
    classDef erased fill:#f3f3f3,stroke:#777,stroke-dasharray:5 3,color:#333
    classDef result fill:#ffe8e8,stroke:#9a3636,stroke-width:1.5px,color:#431717

    S["Source polarization<br/>state rho; intensity I0"]:::carrier

    subgraph TWO["Two crossed polarizers: observation-only shadow"]
      direction LR
      P0a["Instrument P(0°)<br/>project and update"]:::instrument
      I0a["Visible observation<br/>I1"]:::observation
      R0a["Continuation residue<br/>rho1 aligned at 0°"]:::residue
      E0a["ERASE residue"]:::erased
      P90a["Instrument P(90°)"]:::instrument
      Z["Output intensity<br/>I2 = 0"]:::result

      P0a -->|readout| I0a
      P0a -->|posterior state| R0a
      R0a -.-> E0a
      P0a -->|physical continuation rho1| P90a
      P90a --> Z
    end

    subgraph THREE["Three polarizers: residue-preserving sequential net"]
      direction LR
      P0b["Instrument P(0°)"]:::instrument
      I0b["Observation<br/>I1"]:::observation
      R0b["Residue<br/>rho1 at 0°"]:::residue

      P45["Instrument P(45°)"]:::instrument
      I45["Observation<br/>I2 = I1/2"]:::observation
      R45["Residue<br/>rho2 at 45°"]:::residue

      P90b["Instrument P(90°)"]:::instrument
      I90["Observation<br/>I3 = I1/4"]:::result
      R90["Residue<br/>rho3 at 90°"]:::residue

      P0b -->|readout| I0b
      P0b -->|posterior state| R0b
      R0b -->|typed continuation| P45
      P45 -->|readout| I45
      P45 -->|posterior state| R45
      R45 -->|typed continuation| P90b
      P90b -->|readout| I90
      P90b -->|posterior state| R90
    end

    S --> P0a
    S --> P0b
```

## Local interaction rule

For ideal linear polarization at angle `phi`, a polarizer set to `theta` rewrites the incoming packet

```text
POLARIZER(theta) ⋈ STATE(I, phi)
    ->
OBSERVATION(I cos²(theta - phi))
+
RESIDUE(I cos²(theta - phi), theta)
```

The visible observation carries intensity. The residue carries the posterior polarization angle and transmitted intensity.

## Sequential reduction

For the three-filter path:

```text
STATE(I0, 0°)
  -> P(0°)
STATE(I0, 0°)
  -> P(45°)
STATE(I0/2, 45°)
  -> P(90°)
STATE(I0/4, 90°)
```

Hence the final intensity is

\[
I_3
=
I_0\cos^2(45^\circ)\cos^2(45^\circ)
=
\frac{I_0}{4}.
\]

For the crossed two-filter path:

\[
I_2
=
I_0\cos^2(90^\circ)
=
0.
\]

## Structural prediction

The middle polarizer does not reveal an intensity feature hidden in the first scalar observation. It changes the continuation residue from a \(0^\circ\) polarization state to a \(45^\circ\) state, creating a legal nonzero continuation through the final \(90^\circ\) polarizer.

Erasing the posterior-state residue makes sequential prediction impossible:

```text
observation-only shadow
=
intensity value
+
lost continuation constructor
```

The net therefore distinguishes:

- observation equivalence: equal visible intensity;
- instrument equivalence: equal readout, posterior state, residue, and legal continuations;
- sequential coherence: the output type and residue of one polarizer match the input type of the next.
