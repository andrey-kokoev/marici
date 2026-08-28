# The Full Reflection Response Is Faithful on the Signed-Presentation Census

## Correction

The three-state classifier records Smith-depth profiles, not full reflection
responses. Conflating these observation levels falsely makes the atomic
coupled tail inversion appear response-invisible.

## Exact census

All thirty-two legal signed Moore presentations produce distinct \(4\times4\)
integer response matrices. Therefore the full response map is injective on the
bounded presentation census:

\[
X_{\mathrm{legal}}\longrightarrow \operatorname{Mat}_{4\times4}(\mathbb Z).
\]

The atomic simultaneous tail inversion has zero exact-response equalities
across all of its legal edges. Its three connected components contain
sixteen, eight, and eight distinct full matrices.

Exact integral Smith reduction produces five packets. Taking 2-adic
valuations of those factors then produces three depth profiles. The refined
factorization is

\[
X_{\mathrm{legal}}
\longrightarrow
\operatorname{Mat}_{4\times4}(\mathbb Z)
\longrightarrow
\{\text{five exact integral Smith packets}\}
\longrightarrow
\{\text{three Smith-depth profiles}\}.
\]

The first arrow is faithful on the census. Information loss then occurs in two
successive reductions.

## Meaning

The coupled constructor is a source symmetry of the compressed Smith-profile
observation, not a symmetry of the full reflection response. Its authority
signature must therefore name the observation level explicitly.

This restores the first-nonfaithful-arrow diagnosis: presentation distinctions
survive source construction and full response evaluation; Smith reduction
forgets them.

## Replay

Run:

    python research/strominger/checkers/eta_squared_faithful_artin_action_checks.py

The checker verifies sixty-nine exact gates.
