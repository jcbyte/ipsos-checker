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
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to iShopForIpsos
        page.goto("https://uk.ishopforipsos.com/next/fieldportal/")

        page.wait_for_load_state(state="domcontentloaded")

        # Enter credentials and login
        email = require_env("IPSOS_EMAIL")
        page.fill("#email", email)
        password = require_env("IPSOS_PASSW")
        page.fill("#password", password)
        page.click("#btn-login")

        # Click side panel navigator to switch to Task List
        page.click('text="Task Board (List)"')

        # Wait for the results to load
        # ? Waiting until there are no network connections is discouraged
        page.wait_for_load_state(state="networkidle")

        # Get the iframe, the results are stored in
        frame = page.frame_locator("#appContentFrame")

        # Search for given postcode within the results
        postcode = require_env("POSTCODE")
        postcode_count = frame.get_by_text(postcode).count()
        # Print whether the postcode was found or not
        if postcode_count > 0:
            print(f"✨ {postcode} is available!")
        else:
            print(f"❌ No matches for {postcode}")

        # Cleanup
        browser.close()


if __name__ == "__main__":
    load_dotenv()
    main()
