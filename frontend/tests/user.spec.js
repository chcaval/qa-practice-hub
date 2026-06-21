import {test, expect } from '@playwright/test'

test('create user flow', async ({page}) => {
    // 1. Open frontend
    await page.goto('http://localhost:3000/login')
    // 2. Fill the form
    await page.fill('[data-testid="input-name"]', 'Carlos');
    await page.fill('[data-testid="input-email"]', "carlos@test.com")
    // 3. Submit
    await page.click('[data-testid="btn-submit"]')
    // 4. Verify success message
    await expect(page.locator('[data-testid="message"]')).toContainText('created successfully!')

})