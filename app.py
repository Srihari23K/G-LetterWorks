from flask import Flask, render_template, request, redirect, url_for, make_response
from engine.db_models import db, TemplateModel
from engine.template_engine import TemplateEngine
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
import os

app = Flask(__name__)
db_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance')
os.makedirs(db_dir, exist_ok=True)
db_path = os.path.join(db_dir, 'app.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

engine = TemplateEngine()

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    templates = engine.list_templates()
    return render_template("index.html", templates=templates)


@app.route("/editor/<template_key>", methods=["GET", "POST"])
def editor(template_key):
    template = engine.get_template(template_key)
    if not template:
        return "Template not found", 404

    placeholders = engine.get_placeholders(template_key)

    if request.method == "POST":
       
        data = {field: request.form.get(field, "") for field in placeholders}
        letter = engine.generate_letter(template_key, data)
        return render_template("result.html", letter=letter)

    return render_template("editor.html", template=template, placeholders=placeholders)


@app.route("/add_template", methods=["GET", "POST"])
def add_template():
    if request.method == "POST":
        name = request.form.get("name")
        title = request.form.get("title")
        content = request.form.get("content")
        if name and title and content:
            new_template = TemplateModel(name=name, title=title, content=content)
            db.session.add(new_template)
            db.session.commit()
            return redirect(url_for("index"))
    return render_template("add_template.html")


@app.route("/download_pdf", methods=["POST"])
def download_pdf():
    letter_text = request.form.get("letter_text", "")

    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=A4,
                            rightMargin=40, leftMargin=40,
                            topMargin=60, bottomMargin=40)

    styles = getSampleStyleSheet()
    story = []

   
    paragraphs = letter_text.split("\n\n")
    for para in paragraphs:
  
        para = para.replace("\n", "<br/>")
        story.append(Paragraph(para, styles['Normal']))
        story.append(Spacer(1, 12))  

    pdf.build(story)

    buffer.seek(0)
    response = make_response(buffer.read())
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "attachment; filename=letter.pdf"
    return response



if __name__ == "__main__":
    app.run(debug=True)
