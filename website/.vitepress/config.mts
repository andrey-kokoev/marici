import { defineConfig } from 'vitepress'
import { katex } from '@mdit/plugin-katex'

export default defineConfig({
  title: 'Marici',
  description: 'Relational constructions, physical hypotheses, verification boundaries, and excluded branches.',
  cleanUrls: true,
  ignoreDeadLinks: false,
  sitemap: { hostname: 'https://marici.andrei-kokoev.workers.dev' },
  markdown: {
    config(md) {
      md.use(katex, { throwOnError: false, strict: 'error' })
      // Standalone public HTML has no VitePress page module. A target attribute
      // prevents the client router from turning these clicks into SPA routes.
      md.core.ruler.push('standalone-experiment-links', state => {
        for (const block of state.tokens) for (const token of block.children || []) {
          if (token.type === 'link_open' && /^\/experiments\/.+\.html(?:[?#]|$)/.test(token.attrGet('href') || '')) {
            token.attrSet('target', '_self')
          }
        }
      })
    },
  },
  themeConfig: {
    nav: [
      { text: 'Theory', link: '/research/theory/' },
      { text: 'Architecture', link: '/research/system-characteristics/' },
      { text: 'Results', link: '/research/results/' },
      { text: 'Constructions', link: '/experiments/' },
      { text: 'Isotope / R-space', link: '/experiments/isotope-space' },
      { text: 'Matter', items: [
        { text: 'Isotope wiring editor', link: '/experiments/isotope-wiring' },
        { text: 'Observed isotope reference', link: '/experiments/isotope-reference' },
        { text: 'Element & isotope catalogue', link: '/experiments/matter-catalog.html', target: '_self' },
        { text: 'Standard Model graph', link: '/matter/standard-model-graph' },
      ] },
      { text: 'Research', items: [
        { text: 'Reader fields · bounded coherence', link: '/research/results/tessellated-reader-fields' },
        { text: 'AdS–dS projective frontier', link: '/research/programs/ads-ds-projective-frontier' },
        { text: 'Comparison targets', link: '/research/predictions/' },
        { text: 'Research ledger', link: '/research/ledger/' },
        { text: 'Research graph', link: '/explore/graph/' },
        { text: 'Construction workbench modes', link: '/experiments/construction-workbench' },
        { text: 'Native N-cut belt viewer', link: '/experiments/native-belt-guide' },
        { text: 'Conjecture nets', link: '/experiments/conjecture-nets.html', target: '_self' },
      ] },
      { text: 'About', items: [
        { text: 'Team', link: '/about/team/' },
        { text: 'Source repository', link: 'https://github.com/andrey-kokoev/marici' },
      ] },
    ],
    socialLinks: [{ icon: 'github', link: 'https://github.com/andrey-kokoev/marici' }],
    search: {
      provider: 'local',
      options: { locales: { root: { translations: {
        button: { buttonText: 'Search site pages', buttonAriaLabel: 'Search site pages' },
      } } } },
    },
    outline: { level: [2, 3], label: 'On this page' },
    sidebar: {
      '/research/theory/': [{ text: 'Theory · explanations and boundaries', items: [
        { text: 'Current synthesis', link: '/research/theory/#recent-constructive-results-and-exclusions' },
        { text: 'Retained projective frontier', link: '/research/theory/#retained-projective-frontier' },
        { text: 'Witness glossary', link: '/research/theory/#witness-generator-glossary' },
        { text: 'Source-relative higher admission', link: '/research/theory/#source-relative-continuation-and-higher-admission' },
        { text: 'Native joins and readers', link: '/research/theory/#native-joins-and-complete-record-comparisons' },
        { text: 'Actions, content and operations', link: '/research/theory/#comparison-actions-and-operation-valued-boundaries' },
        { text: 'Dependent four-return', link: '/research/theory/#coherent-dependent-four-return' },
        { text: 'Finite-place incidence', link: '/research/theory/#finite-place-incidence-and-physical-descent' },
        { text: 'Carrier and probes', link: '/research/theory/#_1-the-carrier' },
        { text: 'Restriction vs promotion', link: '/research/theory/#_5-the-ladder-descent-—-restriction-versus-promotion' },
        { text: 'Physical comparison boundaries', link: '/research/theory/#_7-qm-projection-—-interference-phases-and-the-born-rule' },
        { text: 'Constants and comparison models', link: '/research/theory/#_17-fundamental-constants' },
        { text: 'Mathematical connections', link: '/research/theory/#_18-mathematical-connections' },
      ] }],
      '/research/system-characteristics/': [{ text: 'Architecture · contracts and assumptions', items: [
        { text: 'Synthesis status', link: '/research/system-characteristics/#current-synthesis-status' },
        { text: 'Native continuation contracts', link: '/research/system-characteristics/#native-continuation-and-comparison-contracts' },
        { text: 'Concrete atom routes', link: '/research/system-characteristics/#concrete-atom-route-transport' },
        { text: 'Structural characteristics', link: '/research/system-characteristics/#structural-characteristics' },
        { text: 'Software architecture', link: '/research/system-characteristics/#system-as-a-software-architecture' },
        { text: 'Record-type cycle', link: '/research/system-characteristics/#record-type-fibration-cycle-supporting-work' },
        { text: 'Conditional dynamics', link: '/research/system-characteristics/#dynamical-characteristics' },
        { text: 'Physical identifications', link: '/research/system-characteristics/#physical-identifications-and-normalization' },
        { text: 'Corrections and scope', link: '/research/system-characteristics/#corrections-and-scope-boundaries' },
        { text: 'Next synthesis step', link: '/research/system-characteristics/#next-synthesis-step' },
      ] }],
      '/research/results/': [{ text: 'Results · checks, exclusions and open tests', items: [
        { text: 'New results frontier · October 2026', link: '/research/results/#new-results-frontier-october-2026' },
        { text: 'Cross-sector follow-ups', link: '/research/results/#cross-sector-follow-ups' },
        { text: 'Native N-cut belt · October 25', link: '/research/results/#october-25-native-n-cut-belt-attachment' },
        { text: 'Reader fields · October 18', link: '/research/results/tessellated-reader-fields' },
        { text: 'October 12 · retained information', link: '/research/results/#october-12-retained-information-and-claim-boundaries' },
        { text: 'Earlier synthesis', link: '/research/results/#current-research-synthesis-october-8–10-2026' },
        { text: 'Exclusions and open selection', link: '/research/results/#exclusions-and-unresolved-selection' },
        { text: 'Comparison-tower checks', link: '/research/results/#current-comparison-tower-checks' },
        { text: 'Spin and charge audit', link: '/research/results/#tetrahedral-spin-and-charge-audit' },
        { text: 'Scoped physical hypotheses', link: '/research/results/#physical-hypotheses-corrected-status' },
        { text: 'Numerical comparison targets', link: '/research/results/#numerical-comparison-targets' },
        { text: 'Next discriminating tests', link: '/research/results/#next-discriminating-tests' },
        { text: 'Source-bound frontier map', link: '/research/frontier/current' },
      ] }],
    },
  },
})
