# Charged-species enhancement no-go (WP423)

## Candidate explanation

WP422 leaves an electromagnetic Higgs-quartic response that is lawful but too
small to measure. A natural proposed enhancement is to add (N) charged
threshold species whose Higgs-dependent loop terms add coherently,

$$
C_{\rm eff}=\sum_{i=1}^N C_i.
$$

This is independently criticizable because the same new particle multiplicity
changes more than the desired response. The Higgs low-energy theorem fixes the
connection between heavy charged thresholds and Higgs-photon operators; the
proposal cannot increase the quartic response while declaring the rest of the
particle content inert.

Primary source: [Higgs low-energy theorem for heavy-particle loops](https://arxiv.org/abs/1206.7120).

## Deliberately favorable envelope

Let (d_{422}) be WP422's exact laboratory shift for unit loop coefficient.
Grant every new species a same-sign unit contribution, much larger than an
ordinary perturbative charged loop. Then the smallest multiplicity capable of
an order-one displacement is

$$
N_{\rm reach}=\left\lceil\frac{1}{d_{422}}\right\rceil.
$$

This envelope removes charge assignments, loop factors, destructive
interference, threshold suppression, and existing collider bounds from the
attack. Any realistic weakly coupled construction needs at least as much
multiplicity unless it supplies a different, independently derived enhancement
mechanism.

## Correlated species-cutoff prediction

For (N) particle species, the gravitational species bound lowers the
effective cutoff to the scale

$$
\Lambda_G\mathrel{\lesssim}\frac{M_{\rm Pl}}{\sqrt N}.
$$

Using the reduced Planck scale (M_{\rm Pl}=2.435\times10^{18}) GeV, the exact
WP422 reach multiplicity gives a cutoff below (2) GeV, hence far below the
electroweak vacuum scale. The heavy charged-threshold EFT used to infer the
enhancement is therefore no longer controlled across the Higgs domain.

Primary source: [Dvali and Redi species bound](https://arxiv.org/abs/0710.4344).

## Verdict and falsifier

Coherent charged-species multiplicity is not an admitted explanation of the
missing reach. Even under unit contribution per species, reaching an order-one
quartic displacement forces the correlated species cutoff below the
electroweak scale. This does not prove that every ultraviolet completion fails;
it proves that the bare additive-species constructor cannot bridge WP422 while
retaining its own heavy-threshold effective description.

The smallest exact falsifier of the no-go is a fully specified source theory
whose independently fixed enhancement reaches the target with

$$
N<N_{\rm EW}=\left(\frac{M_{\rm Pl}}{v}\right)^2,
$$

or whose derived quantum-gravity cutoff law replaces the species-bound premise
while preserving a controlled electroweak matching calculation. Merely fitting
large charges, coherent factors, or a cutoff after seeing the desired response
does not pass the gate.

Run `uv run --with sympy python
research/flavor/checkers/wp423_charged_species_enhancement_no_go.py` to
regenerate the JSON result.
