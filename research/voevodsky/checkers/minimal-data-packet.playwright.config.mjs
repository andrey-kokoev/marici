import { defineConfig } from '@playwright/test';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
export default defineConfig({
  testDir: path.join(root, 'tests'),
  testMatch: 'minimal-data-packet.spec.mjs',
  outputDir: path.join(root, '.ai/tmp/minimal-data-packet-browser'),
  use: { baseURL: 'http://127.0.0.1:4382', viewport: { width: 1440, height: 1000 } },
  webServer: {
    command: 'python -m http.server 4382 --bind 127.0.0.1 --directory website/.vitepress/dist',
    cwd: root,
    url: 'http://127.0.0.1:4382/experiments/minimal-data-packet/',
    reuseExistingServer: false,
    stdout: 'ignore', stderr: 'ignore',
  },
});
