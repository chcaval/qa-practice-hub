import { test, expect } from '@playwright/test';

test('creates a user successfully', async ({ page }) => {
  const email = `user_${Date.now()}_${Math.random().toString(36).slice(2)}@example.com`;

  await page.goto('/');
  await page.getByTestId('input-name').fill('Test User');
  await page.getByTestId('input-email').fill(email);
  await page.getByTestId('btn-submit').click();

  await expect(page.getByTestId('message')).toContainText('User "Test User" created successfully!');
});

test('shows error when email is already registered', async ({ page }) => {
  const email = `user_${Date.now()}_${Math.random().toString(36).slice(2)}@example.com`;

  await page.goto('/');

  await page.getByTestId('input-name').fill('Test User');
  await page.getByTestId('input-email').fill(email);
  await page.getByTestId('btn-submit').click();
  await expect(page.getByTestId('message')).toContainText('created successfully');

  await page.getByTestId('input-name').fill('Test User');
  await page.getByTestId('input-email').fill(email);
  await page.getByTestId('btn-submit').click();
  await expect(page.getByTestId('message')).toContainText('Failed to create user.');
});
