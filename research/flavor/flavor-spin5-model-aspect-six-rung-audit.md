# Spin(5) Model Audit Against Aspect's Six-Rung Tester

## Question

Does the WP877--WP879 simple-parent flavor model pass Aspect's current tester
as a source-derived, falsifier-closed, and experimentally schedulable portal
model?

## Rung one: realization

The model has a partial source realization:

- WP877 gives a renormalizable two-vector breaking potential and its stable
  ordered projector vacuum;
- WP878 gives the primitive Hodge-odd contrast \(H=P_v-P_u\);
- WP879 gives two exact anomaly-free matter completions and their distinct
  one-loop Spin(5) coefficients.

It does not have a complete realization. The source has not selected one
matter completion, fixed the common coupling, derived exotic mass operators,
or supplied a physical record map. The acquisition-level realization is
therefore absent.

## Rung two: present exact tester

The three bounded checkers provide 38 passing source-level gates:

\[
11+14+13=38.
\]

They diagnose six independent hostile directions in a frozen twelve-direction
carrier:

1. singlet-projector rotation;
2. flat relative angle;
3. ordered-frame reversal;
4. nonprimitive contrast normalization;
5. anomaly-completion exchange;
6. off-diagonal threshold mixing.

These are exact mathematical diagnostics. They are not raw apparatus records.

## Rung three: falsifier compiler

Freeze the twelve hostile coordinates as

\[
\begin{aligned}
(&\text{projector rotation},\text{ flat angle},\text{ order reversal},
\text{ nonprimitive contrast},\text{ completion swap},\text{ common gain},\\
&\text{ frozen moving frame},\text{ threshold mixing},\text{ mass scale},
\text{ detector rank collapse},\text{ selected-port zero},
\text{ composite incoherence}).
\end{aligned}
\]

The current source-level observation map has rank six and a six-dimensional
kernel. Its smallest surviving hostile changes only the common gain. The
following directions are unresolved:

- common portal coefficient;
- co-moving source connection;
- exotic mass scale and width packet;
- calibrated detector response rank;
- transmission-zero versus packet-zero classification;
- higher source/RG/threshold/readout coherence.

Adding one exact dual test for each would raise the formal diagnostic rank to
twelve. Aspect's rule forbids interpreting those synthesized rows as physical
probes before their constructors and acquisition contracts exist.

## Rung four: ontology boundary

Closure is relative to the declared twelve-coordinate hostile language. The
model admits Aspect's fresh-term rule. Nonlinear threshold effects,
probe-dependent detector adaptation, new ports, singular support, or a new
matter representation remain possible ontology extensions. No finite carrier
is claimed terminal.

## Rung five: admissibility governance

The six synthesized diagnostics do not share one status:

- common-gain fixed-point row: rejected as a current test because the complete
  source action and beta system are not selected;
- co-moving connection residual: deferred until a source trajectory and
  threshold family are supplied;
- neutral-gap massability and pole row: deferred pending authority for the
  massability requirement and an exact mass action;
- two-excitation detector Jacobian: deferred pending a physical flavor
  instrument;
- complementary Rosenbrock output: deferred pending a dynamic detector
  realization;
- higher coherence residual: deferred until all four constituent arrows
  exist on one common domain.

Speaker authority or desired portal sign cannot promote any of them.

## Rung six: experiment portfolio

No flavor candidate is currently acquisition-authoritative. There are no
measured event rates, setting cells, detector resolutions, source-excitation
ports, or dependency-complete acquisition contracts for this model. The
correct portfolio is therefore empty rather than assigned invented costs.

The first schedulable flavor experiment must jointly provide:

1. two independently excited ordered singlet directions;
2. labelled complementary outputs capable of distinguishing packet and
   transmission zeros;
3. mass and width resolution for the selected completion;
4. retained source-frame and calibration provenance.

## Verdict

The model passes its bounded algebraic source tester and fails to close
Aspect's full tester. Its exact classification is `deferred`, not `rejected`:
WP877--WP879 contain a progressive source geometry and sharp falsifiers, but
the six-dimensional diagnostic kernel and absent acquisition realization
prevent selector or instrument authority.

Aspect's tester changes the immediate priority. Testing neutral-gap
massability alone is insufficient. It must be packaged together with the
completion-specific mass action and the experiment that could resolve the
resulting poles; otherwise it remains another formal row synthesized from the
desired distinction.

## Smallest exact falsifier

Two models with identical \((P_u,P_v,J,H)\), anomaly vector, and current
source-level tester outputs but common gains \(g=1\) and \(g=2\) occupy the
same present diagnostic class while predicting portal intensities in ratio
four.

## Claim boundary

This audit is exact on the declared twelve-dimensional mutation carrier and
the current WP877--WP879 observation rows. It neither proves that the carrier
contains every physical hostile nor assigns experimental costs. The generic
Aspect six-rung framework itself passes its independent checkers; this packet
applies its rules to flavor rather than modifying that framework.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp880_spin5_model_aspect_six_rung_audit.py
~~~

