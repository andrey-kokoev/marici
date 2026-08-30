# The Completed Endpoint Is Not Dualizable for the Closed-Trace Reference

## Finite-cutoff experiment

On an \(N\)-dimensional cutoff \(H_N\), the rigid-category circuit exists:

\[
\mathbf1\xrightarrow{\operatorname{coev}}
H_N^\vee\otimes H_N
\xrightarrow{I\otimes z}
H_N^\vee\otimes H_N
\xrightarrow{\operatorname{ev}}\mathbf1.
\]

For the metaplectic central element \(z=-I\), its value is

\[
\operatorname{Tr}_{H_N}(z)=-N.
\]

Thus every finite cutoff contains a formal invariant experiment that detects
the sign.

## Failure under Hilbert completion

The coevaluation vector is the formal diagonal

\[
\Omega_N=\sum_{n=0}^{N-1}e_n^\vee\otimes e_n,
\qquad
\lVert\Omega_N\rVert^2=N.
\]

It has no Hilbert-space limit. This is the standard dualizability boundary:
only finite-dimensional Hilbert spaces are dualizable in the Hilbert tensor
category. The completed oscillator module therefore does not inherit the
finite-cutoff reference circuit.

Normalizing each cutoff does not fix the problem. The maximally mixed states

\[
\rho_N=\frac1N P_N
\]

are not Cauchy in trace norm. Under the natural inclusion,

\[
\lVert\rho_N-\rho_{2N}\rVert_1=1
\]

for every \(N\). The apparent cutoff-independent expectation \(-1\) is carried
by a family with no completed state.

## Closed-trace repair

A weighted reference such as

\[
\rho_q=(1-q)\sum_{n\ge0}q^n|n\rangle\langle n|,
\qquad 0<q<1,
\]

is trace class and satisfies

\[
\operatorname{Tr}(\rho_q z)=-1.
\]

This repairs the closed-trace analytic defect, but the weight \(q\) is new
source data. It
may represent an energy scale, a prepared reference distribution, or another
authorized positive functional. The endpoint algebra and Hilbert completion
do not select it.

This is not the minimum operational sign experiment. A finite control system
and controlled application of \(z\) detect the sign using any normal endpoint
state, without a dual object or trace-class ensemble. Entry 3703 records that
hostile correction. The theorem here concerns only the basis-independent
closed categorical trace.

## Refined closure theorem

The hierarchy is now:

```text
algebraic finite-grade closure: dual reference circuit exists
Hilbert completion: circuit is lost because coevaluation diverges
nuclear trace closure: trace-class weighting restores the closed circuit
controlled readout closure: a finite control bypasses endpoint dualizability
executable closure: conditional action still requires authority
```

This is a genuine closed-trace completion defect, not a failure of the
metaplectic algebra. It predicts that any claimed observer-free closed-trace
readout must exhibit a nuclear reference functional and state where its
weighting came from. A controlled readout instead owes a conditional-action
constructor.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/completed_metaplectic_reference_dualizability_checks.py
```

The exact checker verifies cutoff duality, divergence, non-Cauchy uniform
states, and a trace-class geometric repair.
