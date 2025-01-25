# Resume-generator

Resume PDF Generator
This script generates a customizable resume in PDF format, with options to modify the font size, font color, and background color.

Features
Adjust font size
Change font color
Modify background color
Save as a PDF file
Installation
To run the script, you'll need to have Python installed on your system along with the required libraries. Follow the instructions below to set up the environment.

1. Clone the repository (if applicable)
bash
Copy
Edit
git clone https://github.com/yourusername/resume-pdf-generator.git
cd resume-pdf-generator
2. Install dependencies
The script uses the reportlab library to generate PDFs. You can install the required dependencies using pip:

bash
Copy
Edit
pip install -r requirements.txt
If you don’t have requirements.txt, simply install reportlab directly:

bash
Copy
Edit
pip install reportlab
3. Ensure Python is installed
You can check if Python is installed with:

bash
Copy
Edit
python --version
Or if you're using python3:

bash
Copy
Edit
python3 --version
Usage
1. Basic Command
To run the script and generate the resume PDF with the default settings (font size 10, black font, white background):

bash
Copy
Edit
python generate_resume.py
2. Customizing the Output
You can customize the resume's appearance by using the following command-line options:

--output-file: Specifies the output file name (default: resume.pdf)
--font-size: Adjusts the font size (default: 10)
--font-color: Sets the font color in hexadecimal (default: black)
--background-color: Sets the background color in hexadecimal (default: white)
Example:
bash
Copy
Edit
python generate_resume.py --output-file "my_resume.pdf" --font-size 12 --font-color "#0000FF" --background-color "#FFFFE0"
This command will generate a PDF file named my_resume.pdf with:

Font size: 12
Font color: Blue (#0000FF)
Background color: Light yellow (#FFFFE0)
Script Explanation
generate_resume.py:

This script generates a resume in PDF format with customizable font size, font color, and background color.
The output file can be specified with the --output-file argument.
The font size and color can be adjusted through --font-size and --font-color arguments.
The background color can be set using the --background-color argument.
Dependencies:

reportlab: A library used to create PDF documents.
