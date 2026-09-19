# Correction: the moment four-port and history four-port require a six-channel common refinement at the fixed seam

## Failed identification

The endpoint-moment packet is

\[
\Gamma_{\rm mom}
=(B_0,Q_0,M,J),
\]

with

\[
B_0(g)=g(0),
\quad Q_0(g)=\int g,
\quad M(g)=g'(0),
\quad J(g)=\int xg(x)\,dx.
\]

The Fourier-saturated fixed-seam history packet is

\[
\Gamma_{\rm hist}^{\rm sat}
=(B_0,Q_0,A_0,C_0),
\]

where

\[
A_0(g)=\int_{-\infty}^0g(x)\,dx,
\qquad
C_0(g)=\operatorname{pv}\int\frac{g(x)}x\,dx.
\]

The half-line value `A_0` is not the first moment `J`, and its Fourier image
forces the nonlocal principal-value channel `C_0`. Hence no four-by-four
history-to-moment identification exists on the Schwartz source.

Accordingly, the proposed equality

\[
W_{01}=W_\Gamma
\]

cannot be justified by matching four ports. The previous core-colocation
construction is valid for the endpoint-moment port itself, but not for the
separately retained Volterra history four-port.

## Minimal fixed-seam refinement

The two packets share `B_0` and `Q_0`. Their minimal joint source record is
therefore the six-channel packet

\[
\boxed{
\Gamma_6
=(B_0,Q_0,M,J,A_0,C_0).
}
\]

It carries two different order-four subrepresentations:

- `(B_0,Q_0,M,J)` for endpoint moments;
- `(B_0,Q_0,A_0,C_0)` for fixed-seam history.

The characteristic and Green Clark constructions must be obtained as separate
quotients or projections of this common refinement, rather than identified
port by port.

## Moving seam

For a generic seam `a != 0`, Fourier saturation of the history packet requires
ten channels. Adding the derivative/first-moment pair not already present
gives a twelve-channel common refinement. Thus the six-channel object is the
fixed-seam degeneration of a larger moving-seam comparison carrier.

## Correct chain-map problem

Let

\[
\pi_{\rm mom}:\Gamma_6\to\Gamma_{\rm mom},
\qquad
\pi_{\rm hist}:\Gamma_6\to\Gamma_{\rm hist}^{\rm sat}.
\]

Construct the characteristic Grushin column from the moment projection and
the Green observation cone from the history projection. Their comparison now
requires a source-derived map on the common six-channel carrier making the two
projection/cone squares commute.

Colocation within either four-port packet is automatic by canonical transpose.
The nontrivial cell is the mixed comparison between the two different
four-port quotients.

## Disposition

The direct four-port Clark chain map is rejected for the history-to-moment
comparison. The next valid finite object has six channels at the fixed seam,
or twelve channels for moving-seam covariance.