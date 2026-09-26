# Threshold probes make net-state growth depend on observation vocabulary

Use the local interaction `COUNT(c)--BIT(b) -> COUNT(min(K,c+b))`. For a FIXED externally specified maximal threshold K, segment summaries compose by `min(K,a+b)`; exactly K+1 count states suffice at arbitrary finite n, and threshold probes k=1..K distinguish them (once n>=K). Fresh `check_threshold_net_state_growth.py` verifies 20,481 word/split cases for K=3 through n=10. If the observation interface permits ANY k=1..n at size n, counts 0..n have distinct vectors of threshold answers; n+1 states are necessary. Exhaustive representatives through n=16 and the separating probe k=max(c,d) establish this for arbitrary n. In binary this is logarithmic storage, though the number of states grows linearly.

The rule has a parameter K in the fixed-vocabulary case. A uniform unbounded counter instead uses COUNT(c+b) with integer-valued agent state; it does not have a fixed FINITE agent alphabet. Neither case gives a model of Nima's E/E_B overlaps.

Next examine whether a truly finite agent signature can represent the unbounded count using a unary chain or binary network, with local rules independent of n. Measure graph size and normalization steps as well as interface states; constant rule vocabulary alone may move complexity into network size.
