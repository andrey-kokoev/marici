# Calibrated six-port scale identification instrument

Owner: `marici.Aspect`

## Result

An independently referenced optical frequency scale closes the instrument-unit
ambiguity in the six-port pencil. It identifies the realized physical scale;
it does not select the flavor source coordinate and is not a new source law.

## Typed construction

The source authority remains Figueiredo's extended flavor source quotient. The
optical instrument receives six pole channels and one external frequency
reference. Its typed ports are the six complex-response inputs, the reference
input, and calibrated pole, width, and residue readouts. Constructor order is:
prepare the reference, interrogate each channel, fit poles in the common frame,
then report calibrated observables. No detector output is fed back as an action
equation.

In log coordinates \((\tau,\upsilon)\), physical scale and instrument unit,
the six unreferenced pole rows are

\[
J_i=(c_i,-c_i),\qquad c_i\in\{1,2,3,5,7,11\}.
\]

Their rank is one and \((1,1)\) is an exact kernel. The reference row
\((0,1)\) raises the detector Jacobian to rank two. Thus the common-scale
hostile is separated only after independent calibration.

## Authority boundary

The flavor source kernel remains \((2,-1,0,0)\), and the target changes along
it. A source equality with gradient \(\ell\) selects only when
\(2\ell_a-\ell_w\ne0\). The optical reference contributes no such \(\ell\): it
changes readout rank, not source rank. Measurement identifies the realized
point; source dynamics must select it.

## Physical apparatus

A realizable instrument is a comb-referenced swept heterodyne network analyzer:
one phase-locked comb or atomic-clock transfer supplies the frequency unit;
six routed heterodyne ports determine complex line shapes; calibrated local
oscillator phase fixes the frame. Conserved quantities are reference coherence
and routed photon flux before declared loss. Dissipation, detector efficiency,
finite bandwidth, and dead time remain explicit calibration channels.

## Completion gate

Once a genuinely transverse source-derived RG, threshold, or other source law
exists, rerun the full calibrated scan and recompute the vacuum, Hessian,
complex poles, widths, and residues. Until then this instrument is an
identification advance and does not reopen the blocked selection claim.

## Exact verification

The dependency-free checker proves the unreferenced and referenced ranks, the
common-scale hostile, separation by the reference, persistence of the source
kernel, and the distinction between a transverse source row and detector data.

Run:

```powershell
python research/aspect/checkers/calibrated_six_port_scale_identification_instrument.py
```
