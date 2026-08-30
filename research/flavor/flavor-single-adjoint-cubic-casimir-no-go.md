# The cubic Casimir observes orientation but cannot select the target

Work package: WP617  
Owner: marici.Figueiredo

## Bounded question

Can the first translation-free, reflection-odd charge invariant arise from a
physically motivated source action and select the centered WP614 charges?

The smallest candidate is one traceless Hermitian \(SU(3)_F\) adjoint
\(\Phi\). Its cubic Casimir \(\operatorname{Tr}\Phi^3\) has exactly the typing
identified by Nima's affine analysis: it is invariant under removal of the
common charge origin and changes sign under \(\Phi\mapsto-\Phi\).

## Complete renormalizable source family

For one adjoint transforming by conjugation, Cayley--Hamilton reduces the
complete eigenvalue-dependent renormalizable potential to

\[
V(\Phi)
=
a\operatorname{Tr}\Phi^2
+b\left(\operatorname{Tr}\Phi^2\right)^2
+k\operatorname{Tr}\Phi^3
+V_0.
\]

There is no independent quartic trace invariant for a traceless
three-dimensional matrix. This is a source-free, coefficient-generic action;
no target eigenvector or fitted charge is inserted.

Centering \(q=(3,2,0)\) gives

\[
x=\left(\frac43,\frac13,-\frac53\right),
\qquad
m_2=\frac{14}{3},
\qquad
m_3=-\frac{20}{9}.
\]

## Exact tangent obstruction

Take

\[
t=(2,-3,1).
\]

At the target,

\[
\mathrm{d}m_1(t)=0,\qquad
\mathrm{d}m_2(t)=0,\qquad
\mathrm{d}m_3(t)=18.
\]

Therefore

\[
\mathrm{d}V_x(t)=18k.
\]

For every nonzero cubic coefficient, the desired three-distinct-eigenvalue
point is not stationary. Setting \(k=0\) removes the residual but leaves every
orientation at fixed \(m_2\) degenerate, so it restores no selector.

The global stationary-locus statement is equally sharp. With a trace
multiplier, every eigenvalue at a stationary point obeys the same quadratic
equation. For \(k\ne0\), a stationary adjoint therefore has at most two
distinct eigenvalues. The target Vandermonde is nonzero, so it is outside that
locus. This is not a failure of the cubic as an observer; it is a failure of
using the observer itself as a source potential.

## Physical spectrum criticism

For a single adjoint Higgs, the three positive-root family gauge-boson masses
obey

\[
m_{ij}^2\mathrel{\propto}(x_i-x_j)^2.
\]

The target charge gaps give the exact pattern

\[
1:4:9.
\]

A two-eigenvalue stationary branch gives

\[
0:1:1
\]

after normalization. It retains an \(SU(2)\times U(1)\) stabilizer rather than
the target's generic Cartan stabilizer.

This supplies an independently typed threshold criticism: resolve the three
family-root vector channels in one calibrated line shape. Observing a
nondegenerate \(1:4:9\) mass-square pattern falsifies the renormalizable
single-adjoint stationary architecture. Conversely, the inference is valid
only after excluding additional Higgs representations contributing to the
same masses.

## Disposition

The cubic Casimir is the correct minimal signed readout but not a viable
single-field selector. The architecture is neither a source selector nor a
presentation rigidifier for the target. It becomes incompatible with the
target when \(k\ne0\), and nonselective when \(k=0\).

The progressive source branch must introduce an independently motivated
second noncommuting flavon or a higher-degree rule. Its complete invariant
family must then be audited: adding enough algebraic freedom to place the
target is not sufficient unless the coefficients and vacuum are themselves
hard to vary. The family-vector mass spectrum remains the direct experimental
criticism.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp617_single_adjoint_cubic_casimir_no_go.py

The generated result is
`research/flavor/results/wp617_single_adjoint_cubic_casimir_no_go.json`.
