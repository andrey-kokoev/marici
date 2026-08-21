# The electron cut composes with the Bell readout

The complete D10 coefficient packet can now be supplied by source-normalized
electron unitarity cuts. At transverse kinematics define

\[
A=g_2+g_3y,qquad
B=-\left(\frac32f_2+\frac14f_3y\right),qquad
C=\frac14h_3y,qquad y=s/m_e^2.
\]

Composing these reconstructed coefficients with

\[
\mathcal I=\frac{4\sqrt2,AB}{A^2+B^2+2C^2}
\]

and solving \(\mathcal I=2\) recovers the independently computed analytic
D10 Bell onset. Thus the bounded chain

\[
\boxed{
\text{electron cut}\longrightarrow
\text{vector helicity crossing}\longrightarrow
\text{D10 coefficients}\longrightarrow
\text{Bell readout}
}
\]

works without fitting a coefficient to the Bell observable.

Reproduce with `research/nima/check_qed_dispersive_bell_onset.py`.
