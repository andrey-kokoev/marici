# Twisted continuum context ladder

## Question

Can WP540's six exact momentum contexts be held fixed across several lattice
spacings so that a continuum extrapolation is defined without retuning the
flavor source?

## Fixed-volume ladder

Freeze a physical extent of \(24\,\mathrm{GeV}^{-1}\) and three independently
scale-set lattice spacings,

\[
a\in\left\{1,{1\over2},{1\over3}\right\}\mathrm{GeV}^{-1}.
\]

The corresponding site counts are \(24,48,72\). For each preregistered WP540
node \(z_j\), impose a partially twisted valence boundary momentum with link
angle

\[
\alpha_j(a)=2\arcsin{a\sqrt{z_j}\over2}.
\]

Then

\[
{4\over a^2}\sin^2{\alpha_j(a)\over2}=z_j
\]

exactly at every spacing. All inverse-sine arguments lie strictly inside the
admissible interval.

## Continuum response

The associated physical momentum is

\[
p_j(a)={\alpha_j(a)\over a}.
\]

For a generic fixed node \(z\), the checker derives

\[
p^2(a)=z+{a^2z^2\over12}+{a^4z^3\over90}+O(a^6),
\qquad
\lim_{a\to0}p^2(a)=z.
\]

Because every spacing has the same six exact \(\widehat q^2\) nodes, every
spacing uses the same nonsingular WP539 context matrix and retains rank six.

## Changed groupoid

The twist holonomies and their Fourier-sector labels are added
reference/control ports. They define a new relational boundary-condition
experiment over the stabilizer preserving those holonomies. They do not reveal
an absolute phase belonging to the original periodic experiment.

The hostile zero-twist experiment makes this distinction exact. If all twists
vanish and only one Fourier sector is retained, all six requested contexts
coincide at zero and the context rank is one rather than six.

## Authority boundary

WP541 provides a continuum-extrapolation grammar and executable kinematic
control in principle. It does not provide measured correlators. Physical
authority still requires:

- a preregistered QCD scale-setting observable;
- the three declared ensembles and their common physical-volume audit;
- four renormalized Ward-channel \(B_s\) bilocal correlators;
- contact subtraction, heavy-quark control, and threshold matching;
- correlated fits of the \(a^2\) and \(a^4\) response;
- the full cross-spacing and cross-context covariance.

The twists neither modify the flavon source action nor select \(t\).

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp541_twisted_continuum_context_ladder.py

The generated result is
research/flavor/results/wp541_twisted_continuum_context_ladder.json.

The reviewed claim and report to marici.Nima were admitted at graph event
ev-000000004877-f770435f-227d-4928-b844-195282e32035. Admission records
reviewed provenance and does not certify truth.
