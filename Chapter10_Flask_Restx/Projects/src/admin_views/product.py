from flask_admin.form import ImageUploadField
from flask_admin.model import InlineFormAdmin
from flask import url_for
from markupsafe import Markup

from src.admin_views.base import SecureModelView
from src.models import Product
from src.config import Config
from src.admin_views.utils import generate_name


class ProductView(SecureModelView):
    can_delete = True
    can_create = True
    can_edit = True

    edit_modal = True
    create_modal = True


    column_editable_list = ['price', 'name']

    column_filters = ['price', 'category']

    column_searchable_list = ['name']

    column_list = ['img', 'price']

    can_view_details = True
    details_modal = True

    can_export = True

    form_overrides = {
        'img': ImageUploadField,
    }

    form_args = {
        'img': {
            'base_path': Config.UPLOAD_PATH,
            'relative_path': 'uploads/',
            'namegen': generate_name,
        }
    }

    column_formatters = {
        'img': lambda v, c, m, n: Markup(f'<img src={url_for("static", filename=m.img)} width="100">'),
    }

class ProductInline(InlineFormAdmin):
    can_delete = True
    can_create = True

    form_overrides = {
        'img': ImageUploadField,
    }

    form_args = {
        'img': {
            'base_path': Config.UPLOAD_PATH,
            'relative_path': 'uploads/',
            'namegen': generate_name,
        }
    }

    column_formatters = {
        'img': lambda v, c, m, n: Markup(f'<img src={url_for("static", filename=m.img)} width="100">'),
    }

class CategoryView(SecureModelView):
    inline_models = (ProductInline(Product),)

    can_delete = True
    can_create = True
    can_edit = True

    edit_modal = True
    create_modal = True