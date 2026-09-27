/**
 * Marici static site builder.
 * Reads .astro pages, strips Astro wrapping, renders KaTeX,
 * generates ledger entries from markdown, produces plain HTML.
 */

import { readFileSync, writeFileSync, mkdirSync, cpSync, existsSync, readdirSync, rmSync } from 'fs'
import { resolve, dirname, join } from 'path'
import katex from 'katex'

const ROOT = resolve(import.meta.dirname, '..')
const DIST = join(ROOT, 'dist')
const SITE_URL = process.env.PUBLIC_SITE_URL || 'https://marici.andrei-kokoev.workers.dev'

const K = (t, d) => { try { return katex.renderToString(t, { displayMode: d, throwOnError: false, output: 'htmlAndMathml' }) } catch { return `<span class="katex-error">${t}</span>` } }
const katexAll = h => h.replace(/<KaTeX\s+tex="((?:\\.|[^"])*?)"\s*\/?>/g, (_, t) => K(t.replace(/\\(.)/g,'$1')))

function P(title, desc, body, path) {
  const e = s => s.replace(/"/g,'&quot;')
  const url = path ? `${SITE_URL}${path}` : `${SITE_URL}/`
  return `<!doctype html><html lang="en" class="dark">
<head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<meta name="description" content="${e(desc)}"/><meta name="theme-color" content="#071117"/>
<meta property="og:title" content="${e(title)}"/><meta property="og:description" content="${e(desc)}"/>
<link rel="canonical" href="${url}"/><link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Cpath fill='%23ffae62' d='M32 4 58 19v30L32 64 6 49V19z'/%3E%3Cpath fill='%23071117' d='m32 15 15 9v17l-15 9-15-9V24z'/%3E%3C/svg%3E"/>
<link rel="stylesheet" href="/katex.min.css"/><link rel="stylesheet" href="/styles.css"/>
<title>${title.replace(/</g,'&lt;')}</title></head>
<body><a class="skip-link" href="#main-content">Skip to main content</a>
<header class="site-header"><a class="brand" href="/" aria-label="Marici home">
<span class="brand-mark" aria-hidden="true"></span><span>Marici</span></a>
<nav aria-label="Primary navigation"><a href="/theory/">Theory</a><a href="/results/">Results</a>
<a href="/#predictions" class="nav-highlight">Predictions</a><a href="/ledger/">Ledger</a></nav></header>
<main id="main-content">${body}</main></body></html>`
}

function W(p, c) { const f = join(DIST, p); mkdirSync(dirname(f), {recursive:true}); writeFileSync(f, c, 'utf-8') }

// Strip Astro wrapping from a .astro file
function stripAstro(path) {
  let s = readFileSync(path, 'utf-8')
  return s.replace(/^---[\s\S]*?---\n*/, '').replace(/^import\s+.*?from\s+['"].*?['"];?\n*/gm, '')
    .replace(/^interface\s+\w+\s*\{[\s\S]*?\}\n*/m, '')
    .replace(/<SiteLayout[\s\S]*?>/, '').replace(/<\/SiteLayout>/, '')
    .replace(/<style[^>]*>[\s\S]*?<\/style>/g, '').trim()
}

// Extract data arrays from .astro frontmatter
function extractData(path) {
  const src = readFileSync(path, 'utf-8')
  const m = src.match(/^---\r?\n([\s\S]*?)\r?\n---/)
  if (!m) return {}
  const clean = m[1].replace(/^import\s+.*\r?\n*/gm, '').replace(/katex\.renderToString\([\s\S]*?\)/g, "''")
  const names = (clean.match(/(?:const|let|var)\s+(\w+)\s*=/g)||[]).map(v => v.replace(/(?:const|let|var)\s+|\s*=\s*/g,'').trim())
  try { const fn = new Function(clean + '\nreturn {' + names.join(',') + '};'); return fn() }
  catch { return {} }
}

// Ledger markdown to HTML
function mdToHtml(body) {
  let md = body.replace(/^#\s+.*$/m, '').trim()

  // 1. Protect code blocks
  const cbs = []
  md = md.replace(/```(\w*)\n([\s\S]*?)```/g, (_, l, c) => {
    cbs.push(`<pre><code class="language-${l}">${c.replace(/</g,'&lt;').replace(/>/g,'&gt;')}</code></pre>`)
    return `\x00CB${cbs.length-1}\x00`
  })

  // 2. Math display: \[...\] and $$...$$
  md = md.replace(/\\\[([\s\S]*?)\\\]/g, (_, t) => `\n{MATH D ${t.trim()}}\n`)
  md = md.replace(/\$\$([\s\S]*?)\$\$/g, (_, t) => `\n{MATH D ${t.trim()}}\n`)

  // 3. Inline math: $...$ (simple, must have space before/after or be at boundary)
  md = md.replace(/(?<!\w)\$(.+?)\$(?!\w)/g, (_, t) => ` {MATH I ${t.trim()}} `)

  // 4. Headings
  md = md.replace(/^##\s+(.+)$/gm, '<h2>$1</h2>').replace(/^###\s+(.+)$/gm, '<h3>$1</h3>')

  // 5. Bold, italic, links
  md = md.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>').replace(/\*(.+?)\*/g, '<em>$1</em>')
  md = md.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank">$1</a>')

  // 6. Replace math placeholders
  md = md.replace(/\{MATH (D|I) ([^}]+)\}/g, (_, m, t) => K(t.trim(), m === 'D'))

  // 7. Split into blocks
  return md.split(/\n{2,}/).map(b => b.trim()).filter(b => b).map(b => {
    if (b.match(/^\x00CB\d+\x00$/)) return cbs[+b.match(/\x00CB(\d+)\x00/)[1]]
    if (b.match(/^[-*]\s/m)) {
      const items = b.split('\n').filter(l => l.trim()).map(l => `<li>${l.replace(/^[-*]\s+/, '').trim()}</li>`)
      return `<ul>${items.join('\n')}</ul>`
    }
    if (b.match(/^\d+\.\s/m)) {
      const items = b.split('\n').filter(l => l.trim()).map(l => `<li>${l.replace(/^\d+\.\s+/, '').trim()}</li>`)
      return `<ol>${items.join('\n')}</ol>`
    }
    if (b.startsWith('>')) return `<blockquote>${b.replace(/^>\s*/gm, '').trim()}</blockquote>`
    if (b.match(/^<[h23pulolidivpreblockquote]/)) return b
    return `<p>${b}</p>`
  }).join('\n')
}

console.log('Building...')
if (existsSync(DIST)) for (const f of readdirSync(DIST)) rmSync(join(DIST, f), {recursive:true,force:true})
mkdirSync(DIST, {recursive:true})

// ── CSS ────────────────────────────────────────────────────────────
const kc = join(ROOT, 'node_modules', 'katex', 'dist', 'katex.min.css')
if (existsSync(kc)) cpSync(kc, join(DIST, 'katex.min.css'))
let css = ''
for (const f of ['src/styles/global.css','../narada/packages/ui/dist/tokens.css',
  '../narada/packages/ui/dist/primitives.css','../narada/packages/ui/dist/design-system.css',
  '../narada/packages/ui/dist/styles.css','src/styles/frontier.css','src/styles/oddballs.css']) {
  const p = join(ROOT, f); if (existsSync(p)) css += readFileSync(p, 'utf-8') + '\n'
}
// Landing-page table styles (were in index.astro <style> block, stripped by stripAstro)
css += '\n.section-heading{grid-template-columns:1fr}' +
  '.dimension-table{width:100%;border-collapse:collapse;border:1px solid var(--line);border-radius:8px;overflow:hidden}' +
  '.dt-role{padding:12px 16px 4px;font:700 .72rem/1.3 Consolas,monospace;letter-spacing:.13em;text-transform:uppercase;color:var(--ochre);border-bottom:1px solid var(--line-soft)}' +
  '.dt-name{padding:12px 16px 4px;font-size:1.1rem;font-weight:650;border-bottom:1px solid var(--line-soft)}' +
  '.dt-body{padding:8px 16px 12px;color:var(--muted);font-size:.85rem;line-height:1.5}' +
  // Ledger page styles (were in ledger.astro <style> block)
  '.ledger-page h1{font-size:clamp(1.6rem,3.2vw,2.4rem);letter-spacing:-.03em;line-height:1.15}' +
  '#search{--pagefind-ui-background:var(--panel);--pagefind-ui-text:var(--ink);--pagefind-ui-border:var(--line);--pagefind-ui-primary:var(--ochre);--pagefind-ui-tag:var(--panel-raised)}' +
  '#search .pagefind-ui__search-clear{background:transparent;border:none;font-size:.85rem;font-weight:450;opacity:.55;padding:0 14px;top:0;right:3px;border-radius:0}' +
  '#search .pagefind-ui__search-clear:hover{opacity:1}\n'
W('styles.css', css)
if (existsSync(join(ROOT, 'public'))) {
  for (const f of readdirSync(join(ROOT, 'public'))) cpSync(join(ROOT, 'public', f), join(DIST, f), {recursive:true})
}
console.log('  CSS + assets')

// ── Landing ────────────────────────────────────────────────────────
W('index.html', P('Marici · Physics from one object',
  'A single 4-point carrier with automorphism group S4 and overlap matrix G_ij gives quantum mechanics, general relativity, the Standard Model.',
  katexAll(stripAstro(join(ROOT, 'src', 'pages', 'index.astro'))), '/'))
console.log('  /index.html')

// ── Ledger ─────────────────────────────────────────────────────────
const LD = join(ROOT, 'src', 'ledger')
const entries = []
for (const f of readdirSync(LD).sort().reverse()) {
  if (!f.endsWith('.md')) continue
  const m = f.match(/^(\d{8})-(\d+)[ _-](.+)$/)
  if (!m) continue
  const [, dk, en, ts] = m
  const body = readFileSync(join(LD, f), 'utf-8')
  const title = body.match(/^#\s+(.+)$/m)?.[1]?.trim() || ts
  const desc = (body.replace(/^#\s+.*$/m, '').trim().split(/\n\n+/).find(p => p.trim()) || body).slice(0, 200)
  const slug = `${dk}-${en}-${ts}`.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'')
  const dt = new Date(dk.slice(0,4)+'-'+dk.slice(4,6)+'-'+dk.slice(6,8))
  entries.push({entry:Number(en), title, slug, body, desc, dt, date:dt.toLocaleDateString('en-US',{dateStyle:'medium',timeZone:'UTC'})})
}

const list = entries.map(e => `<a class="article-card" href="/ledger/${e.slug}/"><div class="article-meta"><span class="entry-no">Entry ${String(e.entry).padStart(3,'0')}</span></div><h2>${e.title}</h2><p>${e.desc}</p><p class="ledger-status-inline">Published source entry</p><div class="article-meta"><time datetime="${e.dt.toISOString()}">${e.date}</time><span>Read entry →</span></div></a>`).join('\n')
W('ledger/index.html', P("The Resident's Ledger · Marici", "Published research ledger entries.",
`<section class="ledger-page" aria-labelledby="ledger-title"><p class="eyebrow">The Resident's Ledger</p><h1 id="ledger-title">Research ledger</h1><p class="lede">Marici authors record the research as numbered entries.</p><p class="ledger-count">${entries.length} published entries · corrections remain new entries.</p><div id="search" style="margin-block:1.5rem;"></div><link href="/pagefind/pagefind-ui.css" rel="stylesheet"><script src="/pagefind/pagefind-ui.js" type="text/javascript" defer></script><script>window.addEventListener('DOMContentLoaded',()=>{new PagefindUI({element:"#search",showSubResults:true,resetStyles:false})});</script><section class="article-list" aria-label="Ledger entries">${list}</section></section>`, '/ledger/'))

let ec = 0
for (const e of entries) {
  const html = mdToHtml(e.body)
  W(`ledger/${e.slug}/index.html`, P(`${e.title} · Marici Ledger`, e.desc,
    `<article class="ledger-entry"><header><p class="eyebrow">Entry ${String(e.entry).padStart(3,'0')}</p><h1>${e.title}</h1><div class="byline"><dl><dt>Entry</dt><dd>${e.entry}</dd></dl><dl><dt>Date</dt><dd><time datetime="${e.dt.toISOString()}">${e.date}</time></dd></dl></div></header><div class="entry-body">${html}</div></article>`, `/ledger/${e.slug}/`))
  ec++
  if (ec % 500 === 0) console.log(`  ...${ec} entries`)
}
console.log(`  /ledger/ (${ec} entries)`)

// ── Team ────────────────────────────────────────────────────────────
const teamData = [
  ['marici.Nima','Categorical architecture and cross-sector synthesis','Develops the shared Carrier calculus, source-relative germ architecture, bidirectional comparison laws, and completion-stable coherence questions connecting sector realizations.','Synthesizes cross-sector invariants, separates source authority from transported evidence, and turns recurring structural patterns into finite hostile tests.','research/nima/'],
  ['marici.Benincasa','Geometric and cohomological machinery','Builds localization, relative and exceptional geometry, nearby-cycle, Gysin, connection, and cross-sector comparison machinery.','Tests whether proposed physical or coefficient objects are supported by source geometry and coherent transport.','research/benincasa/'],
  ['marici.Figueiredo','Flavor reconstruction and observer descent','Separates presentation coordinates from physical quotient data.','Audits flavor and CP readouts, multi-observer reconciliation, quotient faithfulness.','research/flavor/'],
  ['marici.Strominger','Authority composition and repair coherence','Develops typed partial multicategories, constructor-tree authority, fault-indexed quorum proofs.','Tests whether evidence can lawfully compose into operative authority.','research/strominger/'],
  ['marici.Grothendieck','Theta/Tate source geometry and arithmetic completion','Builds the two-sector theta/Tate source architecture.','Supplies source-derived arithmetic incidence and tests finite exactness.','research/grothendieck/'],
  ['marici.Buzzard','Formalization and hidden-assumption detection','Formalizes stabilized exact theorems.','Determines whether informal claims type-check.','research/buzzard/'],
  ['marici.Kitaev','Protected information and observability audits','Develops anyon and Wilson transport, quantum error correction.','Tests which typed ports detect hidden sectors.','research/kitaev/'],
  ['marici.Sontag','Control-theoretic factorization and realization','Factors observability, controllability, feedback through typed Carrier architecture.','Uses control theory to predict missing ports.','research/sontag/'],
  ['marici.Aspect','Optical laboratory and route-effect falsification','Develops source-typed propagation, interference, polarization.','Builds finite apparatus witnesses for common-frame claims.','research/aspect/'],
]
const teamCards = teamData.map(m => `<li class="team-card"><header><div><p class="team-role">${m[1]}</p><h2>${m[0]}</h2></div><a href="#">Graph record</a></header><p>${m[2]}</p><dl><div><dt>Team interface</dt><dd>${m[3]}</dd></div><div><dt>Workspace</dt><dd><code>${m[4]}</code></dd></div></dl></li>`).join('\n')
W('team/index.html', P('Research team | Marici', 'Canonical Marici research identities.',
`<section class="section-shell" aria-labelledby="team-title"><header class="section-heading"><div><p class="eyebrow">Research identities</p><h1 id="team-title">One programme, distinct responsibilities.</h1></div><p>Marici uses qualified research identities so that claims retain an accountable owner while cross-sector work remains part of one shared programme.</p></header><aside class="registry-note"><p><strong>Registry authority</strong></p><p>Human policy: <code>AGENTS.md#canonical-team-identities</code>. Durable identities: <code>marici-epistemic-graph</code> entities of kind <code>team_member</code>.</p></aside><ul class="team-grid" aria-label="Marici team members">${teamCards}</ul></section>`, '/team/'))
console.log('  /team/index.html')

// ── Programmes ──────────────────────────────────────────────────────
W('programmes/nima-amplitudes/index.html', P('Nima amplitudes programme | Marici', 'Research programme on scattering amplitudes.',
  katexAll(stripAstro(join(ROOT, 'src', 'pages', 'programmes', 'nima-amplitudes.astro'))), '/programmes/nima-amplitudes/'))
console.log('  /programmes/nima-amplitudes/')

// ── Results ─────────────────────────────────────────────────────────
const rD = extractData(join(ROOT, 'src', 'pages', 'results', 'index.astro'))
const physics = rD.physics || [], math = rD.math || [], explanations = rD.explanations || []
let rSteps = rD.renderedSteps || []
if (Array.isArray(rSteps) && rSteps.length > 0) rSteps = rSteps.map(s => ({...s, rendered: K(s.formula || '', true)}))

const ss = st => st === 'Partial' ? 'background:#5c5c1a;color:#ff8' : st === 'Schematic' ? 'background:#1a3c5c;color:#8cf' : ''
const physRows = physics.map(p => `<tr><td><a href="/results/${p.slug}/" style="color:inherit;text-decoration:underline;text-underline-offset:2px;">${p.domain}</a></td><td><span class="status-pill" style="${ss(p.status)}">${p.status}</span></td><td>${p.connection}</td></tr>`).join('\n')
const mathRows = math.map(m => `<tr><td>${m.domain}</td><td>${m.connection}</td></tr>`).join('\n')
const expRows = explanations.map(x => `<tr><td><strong>${x.explanation}</strong></td><td>${x.derived}</td></tr>`).join('\n')
const stepCards = rSteps.map(s => `<li class="dimension-card"><header><span class="dimension-number">${s.number}</span><div><p class="dimension-role">${s.name}</p></div></header><div class="formula">${s.rendered}</div></li>`).join('\n')

// Build results page: strip .astro body, replace each {expr} map with generated HTML
function replaceMaps(body) {
  for (const [name, html] of [['renderedSteps', stepCards], ['physics', physRows], ['math', mathRows], ['explanations', expRows]]) {
    const re = new RegExp(`\\{${name}\\.\\([\\s\\S]*?\\)\\}`);
    // This won't work for nested. Instead find by manual parsing.
    const idx = body.indexOf(`{${name}.map(`)
    if (idx < 0) continue
    let depth = 0, i = idx
    while (i < body.length) {
      const c = body[i]
      if ("{([`'".indexOf(c) >= 0) {
        if (c === '{' || c === '(') depth++
        else if (c === '}' || c === ')') { depth--; if (depth < 0) break }
        else if (c === '`') { i = body.indexOf('`', i+1); if (i < 0) break; } // skip template literal
        else if (c === "'" || c === '"') { i = body.indexOf(c, i+1); if (i < 0) break; } // skip string
      }
      i++
    }
    body = body.slice(0, idx) + html + body.slice(i+1)
  }
  return body
}
let rBody = stripAstro(join(ROOT, 'src', 'pages', 'results', 'index.astro'))
rBody = replaceMaps(rBody)
  .replace(/\{physics\.length\}/g, physics.length)
  .replace(/\{math\.length\}/g, math.length)
  .replace(/\{explanations\.length\}/g, explanations.length)
  .replace(/\{renderedSteps\.length\}/g, rSteps.length)
  .replace(/class:\w+=/g, 'class=')
W('results/index.html', P('Results & predictions | Marici', 'Complete results and predictions.', katexAll(rBody), '/results/'))
console.log('  /results/index.html')

// ── Theory ─────────────────────────────────────────────────────────
const tD = extractData(join(ROOT, 'src', 'pages', 'theory', 'index.astro'))
const sections = tD.sections || []
const secHtml = sections.map(s => `<section id="${s.id}"><h2>${s.title}</h2>${s.content}</section>`).join('\n')
let tBody = stripAstro(join(ROOT, 'src', 'pages', 'theory', 'index.astro'))
tBody = tBody.replace(/\{sections\.map\([\s\S]*?\)\}/, secHtml).replace(/\{sections\.length\}/, sections.length)
W('theory/index.html', P('Full derivation | Marici', 'The relational carrier derivation.', katexAll(tBody), '/theory/'))
console.log(`  /theory/index.html (${sections.length} sections)`)

// ── 404 + Sitemap ──────────────────────────────────────────────────
W('404.html', P('Not found | Marici', 'Page not found.',
`<section class="section-shell" style="text-align:center;padding:4rem 1rem;"><h1 style="font-size:3rem;">404</h1><p style="margin-top:1rem;color:var(--muted);">This page does not exist.</p><a href="/" class="primary-action" style="margin-top:1.5rem;display:inline-block;">Return home</a></section>`))

const allUrls = ['/', '/team/', '/results/', '/theory/', '/programmes/nima-amplitudes/', '/ledger/', ...entries.map(e => `/ledger/${e.slug}/`)]
W('sitemap.xml', `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${allUrls.map(u => `  <url><loc>${SITE_URL}${u}</loc></url>`).join('\n')}\n</urlset>`)
console.log(`  /sitemap.xml (${allUrls.length} URLs)`)
console.log('Done.')