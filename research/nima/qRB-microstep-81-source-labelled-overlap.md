# qRB microstep 81: source-labelled overlap compatibility

Construct each finite-packet transport from the same source-labelled feature map, rather than choosing an independent Douglas factorization on each packet.

For `E_k` contained in `E_{k+1}`, define the larger transport by restriction of the same source correspondence. Then

$$
\mathcal D_{k+1}|_{E_k}=\mathcal D_k
$$

holds by construction on source-labelled vectors.

The target Douglas factorization is unique only up to an isometry on generated ranges; source labeling fixes the overlap map, while arbitrary ambient extensions remain irrelevant to the relative readout.

Status: overlap compatibility is closed for source-labelled correspondences; canonical ambient extension and bounded completion remain open.
