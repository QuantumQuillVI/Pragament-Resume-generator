import argparse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def generate_pdf_resume(output_path, base_font_size, font_color, background_color):
    # Creating a canvas for the PDF with letter-sized pages
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter  # Storing the page width and height for positioning elements

    # Setting background color
    c.setFillColor(background_color)  # Set the background color
    c.rect(0, 0, width, height, fill=True)  # Fill the entire page with the background color

    # Defining font size scaling factors based on the base font size
    title_font_size = base_font_size * 2  # Font size for the title (larger)
    section_font_size = base_font_size * 1.5  # Font size for section headers
    text_font_size = base_font_size  # Font size for regular text
    line_spacing = base_font_size * 1.5  # Line spacing for readability

    # Drawing a horizontal line at a given y-coordinate
    def draw_horizontal_line(y):
        c.setStrokeColorRGB(0.5, 0.5, 0.5)  # Setting line color to light gray
        c.setLineWidth(0.5)  # Setting the line width to 0.5
        c.line(50, y, width - 50, y)  # Drawing a line from (50, y) to (width-50, y)

    # Adding the resume title and contact details at the top of the page
    c.setFont("Helvetica-Bold", title_font_size)
    c.setFillColor(font_color)  # Set the font color
    c.drawString(50, height - 50, "Quantum Quill")  # Name
    c.setFont("Helvetica", text_font_size)
    c.drawString(50, height - 70, "Email: QuantumQuill@email.com | Phone: +91-XXXXXXXXXX")  # Contact info
    c.drawString(50, height - 90, "LinkedIn: linkedin.com/in/QuantumQuill | GitHub: github.com/QuantumQuillVI")  # Social media

    # Adding the Education section
    c.setFont("Helvetica-Bold", section_font_size)
    c.drawString(50, height - 130, "Education")  # Section title
    draw_horizontal_line(height - 140)  # Drawing a line under the title
    c.setFont("Helvetica", text_font_size)

    # Adding education details (Column 1)
    c.drawString(60, height - 160, "B.Tech in CSE, IIT Gandhinagar")
    c.drawString(60, height - 160 - line_spacing, "CBSE Class XII")
    c.drawString(60, height - 160 - 2 * line_spacing, "CBSE Class X")

    # Adding education details (Column 2)
    c.drawString(300, height - 160, "CPI: X/10")
    c.drawString(300, height - 160 - line_spacing, "X/100 %")
    c.drawString(300, height - 160 - 2 * line_spacing, "X/100 %")
    draw_horizontal_line(height - 160 - 2.5 * line_spacing)  # Drawing a line after education section

    # Adding the Experience section
    c.setFont("Helvetica-Bold", section_font_size)
    c.drawString(50, height - 160 - 4 * line_spacing, "Experience")  # Section title
    draw_horizontal_line(height - 160 - 5 * line_spacing)  # Drawing a line after title
    c.setFont("Helvetica", text_font_size)
    c.drawString(60, height - 160 - 6 * line_spacing, "Software Development Intern")  # Position title
    c.drawString(60, height - 160 - 7 * line_spacing, "XYZ Tech Solutions, Bangalore, India | May 2024 – July 2024")  # Company and dates
    c.drawString(70, height - 160 - 8 * line_spacing, "- Developed a REST API for an e-commerce platform, reducing server response time by 15%.")  # Achievement 1
    c.drawString(70, height - 160 - 9 * line_spacing, "- Automated unit testing using PyTest, increasing code coverage to 95%.")  # Achievement 2
    draw_horizontal_line(height - 160 - 10 * line_spacing)  # Drawing a line after experience section

    # Adding the Skills section
    c.setFont("Helvetica-Bold", section_font_size)
    c.drawString(50, height - 160 - 11.5 * line_spacing, "Skills")  # Section title
    draw_horizontal_line(height - 160 - 12 * line_spacing)  # Drawing a line after title
    c.setFont("Helvetica", text_font_size)
    c.drawString(60, height - 160 - 13 * line_spacing, "- Programming Languages: Python, Java, C++, JavaScript")  # Skill 1
    c.drawString(60, height - 160 - 14 * line_spacing, "- Web Development: HTML, CSS, React, Node.js")  # Skill 2
    c.drawString(60, height - 160 - 15 * line_spacing, "- Tools: Git, Docker, Jupyter Notebook, VS Code")  # Skill 3
    c.drawString(60, height - 160 - 16 * line_spacing, "- Database Management: MySQL, MongoDB")  # Skill 4
    c.drawString(60, height - 160 - 17 * line_spacing, "- Soft Skills: Problem Solving, Team Collaboration, Leadership")  # Skill 5
    draw_horizontal_line(height - 160 - 18 * line_spacing)  # Drawing a line after skills section

    # Adding the Projects section
    c.setFont("Helvetica-Bold", section_font_size)
    c.drawString(50, height - 160 - 19.5 * line_spacing, "Projects")  # Section title
    draw_horizontal_line(height - 160 - 20 * line_spacing)  # Drawing a line after title
    c.setFont("Helvetica", text_font_size)
    c.drawString(60, height - 160 - 21 * line_spacing, "Personal Finance Tracker (React & Node.js)")  # Project 1 title
    c.drawString(70, height - 160 - 22 * line_spacing, "- Designed a web application to track monthly expenses and visualize data using charts.")  # Project 1 details
    c.drawString(70, height - 160 - 23 * line_spacing, "- Implemented user authentication and CRUD operations using MongoDB and Express.js.")  # Project 1 details
    c.drawString(70, height - 160 - 24 * line_spacing, "- Visualized training loss and accuracy using Matplotlib and TensorBoard.")  # Project 1 details
    c.drawString(60, height - 160 - 25 * line_spacing, "File Compression Tool (C++)")  # Project 2 title
    c.drawString(70, height - 160 - 26 * line_spacing, "- Developed a Huffman Encoding-based file compression program to reduce file sizes by 40%.")  # Project 2 details
    draw_horizontal_line(height - 160 - 27 * line_spacing)  # Drawing a line after projects section

    # Saving the PDF to the output file
    c.save()

# Parsing command-line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Resume PDF with customizable font size, font color, and background color.")
    parser.add_argument("--font-size", type=int, default=10, help="Adjust font size (default: 10)")
    parser.add_argument("--font-color", type=str, default="#000000", help="Adjust font color (e.g., hex code or color name, default: black)")
    parser.add_argument("--background-color", type=str, default="#FFFFFF", help="Adjust background color (e.g., hex code or color name, default: white)")
    parser.add_argument("--output-file", type=str, default="resume.pdf", help="Output file name (default: 'resume.pdf')")
    args = parser.parse_args()

    # Convert color name to hex if needed using HexColor
    font_color = colors.HexColor(args.font_color)  # Correcting color handling for font color
    background_color = colors.HexColor(args.background_color)  # Correcting color handling for background color

    # Call function to generate the resume PDF with user-specified settings
    generate_pdf_resume(args.output_file, args.font_size, font_color, background_color)
