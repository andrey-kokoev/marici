# qRB microstep 25: minimal boundary-interface contract

Let `W_rel` denote the relative boundary object and `H_abs` the absolute positive carrier. The missing `B`-interface is a source-labelled map

$$
J:W_{\rm rel}\longrightarrow H_{\rm abs}^{\,\vee}
$$

(or its rigged/projective replacement) satisfying four minimal conditions:

1. **typing:** `J` is defined on the common Schwartz observer core;
2. **covariance:** `J R=R^\vee J` for admitted transported refinements;
3. **relative readout:** the signed boundary form is the pullback of the carrier cross-readout;
4. **endpoint control:** endpoint rows are finite-rung/projectively continuous.

No positivity of `J` itself is required. Positivity remains a property of the carrier, while orientation is carried by the boundary pairing.

This contract is weaker than an absolute positive embedding and does not imply Weil/GNS positivity.

Status: minimal interface specified; construction of `J` from the actual wall-kernel data remains open.
