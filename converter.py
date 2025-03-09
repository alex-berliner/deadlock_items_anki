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

# javascript_code = """
# document.body.remove();
# """
options = {
    '--run-script': javascript_code,
    "--crop-w": "312"
}

# imgkit.from_url(url, output_path, options=options)
imgkit.from_url('https://deadlock.wiki/Spirit_Lifesteal_(item)', 'out.jpg', options=options)
# imgkit.from_string('Hello!', 'out.jpg')