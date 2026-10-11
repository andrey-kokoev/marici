import fs from 'node:fs/promises'
import path from 'node:path'

// Build-time freshness guard without adding Python to the website toolchain.
// Scientific/schema validation is performed by research/matter/check_catalog.py.
export async function checkMatterAssets(root) {
  const read = async relative => (await fs.readFile(path.join(root, relative), 'utf8')).replaceAll('\r\n', '\n')
  const template = await read('research/matter/catalog.template.html')
  const parts = template.split('__CATALOG_JSON__')
  const html = await read('website/public/experiments/matter-catalog.html')
  const source = JSON.parse(await read('research/matter/element-isotope-catalog.json'))
  const publicData = JSON.parse(await read('website/public/experiments/matter-catalog.json'))
  const standardModelGraph = JSON.parse(await read('research/matter/standard-model-graph.json'))
  const publicStandardModelGraph = JSON.parse(await read('website/public/standard-model-graph.json'))
  const error = () => { throw new Error('Stale matter assets: run python research/matter/prepare_catalog_asset.py') }
  if (parts.length !== 2 || !html.startsWith(parts[0]) || !html.endsWith(parts[1])) error()
  const embedded = html.slice(parts[0].length, html.length-parts[1].length)
  if (embedded.includes('<') || JSON.stringify(JSON.parse(embedded)) !== JSON.stringify(source) || JSON.stringify(publicData) !== JSON.stringify(source)) error()
  if (JSON.stringify(publicStandardModelGraph) !== JSON.stringify(standardModelGraph)) error()
}
