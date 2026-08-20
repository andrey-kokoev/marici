import fs from 'node:fs/promises'
import path from 'node:path'
import process from 'node:process'
import { fileURLToPath } from 'node:url'
import { createMarkdownProcessor, markdownConfigDefaults } from '@astrojs/markdown-remark'
import katex from 'katex'
import rehypeKatex from 'rehype-katex'
import remarkMath from 'remark-math'
import remarkNaradaMath from '../src/lib/remark-narada-math.mjs'
import { convertTexMath, katexOptions } from '../src/lib/ledger-math.mjs'

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const LEDGER_DIR = path.join(ROOT, 'src', 'ledger')
const DIST_DIR = path.join(ROOT, 'dist')
const mode = process.argv[2] || 'source'
let activeMathNodes = null

if (mode !== 'source' && mode !== 'dist') {
  console.error('Usage: node scripts/check-katex.mjs [source|dist]')
  process.exit(2)
}

const processor = await createMarkdownProcessor({
  ...markdownConfigDefaults,
  remarkPlugins: [remarkMath, remarkNaradaMath],
  rehypePlugins: [
    function collectMathPlugin() {
      return function collectMath(tree) {
        if (activeMathNodes) collectMathElements(tree, activeMathNodes)
      }
    },
    [rehypeKatex, katexOptions],
  ],
})

function errorMessage(error) {
  return error instanceof Error ? error.message : String(error)
}

function relativePath(filePath) {
  return path.relative(ROOT, filePath).split(path.sep).join('/')
}

function ledgerSlug(filePath) {
  return path
    .basename(filePath, path.extname(filePath))
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
}

function ledgerPrefix(filePath) {
  const match = path.basename(filePath).match(/^(\d{8})[- _](\d+)/)
  return match ? match[1] + '-' + match[2] + '-' : null
}

function hasDraftFrontmatter(source) {
  const frontmatter = source.match(/^---\s*\r?\n([\s\S]*?)\r?\n---(?:\s*\r?\n|$)/)
  return Boolean(frontmatter && /(?:^|\r?\n)\s*draft\s*:\s*true\s*(?:\r?\n|$)/i.test(frontmatter[1]))
}

async function listMarkdownFiles(directory) {
  const files = []
  const entries = await fs.readdir(directory, { withFileTypes: true })
  for (const entry of entries) {
    const entryPath = path.join(directory, entry.name)
    if (entry.isDirectory()) {
      files.push(...(await listMarkdownFiles(entryPath)))
    } else if (entry.isFile() && /\.(?:md|mdx)$/i.test(entry.name)) {
      files.push(entryPath)
    }
  }
  return files.sort()
}

function maskFencedCode(source) {
  const lines = source.split(/\r?\n/)
  let fenceCharacter = null
  return lines
    .map((line) => {
      const openingFence = line.match(/^\s*(\x60{3,}|~{3,})/)
      if (fenceCharacter === null && openingFence) {
        fenceCharacter = openingFence[1][0]
        return ''
      }
      if (
        fenceCharacter !== null &&
        new RegExp('^\\s*' + fenceCharacter + '{3,}\\s*$').test(line)
      ) {
        fenceCharacter = null
        return ''
      }
      return fenceCharacter === null ? line : ''
    })
    .join('\n')
}

function findDelimiterDefect(source) {
  const visibleSource = maskFencedCode(source)
  const inlineOpenCount = (visibleSource.match(/(?<!\\)\\\(/g) || []).length
  const inlineCloseCount = (visibleSource.match(/(?<!\\)\\\)/g) || []).length
  if (inlineOpenCount !== inlineCloseCount) {
    return 'unpaired custom inline-TeX delimiter'
  }

  const flowOpenCount = (visibleSource.match(/(?<!\\)\\\[/g) || []).length
  const flowCloseCount = (visibleSource.match(/(?<!\\)\\\]/g) || []).length
  if (flowOpenCount !== flowCloseCount) {
    return 'unpaired custom display-TeX delimiter'
  }

  const visibleLines = visibleSource.split('\n')
  for (let index = 0; index < visibleLines.length; index += 1) {
    const line = visibleLines[index].replace(/\\\$/g, '').replace(/\$\$/g, '')
    const singleDollarCount = (line.match(/\$/g) || []).length
    const looksLikeTeX = /\$\s*(?:\\[A-Za-z]|[A-Za-z]*[{}_^])/.test(line)
    if (singleDollarCount % 2 === 1 && looksLikeTeX) {
      return 'unpaired inline-dollar delimiter near source line ' + (index + 1)
    }
  }

  return null
}

function textContent(node) {
  if (!node || typeof node !== 'object') return ''
  if (node.type === 'text') return String(node.value ?? '')
  return Array.isArray(node.children) ? node.children.map(textContent).join('') : ''
}

function collectMathElements(node, result = []) {
  if (!node || typeof node !== 'object') return result
  const className = node.properties?.className
  const classes = Array.isArray(className) ? className : [className]
  if (node.type === 'element' && (classes.includes('math-inline') || classes.includes('math-display'))) {
    result.push({
      value: textContent(node),
      displayMode: classes.includes('math-display'),
      position: node.position,
    })
  }
  if (Array.isArray(node.children)) {
    for (const child of node.children) {
      collectMathElements(child, result)
    }
  }
  return result
}

function nodeLine(node) {
  const line = node.position?.start?.line
  return line ? ':' + line : ''
}

function countKaTeX(html) {
  return (html.match(/class="katex"/g) || []).length
}

async function validateSource(filePath) {
  const source = await fs.readFile(filePath, 'utf8')
  const convertedSource = convertTexMath(source)
  const relative = relativePath(filePath)
  const failures = []
  const delimiterDefect = findDelimiterDefect(source)

  if (delimiterDefect) {
    failures.push({ file: relative, message: delimiterDefect })
  }

  const mathNodes = []
  let html = ''
  activeMathNodes = mathNodes
  try {
    const rendered = await processor.render(convertedSource)
    html = rendered.code
  } catch (error) {
    failures.push({ file: relative, message: 'Production Markdown render failed: ' + errorMessage(error) })
  } finally {
    activeMathNodes = null
  }

  let rejectedFormulaCount = 0
  for (const node of mathNodes) {
    try {
      katex.renderToString(String(node.value), {
        ...katexOptions,
        displayMode: node.displayMode,
      })
    } catch (error) {
      rejectedFormulaCount += 1
      failures.push({
        file: relative + nodeLine(node),
        message: 'KaTeX rejected formula "' + String(node.value).replace(/\s+/g, ' ').slice(0, 160) + '": ' + errorMessage(error),
      })
    }
  }

  if (html && mathNodes.length > 0) {
    const renderedMathCount = countKaTeX(html)
    if (renderedMathCount + rejectedFormulaCount < mathNodes.length) {
      failures.push({
        file: relative,
        message: 'rendered ' + renderedMathCount + ' and rejected ' + rejectedFormulaCount + ' KaTeX formula(s), but the source contains ' + mathNodes.length,
      })
    }
    if (!html.includes('katex-mathml') && rejectedFormulaCount === 0) {
      failures.push({ file: relative, message: 'rendered math has no KaTeX MathML output' })
    }
    if (html.includes('katex-error') && rejectedFormulaCount === 0) {
      failures.push({ file: relative, message: 'rendered HTML contains a KaTeX error marker' })
    }
  }

  return {
    filePath,
    relative,
    slug: ledgerSlug(filePath),
    draft: hasDraftFrontmatter(source),
    mathCount: mathNodes.length,
    failures,
  }
}

async function validateArtifacts(results) {
  const failures = []
  for (const result of results) {
    if (result.mathCount === 0 || result.draft) continue
    const ledgerDistDir = path.join(DIST_DIR, 'ledger')
    let artifactPath = path.join(ledgerDistDir, result.slug, 'index.html')
    let html
    try {
      html = await fs.readFile(artifactPath, 'utf8')
    } catch (error) {
      const prefix = ledgerPrefix(result.filePath)
      const candidates = prefix
        ? (await fs.readdir(ledgerDistDir, { withFileTypes: true }))
            .filter((entry) => entry.isDirectory() && entry.name.startsWith(prefix))
            .map((entry) => path.join(ledgerDistDir, entry.name, 'index.html'))
        : []
      if (candidates.length === 1) {
        artifactPath = candidates[0]
        try {
          html = await fs.readFile(artifactPath, 'utf8')
        } catch (candidateError) {
          failures.push({
            file: relativePath(artifactPath),
            message: 'generated ledger artifact could not be read: ' + errorMessage(candidateError),
          })
          continue
        }
      } else {
        const suffix = candidates.length === 0 ? 'none found' : candidates.length + ' candidates found'
        failures.push({
          file: relativePath(artifactPath),
          message: 'missing generated ledger artifact (' + suffix + ' for entry prefix ' + (prefix ?? 'unknown') + ')',
        })
        continue
      }
    }

    const renderedMathCount = countKaTeX(html)
    if (renderedMathCount < result.mathCount) {
      failures.push({
        file: relativePath(artifactPath),
        message: 'generated artifact contains ' + renderedMathCount + ' KaTeX formula(s), expected at least ' + result.mathCount,
      })
    }
    if (!html.includes('katex-mathml')) {
      failures.push({ file: relativePath(artifactPath), message: 'generated artifact has no KaTeX MathML output' })
    }
    if (html.includes('katex-error')) {
      failures.push({ file: relativePath(artifactPath), message: 'generated artifact contains a KaTeX error marker' })
    }
  }
  return failures
}

async function main() {
  const files = await listMarkdownFiles(LEDGER_DIR)
  const results = []
  for (const filePath of files) {
    results.push(await validateSource(filePath))
  }

  const failures = results.flatMap((result) => result.failures)
  if (mode === 'dist') {
    failures.push(...(await validateArtifacts(results)))
  }

  if (failures.length > 0) {
    console.error('KaTeX check failed with ' + failures.length + ' finding(s):')
    for (const failure of failures) {
      console.error('- ' + failure.file + ': ' + failure.message)
    }
    process.exitCode = 1
    return
  }

  const formulaCount = results.reduce((sum, result) => sum + result.mathCount, 0)
  const suffix = mode === 'dist' ? ' and generated artifacts' : ' sources'
  console.log('KaTeX check passed: ' + results.length + suffix + ', ' + formulaCount + ' formula(s).')
}

await main()
