# Certificate-directed completion planning — net iteration4

The complete experimental D2 graph now has an addition-only completion policy.

## Classification

| Class | States |
|---|---:|
| Already exit-certified |698|
| Reach a certificate by additions |9,984|
| No certified continuation at D2 |232,352|
| Total |243,034|

Minimum added-packet distances0 through7 have counts **698,2050,2920,2658,1610,616,122,8**. Every graph step that changes state adds exactly one retained packet, so these are shortest addition-operation distances. Revisit operations cannot shorten them.

All698 targets were freshly identified with the direct source audit. Reverse breadth-first search and reverse-topological dynamic programming agree for every state. Distance/closed-dead-region conditions hold on all7,018,785 labelled edges, including revisits. One source-replayed completion path is saved for every distance level; the full policy stores a next state and interface for every nonterminal completable state.

## No hidden insertion-order obstruction at the target level

A separate index asks which of the698 certified states contain each selected packet set. Every dead state has **no certified superset**. No state has a certified superset yet lacks a completion path through the graph. For all10,682 live states, graph distance equals the smallest certified-superset cardinality difference.

Individual insertion orders can fail, as earlier tests showed. Here some valid ordering always reaches a minimum-size certified superset whenever one exists.

## Nine-pattern exact obstruction cover

The following retained-packet patterns classify all dead states in this D2 family:

| Pattern (D2 packet IDs) | Priority-assigned dead states |
|---|---:|
|14|156,672|
|3,18|1,644|
|4,7|38,652|
|4,19|19,320|
|7,18|1,336|
|13,18|3,360|
|16,9|8,584|
|18,19|492|
|9,10|2,292|

A configuration is dead **iff** it contains at least one listed pattern. Each pattern is geometrically/role compatible. No certified target contains it; every proper subset does have a certified superset. Thus these are completion obstructions, not simply illegal pair occupancies.

The counts above assign each dead state to the first matching pattern in the listed priority order. Patterns overlap. This is a sufficient nine-pattern cover, not a claim that these are all minimal cores or a globally minimum cover.

Across the complete packet universe, certified-superset intersection finds3 singleton and88 pair minimal exclusions, and no minimal triples. Many cannot appear independently in a rooted compatible configuration or are redundant for this cover. The nine selected patterns were explicitly checked against every state, including all live states.

These patterns were learned from the completed target family. The next test asks whether their impossibility can be derived directly from source interfaces and guards, without using target membership. Success would turn an empirical complete-atlas classifier into a reusable synthesis-pruning rule.

## Artifacts and reproduction

- [Receipt, obstruction cover and representative shortest words](results/pne-completion-planner/verification.json)
- [Full completion policy](results/pne-completion-planner/completion-policy.jsonl.gz)
- [Checker](checkers/check_pne_completion_planner.mjs)

```sh
node research/nima/checkers/check_pne_completion_planner.mjs
```

The policy is indexed by configuration IDs in the [D2 source graph](results/interface-driven-synthesis/D2-graph.jsonl.gz). Each row stores distance and next-state/interface pointers; distance−1 denotes the verified closed no-certificate region. The source graph hash and all243,034 decompressed policy rows were checked.

The origin budget stays2. This classifies additions retaining the selected records; it does not supply a deletion/rearrangement policy.
