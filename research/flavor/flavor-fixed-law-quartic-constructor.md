# Fixed-law Higgs-quartic constructor (WP420)

## Correctly typed task

WP419 shows that changing the Standard Model parameter $\lambda$ while keeping
the Standard Model fixed is not a physical state transformation. A legitimate
constructor must keep one action fixed and vary the prepared state of a source
substrate.

The minimal conditional EFT interaction is

$$
\Delta\mathcal L=-\frac{g}{\Lambda}S(H^\dagger H)^2,
$$

where $S$ is a new gauge-singlet scalar substrate, while $g$ and $\Lambda$ are
fixed theory coefficients. If an apparatus prepares an approximately
homogeneous state $s=\langle S\rangle$ over the Higgs interaction region, then

$$
\lambda_{\rm eff}(s)=\lambda+\frac{g}{\Lambda}s,
\qquad
\frac{\partial\lambda_{\rm eff}}{\partial s}=\frac{g}{\Lambda}.
$$

The executable task is now $s_1\to s_2$, not $\lambda_1\to\lambda_2$ as a
change of laws. The predicted quartic separation is

$$
\lambda_{\rm eff}(s_2)-\lambda_{\rm eff}(s_1)
=\frac{g}{\Lambda}(s_2-s_1).
$$

## Inherited rank-two response

Combine the WP412 quadratic deformation with the source-state command. The
curvature/tadpole Jacobian becomes

$$
J_{\rm src}=
\begin{pmatrix}
1&3v_0^2g/\Lambda\\
v_0&v_0^3g/\Lambda
\end{pmatrix},
\qquad
\det J_{\rm src}=-\frac{2gv_0^3}{\Lambda}.
$$

For positive detector weights,

$$
\det(J_{\rm src}^TWJ_{\rm src})
=\frac{4g^2v_0^6w_Hw_J}{\Lambda^2}.
$$

Thus an observed, preparable source state would inherit WP416's rank-two
authority without asking an apparatus to change a fundamental constant.

## Exact falsifiers

The constructor loses all actuation authority if $g=0$, if the two prepared
states coincide, or in the decoupling limit $\Lambda\to\infty$. Experimental
closure additionally fails if the source state cannot be prepared repeatedly,
does not remain coherent over the Higgs production region, or is inferred only
from the desired quartic result.

## Authority boundary

WP420 specifies a possible fixed-law task; it does not establish that $S$
exists. Admission requires independent evidence for the particle or collective
source, a measured nonzero coupling $g/\Lambda$, two detector-calibrated source
settings, finite-width and stability control, and a sealed quartic-sensitive
record. Until then this is the minimal constructor specification, not a closed
physical instrument.

Run `uv run --with sympy python
research/flavor/checkers/wp420_fixed_law_quartic_constructor.py` to regenerate
the JSON result.
