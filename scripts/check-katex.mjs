import fs from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import matter from 'gray-matter'
import MarkdownIt from 'markdown-it'
import { katex as markdownKatex } from '@mdit/plugin-katex'
import { ledgerMathMacros, normalizeLedgerForPublication } from './ledger-math-publication.mjs'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const mode = process.argv[2] || 'source'
if (!['source','dist'].includes(mode)) throw new Error('Usage: node scripts/check-katex.mjs [source|dist]')
const markdown = new MarkdownIt().use(markdownKatex, { throwOnError: true, strict: 'error', macros: { ...ledgerMathMacros } })
async function walk(dir) {
  const out=[]
  for(const entry of await fs.readdir(dir,{withFileTypes:true})) {
    const file=path.join(dir,entry.name)
    if(entry.isDirectory()) out.push(...await walk(file))
    else if(/\.md$/i.test(entry.name)) out.push(file)
  }
  return out
}
if(mode==='source') {
  const files=await walk(path.join(root,'src','ledger'))
  let rendered=0, formulas=0, failures=0
  for(const file of files) {
    const source=await fs.readFile(file,'utf8'), parsed=matter(source)
    if(parsed.data.draft===true) continue
    const match=path.basename(file).match(/^(\d{8})-(\d+)[ _-](.+)\.md$/i)
    if(!match) continue
    try {
      const html=markdown.render(normalizeLedgerForPublication(parsed.content, Number(match[2])))
      // The plugin catches KaTeX exceptions and emits an error element even
      // with throwOnError enabled. Treat that output as a failed render.
      if (/\bclass=["'][^"']*\bkatex-error\b/.test(html)) throw new Error('KaTeX error element emitted')
      formulas+=(html.match(/class="katex"/g)||[]).length; rendered++
    } catch(error) {
      failures++
      console.error(`${path.relative(root,file)}: ${error instanceof Error?error.message:String(error)}`)
    }
  }
  console.log(`Rendered publication-normalized math in ${rendered} ledger entries; ${formulas} KaTeX formulas; ${failures} errors. Historical sources unchanged.`)
  if(failures) process.exitCode=1
} else {
  const dist=path.join(root,'website','.vitepress','dist','research','ledger')
  const entries=await fs.readFile(path.join(dist,'index.json'),'utf8').then(JSON.parse)
  let formulas=0, checked=0, failures=0
  for(const entry of entries) {
    const html=await fs.readFile(path.join(dist,entry.slug,'index.html'),'utf8').catch(()=>null)
    if(!html){failures++;console.error(`Missing rendered ledger entry: ${entry.slug}`);continue}
    checked++;formulas+=(html.match(/class="katex"/g)||[]).length
    if (/\bclass=["'][^"']*\bkatex-error\b/.test(html)) {
      failures++; console.error(`KaTeX error element: ${entry.slug}`)
    }
    const visibleText = html
      .replace(/<!--[^]*?-->/g, '')
      .replace(/<head\b[^>]*>[^]*?<\/head>/i, '')
      .replace(/<(annotation|script|style|pre|code)\b[^>]*>[^]*?<\/\1>/gi, '')
      .replace(/<[^>]+>/g, ' ')
      .replace(/&(?:#92|#x5c|bsol);/gi, '\\')
    if(/\\\(|\\\[/.test(visibleText)){failures++;console.error(`Unconverted visible TeX delimiters: ${entry.slug}`)}
  }
  console.log(`Checked ${checked}/${entries.length} rendered ledger entries; ${formulas} KaTeX formulae; ${failures} errors.`)
  if(failures) process.exitCode=1
}
