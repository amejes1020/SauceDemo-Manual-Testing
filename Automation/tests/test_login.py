import pytest
from playwright.sync_api import expect, sync_playwright


def test_valid_login(page):
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()
    #validate
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        #expect(page).to_have_title("Products")
    #browser close


def test_invalid_login(page):
        page.locator("#user-name").fill("invalid_user")
        page.locator("#password").fill("invalid_password")
        page.locator("#login-button").click()
    #error message
        error_messaqe=page.locator('[data-test="error"]')
    #validate
        expect(error_messaqe).to_be_visible()
        expect(error_messaqe).to_have_text("Epic sadface: Username and password do not match any user in this service")

def test_blank_login(page):
        page.locator("#login-button").click()
    #error message
        error_messaqe=page.locator('[data-test="error"]')
    #validate
        expect(error_messaqe).to_be_visible()
        expect(error_messaqe).to_have_text("Epic sadface: Username is required")

def test_blank_username(page):
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()
    #error message
        error_messaqe=page.locator('[data-test="error"]')
    #validate
        expect(error_messaqe).to_be_visible()
        expect(error_messaqe).to_have_text("Epic sadface: Username is required")

def test_blank_password(page):
        page.locator("#user-name").fill("standard_user")
        page.locator("#login-button").click()
    #error message
        error_messaqe=page.locator('[data-test="error"]')
    #validate
        expect(error_messaqe).to_be_visible()
        expect(error_messaqe).to_have_text("Epic sadface: Password is required")


