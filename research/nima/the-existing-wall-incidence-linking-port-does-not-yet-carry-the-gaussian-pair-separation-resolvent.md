# The existing wall-incidence linking port does not yet carry the Gaussian-pair separation resolvent

## Question

Is the newly derived endpoint-forced separation resolvent already the ordered
linking port declared in the retained Green architecture?

## Claim boundary

No typed identification is currently available. The declared linking port is a
bounded bilinear form on a one-copy wall/incidence graph. The separation
resolvent acts on an ordered-pair Gaussian correlation carrier and retains a
separation coordinate, pair-dependent operator, and shell initial value. This
is an interface mismatch, not a proof that no enlargement or comparison map
can exist.

## Declared linking port

The retained wall graph carries two scalar coordinates,

\[
 \gamma_0f=f(0)
 \quad\text{and}\quad
 \eta(f).
\]

For a source loading \(c_p\), the declared linking polarization is

\[
 \mathfrak L_{c_p}(f,g)
 =ic_p\left(
 \overline{\gamma_0f}\,\eta(g)
 -\overline{\eta(f)}\,\gamma_0g
 \right).
\]

Its established properties are continuity, reciprocal slot sign, centered
arithmetic summability, and compatibility with the retained wall graph. Its
shell value was explicitly left open.

## Gaussian-pair response

The source-derived correlation carrier has basis

\[
 e_n\otimes\overline{e_m}.
\]

On each basis pair the shell density obeys

\[
 \mathcal A_{nm}\rho_{nm}^{[a,b]}
 =\alpha_{nm}
 \left[g_{nm}(b,\cdot)-g_{nm}(a,\cdot)\right],
\]

where

\[
 \mathcal A_{nm}
 =\partial_t+2\pi\frac{n^2m^2}{n^2+m^2}t
\]

and

\[
 \alpha_{nm}=\frac{m^2}{n^2+m^2}.
\]

The solution also retains

\[
 \rho_{nm}^{[a,b]}(0)
 =\int_a^b e^{-\pi(n^2+m^2)x^2}\,dx.
\]

## Missing interface data

The wall-incidence formula does not presently declare:

1. an ordered-pair input \((n,m)\);
2. the separation coordinate \(t\);
3. the pair-dependent operator \(\mathcal A_{nm}\);
4. the asymmetric coefficient \(\alpha_{nm}\);
5. the shell initial value \(\rho_{nm}^{[a,b]}(0)\);
6. a map from the resulting density to the analytic-transpose Evans shell.

A bounded coefficient \(c_p\) cannot be identified with this missing data by
matching one asymptotic coefficient. The source maps must be constructed.

## Minimal enlargement

Introduce a pair-response graph with elements

\[
 (h_{nm},F_{nm},h_{nm}(0))
\]

satisfying

\[
 \mathcal A_{nm}h_{nm}=F_{nm}.
\]

The Gaussian source section is

\[
 h_{nm}=\rho_{nm}^{[a,b]},
\]

\[
 F_{nm}=\alpha_{nm}
 \left[g_{nm}(b,\cdot)-g_{nm}(a,\cdot)\right].
\]

A comparison with the retained linking port would require a map

\[
 \mathcal T_{\rm pair\to link}
 :\mathcal G_{\rm pair}
 \longrightarrow
 \mathcal G_{\rm wall,inc}
\]

that preserves ordered labels, reciprocal orientation, shell concatenation,
and the analytic-transpose Laplace readout.

## Required commuting readout

Let

\[
 \mathcal L_z(h)=\int_0^\infty e^{-zt}h(t)\,dt.
\]

For candidate one, the comparison must satisfy

\[
 \mathfrak L_{c_p}
 \bigl(\mathcal T_{\rm pair\to link}(\rho^{[a,b]}),u_z\bigr)
 =\mathcal L_z(\rho^{[a,b]})
\]

with the source-fixed sign needed to cancel the ordinary residual, after the
separate endpoint-flux term is removed. Equality at isolated zeros is
insufficient; equality on an open parameter set is the density-level test.

## Shell concatenation test

For \(a<b<c\),

\[
 \rho_{nm}^{[a,c]}
 =\rho_{nm}^{[a,b]}+\rho_{nm}^{[b,c]}.
\]

Any admissible comparison must preserve this identity. A fitted prime-shell
coefficient that does not compose under adjacent-shell concatenation is not a
source current.

## Disposition

The existing linking port is topologically closed but is not yet the
Gaussian-pair separation response. Candidate one now requires an explicit
pair-to-link comparison or an authorized enlargement of the linking carrier.
The currently frozen scalar wall-incidence formula alone does not close that
requirement. No RH conclusion is authorized.
