from datetime import datetime, timezone
from datetime import timedelta

from flask import Blueprint, url_for, request, render_template
from werkzeug.utils import redirect

from app import db
from models import Code

import json
import uid

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/<uid>')
def code(uid):
    code_query = Code.query.get_or_404(uid)
    return render_template('code.html', code=code_query)

@bp.route('/', methods=['POST'])
def register():
    if not request.is_json:
        return json.dumps({"result": "", "error": "Not valid data-type"})
    
    params = request.get_json()

    try:
        code = params['code']
        name = params['name']
        title = params['title']
    except:
        return json.dumps({"result": "", "error": "No required data"})

    # Generate unique id
    while True:
        code_uid = uid.generate()
        code_query = Code.query.filter_by(uid=code_uid)
        if code_query.count() == 0:
            break

    expire_date = datetime.now(timezone.utc) + timedelta(days=7)
    code = Code(uid=code_uid, title=title, name=name, ip=request.remote_addr, code=code, expire_date=expire_date)
    db.session.add(code)
    db.session.commit()

    return redirect(url_for('main.code', uid=code.uid))

@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')
