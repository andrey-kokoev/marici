# Seven Low-Mode Ports Execute the Grade Change as a Derived Readout

## Authority split

The existing 21-port magnetic repair observes the spin-2 source harmonics of degrees (l=2,3,4). It does not directly observe the spin-3 and spin-4 cokernel carriers used by the grade-changing correspondence.

Nevertheless its seven (l=3) ports provide exactly the coefficients needed to compile a derived grade-changing readout. This authorizes observation post-processing, not target-field actuation.

## Compiled map

Let (P_{3m}(C)), (-3\leq m\leq3), be the seven executable finite-integral ports extracting the spin-2, degree-three source coefficients. First apply one spin raise:

\[
\eth:\mathcal H_3^{(2)}\longrightarrow\mathcal H_3^{(3)}.
\]

Its squared coefficient is six. Then apply the axis-marked endpoint correspondence

\[
J_{\hat n}:\mathcal H_3^{(3)}\longrightarrow\mathcal H_4^{(4)}.
\]

The composite

\[
K_{\hat n}=J_{\hat n}\eth
\]

has squared coefficient

\[
\lvert K_{\hat n}(3,m)\rvert^2
=\frac{16-m^2}{3},
\qquad -3\leq m\leq3.
\]

Every coefficient is nonzero. Therefore the seven input ports compile faithfully into the seven-dimensional image of (J_{\hat n}) inside the nine-dimensional target. The missing target weights are (m=\pm4).

Deleting any one of the seven (l=3) input ports deletes its unique output weight and lowers the rank to six. Thus seven ports are minimal for this readout.

## Why this is executable

The existing source contract independently declares:

- the low harmonic ports executable as finite integrals;
- the weak-star dual pairing source-authorized;
- finite linear aggregation of the ports authorized.

The compiled map is a finite diagonal linear transformation of those seven records. It therefore has an operational witness as a readout algorithm.

Under Aspect's six-gate policy, the derived readout passes all gates and receives `admit`.

## What is not admitted

The admitted capability has type

```text
seven measured spin-2 coefficients
  -> seven derived coefficients labelled in the H4 image
```

It does not have type

```text
physical spin-3 field
  -> physical spin-4 field
```

No physical higher-spin field is created. No target actuator is authorized. No independent measurement of an actual spin-4 output is supplied. The derived coefficients cannot be used as evidence that the corresponding target field exists independently of the calculation.

Thus the earlier `defer` splits into two dispositions:

- finite derived observation transform: `admit`;
- physical grade-changing dynamics or target injection: `defer`.

## Evidence replay

The checker reads the existing executable-port and aggregation authority fields from `distinction-preserving-completion.v1.json`, derives the seven exact composite coefficients, proves minimality under deletion, and invokes Aspect's current decision function.

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/grade_change_compiles_from_seven_low_mode_ports.py
```

Machine-readable results are written to `research/strominger/results/grade_change_compiles_from_seven_low_mode_ports.json`.
