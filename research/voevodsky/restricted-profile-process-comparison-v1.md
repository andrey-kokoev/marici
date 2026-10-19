# Restricted grammar versus the registered Bool process

Target: `parent:formulation-and-quantifiers`, still open.
Checker: `research/voevodsky/checkers/check_restricted_profile_process_comparison.py`.
Receipt: `research/voevodsky/results/restricted-profile-process-comparison-v1.json`.

## Fresh candidate and outcome

The live physics source register contains `native-bool-square-pilot`: four Bool×Bool labels, left/right flips, and complete retained finite words. Its registered physical embedding, clock/energy/preparation/readout are missing. This turn tests that actual software API, not an imagined physical gate machine.

A fixed syntax codec into its retained words is constructed. The endpoint-only candidate is rejected. The retained codec itself is NOT admitted as execution of the restricted Resolve grammar: a source/proof/resource semantics bridge is still missing. This distinction directly tests the parent's rival of a universal interpreter with supplied answers or unrelated operations.

## Explicit encoding and resource statement

The restricted grammar has five constructor tags (literal, identity, pair, false-selection, true-selection). Assign the fixed three-bit headers 000,001,010,011,100, respectively, followed by each child encoding in order. Header arities are 0,1,2,2,2. Interpret zero as the actual LEFT operation and one as actual RIGHT.

The prefix parser reconstructs the syntax tree from the complete word. Inductively, the fixed header determines its arity, each recursive parse consumes exactly one subtree, and the next child begins at the returned boundary. Hence decoding an encoded term returns that term. Unknown headers, truncated children and trailing nodes are rejected.

For the declared unit-cost flip model, a term with n syntax nodes has exactly 3n operations. This follows by structural recursion, including both branches of selection. It is a translation between two stipulated mathematical counts, not a physical budget/authority witness or runtime bound for evaluating dependent proof objects.

The checker exercises all terms generated through two rounds from the literal, checks parsing, and splits every emitted word at every position. `PathRecord.then` from the actual source module reconstructs the original path using the actual intermediate endpoint. No independent path calculus is substituted.

## Endpoint-only obstruction, with retained-history escape

Five distinct source commands are obtained by zero through four nested identity constructors around the literal. Any map of these five commands into the four endpoint labels must collide; the checker exhausts all 4^5 assignments. Complete syntax recovery from endpoint state alone is therefore impossible even on this subdomain.

The fixed codec also supplies an actual colliding pair with different syntax-node costs and retained operation words. Equality of endpoints cannot recover the source term, its resource count or its derivation. This is a bounded impossibility for endpoint-only storage, not a no-go for the registered retained process: its histories are unbounded and preserve these distinctions.

## Why this is not yet the desired realization

The source `identity` rule constructs an identity-COMPARISON package, not an identity action on a two-bit state. `pair` builds a dependent product package; it is not grouping two endpoints. `select` retains both complete input branches and their derivations; it is not just choosing one output bit.

The word codec records these tags, but flips alone do not interpret the output package, compute its actual selected value or transport proof payloads. Reconstructing the syntax and then importing the existing Agda evaluator would be an explicitly supplied interpreter, not derivation of that evaluator from the flip operations. The checker requires actual native-rule output squares, proof-payload transport and resource/guard translation before admitting a semantic bridge; the encoding-only claim fails that gate.

Thus the endpoint-only rival fails constructively, while the stronger retained candidate remains open for a real semantics extension. No rejected candidate here refutes all possible P. No physical evidence is supplied.

## Next gate

Use the existing native recursive-table source, rather than pretending raw flip words already execute Pi/E/identity. Specify its instruction/resource machine and show the three actual operations preserve complete packages and derivations. A separate comparison to the physical source still needs preparation, operation and resource evidence. The parent's formulation gate remains open until the F/K/E scope is fixed; these results narrow candidate claims without silently reducing universal mathematics to this grammar.
