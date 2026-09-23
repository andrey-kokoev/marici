# Positive slope-face images of A/C and B/D separate in their interiors

There are two distinct positive `t=u` source-face types in the four-cell square: **A=C** and **B=D**. For **any strictly totally positive rank-six external data**, no point of the A/C face with `w₄>0` maps to the **same target plane** as a point of the B/D face with all weights positive.

Let `P₄=span(Z₁,Z₂,Z₄,Z₅)`. The B/D target plane is spanned by `S_B=Z₁+w₂Z₂−T` and `Q_B=Z₄+u(Z₁+w₂Z₂)`, with `T=(w₄/u)Z₅+w₅Z₆+w₆Z₇+w₇Z₈+w₈Z₉`. Here `Q_B∈P₄`, while `S_B∉P₄`: the determinant `det(Z₁,Z₂,Z₄,Z₅,S_B)` is a **strictly negative sum of ordered positive five-minors** weighted by `w₅,w₆,w₇,w₈`. Consequently the B/D plane intersects `P₄` precisely in `span(Q_B)`, whose `Z₅` coefficient is zero. But the A/C face plane contains `Q_A=Z₄+u_A(Z₁+w₂_A Z₂)+w₄_A Z₅∈P₄`, with **strictly positive `Z₅` coefficient** when `w₄_A>0`. These planes cannot coincide.

The closures **can** meet. For two exact positive B/D face-target controls, the full positive weight fibre reaches `w₄=0` at `λ=−14/55` and `λ=−1213/645`, respectively. Every other required weight remains positive, **all four source matrices coincide** there, and the target plane is exactly unchanged along the fibre. This identifies a concrete lower-dimensional shared target stratum, without promoting it to a complete image-boundary classification or a pushed-form residue.

Checker: `research/nima/checkers/check_nine_point_slope_face_strata_separation.py`; certificate: `research/nima/results/nine-point-slope-face-strata-separation.json`.
