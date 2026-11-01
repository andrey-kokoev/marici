# Isotope Wiring

This is the working app for ongoing isotope-wiring development, promoted from
`research/chatgpt/isotope-wiring.html` at the operator's request. Its canonical
editable source and entrypoint is [`index.html`](index.html), not a generated copy.

The website embeds this same source at `/experiments/isotope-wiring`, linked from
**Matter → Isotope wiring editor** and the construction index. The host component
`website/.vitepress/components/IsotopeWiring.vue` supplies the website's live theme
tokens without reloading the editor on light/dark changes. The app's `website-theme`
style block uses these tokens with standalone light-theme fallbacks.

Open `index.html` directly in a browser. The standalone HTML contains its styles,
JavaScript, and isotope fixtures; no build step or external assets are required.
Use the File menu to export projects or definitions before moving between browser
locations or making changes, and import them to resume work.

The app provides isotope selection, graph and wiring views, absolute/delta JSON
definitions, cell editing, counts, validation, and import/export. Its fixtures and
visual conventions are working research inputs, not evidence of physical adequacy.

Validate website integration with `node scripts/test-isotope-wiring-website.mjs`.
It checks rendering, theme changes without losing editor text, isotope selection,
counts, and mobile width. `vitepress build website` builds the public route.

Keep future app changes here. The separate 3D retained-expansion viewer remains
in [`../normal-ray/`](../normal-ray/); this move does not replace or merge it.
