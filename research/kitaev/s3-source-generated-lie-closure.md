# Source-generated Lie closure after local compilation

Owner: `marici.Kitaev`

Status: exact finite composition theorem; executable hardware remains
conditional on the compiled gate contracts.

## Bounded question

After replacing all three abstract endpoint ports by their microscopic
compilers, what dynamical Lie algebra is actually certified?

The source inventory is:

\[
\{\text{gauge quadratures},B^t,B^c,K_c\},
\qquad
K_c=\frac{B^cU_c-U_c^{-1}B^c}{2i}.
\]

The two diagonal ports have exact nine-gate holonomy-ancilla compilers, and
`K_c` has the exact thirteen-gate orbit compiler.  Therefore the source map
lands on the same endpoint generators used in the prior Lie certificate; no
endpoint matrix is newly assumed.

## Exact closure

The commutator algebra is already

\[
\bigoplus_a\mathfrak{su}(d_a),
\qquad\dim=28.
\]

The two diagonal ports supply central rank five.  `K_c` has a trace vector
independent of that center because it gives opposite nonzero `G,H`
signatures, raising central rank to six.  Its traceless block parts add no new
directions because every block's full special-unitary algebra is already
present.  Hence

\[
\boxed{\dim\mathfrak L_{\rm source}=28+6=34.}
\]

This remains smaller than the full block-unitary dimension 36.  Exactly two
central phase directions are missing.

## Operational interpretation

Dimension 34 is sufficient for the two channel ingredients already isolated:
full within-block conjugation and a central generator with eight distinct
sector residues.  It is not sufficient for arbitrary independent phase
control on all eight blocks.  Thus channel sufficiency and full coherent
control remain distinct.

The result is source-typed only relative to the gate contracts of the two
compiler packets.  It does not assert that a specific device supplies clean
ancillas, exact Fourier gates, calibrated phases, or uniform random branches.

## Compatibility preflight and verification

The composition freezes coefficient group `S3`, endpoint order
`A,B,C,D,E,F,G,H`, ambient endpoint dimension 16, and block-algebra dimension
36.  The checker records SHA-256 digests of all three input result packets.

Run:

```text
python research/kitaev/checkers/check_s3_source_generated_lie_closure.py
```

It checks schemas and compiler gates, composes the exact ranks, verifies eight
distinct residues, and contains a deliberate failure of the 36-dimensional
claim.  Eight aggregate gates are declared.  Saved result:
`research/kitaev/results/s3-source-generated-lie-closure.json`.

Falsifiers are failure of any compiler map, derived rank other than 28,
central rank other than six, collision of any sector residues, or a direct
Lie calculation contradicting dimension 34.
