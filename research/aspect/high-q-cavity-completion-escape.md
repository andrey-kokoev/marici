# High-Q cavity completion escape

Owner: `marici.Aspect`

Strength: finite-family completion-escape theorem.

## Bounded question

Can every finite causal detector be injective while a sequence of unit-energy
states becomes invisible in every fixed observation window?

## Source, ports, and constructor order

The source is a unit-energy excitation of one cavity mode. At cutoff parameter
\(n\), the retained and leakage amplitudes are

\[
r_n=\frac{n^2-1}{n^2+1},\qquad
l_n=\frac{2n}{n^2+1}.
\]

They obey \(r_n^2+l_n^2=1\), so the cavity-plus-output coupler is exactly
passive. The typed ports are the internal cavity state and the time-ordered
leakage bins. Constructor order is initial preparation, one causal coupling
per time step, ordered leakage detection, then finite-window integration.
No advanced input enters an earlier bin.

## Exact ringdown identity

The amplitude in leakage bin \(k\) is \(l_nr_n^k\). For an observation horizon
\(H\), the captured energy is

\[
E_{n,H}=l_n^2\sum_{k=0}^{H-1}r_n^{2k}=1-r_n^{2H}.
\]

The omitted causal tail is \(r_n^{2H}\), so captured plus omitted energy is
exactly one. At every finite \(n\), the infinite ringdown recovers the complete
unit energy.

## Completion hostile

Fix \(H=3\). For \(n=1,2,4,8,16\), the exact checker proves that every
finite-window map is injective but its captured energy strictly decreases.
As \(n\) grows, \(r_n\) tends to one and \(E_{n,3}\) tends to zero. A unit
internal state therefore escapes every fixed external observation window.

This distinguishes pointwise faithfulness from a cutoff-uniform observability
bound. The detector kernel is zero at every finite cutoff, yet the inverse
conditioning diverges in completion.

## Conserved quantities and frame

Total internal-plus-leaked energy is conserved. The calibrated frame includes
the clock, bin ordering, coupler parameter, and observation horizon. Extending
the horizon with cavity lifetime can recover the energy; silently keeping a
fixed horizon while increasing \(Q\) cannot.

## Completion gate

Excluding escape requires either a cutoff-uniform lower observability bound in
the completed graph norm or a source-authorized horizon scaling. Finite
injectivity, causality, stability, and exact infinite-tail recovery do not
supply that bound. This optical family is a completion falsifier, not a theorem
about theta or adelic states.

Run:

```powershell
python research/aspect/checkers/high_q_cavity_completion_escape.py
```
