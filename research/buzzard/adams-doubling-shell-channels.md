# Adams-doubling shell channels: Lean packet

Source: `research/grothendieck/adams-doubling-aligns-shell-anomaly-channels.md`.

The formal coefficient type is an arbitrary field `K`; the source labels form
a finite type `ι`; the parameter type `S` is arbitrary. For labelled amplitudes
`a_i(s)`, Lean defines

\[
C_1(s)=\sum_i a_i(s),\qquad
C_2(s)=2^{-1}\sum_i a_i(s)^2.
\]

`RealizesSecondAdams double amplitude` is the explicit source law

\[
a_i(\operatorname{double}(s))=a_i(s)^2.
\]

Under precisely that law,
`finiteQuadraticChannel_eq_half_linearChannel_double` proves

\[
C_2(s)=2^{-1}C_1(\operatorname{double}(s)).
\]

Two one-label rational hostiles keep the premises visible. Omitting the
determinant-log factor turns `1/2` into `1`; omitting the Adams map for source
amplitude `2` compares the correct value `2` with the wrong value `1`.

The theorem does not identify gamma-resolvent dependence with shell-center
time. It does not define complex prime powers, continue the prime-zeta channel
to `Re(s)=1`, prove the displayed sinc/exponential defect formula, construct a
relative mapping cone, choose a finite part at `2s=1`, or establish reflection
compatibility. These remain separate analytic, chain-complex, and source
interfaces. In the intended prime fixture, `double(s)=2s` and the Adams law
must be proved from a convention-fixed complex-power definition.

Verification boundary: Nima's active no-build instruction remains in force.
Only bounded static scans are run, and this module remains outside
`MariciFormal.lean`.
