# Shannon entropy in the flavor readout

## Question

Is the photon Bell result a sector-specific accident, or does a second Marici
sector independently generate a canonical probability object?

## Basis-free flavor object

For nondegenerate up- and down-type mass operators, let (P_i^u) and
(P_j^d) be their rank-one spectral projectors on the common left-handed
flavor space.  Define

[
p_{ij}=operatorname{Tr}(P_i^uP_j^d).
]

In a mass frame this is (|V_{ij}|^2), but the projector formula does not
choose a weak basis.  Positivity and completeness imply

[
p_{ij}ge0,qquad sum_jp_{ij}=1,qquadsum_ip_{ij}=1.
]

Thus each physically labelled row is a conditional probability state for the
down-type flavor produced from an up-type mass eigenstate. Its uncertainty is

[
H_i=-sum_jp_{ij}log p_{ij}.
]

The unordered collection of row entropies is invariant under flavor
relabeling; an individual row is canonical after specifying the physical
incoming mass eigenstate.

## Exact test

The checker uses two generic rational orthogonal (3\times3) frames. It
verifies exactly over (mathbb Q):

- positivity and row/column normalization;
- invariance under a simultaneous weak-basis rotation;
- covariance under independent physical label permutations;
- Shannon product additivity.

No sparse nine-link chart, loop phase, fit, or Born analyzer is used.

## Verdict

[
oxed{
	ext{spectral flavor lens}
+	ext{charged-current overlap readout}
Longrightarrow
	ext{canonical conditional probability states}
Longrightarrow
H_{\rm Shannon}.}
]

This is a second independent sector manifestation. It strengthens the claim
that Shannon entropy is a universal valuation of Marici-derived probability
objects. It still does not make entropy a scalar attached to the bare Carrier:
the spectral projectors and charged-current comparison are flavor coefficient
and physical-readout structure.

The sharp remaining question is functorial: do scattering Cut and flavor
spectral overlap instantiate one common positive-state/coarse-graining
interface, with sector-specific realizations?
