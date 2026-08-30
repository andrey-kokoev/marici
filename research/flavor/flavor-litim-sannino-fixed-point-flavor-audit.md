# Litim--Sannino Fixed-Point Flavor Audit

## Question

Does the canonical perturbative four-dimensional gauge--Yukawa ultraviolet
fixed point realize WP801's conditional selector as a complete asymmetric
flavor source?

## Admitted source

The source is the Litim--Sannino (SU(N_C)) gauge theory in the Veneziano
limit. It contains (N_F) Dirac fundamental fermions (Q), a gauge-singlet
complex matrix scalar (H), and the Yukawa interaction

\[
y\operatorname{Tr}(\overline Q_L H Q_R+\overline Q_RH^\dagger Q_L).
\]

The normalized couplings are (alpha_g=g^2N_C/(4\pi)^2) and
(alpha_y=y^2N_C/(4\pi)^2). At next-to-leading order their beta functions
are

\[
\begin{aligned}
\beta_g&=\alpha_g^2\left[
\frac43\epsilon+\left(25+\frac{26}{3}\epsilon\right)\alpha_g
-2\left(\frac{11}{2}+\epsilon\right)^2\alpha_y\right],\\
\beta_y&=\alpha_y\left[(13+2\epsilon)\alpha_y-6\alpha_g\right].
\end{aligned}
\]

Here (epsilon=N_F/N_C-11/2) is positive and small.

## Exact fixed-point result

The interacting fixed point is

\[
\alpha_g^*=\frac{26\epsilon+4\epsilon^2}
{57-46\epsilon-8\epsilon^2},
\qquad
\alpha_y^*=\frac{12\epsilon}{57-46\epsilon-8\epsilon^2}.
\]

Consequently,

\[
\frac{\alpha_y^*}{\alpha_g^*}=\frac{6}{13+2\epsilon}.
\]

The checker substitutes (epsilon=1/20), verifies both beta functions vanish
exactly, and proves that the two-coupling stability determinant is negative.
There is exactly one relevant and one irrelevant direction. The Yukawa--gauge
ratio is therefore predicted along the one-dimensional ultraviolet critical
surface, while its trajectory coordinate remains free.

## Why this is not the flavor portal

First, the fixed quantity is (alpha_y\propto y^2). It is blind to the sign of
(y), and the transformation (H\mapsto-H), (y\mapsto-y) preserves the
interaction. No physical relative-sign invariant has been constructed.

Second, (Q_L) and (Q_R) are the two chiral components of Dirac fermions in
the same gauge representation. Their gauge-anomaly coefficients cancel. This
is a vectorlike ultraviolet source, not a chiral Standard Model embedding and
not an asymmetric (g_n-g_m) constructor.

Third, the relevant critical coordinate introduces the crossover scale
(Lambda_c). The exact choices (Lambda_c=1) and (Lambda_c=2) share all
fixed-point coordinates and critical ratios. Scalar and fermion masses are
also relevant perturbations; dimensionless mass ratios (m^2/\mu^2) vanish
at the same ultraviolet endpoint for distinct finite masses. Neither the
massive threshold state nor its absolute scale is selected.

Finally, fixed-point correlation functions are source instruments for the
gauge--Yukawa theory. They are not an experimentally calibrated map to the
faithful physical16 flavor quotient.

## Contextual partition

On ((\epsilon,\Lambda_c,\alpha_{\rm det})), intrinsic fixed-point probes have
rank one and a two-dimensional kernel. They determine the fixed dimensionless
couplings as functions of (epsilon), while leaving the crossover scale and
detector calibration unresolved. Adding mass thresholds or detector responses
would refine the partition only after new source-derived instruments are
declared.

## Classification

- Dimensionless gauge--Yukawa ratio: selector on the UV critical surface.
- Yukawa sign: neither selected nor physically typed by the squared coupling.
- Chiral flavor asymmetry: absent.
- RG basin: one-dimensional family of ultraviolet-complete trajectories.
- Threshold survival: not selected because crossover and mass scales remain.
- Physical readout: no physical16 instrument.

## Smallest exact falsifier

Hold (epsilon=1/20) and the complete fixed point fixed. The sources with
(Lambda_c=1) and (Lambda_c=2) have identical dimensionless ultraviolet
data and different crossover scales. For sign, (y=+1) and (y=-1) give the
same (alpha_y) and are related by (H\mapsto-H).

## Disposition

The canonical perturbative fixed point realizes WP801's limited mechanism but
fails the desired source type. The positive successor cannot be obtained by
attaching Standard Model fields to this vectorlike model through another free
portal. It must begin with a chiral anomaly-complete matter representation in
which a rephasing-invariant orientation-odd coupling is itself irrelevant at an
isolated fixed point. Its remaining relevant direction must then be tied to a
source-generated physical clock or a uniquely selected massive vacuum.

Verification:

- checker: research/flavor/checkers/wp802_litim_sannino_fixed_point_flavor_audit.py
- generated result: research/flavor/results/wp802_litim_sannino_fixed_point_flavor_audit.json
- exact invocation: uv run --with sympy python research/flavor/checkers/wp802_litim_sannino_fixed_point_flavor_audit.py
- primary source: [Litim and Sannino](https://arxiv.org/abs/1406.2337)
