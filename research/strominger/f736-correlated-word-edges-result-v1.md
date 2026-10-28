# Typed correlated-word edges on F736

Registered before execution in revision42 and
`contracts/f736-correlated-word-edges-attempt.v1.json`.

## Concrete failed shortcut

The existing strict evaluator's E514 and E539 programs each run from parent
chart1 to parent chart4. Concatenating them as fine-edge arrows fails at the
second R1: the current carrier is V4, not V1. The exact failure is retained.
Those programs evaluate entire lifted parent words; they were never operators
between the fine-vertex objects. Equal normal forms do not fix that type error.

## Declared correlated-word realization

For a vertex word w of length7 define

    Gamma_w(D)={(S_w0 d,...,S_w6 d): d in the same admitted D}.

These are correlated essential images of the source common domain, not arbitrary
products of completed chart spaces. The realization retains the word, all seven
occurrences and the source links between adjacent occurrences.

For a fine edge u->v define its kth component as `S_vk R_uk`. The frozen source
image identities show that this sends the kth component of Gamma_u(d) to that
of Gamma_v(d). The maps are invertible on these declared images only. No analytic
inverse theorem is proved anew.

The actual vertex words are:

    V104: 1,1,1,1,2,4,4
    V111: 1,1,1,1,1,3,4
    V113: 1,1,1,1,1,2,4.

In the retained refinement orientation, E539 runs V113->V111, followed by E514
from V111->V104. E515 is direct V113->V104. The geometric orientation uses their
inverses. All42 oriented component maps,14 route squares and36 adjacent-occurrence
naturality squares pass. The component data reassemble the original21-position
face word without deleting repetitions.31 checks pass, including controls for
erased occurrences, independent observers and wrong chart domains.

## Local labels are not component-witness identities

The registry still labels F736 H134 in both incident tetrahedra. It is unchanged.
In this declared coordinatewise realization, the seven component triangles are:

    occurrences0..3: (1,1,1)
    occurrence4:    (1,1,2)
    occurrence5:    (2,3,4)
    occurrence6:    (4,4,4).

Thus the only nondegenerate COMPONENT triangle is parent **H234**, at zero-based
occurrence5. Its retained-direction comparison is C23 then C34 versus C24.
This does not identify the entire proof-relevant F736 filler with H234: cross-
occurrence coherence and the comparison with the local H134 presentation remain
part of the witness-level obligation. Strict naturality squares alone supply
no regulator-dependent analytical modification.

## Disposition and next obligation

Typed fine-edge maps are now supplied conditionally for this explicit realization.
The blanket claim that no fine-edge realization exists would be too strong. The
intended analytical face comparison is still open.

Next construct or audit the witness-preserving comparison between the local H134
regulator presentation and this correlated-word realization. It must retain the
parent H234 component, adjacent-occurrence data, finite-cutoff residual and both
physical placement channels. The source faithful-whiskering recovery may be used
only with its admitted carrier, represented maps and required other face witnesses;
the occurrence label alone does not provide them. No identity filler is installed.

No completion extension, full Pb construction or physical evolution follows.

```sh
python research/strominger/checkers/check_f736_correlated_word_edges.py
```

Artifacts: `results/f736-correlated-word-edges/realization.json` and
`results/f736-correlated-word-edges/verification.json`.
