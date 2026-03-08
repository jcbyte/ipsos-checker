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
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("1: Navigating to iShopForIpsos")
        page.goto("https://uk.ishopforipsos.com/next/fieldportal/")

        email = require_env("IPSOS_EMAIL")
        password = require_env("IPSOS_PASSW")
        page.fill("#email", email)
        page.fill("#password", password)

        input("AWAIT")
        browser.close()


if __name__ == "__main__":
    load_dotenv()
    main()
