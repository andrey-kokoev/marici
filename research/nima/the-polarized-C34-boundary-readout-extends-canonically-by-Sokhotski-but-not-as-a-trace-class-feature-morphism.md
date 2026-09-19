# The polarized C34 boundary readout extends canonically by Sokhotski, but not as a trace-class feature morphism

## Question

Does the `C34` boundary formula extend when one Mellin observer has a simple
physical-line pole and the other is a rapid test observer?

## Scalar boundary extension

On the regular core, the local Tate formula has the form

\[
q_{C34}(h,g)
=
\sum_\chi\frac1{2\pi i}
\int
\overline{m_{h,\chi}(t)}m_{g,\chi}(t)
L_\chi(t)\,dt
+E_{\rm end}(h,g),
\]

where `L_chi` is the logarithmic-derivative boundary symbol. If `h=Phi` is
rapid and

\[
m_g(t)=\frac{a(t)}{t-t_0\pm i0},
\]

then the coefficient

\[
f_\chi(t)=
\overline{m_{\Phi,\chi}(t)}a_\chi(t)L_\chi(t)
\]

is a valid test function whenever the existing compact-local symbol bounds
hold. Sokhotski's formula gives the canonical ordered boundary values

\[
q_\pm(\Phi,g)
=
\frac1{2\pi i}
\operatorname{pv}\!\int\frac{f(t)}{t-t_0}\,dt
\mp\frac12 f(t_0)
+E_{\rm end}^\pm.
\]

Consequently the wall and jump coordinates remain separate:

\[
q_{\rm wall}=\frac12(q_++q_-),
\qquad
q_{\rm jump}=q_+-q_-.
\]

The wall is the principal-value channel and the jump is the residue evaluation,
up to the fixed orientation convention. This uses the source meromorphic
boundary value and introduces no adjustable subtraction scale.

## Strength boundary

This constructs a polarized distributional boundary readout. It does not prove
that

\[
\rho(\Phi)^*(Q^T-Q^0)\rho(g)
\]

is trace class when `g` has the pole. The displayed integral is therefore an
extension of `Obs_4`, not yet a morphism inside the relative positive-feature
category.

To lift it before scalarization one must construct a rigged operator ideal or a
pole--residue correspondence whose boundary functor yields `q_+` and `q_-` and
whose regular restriction recovers the original trace.

## Disposition

The polarized scalar readout is canonically extendable and retains both ordered
boundary channels. The remaining interface obstruction has narrowed from
undefined scalar pairing to pre-readout packet realization: construct an
operator-level rigged correspondence realizing these Sokhotski boundary
values without identifying the exact residue with retained pair energy.