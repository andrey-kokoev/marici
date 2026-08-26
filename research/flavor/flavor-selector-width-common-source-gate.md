# Selector-width common-source gate

Work package: WP536  
Owner: marici.Figueiredo

## Question

Do WP477's withheld five-TeV ratio and WP534's channel-complete width/residue
packet describe one admitted source point?

## Exact source coordinates

In the WP489 common-source normal form,

\[
c=\frac{a}{g_F^2y^2},
\qquad
\frac{g_Ff}{v}=\sqrt{\frac3c}.
\]

The WP527/WP534 width witness has

\[
g_F^2=2,\qquad y^2=1,\qquad a=30258,
\]

and therefore

\[
c_{\mathrm{width}}=15129,
\qquad
\left(\frac{g_Ff}{v}\right)_{\mathrm{width}}
=\frac{\sqrt3}{123}.
\]

WP477's withheld readout instead requires

\[
c_{\mathrm{target}}
=\frac{151560721}{125000000000}.
\]

The ratio of target to width-witness clocks is

\[
\frac{(g_Ff/v)_{\mathrm{target}}}
{(g_Ff/v)_{\mathrm{width}}}
=\frac{30750000\sqrt2}{12311}
\approx3532.37.
\]

This is a dimensionless mismatch. Rescaling the common dimensional clock
\(w\) cannot change it.

## Hostile common-source transport

Keep \(g_F^2=2\), \(y^2=1\), the measured \(v=246\) GeV and the other WP527
witness coefficients fixed. Imposing \(c_{\mathrm{target}}\) requires

\[
a_{\mathrm{target}}
=\frac{151560721}{62500000000},
\qquad
w_{\mathrm{target}}^2
=\frac{1891125000000000}{151560721}.
\]

The quintet mass squared becomes

\[
M_Q^2
=\frac{11346750000000000}{151560721}\,\mathrm{GeV}^2.
\]

At the WP534 width point the lightest entrance-scalar pair lies above the
quintet threshold. At the target-coefficient point the exact margin reverses
sign:

\[
M_Q^2-4m_{\mathrm{entrance,min}}^2
=\frac{1815490613002112637120}
{24249866920721}\,\mathrm{GeV}^2>0.
\]

Thus that scalar pair is open. One newly open channel is already enough to
invalidate reuse of WP534's widths as channel-complete widths at the target
ratio.

## Disposition

The ratio packet and width packet are separately valid conditional objects,
but they are not composable as one selected-source prediction. WP535 remains
the correct form of downstream instrument, yet it currently targets only the
WP534 source witness rather than a source-selected target-ratio pole packet.

This is not a proof that no source-selected target point can have complete
widths. It proves that the existing width packet cannot be transported there
by relabeling or common scaling.

The smallest exact falsifier is the entrance-scalar pair: it is closed at the
WP534 point and open after imposing the target \(c\) while retaining the other
declared coefficients.

The remaining gate is to derive \(c\) independently from coefficient
dynamics, solve the full vacuum at that selected point, redo every scalar and
messenger threshold, and recompute the invariant poles, residues and widths
before applying WP535.

## Reproduction

Run uv run --offline --with sympy python
research/flavor/checkers/wp536_selector_width_common_source_gate.py.

The generated result is
research/flavor/results/wp536_selector_width_common_source_gate.json.
