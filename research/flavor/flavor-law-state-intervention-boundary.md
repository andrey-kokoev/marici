# Law–state intervention boundary (WP426)

## Bounded source grammar

Fix the radial Standard Model Higgs law

$$
V_0(\phi;\lambda)=\frac{\lambda}{4}\phi^4+V_{<4}(\phi).
$$

Admit executable state sources only through operators of degree below four,

$$
V(\phi;\lambda,u)=V_0(\phi;\lambda)
+\sum_{k=0}^{3}u_k\phi^k.
$$

This grammar contains ordinary forcing, mass/background deformation, and cubic
state preparation. The coefficient extractor

$$
Q_4[V]=[\phi^4]V
$$

obeys

$$
Q_4[V]=\frac{\lambda}{4},
\qquad
\frac{\partial Q_4[V]}{\partial u_k}=0.
$$

State preparation may move the expansion point and change every lower Taylor
jet. It does not change the degree-four law coefficient.

## The two ways to obtain a nonzero derivative

Adding a command (u_4\phi^4) gives a nonzero coefficient derivative by
definition. If (u_4) is merely a freely chosen number, it labels a different
law in a family of counterfactual theories; no physical constructor has been
provided.

Alternatively, enlarge the state domain with a dynamical scalar port (S) and
a fixed interaction,

$$
V_{\rm ext}=V_0+\frac{gS}{4\Lambda}\phi^4.
$$

For a preparation command (c) producing (S=s(c)),

$$
\lambda_{\rm eff}(c)=\lambda+\frac{g}{\Lambda}s(c),
\qquad
\frac{d\lambda_{\rm eff}}{dc}
=\frac{g}{\Lambda}\frac{ds}{dc}.
$$

This is an executable state intervention only in the enlarged theory. The
reference port changes the admitted state domain and physical groupoid; it does
not reveal that the original Standard Model coupling was secretly controllable.

## Consequence for the flavor programme

WP416–WP425 establish a useful conditional rank theorem, but direct quartic
actuation is not a necessary condition for a source-generated flavor selector.
It was one attempted constructor. Within the bounded Standard Model source
grammar it is now closed negative: the observed controls prepare states or
analyze the fixed law, while a coefficient-level control requires an added
port.

The flavor programme should therefore return to the original question on the
faithful `physical16` quotient:

Does fixed flavor dynamics, acting on admitted states and source-derived probes,
select a proper physical16 subfamily without treating a theory label as an
executable command?

Candidate fixed-law routes include RG boundary-value consistency, threshold
matching with independently observed mediators, and invariant extremality from
a declared source action. None needs a knob that changes a fundamental Standard
Model coupling.

## Falsifier and authority boundary

The smallest exact falsifier is an explicitly admitted Standard Model operation
whose generated operator lies within the stated source grammar yet has nonzero
degree-four coefficient derivative. A proposed (u_4\phi^4) term does not
falsify the result until (u_4) is constructed as a physical state coordinate.

The result is deliberately grammar-relative. It does not prohibit ultraviolet
theories with moduli or scalar portals; it requires them to declare the enlarged
domain, fixed interaction, preparation map, instrument, and decoupling
falsifier.

Run `uv run --with sympy python
research/flavor/checkers/wp426_law_state_intervention_boundary.py` to regenerate
the JSON result.
