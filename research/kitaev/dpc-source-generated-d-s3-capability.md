# DPC: source-generated D(S3) capability

Owner: `marici.Kitaev`

## Status

This packet gives an exact conditional realization at the logical endpoint
layer. A subsequent hostile source-independence audit retracts its original
classification as a proper Deutschian explanation: the proposed generators
are target spectral logarithms and are not derived from the native D(S3)
Hamiltonian. It does not promote the complete five-rail compiler to
`Executable`.

## Independently stated source

Let (n=|1\rangle\langle1|) on a binary control. Admit switchable coherent
couplings

\[
H_2(j,k)=n_jn_k,
\qquad
H_3(j,k,l)=n_jn_kn_l,
\]

and, on a qubit--qutrit pair,

\[
H_{\rm ex}=n_c\otimes K_{12},
\qquad
K_{12}=\frac{(|1\rangle-|2\rangle)(\langle1|-\langle2|)}2.
\]

These are occupation and exchange interactions, specified without naming the
desired endpoint gates. Their execution still requires calibrated signed
durations, switchable support, and a coherent occupation basis.

## Generated operations

Because (K_{12}) is the antisymmetric exchange projector,

\[
e^{-i\pi H_{\rm ex}}
=|0\rangle\!\langle0|\otimes I_3
 +|1\rangle\!\langle1|\otimes I_{\{0\}}\oplus X_{12},
\]

which is exactly

\[
|e,k\rangle\longmapsto |e,(-1)^e k\rangle.
\]

Thus the hybrid controlled inversion is generated directly rather than
declared available.

For a record control (c) and binary label
(r=4b_2+2b_1+b_0), commuting (H_2(c,b_j)) pulses give

\[
\prod_{j=0}^2e^{-i\pi p2^j n_cn_{b_j}/4}
=e^{-i\pi pcr/4}.
\]

The fractional pulses supply the missing controlled-(T)- and
controlled-(S)-type phases for powers one and two; the power-four phase
reduces to the already available Clifford branch.

There is an independent qubit realization. A (pi)-pulse of (H_3) is
CCZ; conjugating one leg by (H) gives Toffoli; one Toffoli and two CNOTs give
Fredkin. On the embedding
(|0\rangle\mapsto|00\rangle, |1\rangle\mapsto|01\rangle,
|2\rangle\mapsto|10\rangle), Fredkin is controlled qutrit inversion and
fixes the unused state.

## Why this initially appeared explanatory

The same microscopic property—nonlinear conditional phase or exchange—both
changes the Clifford-hierarchy invariant and generates the missing endpoint
operations. The account is hard to vary in three ways:

1. deleting the control from the exchange pulse destroys controlled
   inversion;
2. replacing the fractional angles by the next Clifford-compatible angle
   changes controlled (T/S) into a different gate;
3. deleting the least-significant label coupling destroys the exact record
   character.

All hostile sources retain the same Hilbert-space support. Their failure is
therefore dynamical, not a restatement that the requested gate was absent.

## Fault-tolerance boundary

A rail-local two- or three-body source fault affects at most one rail in each
participating block, which is locally compatible with distance-three
recovery. This spread bound is necessary but insufficient. One must still
prove that the transversal source pulse intertwines the frozen five-rail code
projectors, or construct and verify a code-switch/resource-injection factory.

The direct intertwining audit resolves the first alternative negatively for
the frozen codes. Maximum codespace leakage norms are

\[
0.99344398\quad(H_{\rm ex}),\qquad
0.66487330\quad(CT),\qquad
0.95491635\quad(CS).
\]

Thus the raw transversal pulses do not preserve the relevant code spaces.
This is not a failure of the logical mechanism; it proves that the physical
lift genuinely needs a different encoding, verified injection, or explicit
code-switch surface.

Consequently:

\[
\begin{array}{c|c}
\text{resource theory}&\text{status}\\
\hline
\text{frozen stabilizer source}&\text{Obstructed}\\
\text{logical nonlinear source}&\text{Executable at endpoint algebra level}\\
\text{complete five-rail compiler}&\text{Conditional}
\end{array}
\]

The logical realization is generative after the couplers are postulated. It
is not yet a physical explanation because neither the couplers nor their
calibrations are independently derived, and the encoded-intertwining theorem
fails for their raw transversal use.

## Falsifiers

- The direct conditional-exchange exponential differs from controlled
  inversion.
- The three (H_2) factors fail to reproduce the exact record character.
- A hostile source mutation still generates the target operation.
- A single rail-local source fault creates two bad rails in one distance-three
  block.
- No encoded realization or verified factory can preserve the one-fault
  contract; in that case the logical explanation has no physical lift.

## Artifacts

- Checker: `checkers/check_s3_dpc_nonlinear_source_mechanism.py`
- Result: `results/s3-dpc-nonlinear-source-mechanism.json`
- Frozen-code checker: `checkers/check_s3_dpc_five_rail_intertwining.py`
- Frozen-code result: `results/s3-dpc-five-rail-intertwining.json`
- Consolidated checker: `checkers/check_s3_dpc_explanation_audit.py`
- Consolidated result: `results/s3-dpc-explanation-audit.json`
- Epistemic graph claim: `claim:ff518eb5a5c72ef3a36f`
- Graph event: `ev-000000003315-8d630deb-f2c2-4990-af4a-21da43959fd5`
- Hostile correction: `dpc-hostile-source-independence-audit.md`
