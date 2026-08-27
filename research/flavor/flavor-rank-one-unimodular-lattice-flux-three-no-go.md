# A primitive rank-one Green--Schwarz lattice cannot select flux three: WP782

## Question

Can the smallest quantum-consistent Green--Schwarz charge lattice supply a
primitive characteristic vector whose pairing forces three and fixes the
physical normalization?

## Rank-one lattice gate

Let the rank-one integral lattice have generator \(e\) and Gram form

\[
e\cdot e=N.
\]

For positive \(N\), unimodularity requires

\[
|\det[N]|=N=1.
\]

This is the self-dual string-charge-lattice requirement emphasized by
[Seiberg and Taylor](https://arxiv.org/abs/1103.0019) and by the quantization
analysis of [Monnier, Moore, and Park](https://arxiv.org/abs/1711.04777).

The primitive vectors in rank one are only \(\pm e\). Their pairings in the
unimodular lattice have magnitude one:

\[
|(\pm e)\cdot(\pm e)|=1.
\]

The generator is characteristic because, for every integer \(n\),

\[
e\cdot(ne)-(ne)\cdot(ne)=Nn(1-n)
\]

is even. Thus characteristic parity adds no selection of \(N=3\).

## The two ways to obtain three both insert it

Choosing the Gram form \([3]\) gives

\[
e\cdot e=3,
\]

but its determinant is three, so it is not unimodular. Keeping the admissible
form \([1]\) gives

\[
e\cdot(3e)=3,
\]

but \(3e\) is nonprimitive. The desired integer has then been written directly
into the flux vector.

## Orientation and normalization fibers

The map \(e\mapsto-e\) is a lattice isometry. A bare rank-one lattice
therefore supplies no absolute orientation.

Moreover, the integral intersection form does not determine the positive
Hodge or kinetic metric. At fixed lattice and Green--Schwarz coefficient, a
Stückelberg mass of the form

\[
M_F^2=g_F^2h k^2
\]

changes when the continuous metric modulus \(h\) changes. F-theory effective
gauge couplings depend on compactification moduli; see
[Grimm](https://arxiv.org/abs/1008.4133).

## Classification

The primitive rank-one lattice is neither a flux-three selector nor a
physical-normalization selector. Gram three violates the self-duality gate;
the vector \(3e\) relocates the desired integer into nonprimitive source data;
orientation and kinetic normalization remain independent.

The next finite search is the smallest higher-rank unimodular lattice. It must
be quotiented by its full automorphism group and must contain a uniquely
distinguished primitive characteristic/flux pair of pairing three. Even that
would still require a source potential stabilizing its continuous metric and
an experimental mediator port.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp782_rank_one_unimodular_lattice_flux_three_no_go.py

Generated result:
research/flavor/results/wp782_rank_one_unimodular_lattice_flux_three_no_go.json
