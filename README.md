# Resume PDF Generator

The Python script (gen.py) generates a customizable resume in PDF format. It allows you to modify the font size, font color, and background color, and saves the output as a PDF file. You can also specify the output filename.

## Features
- **Adjustable font size**
- **Customizable font color**
- **Customizable background color**
- **Saves output as a PDF file**
- **Command-line arguments for customization**

---

### 1. Dependencies : 
To run the script, you'll need Python and the required libraries.
```bash
python --version
```

The script uses the reportlab library to generate PDFs. You can install the required dependencies using pip: 
```bash
pip install reportlab
```

## Usage
### 1. Basic Command
To run the script and generate the resume PDF with the default settings (font size 10, black font, white background):
```bash
python gen.py
```
This will generate a PDF file named resume.pdf in the current folder with the default font size and colors.
- (Sample PDF generated using the command is attached (resume.py))

### 2. Customizing the Output
You can customize the resume's appearance by using the following command-line arguments:

- **output-file**: Specifies the output file name (default: resume.pdf)
- **font-size**: Adjusts the font size (default: 10)
- **font-color**: Sets the font color in hexadecimal (default: black)
- **background-color**: Sets the background color in hexadecimal (default: white)



**Example :**
```bash
python gen.py --output-file "my_resume.pdf" --font-size 12 --font-color "#0000FF" --background-color "#FFFFE0"
```
This will create a PDF named my_resume.pdf with:

- **Font size**: 12
- **Font color**: Blue (#0000FF)
- **Background color**: Light Yellow (#FFFFE0)
- (Sample PDF generated using the command is attached (my_resume.py))

