import { existsSync, readFileSync } from 'node:fs'
import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import { spawnSync } from 'node:child_process'

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..')
const config = JSON.parse(readFileSync(resolve(root, 'config/narada-source.json'), 'utf8'))
const checkout = process.env.NARADA_SOURCE_CHECKOUT
  ? resolve(process.env.NARADA_SOURCE_CHECKOUT)
  : resolve(root, config.checkout)
const checkOnly = process.argv.includes('--check')

function git(args, cwd = root) {
  const result = spawnSync('git', args, { cwd, encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] })
  if (result.status !== 0) throw new Error((result.stderr || result.stdout || `git ${args[0]} failed`).trim())
  return result.stdout.trim()
}

if (!existsSync(resolve(checkout, '.git'))) {
  if (checkOnly) throw new Error(`narada_source_checkout_missing: ${checkout}`)
  git(['clone', '--filter=blob:none', '--no-checkout', config.repository, checkout])
  git(['fetch', '--depth', '1', 'origin', config.revision], checkout)
  git(['checkout', '--detach', config.revision], checkout)
}

const head = git(['rev-parse', 'HEAD'], checkout)
if (head !== config.revision) throw new Error(`narada_source_revision_mismatch: expected ${config.revision}, received ${head}`)

for (const packagePath of config.packages) {
  if (!existsSync(resolve(checkout, packagePath, 'package.json'))) throw new Error(`narada_source_package_missing: ${packagePath}`)
  const changed = git(['status', '--porcelain', '--', packagePath], checkout)
  if (changed) throw new Error(`narada_source_package_dirty: ${packagePath}`)
}

console.log(JSON.stringify({ status: 'ready', revision: head, checkout, packages: config.packages }))
