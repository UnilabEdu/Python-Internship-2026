from flask import url_for
from markupsafe import Markup
from flask_admin.form import ImageUploadField
from src.config import Config
from wtforms.fields import SelectField
from src.admin_views.base import SecureModelView
from src.admin_views.utils import generate_name


class PatientView(SecureModelView):
    can_delete=True
    can_create=True
    can_edit=True

    edit_modal=True
    create_modal=True

    form_overrides = {
        "gender": SelectField,
        'img': ImageUploadField,
        'namegen': generate_name
    }

    form_args = {
        'img': {
            'base_path': Config.UPLOAD_PATH,
            'relative_path': 'static/uploads'
        },
        'gender': { 
            'choices': [('male', 'Male'), ('female', 'Female')]
        }
    }

#     column_formatters = {
#     'img': lambda v, c, m, n:Markup( f'<img src="{url_for("static", filename=m.img)}">')
#    }
    column_formatters = {
        'img': lambda v, c, m, n: Markup(f'<img src="{url_for("static", filename="uploads/" + m.img)}" width="70">') 
    }
    column_editable_list = ['name','age','city']
    column_filters = ['name','age','city','gender']
    column_searchable_list = ['name','age','city','gender']
    column_list = ['img','name','age','city','gender']

    can_view_details=True
    details_modal=True

    can_export = True
  
  
    
