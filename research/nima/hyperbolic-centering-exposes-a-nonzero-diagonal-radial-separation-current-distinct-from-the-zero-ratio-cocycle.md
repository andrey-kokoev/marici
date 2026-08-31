# Hyperbolic centering exposes a nonzero diagonal radial separation current distinct from the zero ratio cocycle

## Question

What survives on a diagonal theta-label pair after the oriented ratio segment
collapses to zero?

## Claim boundary

A nonzero half-line radial separation current survives. Hyperbolic centering
shows that the ratio displacement and the physical separation coordinate are
distinct: the ratio-Stokes segment vanishes at equal labels, while the
localized pair density still moves along the radial coordinate and through a
moving two-endpoint window. This constructs an exact diagonal transport
identity, not yet its comparison with the G4 linking port.

## Centered pair coordinates

For two source points \((u,v)\), define

\[
 S=u+v,
 \qquad
 D=u-v.
\]

For labels \((n,m)\), let

\[
 c_{nm}=\log(m/n),
 \qquad
 \delta=D-c_{nm}.
\]

Define the centered pair density

\[
 H_{nm}(S,\delta)
 =\Phi_n\!\left(\frac{S+c_{nm}+\delta}{2}\right)
  \Phi_m\!\left(\frac{S-c_{nm}-\delta}{2}\right).
\]

The completed-atom calculation gives

\[
 H_{nm}(S,-\delta)=H_{nm}(S,\delta).
\]

Its exponential factor depends on the centered variable through
\(\cosh\delta\).

## Shell autocorrelation in centered coordinates

In the shell density, set \(v=u+t\). Then

\[
 S=2u+t,
 \qquad
 D=-t,
 \qquad
 \delta=-(t+c_{nm}).
\]

Since \(dS=2\,du\),

\[
 \rho_{nm}^{[a,b]}(t)
 =\frac12
 \int_{2a+t}^{2b+t}
 H_{nm}\bigl(S,-t-c_{nm}\bigr)\,dS.
\]

This is an exact rewriting of the completed-theta incomplete-gamma density.
It retains both moving endpoints.

## Diagonal specialization

For \(n=m\), one has \(c_{nn}=0\), hence

\[
 \rho_{nn}^{[a,b]}(t)
 =\frac12
 \int_{2a+t}^{2b+t}H_{nn}(S,-t)\,dS.
\]

The oriented ratio segment has length zero because \(c_{nn}=0\). Nevertheless
\(t\ge0\) remains a nontrivial radial coordinate. Therefore diagonal vanishing
of the ratio-Stokes cocycle does not imply vanishing of the diagonal pair
current.

## Exact radial transport identity

Differentiate the moving-window formula. Write

\[
 S_-(t)=2a+t,
 \qquad
 S_+(t)=2b+t.
\]

Then

\[
 \frac{d}{dt}\rho_{nn}^{[a,b]}(t)
 =\frac12\left[
 H_{nn}(S_+(t),-t)-H_{nn}(S_-(t),-t)
 \right]
 -\frac12\int_{S_-(t)}^{S_+(t)}
 \partial_\delta H_{nn}(S,-t)\,dS.
\]

This splits the diagonal separation current into:

- a two-endpoint moving-window flux;
- an interior radial derivative.

At \(t=0\), evenness in \(\delta\) gives

\[
 \partial_\delta H_{nn}(S,0)=0,
\]

so

\[
 \rho_{nn}^{[a,b]\,\prime}(0)
 =\frac12\left[H_{nn}(2b,0)-H_{nn}(2a,0)\right].
\]

The first radial derivative is therefore an exact endpoint difference, while
higher radial data retain interior derivatives.

## Relation to prior candidate ports

The off-diagonal ratio cocycle transports along the finite label-ratio segment
from zero to \(c_{nm}\). The diagonal radial current instead transports along
\(t\in[0,\infty)\) after that segment has collapsed. They are different
source paths and require different initial data.

The existing wall/incidence linking form can represent the endpoint bracket
only after a typed trace comparison. Its two scalar coordinates do not by
themselves represent the interior radial derivative for all \(t\).

## Candidate response graph

The smallest diagonal enlargement is a radial graph retaining

\[
 \left(
 \rho_{nn}^{[a,b]},
 \partial_t\rho_{nn}^{[a,b]},
 H_{nn}(S_+(t),-t),
 H_{nn}(S_-(t),-t)
 \right),
\]

with the interior derivative fixed by the transport identity. Its Laplace
readout supplies every Evans jet through radial moments.

## Hostile

Any proposed diagonal response fails if it sets the pair current to zero when
\(c_{nn}=0\), or if it retains only the endpoint bracket while discarding the
interior radial derivative for \(t>0\).

## Disposition

The diagonal blocker is retyped as a radial-separation Green response, not a
missing value of the zero-initial ratio cocycle. Hyperbolic centering supplies
its exact moving-window transport identity and two endpoint traces. The map
from this radial graph into the retained G4 reciprocal/linking carrier remains
open. No RH conclusion is authorized.
