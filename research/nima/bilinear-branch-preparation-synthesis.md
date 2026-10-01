# Bilinear composition reaches branch detail, with single-product constraints

## Existing operation, now exposed by the ledger

The earlier path bridge declared the free bilinear coefficient extension

    B(x,y)_[a b] = x_a y_b

on the ten actual endpoint-compatible words. `RetainedSuccessorLedger.compose_primitive_payloads(stage, left, right)` now exposes that same rule for a registered direct successor of its primitive root. Inputs remain supplied exact rational coefficients. Nothing here specifies their physical preparation, normalization, probability interpretation or execution schedule.

The unchanged-copy lift is precisely B(x,1)=Lx. General right inputs therefore test the existing operation rather than adding a new coupling operator.

## Exact sibling-detail formula

Use the previously checked basis

    c_AB: [AB BA]-[AB BC],   c_DB: [DB BA]-[DB BC],
    c_CA: [CA AB]-[CA AD],   c_BA: [BA AB]-[BA AD].

Writing c_a also for the coefficient of that basis direction, the remainder (I-LD)B(x,y) has coordinates

    c_AB = x_AB (y_BA-y_BC)/2,
    c_DB = x_DB (y_BA-y_BC)/2,
    c_CA = x_CA (y_AB-y_AD)/2,
    c_BA = x_BA (y_AB-y_AD)/2.

These bilinear identities are verified on every pair of primitive basis inputs, as well as nonzero rational fixtures. Uniform continuation coefficients give zero detail, as required.

For a fixed left input nonzero in all branching positions, varying the right input produces a detail space of rank TWO: each vertex supplies one outgoing contrast shared by its incoming rows. This restriction is not the image when both inputs may be supplied independently.

## All four details are attainable in one composition

Set

    y_AB=y_BA=1,
    y_AD=y_BC=-1,
    y_CA=y_DB=0.

Choose x_AB, x_CA, x_BA and x_DB equal to any desired four detail coordinates, with x_BC=x_AD=0. Then B(x,y) is exactly that pure detail vector, with zero decoded-parent mean. This is an explicit single-product witness for surjectivity onto the four-dimensional sibling-detail space, not just a linear-span argument.

The witness uses signed, unnormalized coefficient inputs. It establishes algebraic reachability under the declared rule, not realizability as probabilities or as a physically selected preparation.

## What the coarse summary sees

For the detail alone,

    A r = (c_AB+c_DB)(BA-BC) + (c_CA+c_BA)(AB-AD).

Hence it is hidden exactly when both sums vanish. The checker constructs a nonzero pure hidden detail in one product.

More generally,

    A B(x,y) = diag(y) K x.

This exact bilinear identity shows that ANY left input in ker(K) remains invisible to final-occurrence aggregation for EVERY right input. Nonuniform right coefficients can nonetheless create nonzero branch detail in its retained path output. Thus changing the right operand does not defeat this particular reader's prefix blindness. It does not imply blindness of the retained/source-resolved interface.

## A single product does not fill the ten-word carrier

Group the product by the shared intermediate vertex. Each block is the outer product of the left coefficients entering that vertex and the right coefficients leaving it:

| Interface vertex | Incoming occurrences | Outgoing occurrences | Block |
|---|---|---|---|
|A|CA, BA|AB, AD|2x2|
|B|AB, DB|BC, BA|2x2|
|C|BC|CA|1x1|
|D|AD|DB|1x1|

Each primitive left coefficient belongs to exactly one incoming block, and each right coefficient to exactly one outgoing block. Consequently a full output is a single B(x,y) if and only if EVERY block has rank at most one. This is equivalent here to two determinant-zero conditions, one for A and one for B.

The checker includes a rational factorization algorithm for every block satisfying that condition, including zero blocks and pivots away from the first cell. It rejects rank-two block fixtures that are sums of two individually admissible products.

The two rank-one 2x2 blocks have generic dimension three each; the two scalar blocks contribute one each. Thus the single-product image has generic dimension EIGHT. An exact Jacobian at a nonzero fixture has rank eight, with four independent interface-vertex rescaling directions in its input kernel.

Nevertheless the LINEAR SPAN of single products is all TEN dimensions: every individual word basis vector is a primitive basis-pair product. Taking a sum of products is not the same preparation as a single input pair.

## Parent means and details are not jointly unconstrained

Let m=DB(x,y) be the six decoded parent means. The determinant conditions become

    m_CA c_BA = m_BA c_CA,
    m_AB c_DB = m_DB c_AB.

For generic fixed means, these are two independent linear constraints on the four detail coordinates, leaving two detail parameters. When the parent means vanish, all four details can vary, as the explicit pure-detail witness shows. The four-detail reachability result must therefore not be mistaken for independent control of six means plus four details in one product.

No probability, conservation law, new eigenvalue or ambient spectral promotion is inferred from these algebraic dimensions.

## Verification

    python research/nima/checkers/check_bilinear_branch_preparation.py
    python research/nima/checkers/check_retained_path_successor.py
    python research/nima/checkers/check_retained_branch_comparisons.py
    python research/nima/checkers/check_glued_seed_path_spectral_bridge.py

All fresh runs pass. The new checker covers all 36 primitive basis pairs, the exact detail/coarse formulas, single-product detail reachability, rank-one factorization, rank-two negative controls, full span, generic Jacobian rank and fixed-mean compatibility. Invalid stage scope, copied stages, coefficient dimensions and float inputs are rejected.

Report: `results/bilinear-branch-preparation.json`.

## Synthesis

The previously unpopulated branch-comparison directions can be supplied by the already declared bilinear rule, without another comparison operator. What remains unestablished is physical authority to prepare those input coefficients and any interpretation of that preparation as dynamics. The mathematical distinctions are now explicit: unchanged-copy inputs, single bilinear products, sums of products and arbitrary path payloads are different domains.
