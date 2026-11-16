import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const engines = process.argv.slice(2).length ? [...new Set(process.argv.slice(2))] : ['chromium', 'firefox', 'webkit'];
assert(engines.every(name => ['chromium', 'firefox', 'webkit'].includes(name)), 'Arguments must be chromium, firefox or webkit');
const cases = [
  ['test-isotope-browser-network.mjs'],
  ['test-isotope-wiring-standalone.mjs'],
  ['test-isotope-wiring-accessibility.mjs'],
  ['test-isotope-wiring-ux.mjs'],
  ['test-isotope-wiring-placement.mjs', '--standalone'],
  ['test-isotope-wiring-witness-placement.mjs'],
  ['test-isotope-wiring-survey.mjs'],
  ['test-isotope-wiring-website.mjs'],
  ['test-isotope-wiring-placement.mjs'],
  ['test-isotope-wiring-witness-placement.mjs', '--hosted'],
  ['test-isotope-wiring-survey.mjs', '--hosted'],
];
// Sequential execution avoids competing VitePress dependency optimizers. Missing
// engines and test failures fail the run; they are never silently skipped.
for (const engine of engines) for (const [script, ...args] of cases) {
  console.log(`\n=== ${engine}: ${script} ${args.join(' ')} ===`);
  const result = spawnSync(process.execPath, [fileURLToPath(new URL(script, import.meta.url)), ...args], {
    cwd: fileURLToPath(new URL('../', import.meta.url)), env: { ...process.env, ISOTOPE_BROWSER: engine },
    stdio: 'inherit', timeout: 180000, shell: false,
  });
  if (result.error || result.status !== 0) {
    console.error(`FAIL: ${engine} ${script}`, result.error?.message || `exit ${result.status}, signal ${result.signal}`);
    process.exit(result.status || 1);
  }
}
console.log(`\nPASS: ${engines.length * cases.length} browser runs (${engines.join(', ')}), including network-isolation checks.`);
