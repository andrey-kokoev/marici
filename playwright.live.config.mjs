import { defineConfig } from '@playwright/test'

export default defineConfig({
  testDir: './tests',
  outputDir: '.ai/tmp/playwright-live-results',
  use: {
    baseURL: 'https://marici.andrei-kokoev.workers.dev',
    viewport: { width: 1440, height: 1000 },
  },
})
