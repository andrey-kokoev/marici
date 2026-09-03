[Download the 14-page literature-sweep report](sandbox:/mnt/data/arithmetic_exclusion_finite_double_contact.docx)

[Download the executable bridge-certificate verifier](sandbox:/mnt/data/verify_window_bridge.py)

[Download the certificate JSON template](sandbox:/mnt/data/window_bridge_certificate_template.json)

## Verdict

No unconditional theorem was found that proves

$$
\partial_\xi\Theta(t,\xi)=0\Longrightarrow \Theta(t,\xi)>0
$$

for every \(t>0\) and \(\xi\in\mathbb R\), or otherwise excludes every finite double contact. No located conditional theorem closes the problem using an independently verified assumption strictly weaker than RH.

The sweep satisfies the acceptance criterion through a **rigorous obstruction**: a nonzero compact-support Mellin transform is entire of finite exponential type and therefore has only \(O(R)\) zeros in \(|s|\le R\), while the nontrivial zeta-zero multiset has \(\asymp R\log R\) nodes. Exact compact-support cardinal isolation of one reciprocal zero pair—vanishing at every other zero—is therefore impossible. This does not exclude the weaker requirement \(|F(\rho')|\le q<1\) at every other node. Bondarenko–Radchenko–Seip obtain unconditional exact zero-node interpolation only by using entire basis functions outside the finite-exponential-type Paley–Wiener class. ([arXiv][1])

## Strongest surviving route

With Suzuki’s additive convention and

$$
v_{t,\xi}(x)=\frac{1}{\sqrt{2\pi t}}
e^{-x^{2}/(2t)}e^{i\xi x},
$$

the exact interface is

$$
Q_W(v_{t,\xi})=2\Theta(t,\xi),\qquad
\partial_\xi\Theta(t,\xi)=
\Re Q_W(ixv_{t,\xi},v_{t,\xi}).
$$

Suzuki’s 2026 result supplies the exact localized self-adjoint operator with compact resolvent, an attained lowest eigenvalue, and a compact generalized eigenproblem after applying the inverse Neumann Laplacian. It uses the complete signed Weil functional and does not assume RH. ([arXiv][2])

Zhu’s corrected September 2 preprint states

$$
Q_W(f)\ge 8.9\times10^{-18}\|f\|_2^2
\quad
\text{for every complex }f
\text{ supported in }[-0.8,0.8].
$$

The earlier support-\(2.38\) claim was retracted after a wrong-direction prime estimate. I could not independently retrieve and replay the stated supplementary certificate, so the \(8.9\times10^{-18}\) constant is classified as **provisionally applicable, certificate replay pending**. ([arXiv][3])

Groskin’s current v3 construction gives an exact finite zero–source dictionary preserving endpoints, prime powers, and the archimedean term. Its public package includes symbolic checks, Arb interval matrix assembly, interval \(LDL^{T}\) inertia certification, hashes, and provenance records. It rigorously certifies specified finite Galerkin subspaces, but explicitly lacks an inverse or approximation theorem taking the shifted Gaussian family into those subspaces with controlled residual. ([arXiv][4])

## First missing estimate

For \(P_L=\mathbf1_{[-L,L]}\), the decisive object is a rectangle-uniform full-source enclosure

$$
E_W(I_t,X,L)\ge
\max_{\substack{t\in I_t\\|\xi|\le X}}
\left|
Q_W(v_{t,\xi})-Q_W(P_Lv_{t,\xi})
\right|.
$$

A window is certified positive when

$$
E_W(I_t,X,L)
<
\lambda_L\,
\frac{1}{2\sqrt{\pi t_1}}
\operatorname{erf}\!\left(\frac{L}{\sqrt{t_1}}\right),
\qquad I_t=[t_0,t_1].
$$

The certificate must separately enclose the endpoint error, gamma error, finite prime-overlap error, infinite prime tail, quadrature error, and rounding error. This hypothesis is strictly weaker than RH and independently testable. The supplied verifier checks its convention lock, provenance fields, interval signs, and final strict inequality. Its positive and negative self-tests pass.

The priority order is:

1. **Compact-window bridge:** primary.
2. **Uniform nonzero strict peak:** secondary; exact cardinality is eliminated.
3. **Direct critical-point inequality:** lowest priority; located Turán, positive-definite, large-sieve, and phase-alignment results fail the \((\Theta,\Theta_\xi)\) interface, provide average rather than pointwise control, or are RH-equivalent.

[1]: https://arxiv.org/abs/2005.02996 "https://arxiv.org/abs/2005.02996"
[2]: https://arxiv.org/abs/2606.09096 "https://arxiv.org/abs/2606.09096"
[3]: https://arxiv.org/abs/2608.24827v2 "https://arxiv.org/abs/2608.24827v2"
[4]: https://arxiv.org/abs/2607.02828 "https://arxiv.org/abs/2607.02828"
