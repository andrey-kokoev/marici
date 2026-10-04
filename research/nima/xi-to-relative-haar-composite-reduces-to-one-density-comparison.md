# Xi-to-relative-Haar composite reduces to one density comparison

The existing maps compose as

$$
\mathcal J_{\rm cyc}
:
H_{\rm Ev}
\xrightarrow{\Delta_\Phi}
P_{\rm pair}
\xrightarrow{T_{\rm PB}}
B_{\rm border}
\xrightarrow{Q_{\rm tr}}
\mathcal I_1(E)\widehat\otimes H_{\rm sep}.
$$

This composite is linear, parameter-holomorphic in the analytic lane, multiplicity-preserving, and noncollapsing when its faithful graph coordinate is retained. Cyclic Adams-two evaluation acts by the exact character `p^(-2s)`.

The relative-Haar positivity theorem lives instead on

$$
H_{\rm Haar}
=H_{\rm add}\widehat\otimes\overline{H_{\rm mult}}.
$$

A stronger density-only formulation would ask for a comparison

$$
\iota_{\rm sep\to Haar}:
H_{\rm sep}\longrightarrow H_{\rm Haar}
$$

satisfying:

1. prime dilation intertwining;
   $$
   \iota_{\rm sep\to Haar}T_p^{\rm sep}
   =T_p^{\rm Haar}\iota_{\rm sep\to Haar};
   $$
2. energy compatibility with the relative-Haar form;
3. noncollapse on the source-generated densities `rho_(Phi,u_z)`;
4. reciprocal and shell naturality;
5. compatibility with the Xi-relative identity `Delta_- - Delta_+ = tau h`.

If this arrow exists, then

$$
\mathcal J_{\rm Haar}
=(I\otimes\iota_{\rm sep\to Haar})\mathcal J_{\rm cyc}
$$

places the Xi lift in the positive modular square. At `tau(z)=0`, route equality gives

$$
(1-p^{-2\operatorname{Re}z})
\mathcal E_z(\mathcal J_{\rm Haar}u_z)=0.
$$

Noncollapse then forces `Re z=0`.

Current status: the outer arrows and source-retaining state placement are constructed. The fixed-forcing joint graph in `fixed-forcing-correlation-graph-is-the-density-to-haar-comparison.md` avoids requiring an inverse or standalone map from density alone. Its covariance is the based one-leg action, while diagonal relative-Haar transport also moves the forcing base; see `fixed-forcing-placement-and-diagonal-haar-transport-are-different-squares.md`. The remaining Xi-specific condition is one-step route-energy equality, not another spectral-to-label realization.
