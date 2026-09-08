# Rzk coefficient interface v4: filtered-symbol normalization

## Question and scope

Operator instruction: implement the Gysin-normal packet's interface implications and exact regressions. This extends v1-v3 without changing Fact_n or generic Segal/Rezk composition. These are specification records, not compiled Rzk definitions or a complete formal certificate validator.

Source: research/chatgpt/gysin-normal-comparision/gysin_normal_comparison.md. Its local normal calculation does not supply the full spatial chart/overlap/endpoint/generic-Q natural transformation. This version prevents interpreting the earlier weighted overlap correction as that transformation merely because it is a polynomial chain map.

## Distinct arrow types

NormalContext records the actual ring, named normal equations and their regularity, admitted inverses, selected divisor component/support, coefficient spectators, chain/cochain conversion, filtration ideals, and source locators. Product equations do not identify components: w=tx has both coordinate divisors, and its x-conormal comparison has coefficient t, not a unit on the entire chart.

AmbientMap has source/target complexes and the original coefficient action. A map tx*rho retains that type until an explicitly supplied operation changes it.

PrincipalIdealFactorization has a source-justified ideal target, map into that ideal, and its inclusion into the ambient module, with a commuting factorization. Merely having image in an ideal does not identify the resulting source operation with physical Gysin normalization.

ConnectingSymbolCertificate has the filtered complex, chosen Cartier equation, connecting operation and its degree, divisibility witness, and lift-independence proof; the second filtration and its leading order; the associated-graded/conormal target; and the exact induced map. Retain line twists and shifts. Division on a proved principal ideal is not inversion of the generator in the coefficient ring.

FramedEvaluationCertificate has a conormal line L, its dual L^vee, the canonical evaluation L tensor L^vee -> base, and a source-supplied frame/orientation with its transformation law. Orientation alone on an unframed algebraic line does not choose a trivialization. Under a frame change both the line and dual transform contragrediently. Ordered products retain the odd normal degrees and Koszul signs.

These four types are not aliases for the same arrow. A comparison between them must be given with its actual source, target, shifts, and filtration operation. None may be coerced to a degree-zero scalar endomorphism of the original coefficient complex.

## Local model and normalization

Use homological P=[Ah --tx--> Ap], h in degree one, p in degree zero, with A=B[t,x,(1+tx)^-1]. Neither t nor x is inverted. On C=A/(x), the differential vanishes but the first x-filtered connecting operation is beta_x([a(t,0)h])=t*a(t,0)[p].

On B0=C/(t), its first t-symbol is bar_beta:B0[h] -> L_t tensor B0[p], bar_beta(a h)=[t] tensor a p, with L_t=(t)/(t^2). Lift changes by t alter the result by t^2 and do not change the symbol. The effective-Cartier dual object has L_t^vee in cohomological degree one; retain that shift before comparing to a degree-zero readout. A source-labelled dual frame theta_t with theta_t([t])=1 produces theta_t(bar_beta(a h))=a p.

NormalizationCertificate therefore records this composite, the restriction of spectator coefficients to the two stated fibres, the probe and target marking problem, and compatibility with the required source maps. It must not say tx maps to one as an ordinary specialization.

## Nullity versus retained symbol

On K_x=[Ae --x--> A], the degree-plus-one H sending 1 to t e gives dH+Hd=tx id. Thus derived Cartier restriction of the ambient map tx*rho is null-homotopic for a chain map rho, with appropriate tensor signs. Its filtered connecting symbol can nevertheless be nonzero. A v3 derived-equivalence argument in an unfiltered category cannot recover discarded symbol information or certify the needed filtered comparison.

Similarly, ambient inclusion (x) -> A reduces to zero under ordinary fibre restriction, whereas the framed conormal map (x)/(x^2) -> A/(x) sends [x] to one. These facts concern different targets and operations. The map [w] -> t[x] is not invertible at t=0; framing the product ideal alone does not select the desired component.

## Normalization acceptance gates

1. Identify all four arrow types and the connecting degree, filtration grade, conormal twist, and source frame before reporting unit normalization.
2. Verify the unit on the declared normal symbol, not on an arbitrarily specialized polynomial coefficient.
3. Construct compatibility with actual chart, overlap, endpoint-relative and generic-Q operations. Passing the local symbol test alone is not a certificate for those squares.
4. Record independent coordinate systems: occurrence/Rees, conductor branch, and physical channel coordinates need explicit comparisons. Do not infer identifications from matching formulas.
5. In the separate characteristic-zero pole model, kappa(X)=1/(exp(X)-1) has residue one as kappa dX; multiplying by exp(X)-1 gives the regular form dX and residue zero. This tests the lambda=1 instance and the general pole-cancellation mechanism, not an integral model of analytic coefficients.

## Regression fixtures and disposition

Conjecture: explicitly typed symbol normalization distinguishes the primitive normal unit from raw scalar multiplication. Rival: the weighted overlap map acquires the unit under ordinary or unfiltered derived Cartier restriction. The exact null-homotopy and residue cancellation refute that rival in the declared models. They do not prove a complete physical Gysin comparison.

The standard-library checker computes integer polynomial connecting symbols with an independent spectator, verifies lift independence on exact polynomial inputs, the scalar Koszul null-homotopy, conormal degeneration at t=0, frame sign cancellation, and two-normal exterior contraction identities. A separate exact rational series calculation at lambda=1 checks the normalized pole and its cancellation. Finite series order and polynomial test inputs are bounded fixtures; general conclusions use the displayed divisibility, evaluation, and resolution identities, not extrapolation from tests.

Checker: research/nima/checkers/check_rzk_coefficient_interface_v4.py. Results: research/nima/results/rzk_coefficient_interface_v4.json. Command: python research/nima/checkers/check_rzk_coefficient_interface_v4.py through structured-command. The polynomial fixture does not implement every rational function in A; the source's allowed unit has constant fibre value one. Full localized-ring and global spatial checks are not claimed. No Rzk terms or other-owner code changed; Git operations remain prohibited.
