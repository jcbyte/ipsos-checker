import os

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright


def require_env(name: str) -> str:
    value = os.getenv(name)
    if value is None:
        raise KeyError(f"{name} environment variable is not set")

    return value


def main():
    with sync_playwright() as p:
        # Launch browser instance
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to iShopForIpsos
        page.goto("https://uk.ishopforipsos.com/next/fieldportal/")

        email_field = page.locator("#email")
        password_field = page.locator("#password")
        login_btn = page.locator("#btn-login")

        # Wait for login elements to load before continuing
        email_field.wait_for()
        password_field.wait_for()
        login_btn.wait_for()

        # Enter credentials and login
        email = require_env("IPSOS_EMAIL")
        email_field.fill(email)
        password = require_env("IPSOS_PASSW")
        password_field.fill(password)
        login_btn.click()

        input("AWAIT")
        browser.close()


if __name__ == "__main__":
    load_dotenv()
    main()
