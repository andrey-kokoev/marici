// Rendering compatibility only. Never rewrite the historical ledger files.
// Use named operators for source commands unavailable in KaTeX.
export const ledgerMathMacros = {
  '\\shuffle': '\\mathbin{\\operatorname{shuffle}}',
  '\\bigboxtimes': '\\mathop{\\boxtimes}\\limits',
  '\\dlog': '\\operatorname{dlog}',
}

// Entry-scoped syntax repairs, retaining the mathematical operands and order.
// If a source is corrected upstream, require review/removal of its adapter.
const repairs = new Map([
  [53, ['\\tag{ER_e}', '\\tag{ER\\_e}']],
  [63, ['B_0(K)' + String.fromCharCode(13) + 'ight]_c.', 'B_0(K)\\right]_c.']],
  [304, ['\\frac{dr}\n-2xy(r+1)+E(yr^2+2x+y-E)}', '\\frac{dr}\n{-2xy(r+1)+E(yr^2+2x+y-E)}']],
  [1472, ['\\partial_\\eta\\!left(a^2G\\phi\\right)', '\\partial_\\eta\\!\\left(a^2G\\phi\\right)']],
  [3010, ['\\left{\n\\frac{1}{1+\\varepsilon^2}', '\\left\\{\n\\frac{1}{1+\\varepsilon^2}']],
])
export const repairedLedgerEntries = new Set(repairs.keys())
export function normalizeLedgerForPublication(source, entry) {
  // Canonicalize CRLF, but retain the lone CR typo for its explicit repair.
  let text = source.replaceAll('\r\n', '\n')
  const repair = repairs.get(entry)
  if (repair) {
    const [from, to] = repair
    if (text.split(from).length !== 2) {
      throw new Error(`Entry ${entry}: publication notation repair no longer matches uniquely; review source`)
    }
    text = text.replace(from, to)
  }
  return text
    .replace(/^\s*\\\[[ \t]*$/gm, () => '$$')
    .replace(/^\s*\\\][ \t]*$/gm, () => '$$')
    .replace(/\\\((.*?)\\\)/g, (_, formula) => `$${formula}$`)
}
