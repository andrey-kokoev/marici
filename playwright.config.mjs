import { defineConfig } from '@playwright/test'

export default defineConfig({
  testDir: './tests',
  outputDir: '.ai/tmp/playwright-results',
  use: { baseURL: 'http://127.0.0.1:4321', viewport: { width: 1440, height: 1000 } },
  webServer: {
    command: 'pnpm preview --host 127.0.0.1',
    url: 'http://127.0.0.1:4321/graph/',
    reuseExistingServer: false,
  },
})
