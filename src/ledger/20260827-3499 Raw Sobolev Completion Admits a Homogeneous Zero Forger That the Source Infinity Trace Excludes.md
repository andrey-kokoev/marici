# Raw Sobolev Completion Admits a Homogeneous Zero Forger That the Source Infinity Trace Excludes

For `Re(z)>0`, the source tail equation admits the Sobolev family

\[
G_+^{\rm src}+Ce^{-zq}.
\]

The homogeneous addition is decaying and belongs to `H^1`. Choosing
`C=-X(z)` manufactures the symmetric Dirichlet condition at any off-seam
parameter without changing the differential equation.

The Volterra source rejects this mode through

\[
\lim_{q\to\infty}e^{zq}G_+(q)=0.
\]

For `Re(z)<0`, the reciprocal sheet carries the analogous mode and trace. The
zero-trace source domain is not closed in the raw graph norm: cutoff
homogeneous modes converge in `H^1` while their limiting weighted infinity
trace jumps from zero to a nonzero value.

Thus the zero-to-Dirichlet equivalence requires an independent infinity port
or a stronger weighted topology. Raw Sobolev completion preserves the finite
seam but loses source provenance at infinity.

Research packet:
`research/grothendieck/raw-sobolev-completion-admits-a-homogeneous-zero-forger-that-the-source-infinity-trace-excludes.md`

Checker:
`research/grothendieck/checkers/check_homogeneous_zero_forger_infinity_trace.py`

The checker passes 5/5 gates.
