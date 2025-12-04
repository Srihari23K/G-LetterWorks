# engine/db_models.py
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy (to be linked with Flask app)
db = SQLAlchemy()

# -----------------------------
# Template Model
# -----------------------------
class TemplateModel(db.Model):
    __tablename__ = "templates"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)

    fields = db.relationship("FieldModel", backref="template", lazy=True)

    def __repr__(self):
        return f"<Template {self.name}>"


# -----------------------------
# Field Model
# -----------------------------
class FieldModel(db.Model):
    __tablename__ = "fields"

    id = db.Column(db.Integer, primary_key=True)
    template_id = db.Column(db.Integer, db.ForeignKey("templates.id"), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    value = db.Column(db.String(200))

    def __repr__(self):
        return f"<Field {self.name} for template_id {self.template_id}>"
