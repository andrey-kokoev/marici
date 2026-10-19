# Conjecture-net explorer

The same generated, self-contained HTML works from disk and at `/experiments/conjecture-nets.html` on the public website. It requires no Graphviz installation, CDN, application server, or network access to browse its bundled graph data.

## Open locally

First generate or refresh the snapshot from the repository root:

```sh
pnpm nets:prepare
```

Open `website/public/experiments/conjecture-nets.html` in a browser. On this checkout the full path is:

```text
C:\Users\andrey\src\marici\website\public\experiments\conjecture-nets.html
```

The HTML remains a snapshot until regenerated; it does not watch the source tree. It can be copied elsewhere for offline browsing, but its relative repository-source links only resolve from the original checkout location. No research data is rewritten by the app.

## Website

The regular `pnpm dev` / `pnpm build` preparation generates the same assets. Site navigation has **Research → Conjecture nets**, and the construction gallery links to the app. The route is `/experiments/conjecture-nets.html`. Generation or a local test is not deployment; publishing still uses the separately authorized website deployment workflow.

## Controls

- **Research net:** switch among arrow seeds/isotope atlas, low-energy scattering, core bridge/inverse, high-energy scattering and the existing local-core proof-outcome net.
- **Tabs:** Dependencies and Four-port implications. Both graph canvases span the page width and are 90vh high; arrow keys switch focused tabs.
- **Selection:** initially nothing is selected. Clicking a node opens an overlaid sliding right panel; it never reduces the graph width. Close or Escape deselects it and clears reachability highlighting. Click a node, or focus it and press Enter/Space, to inspect its source statement, status, formal outcome, scope, next action, acceptance, dependencies and evidence. Long raw IDs remain available in the detail view.
- **Search / Show:** display matching-node buttons only while a search or filter is active. There is no permanent Nodes column. The complete graph stays visible so a filtered result cannot hide prerequisites.
- **Zoom / Fit:** the dependency graph uses resize/scroll controls with a 75% minimum Fit scale. The D3 graph supports wheel/pinch zoom, background pan, node dragging, Fit and Pause/Resume layout. Reduced-motion users start with a settled, paused layout. Labels wrap without ellipses; source text is fully accessible by scrolling the details panel.
- **External prerequisite:** a node's detail panel links to the corresponding node in another bundled net. The source relation remains explicit; it is not a proof import.
- **Deep links:** the URL fragment records the net, active tab and selected node and survives reload. Port/arrow reachability selection is temporary. For local imports, reload requires importing the file again.
- **Download:** save the current original source contract, without display-derived statuses.
- **Open another local net:** accept a JSON object with `conjectures`, each with `id` and optional `depends_on` (absent means no declared dependencies). Optional statement, status, frontier, outcome, evidence and boundary fields are retained. Imports stay in the tab, are not uploaded or persisted, and do not enter the public catalog. Limit: 2 MB and 500 nodes. Duplicate IDs, missing dependencies, cycles and invalid frontier references are rejected.

Source links point to relative repository files under `file://` and GitHub under HTTP. Current local source files may not yet exist on the public GitHub branch. No scientific claim is verified by following a link.

## Four-port implications

Every conjecture has four distinct attempt-outcome ports: `++` proved, `+-` failed to prove, `-+` successfully rejected, `--` failed to reject. A failed proof is not rejection; failed rejection is not proof. There are no implicit internal edges between these ports.

The explorer reads explicitly port-typed `proof_relations` in the existing local-core contract, including multi-premise rules. Relations without a conclusion outcome, such as branch activation, are counted but not drawn as outcome implications. The scattering nets currently have no such relations. Their dependency edges appear as **dashed node-to-node arrows**, never as port implications; solid arrows are reserved for declared port implications. Clicking a dashed arrow inspects the prerequisite relation and highlights downstream research dependents. Port reachability never traverses dashed dependencies.

Local imports may instead declare:

```json
{
  "id": "example",
  "conjectures": [{"id":"A"}, {"id":"B"}, {"id":"C"}],
  "port_implications": [
    {"id":"A-proves-B", "from":{"node":"A","port":"++"}, "to":{"node":"B","port":"++"}, "weight":4},
    {"id":"both-required", "premises":[{"node":"A","port":"++"},{"node":"B","port":"++"}], "to":{"node":"C","port":"++"}, "weight":1}
  ]
}
```

The D3 gravity-weighted simulation uses radial gravity toward the layout center, many-body repulsion, collision avoidance and weighted springs. The Gravity slider adjusts central attraction, including zero; dragging reheats a running layout. Paused/reduced-motion layouts recompute without animation when gravity changes.

Weights are positive finite numbers shown on arrows and controlling line width and spring attraction. Heavier edges pull more strongly and have shorter preferred gaps, with node sizes respected. An omitted weight is **1, a layout default**, never a probability or confidence estimate. Invalid endpoints/ports/weights are rejected. The D3 7.9.0 code and its ISC license are embedded in the generated HTML; it works without a CDN.

Click a port to follow directed implication reachability from precisely that port. Unreachable nodes, ports and arrows dim but remain clickable. An AND gate becomes reachable only when every premise port is reached; one input does not activate it. Clicking an arrow previews the rule with all its premises assumed together and then follows downstream routes. The panel shows that assumption and any source witness condition. This is structural reachability, not a proof checker: it does not certify scopes, discharge same-witness conditions, assign outcomes or silently add contrapositives. Clear selection restores the complete graph.

## Authored sources and publication

- `src/conjecture-nets/catalog.json`: explicit public selection of five source contracts, not an automatic mirror of the full research registry.
- `src/conjecture-nets/model.js`: shared validation and safe source-link construction.
- `src/conjecture-nets/app.html`, `app.js`: authored UI and selection drawer.
- `src/conjecture-nets/ports.js`, `port-view.js`: typed implication extraction, AND-aware reachability and D3 force rendering.
- `scripts/prepare-conjecture-nets.mjs`: deterministic bundle with per-contract SHA-256 identities, embedded JSON and inline code.
- Generated `website/public/experiments/conjecture-nets.html` and `conjecture-nets.json`: do not edit manually.

To add a public net, review its contents and add an explicit catalog entry. Its local dependency DAG must validate; every declared external prerequisite must point to a node in another bundled contract. This is an implementation constraint of the current curated explorer, not a restriction on scientific graphs in general. The source evidence files themselves are not copied into the public bundle.

The app does not automatically promote `constructed`, `resolved`, `source_located` or similar research dispositions into formal outcomes. Null outcomes are displayed as **none recorded**. Declared boundaries and raw nodes remain inspectable. Snapshot hashes identify source bytes; they do not rerun scientific checkers, verify their dependencies, or certify physics.

## Verification

```sh
pnpm nets:prepare
pnpm nets:check
pnpm nets:test
pnpm nets:test:browser
```

Unit/build tests cover dependency failures, input preservation, link safety, inline-script escaping, determinism, source freshness and broken external references. Chromium tests open the identical asset by both file URL and a temporary HTTP server; they exercise full-width/90vh geometry, closable selection, tabs, D3 weights, port/arrow selection and AND-aware dimming, keyboard navigation, filtering, external dependencies, fragment reload, JSON download, hostile local input and mobile width. Browser binaries must already be installed for Playwright (otherwise install Chromium with the project's approved dependency workflow).

The tests validate the explorer, not the source conjectures. No deployment or central epistemic admission is performed.
