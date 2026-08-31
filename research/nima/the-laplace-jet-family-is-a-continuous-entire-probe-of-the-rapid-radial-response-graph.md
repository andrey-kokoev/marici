# The Laplace-jet family is a continuous entire probe of the rapid radial response graph

## Question

Can the function-valued radial graph be scalarized into the full Evans
parameter family without losing continuity, shell composition, or multiplicity
jets?

## Claim boundary

Yes. On the rapid radial source, Laplace evaluation and every parameter
derivative are continuous, locally uniformly in the spectral parameter. This
constructs the analytic probe family required before arithmetic loading. It
does not identify the probe with the frozen G4 incidence coordinate or fix the
primewise codiagonal coefficient.

## Rapid radial topology

For a radial function \(f\), define seminorms

\[
 q_{A,N}(f)
 =\int_0^\infty e^{At}(1+t)^N|f(t)|\,dt,
 \qquad A,N\ge0.
\]

Let \(\mathcal E_{\rm rad}\) be the completion of the translated completed-theta
shell currents in all these seminorms. Superexponential decay of \(\Phi\) and
its derivatives places the autocorrelation, endpoint, and Wronskian coordinates
in \(\mathcal E_{\rm rad}\).

## Entire Laplace probe

Define

\[
 \mathcal L_zf
 =\int_0^\infty e^{-zt}f(t)\,dt.
\]

For \(|\operatorname{Re}z|\le A\),

\[
 |\mathcal L_zf|
 \le q_{A,0}(f).
\]

Differentiation under the integral gives

\[
 \partial_z^j\mathcal L_zf
 =(-1)^j\int_0^\infty t^je^{-zt}f(t)\,dt,
\]

and hence

\[
 \sup_{|\operatorname{Re}z|\le A}
 |\partial_z^j\mathcal L_zf|
 \le q_{A,j}(f).
\]

Thus \(z\mapsto\mathcal L_zf\) is entire, and every jet probe is continuous on
the same rapid source.

## Probe of the radial graph

For a graph element

\[
 x=(\rho,e,w,\rho(0)),
\]

define

\[
 \Pi_zx
 =\left(
 \rho(0),
 \mathcal L_z e,
 \mathcal L_z w,
 \mathcal L_z\rho
 \right).
\]

The first-order graph law becomes

\[
 z\,\Pi_z^{(\rho)}x-\Pi_z^{(0)}x
 =\Pi_z^{(e)}x-\frac12\Pi_z^{(w)}x.
\]

This relation holds as an identity of entire functions and therefore transports
all multiplicity jets without separate recurrence assumptions.

## Shell composition

Radial graph coordinates add under adjacent-shell concatenation. Since
\(\Pi_z\) is linear,

\[
 \Pi_zx_{[a,c]}
 =\Pi_zx_{[a,b]}+\Pi_zx_{[b,c]}.
\]

The intermediate endpoint cancels before probing. The analytic family is
therefore cutoff-natural.

## Label transport

Theta-label changes are logarithmic translations with the fixed half-density
coefficient. Because the radial source topology contains every exponential
weight, translated probes remain continuous. The ordered-pair product and ratio
characters must still be retained when summing labels; the probe itself does
not codiagonalize them.

## Arithmetic loading

Let \(\omega_p\) be a separately source-declared prime-shell loading. The
candidate arithmetic probe is

\[
 (\Pi_{U,z}x)_p=\omega_p\Pi_zx_p.
\]

For the completed theta shells, every radial seminorm decays
superexponentially in the lower shell endpoint \(a=\log p\). Consequently any
of the already admitted centered half-density/logarithmic loadings is dominated
by a convergent prime majorant, locally uniformly in \(z\) and for every jet.

This proves analytic summability conditional on the declared \(\omega_p\). It
does not select \(\omega_p\) or its sign.

## Distinction from a fixed scalar port

For one fixed \(z\), \(\Pi_z\) returns finitely many scalars. The complete
object is the entire family

\[
 \{\Pi_z:z\in\mathbb C\},
\]

or equivalently its faithful collection of all radial moments. Replacing this
family by one fixed incidence scalar loses the density and cannot preserve
multiplicity.

## Hostile

A proposed G4 attachment fails if its incidence coordinate agrees with
\(\Pi_z^{(w)}\) at selected Xi zeros but does not extend to the locally uniform
entire probe family on \(\mathcal E_{\rm rad}\).

## Disposition

The radial-to-analytic probe family is constructed: it is continuous, entire,
jet-compatible, shell-additive, and summable under every currently admitted
prime loading. Candidate one is narrowed to identifying this family with the
canonical G4 incidence/readout and deriving the source primewise coefficient
and codiagonal sign. No RH conclusion is authorized.
