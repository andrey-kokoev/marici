# Laplace transform of the Gaussian-pair Green identity gives an exact spectral jet recurrence

## Question

What does the endpoint-forced separation equation become under the same
analytic-transpose Laplace readout that defines the ordinary Evans shell?

## Claim boundary

It becomes an exact first-order differential identity in the complex Evans
parameter. This turns every ordered-pair ordinary shell and all of its jets
into explicit endpoint-transform data plus one source initial value. The
identity does not yet identify the resulting parameter-derivative operator with
a frozen G4 port.

## Separation identity

For an ordered Gaussian pair, write

\[
 \rho(t)=\rho_{nm}^{[a,b]}(t),
 \qquad
 \kappa=\frac{n^2m^2}{n^2+m^2},
 \qquad
 \alpha=\frac{m^2}{n^2+m^2}.
\]

Let

\[
 f_{a,b}(t)=g_{nm}(b,t)-g_{nm}(a,t).
\]

The source vacuum gives

\[
 \rho'(t)+2\pi\kappa t\rho(t)=\alpha f_{a,b}(t).
\]

## Analytic-transpose readout

Define

\[
 R_{nm}^{[a,b]}(z)
 =\int_0^\infty e^{-zt}\rho(t)\,dt
\]

and

\[
 F_{nm}^{[a,b]}(z)
 =\int_0^\infty e^{-zt}f_{a,b}(t)\,dt.
\]

Gaussian decay makes both entire in \(z\), and differentiation under the
integral is valid on compact parameter sets.

Laplace transformation gives

\[
 zR_{nm}^{[a,b]}(z)-\rho_{nm}^{[a,b]}(0)
 -2\pi\kappa\,\partial_zR_{nm}^{[a,b]}(z)
 =\alpha F_{nm}^{[a,b]}(z).
\]

## Ordinary-shell convention

The ordered-pair ordinary Evans shell is

\[
 I_{nm}^{(0),[a,b]}(z)=-R_{nm}^{[a,b]}(z).
\]

Therefore

\[
 2\pi\kappa\,\partial_z I_{nm}^{(0),[a,b]}(z)
 -zI_{nm}^{(0),[a,b]}(z)
 =\rho_{nm}^{[a,b]}(0)
 +\alpha F_{nm}^{[a,b]}(z).
\]

Every coefficient is fixed by \((n,m,a,b)\). No Xi zero enters the identity.

## Jet recurrence

For \(j\ge0\), differentiation gives

\[
 2\pi\kappa I_{nm}^{(j+1)}(z)
 -zI_{nm}^{(j)}(z)
 -jI_{nm}^{(j-1)}(z)
 =\delta_{j0}\rho_{nm}^{[a,b]}(0)
 +\alpha F_{nm}^{(j)}(z),
\]

where the term with \(I^{(-1)}\) is omitted.

Thus multiplicity jets are not independent shell conditions on the Gaussian
pair carrier. They form a source-derived triangular recurrence driven by
endpoint transforms.

## Relation to the five-port residual

The existing regular-derivative and wall ports totalize to a spatial endpoint
Green difference. The identity above is different: it uses differentiation in
the complex Evans parameter and an ordered-pair endpoint-product transform.
Neither operation may be silently identified with the existing spatial
first-order port.

A comparison theorem would need to show that the reciprocal/linking sector
implements the operator

\[
 2\pi\kappa\partial_z-z
\]

on the pairwise ordinary shell, together with the source initial-value term and
endpoint transform.

## Top-jet warning

At a Xi zero of multiplicity \(m\), the recurrence at order \(m-1\) contains

\[
 I_{nm}^{(m)}(z_0).
\]

The usual local divisibility test retains residual jets only through order
\(m-1\). Therefore this recurrence does not close the multiplicity chain unless
the proposed response is defined as an entire parameter-differential section,
not merely as independently fitted values on the root vectors below
multiplicity.

## Shell concatenation

All terms respect adjacent-shell addition. For \(a<b<c\),

\[
 R^{[a,c]}=R^{[a,b]}+R^{[b,c]},
\]

\[
 F^{[a,c]}=F^{[a,b]}+F^{[b,c]},
\]

and the initial values add. Hence the spectral identity is cutoff-natural.

## Disposition

The Gaussian-pair bulk response now has an exact entire spectral Ward identity
and jet recurrence. This supplies a concrete comparison target for the
reciprocal/linking ports and exposes a top-jet requirement absent from the
current finite wall-incidence formula. No RH conclusion is authorized.
