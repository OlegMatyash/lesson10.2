import json

def loading_candidates():

    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)

    return candidates


def candidates_all():
    return loading_candidates()


def candidates_by_skill(skill):
    candidates = loading_candidates()
    skilled_candidates = []
    skill_lower = skill.lower()

    for candidate in candidates:
        candidate_skills = candidate["skills"].lower().split(", ")
        if skill_lower in candidate_skills:
            skilled_candidates.append(candidate)

    return skilled_candidates


def candidate_by_id(uid):
    candidates = loading_candidates()
    for candidate in candidates:
        if candidate["id"] == uid:
            return candidate

def build_preformatted_list(candidates):

    page_content = ""

    for candidate in candidates:
        page_content += candidate["name"] + "\n"
        page_content += candidate["position"] + "\n"
        page_content += candidate["skills"] + "\n"
        page_content += "\n"

    return "<pre>" + page_content + "</pre>"


