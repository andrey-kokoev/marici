# Alternative encoders: the rational obstruction survives native C3 preservation

## Question

Was equality to the old polar matrix an unnecessarily strong target? Keep the original source and post-storage Hamiltonians fixed, but allow any metric-isometric encoder. Test native C3 preservation separately from energy compatibility alone. No Hamiltonian is defined by conjugating a proposed answer.

Protocol: `inputs/alternative-energy-encoder-protocol-v1.json`.
Checker: `checkers/check_alternative_energy_encoder.py`.
Receipt: `results/alternative-energy-encoder/verification.json`.

## Source spectral sector

The existing bright space has dimension5: one zero-energy direction and a4-dimensional positive invariant image. The source rotation fixes that entire bright space. Its positive restriction S_positive and characteristic polynomial p are reconstructed exactly from the source energy and metric.

The target Hamiltonian remains

    H_after=diag(A0,H_memory),

where A0 is the original native phase/alignment block and H_memory is the existing collective occurrence-memory operator. The target memory C3 action is reconstructed from the actual residual rows by

    B R_native = R_memory B.

It preserves the memory metric Gamma, has order3 and commutes with H_memory. No target symmetry representation is chosen to fit an encoder.

## Target multiplicities, before choosing an encoder

Any energy intertwiner maps the positive source image into ker(p(H_after)). Exact ranks give:

| Target component | Matching dimension |
|---|---:|
| Native24-coordinate block |0|
| Full21-coordinate memory |12|
| C3-fixed part of memory |4|

Thus every C3-preserving energy encoder must map the4-dimensional positive source image onto the SAME4-dimensional target memory subspace. The basis F=B V spans that subspace, where V is the source's rational positive basis. This identifies the image from energy and symmetry, not from equality to the polar map.

## Rational metric obstruction for every encoder in this class

Let

    g_source=V^T M V,
    g_target=F^T Gamma F.

Both matrices and the bases are rational. Their exact determinant ratio is

    det(g_source)/det(g_target)=35676273088/28845111555.

It is not a rational square. Any rational encoder onto this forced image would have F A as its matrix with rational invertible A. Metric preservation requires

    A^T g_target A=g_source,

so det(A)^2 must equal the displayed nonsquare ratio. This is impossible.

Consequently there is NO rational isometric encoder preserving both the fixed energy and existing native C3 action on the positive bright sector. Equality to the polar encoder, its native output, or its old residual reader was not used in this argument. Failure on this subspace already prevents an encoder on the full bright space.

The current finite rational local gates therefore cannot evade the earlier obstruction merely by choosing a different C3-compatible encoder. This does not turn arithmetic representability into a physical impossibility: a suitable continuous realization can have irrational matrix entries in these charts.

## Nonpolar encoders still exist

Let J be the previously established energy-compatible polar embedding. The target map

    D=diag(I24,-I21)

is a metric isometry commuting with BOTH H_after and target C3. Therefore J_alt=D J is another energy-compatible isometric embedding. It differs from J on the positive sector because its memory component is nonzero there.

This verifies nonuniqueness without changing the Hamiltonian. Its inverse/readers must include D: if R J recovers a residual, then (R D^-1) J_alt recovers the same residual. Similarly a contact transported with J_alt preserves the source contact reading. Keeping the original memory-sign reader fixed would instead change that reading.

The checker verifies D's exact metric, Hamiltonian and symmetry identities. The existence argument uses the earlier polar theorem, not a fresh numerical construction of J. The sign-modified encoder remains irrational on the relevant sector and is not an implementation by the current rational gates.

## The larger class remains open

Without requiring native C3 intertwining, the energy-compatible target has dimension12 rather than4. The square-determinant argument for equal-dimensional images no longer excludes embeddings into that larger space. This test neither constructs nor rules out a rational isometric encoder there.

Such an encoder would change how the prepared C3-fixed source is represented under the existing memory rotation. That would need an explicit symmetry/control account, not a silent relaxation called equivalent assembly. Approximation and source-supported continuous controls remain separate alternatives; none is implemented by this packet.

## Verification

Six exact groups, targeted SCC check and frozen challenge pass under `608475b4a2719c3b`. The receipt stores the positive spectral polynomial, forced source/target bases, both metrics, reconstructed memory C3 action and nonsquare determinant certificate.

    python research/strominger/checkers/check_alternative_energy_encoder.py
    python research/aspect/scc/scc.py check alternative-energy-encoder
    python research/aspect/scc/scc.py challenge alternative-energy-encoder research/strominger/checkers/check_alternative_energy_encoder.py survives

Other-owner sources and results are read-only and hash-bound. No new Hamiltonian, Agda compilation, physical symmetry-breaking law, commit or push was supplied.
