import os
from playwright.sync_api import sync_playwright

def make_item_image(url):
    img_name=url.split("/")[-1].strip()
    front_path = f"build/collection.media/{img_name}_front.png"
    back_path = f"build/collection.media/{img_name}_back.png"

    if os.path.exists(front_path) and os.path.exists(back_path):
        return

    with sync_playwright() as p:
        # Open browser and wiki page
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded")

        # Ensure positions are from the top of the page
        page.evaluate("window.scrollTo(0, 0)")

        # Find the item info box
        table = page.locator("table.item-infobox").first
        rows = table.locator("tr")

        # Where to split the table for the front and back image
        # First 2 are item name and image, which we want to keep
        split_at = 2

        # Search for header to sounds section, so that sounds section is not included
        has_sound_header = rows.evaluate_all(
            "trs => trs.map(tr => tr.querySelector('td.sounds-header') !== null)"
        )

        # Cutoff for unwanted sections, like sounds
        cutoff = next((i for i in range(split_at, rows.count()) if has_sound_header[i]), None)

        # Get the info box's bounding box
        t = table.bounding_box()
        # Bounding box of the last element of the front section
        last_of_first = rows.nth(split_at - 1).bounding_box()

        # Screenshot the front section using bounding boxes
        page.screenshot(
            path=front_path,
            full_page=True,
            clip={"x": t["x"], "y": t["y"], "width": t["width"],
                "height": last_of_first["y"] + last_of_first["height"] - t["y"]},
        )

        # Bounding box of first element in the back section
        first_of_rest = rows.nth(split_at).bounding_box()
        if cutoff is None:  # No sounds section
            bottom = t["y"] + t["height"]
        else:               # Sounds section found, needs to be cut off
            last_kept = rows.nth(cutoff - 1).bounding_box()
            bottom = last_kept["y"] + last_kept["height"]
        page.screenshot(
            path=back_path,
            full_page=True,
            clip={"x": t["x"], "y": first_of_rest["y"], "width": t["width"],
                "height": bottom - first_of_rest["y"]},
        )

        browser.close()
