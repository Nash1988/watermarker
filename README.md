# watermarker


This script is designed to add a watermark to PDF documents, offering a solution for tracking sensitive documents in case of leaks or unauthorized sharing.
Adding a watermark provides a visible indication of ownership or confidentiality, making it easier to identify the source if the document is shared without permission.

## Features 
- **Watermark Addition** : Easily add a customizable watermark to PDF documents. 
- **Tracking Sensitivity** : Track leaked or shared documents by marking them with identifiable watermarks. 
- **Customization** : Modify watermark text, position, transparency, and other settings to suit your needs.
## Requirements
- Python 3.x 
- `PyPDF2` library
## Installation 
1. Clone the repository:

```bash
git clone https://github.com/Nash1988/watermarker.git
``` 
2. Install necessary dependencies:

```bash
pip install PyPDF2
```
## Usage 
1. Navigate to the project directory:

```bash
cd watermarker
``` 
2. Run the script with the following command:

```bash
python watermarker.py input_file.pdf output_file.pdf "Your Watermark Text"
```



Replace `input_file.pdf` with the path to your original PDF document.
Replace `output_file.pdf` with the desired name for the watermarked PDF output.
Replace `"Your Watermark Text"` with the text you want to use as the watermark. 
3. Adjust optional parameters such as watermark position, font, size, and transparency directly in the `watermarker.py` script.
## Example

```bash
python watermarker.py sensitive_document.pdf watermarked_sensitive_document.pdf "Confidential - For Internal Use Only"
```


## Notes
- Use this script responsibly and in accordance with applicable laws and regulations.
- Watermarking documents may alter their appearance and content. Always test on non-sensitive documents first.
- Ensure proper permissions before watermarking any documents.
## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.
## License

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/c/LICENSE)  file for details.---
