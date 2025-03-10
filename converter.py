import os
import imgkit

javascript_code = """
try {
    let originalBody = document.body;
    let replacementElement = document.evaluate('/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div/table', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;

    if (replacementElement) {
        let newBody = document.createElement('body');
        newBody.appendChild(replacementElement.cloneNode(true)); // Clone to avoid removing from original DOM
        document.documentElement.replaceChild(newBody, originalBody);
        document.body.style.backgroundColor = 'transparent';
    } else {
        console.error('XPath element not found.');
    }

} catch (error) {
    console.error('JavaScript error:', error);
}
"""

def make_item_image(url):
    if not os.path.exists("images"):
        os.makedirs("images")
    front_options = {
        '--run-script': javascript_code,
        "--crop-w": "312",
        "--crop-h": "195",
    }
    back_options = {
        '--run-script': javascript_code,
        "--crop-w": "312",
        "--crop-y": "195"
    }
    img_name=url.split("/")[-1].strip()
    front_path = f"images/{img_name}_front.png"
    back_path = f"images/{img_name}_back.png"
    if not os.path.exists(front_path):
        imgkit.from_url(url, front_path, options=front_options)
    if not os.path.exists(back_path):
        imgkit.from_url(url, back_path, options=back_options)
