from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("1: Navigating to iShopForIpsos")
        page.goto("https://uk.ishopforipsos.com/next/fieldportal/")

        input("AWAIT")
        browser.close()


if __name__ == "__main__":
    main()
