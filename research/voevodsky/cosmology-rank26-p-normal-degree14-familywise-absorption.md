# Degree-14 p-normal absorption by source relation family

## Question

Is the rowwise p-normal absorption concentrated in one accidental relation family, or does it hold across the complete labelled presentation?

## Result

The degree-14 raw relation generator has three ordered source families:

| source relation family | rows per normal direction |
|---|---:|
| IBP derivative relations | 480 |
| \(K\)-multiplication relations | 4,224 |
| marked-\(q\) multiplication relations | 25,200 |
| **total** | **29,904** |

The prior fixed-basis certificate showed that every one of the 29,904 `nx` rows and every one of the 29,904 `ny` rows reduces to zero modulo `S+T`, over each of \(\mathbb F_{32003}\) and \(\mathbb F_{32009}\).

Using the exact row-order contract of `raw_relations`, this decomposes familywise as follows for each prime and each normal direction:

- all 480 IBP derivative rows reduce to zero;
- all 4,224 \(K\)-multiplication rows reduce to zero;
- all 25,200 marked-\(q\) multiplication rows reduce to zero.

## Meaning

The zero p-normal image is not confined to a single presentation artifact. It holds across the IBP, bulk \(K\), and all marked-wall multiplication families in the complete finite labelled presentation.

This narrows the search for an algebraic explanation: any uniform homotopy must respect all three source relation constructors, rather than repairing only one defective family.

The result inherits the generator's fixed row-order contract. Reduction coefficients are not retained, and no uniform homotopy, horn map, Bockstein, or physical period is constructed.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_degree14_familywise_absorption.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_degree14_familywise_absorption.json`
