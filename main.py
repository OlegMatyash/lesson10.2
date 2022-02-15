from flask import Flask

import utils

app = Flask(__name__)

@app.route("/")
def index_page():

    candidates = utils.candidates_all()
    page_content = utils.build_preformatted_list(candidates)
    return page_content

@app.route("/skill/<skill_name>")
def skill_page(skill_name):

    candidates = utils.candidates_by_skill(skill_name)
    page_content = utils.build_preformatted_list(candidates)
    return page_content

@app.route("/candidate/<int:uid>")
def candidate_page(uid):

    candidate = utils.candidate_by_id(uid)
    candidates = [candidate]
    page_content = utils.build_preformatted_list(candidates)
    return page_content

app.run()