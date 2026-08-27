# Simultaneous singlet-triplet nullcline no-go: WP735

## Question

Do the source-derived shared-field anomalous dimensions preserve the positive
simultaneous model-A/model-B Yukawa fixed surface required by WP733?

## Admitted source and domain

The source theory is the direct sum of models A and B of Hiller,
Hormigos-Feliu, Litim, and Steudtner, *Model Building from Asymptotic Safety
with Higgs and Flavor Portals*, Phys. Rev. D 102, 095023 (2020), with three
flavor-diagonal copies in each vectorlike sector. The shared fields are the
Standard Model lepton doublet (L) and Higgs doublet (H). The new right-handed
fermions transform as an electroweak singlet and triplet, respectively.

The calculation is one loop in the Yukawa beta functions. Its source domain is

\[
g_1\geq0,\qquad g_2\geq0,\qquad T=\alpha_t+\alpha_b\geq0.
\]

All symbols denote the paper's rescaled squared couplings. Threshold matching,
two-loop Yukawa terms, the complete scalar direct sum, and detector response
are outside this packet.

## Executable tensor derivation

PyR@TE 3 was run from its official repository at revision
`04b219c2016f3fc4f2371d72607edc26a7e06364`. The model used a complex Higgs
doublet, three generations each of (L,psi_A,psi_B), and the contractions

\[
\kappa_A\bar L_iH_i\psi_A,
\qquad
\kappa_B\bar L_i(t^a)_{ij}H_j\psi_B^a.
\]

For flavor-diagonal real Yukawa matrices, its one-loop matrix output reduces
to

\[
\begin{aligned}
\frac{\beta_{\kappa_A}}{\kappa_A}
&\supset \frac92\kappa_A^2+\frac{21}{8}\kappa_B^2,\\
\frac{\beta_{\kappa_B}}{\kappa_B}
&\supset \frac72\kappa_A^2+\frac{23}{8}\kappa_B^2.
\end{aligned}
\]

Passing to squared couplings doubles these coefficients. Therefore WP734's
previously free cross coefficients are fixed as

\[
x=\frac{21}{4},\qquad y=7.
\]

The same reduction gives the published diagonal coefficients
(E_{\kappa_A\kappa_A}=9) and
(E_{\kappa_B\kappa_B}=23/4). This is the internal normalization test. The
published gauge coefficients are also reproduced by the same tensor model.

## Exact simultaneous nullcline

Insert the derived cross terms into the four one-loop nullclines:

\[
\begin{aligned}
8y_A+2\kappa_A&=12g_1,\\
3y_A+9\kappa_A+\frac{21}{4}\kappa_B+6T
  &=\frac{15}{2}g_1+\frac92g_2,\\
12y_B+\frac12\kappa_B&=12g_1+24g_2,\\
3y_B+\frac{23}{4}\kappa_B+7\kappa_A+6T
  &=\frac{15}{2}g_1+\frac{33}{2}g_2.
\end{aligned}
\]

Their unique solution is

\[
\begin{aligned}
y_A&=\frac{3(4T+115g_1+53g_2)}{206},\\
\kappa_A&=-\frac{6(4T+12g_1+53g_2)}{103},\\
y_B&=\frac{20T+575g_1+1089g_2}{618},\\
\kappa_B&=\frac{4(-20T+43g_1+147g_2)}{103}.
\end{aligned}
\]

Consequently, throughout the nonnegative source domain,

\[
\kappa_A\leq0,
\]

with equality only at the Gaussian source point (T=g_1=g_2=0). There is no
point with all four Yukawa squared couplings strictly positive. This is not a
cancellation-margin result: the proposed simultaneous fully interacting
source surface is empty at one loop.

The formal additive portal contrast is

\[
-4y_A\kappa_A+3y_B\kappa_B
=\frac{2(-28T+431g_1+453g_2)(4T+115g_1+465g_2)}{10609},
\]

but it has no selector authority on a fully positive fixed surface because no
such surface exists.

## Classification and falsifiers

The singlet-triplet representation asymmetry is an oriented source grammar,
but this direct-sum completion is neither a viable selector nor a viable
rigidifier of the desired positive portal fixed point. Shared-field
backreaction removes the candidate fixed surface that separate-model
nullclines appeared to provide.

The smallest exact falsifier is the sign identity

\[
103\kappa_A=-6(4T+12g_1+53g_2).
\]

Any strictly positive (T), (g_1), or (g_2) makes (kappa_A<0). The no-go
would be falsified by an independently derived omitted source term that changes
this numerator while remaining perturbatively controlled and preserving all
required symmetries. Merely tuning an extra coefficient does not qualify.

## Consequence for the Deutschian objective

This closes the simplest gauge-parallelized singlet-triplet constructor. It
does not supply the sought hard-to-vary explanation. A successor source
principle must alter the simultaneous nullcline structurally, derive the
alteration independently, and then still fix magnitude, RG basin, threshold
survival, and calibrated readout.

Reproduce the exact theorem with:
`uv run --with sympy python research/flavor/checkers/wp735_simultaneous_singlet_triplet_nullcline_no_go.py`.

Generated result:
`results/wp735_simultaneous_singlet_triplet_nullcline_no_go.json`.
