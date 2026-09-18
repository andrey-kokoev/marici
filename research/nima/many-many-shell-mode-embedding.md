# Many-many shell-to-mode embedding

At finite shell cutoff `J`, choose pairwise disjoint measurable mode bands

$$
\Omega_1,\ldots,\Omega_J
$$

and define

$$
H_{\rm opt}^{(J)}=\bigoplus_{j=1}^J L^2(\Omega_j;\mathbb C^{d_j}).
$$

Embed the labelled shell carrier by

$$
\iota_J(x_1,\ldots,x_J)=(\iota_1x_1,\ldots,\iota_Jx_J),
$$

with each `iota_j` an isometry into the corresponding mode band. Define optical attenuation by

$$
(\widetilde V_t f)|_{\Omega_j}=t^j f|_{\Omega_j}.
$$

Then

$$
\widetilde V_t\iota_J=\iota_JV_t,
\qquad
E_{\rm loss}(t)|_{\Omega_j}=(1-t^{2j})I.
$$

A detector coupler `C_tilde` realizes the common-history readout when

$$
\widetilde C\iota_J=C_J.
$$

The construction is mathematically available for every finite cutoff. A source-derived assignment of shell labels to physical mode bands, together with compatible embeddings as `J` grows, is required for physical admission.

Status: finite abstract shell-to-mode embedding constructed; source calibration and infinite compatibility remain open.
