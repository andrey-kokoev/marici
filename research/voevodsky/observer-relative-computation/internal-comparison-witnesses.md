# Internal comparison codes: fixed fibres versus total certificates

`agda/ObserverInternalComparison.agda` adds two first-order comparison codes, stationary and turn, interpreted as reflexivity and the existing nontrivial cover loop. A package contains the code, an actual comparison path and its certification. No constructor stores an arbitrary evaluator.

## Checked distinction and its exact boundary

The interpreted paths are unequal with the visible reply FIXED. This is not merely a distinction between constructor labels: transporting true through those paths reads true and false respectively.

But the total certificate space Σ(reply) (base = reply) is contractible. The two corresponding certificates are connected by an explicit path that moves the reply around the loop. Unequal paths in a fixed-reply fibre therefore do NOT establish inequality of the complete certificates when their reply is allowed to move.

Consequently no constant Bool-valued function on the total certificate space can extend both fixed-fibre readings. The actual valid extension has dependent codomain: its value lies in the fibre over the moving reply. A checked PathP relates the two readouts along the certificate path. There is no contradiction between different endpoint Boolean presentations and this dependent comparison.

This is a concrete boundary test, not a claim that the earlier set-valued restriction theorem is false. Its hypotheses differ. Nor does forgetting to a contractible certificate identify the code-bearing packages themselves: the code field was explicitly forgotten in that map.

## Verification

Fresh safe Cubical Agda --ignore-interfaces -Werror passes: results/agda-internal-comparison.log. The module is included in the aggregate. A fresh check_transport_gate.py run passes all checks with stable inventoried sources: results/transport-gate.json.

## Next

Package the dependent observed value together with its reply and comparison path, then normalize by transporting back to the anchored source fibre. Test which apparent Boolean differences disappear under coherent change of reply and which distinctions remain for genuinely different anchored values. Seek a roundtrip equivalence, rather than erasing comparison data or treating changing fibres as a single constant codomain. This remains a mathematical finite-language model, not a physical observer or causal theory.
