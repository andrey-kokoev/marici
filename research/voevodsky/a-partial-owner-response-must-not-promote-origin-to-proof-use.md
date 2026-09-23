# A partial owner response must not promote origin to proof use

A FICTIONAL response to the prepared Farkas row request says `attest-primitive-row-origin: attested` while `authorize-future-source-rooted-proof-use: declined`. The action states remain separate: origin is only a TEST-ONLY unauthenticated claim and proof use is explicitly denied in that fixture. Fresh `check_partial_owner_action_response.py` refuses mismatched request digest, row manifest, source generation, omitted action and altered action disposition.

No actual owner recipient, owner event, response signature or trust-root verifier exists. Thus the REAL request has no response at all; the model does not turn its fictional origin statement into row authority. Even an independently authenticated future origin attestation would not override an explicit proof-use denial or imply analytic correspondence.

Next test a REVISED response after an earlier decline: a later hypothetical proof-use grant must explicitly reference the earlier event, exact request and live generation/revocation state. Graph order alone cannot supersede denial; retain both decisions as evidence rather than overwriting history. Analytic S,A,R,C,G mapping deferred.
