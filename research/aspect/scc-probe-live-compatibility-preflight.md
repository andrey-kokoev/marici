# SCC probe live-compatibility preflight

## Question

Can the probe-semantics candidate be consumed by the live SCC compiler without changing version-1 behavior?

## Claim boundary

This is a read-only structural preflight. It runs the live regression suite and shadow compiler but does not modify the compiler, contract, registry, models, or state.

## Results

The live SCC regression suite passes 31 tests. Both probe shadow entries also pass their sidecar compiler, which reports the live SCC files unchanged. The version-2 candidate preserves all version-1 stages and binds the current live contract digest.

These facts establish noninterference, not live compatibility. The live compiler loads `registry.v1.json` directly at module import. It has no contract-version dispatch, none of the six candidate probe checks are registered, and no validators exist for probe configurations, matching maps, continuation interfaces, or rewrite naturality. Consequently, a live probe entry cannot be admitted merely by placing candidate fields in a model.

## Exact blockers

1. registry loading is hardwired to version 1;
2. contract selection is not injected into the compiler;
3. probe checks have no live registry definitions;
4. probe certificate sections have no live validators;
5. passing shadow entries demonstrate sidecar validation only.

## Safe adapter boundary

The smallest compatible implementation step is contract-and-registry injection with version 1 retained as the default. Probe validators should be added only behind an explicit version-2 selection. This separates legacy behavior preservation from semantic extension and gives the existing regression suite a meaningful compatibility role.

## Disposition

The preflight passes with four implementation blockers. The candidate is structurally noninterfering but not consumable by the live compiler. No live admission is warranted until version dispatch and validators exist and both the legacy suite and probe fixtures pass through the same executable path.
