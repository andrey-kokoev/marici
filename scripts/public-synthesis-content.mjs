// Canonical public projections shared by the publisher and freshness checks.
export const synthesisPages = [
  { source: 'docs/landing-page.md', target: 'website/index.md', route: '/' },
  { source: 'docs/theory-page.md', target: 'website/research/theory/index.md', route: '/research/theory/' },
  { source: 'docs/results-page.md', target: 'website/research/results/index.md', route: '/research/results/' },
  { source: 'docs/system-characteristics.md', target: 'website/research/system-characteristics/index.md', route: '/research/system-characteristics/' },
]

export function normalizePublicSynthesis(content) {
  return content
    .replaceAll('](/results/#bridges)', '](#postnikov-descent)')
    .replaceAll('](/results/#control)', '](#the-universe-as-a-feedback-system)')
    .replaceAll('](/results/#frontier)', '](/research/results/)')
    .replaceAll('](/results/', '](/research/results/')
    .replaceAll('](/theory/', '](/research/theory/')
    .replace(/\]\(\.\.\/research\/([^)]*)\)/g, (_, relative) => `](https://github.com/andrey-kokoev/marici/blob/main/research/${relative})`)
    .replaceAll('](theory-page.md', '](/research/theory/')
}

export function predictionTargets(landingSource) {
  const start = landingSource.indexOf('## Predictions')
  const end = landingSource.indexOf('**Construction and formalizations**', start)
  const section = start >= 0 ? landingSource.slice(start, end > start ? end : undefined) : '# Predictions\n\nSee the [landing page](/#predictions).\n'
  return `# Predictions and comparison targets\n\n${section.replace(/^## Predictions(?: and comparison targets)?\s*/, '').replaceAll('](/results/', '](/research/results/').replaceAll('](/theory/', '](/research/theory/')}`
}
