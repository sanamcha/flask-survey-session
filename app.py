from flask import Flask, session, request, render_template, redirect, make_response, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys

KEY_CURR_SURVEY = 'current_survey'
KEY_RESPONSES = 'responses'

app = Flask(__name__)
app.config['SECRET_KEY'] = "abcdef12345"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route("/")
def show_pick_survey_form():
    return render_template("survey_picking.html", surveys=surveys)


@app.route("/", methods=["POST"])
def pick_survey():
    survey_id = request.form['survey_pick']

    if request.cookies.get(f"completed_{survey_id}"):
        return render_template("completed_survey.html")

    survey = surveys[survey_id]
    session[KEY_CURR_SURVEY] = survey_id

    return render_template("survey_start.html", survey=survey)


@app.route("/begin", methods=["POST"])
def start_survey():
    """Clear the session of responses."""

    session[KEY_RESPONSES] = []

    return redirect("/questions/0")


@app.route("/answer", methods=["POST"])
def handle_question():
    """Save response and redirect to next question."""

    answer = request.form['answer']
    text = request.form.get("text", "")
    responses = session[KEY_RESPONSES]
    responses.append({"answer": answer, "text": text})

    session[KEY_RESPONSES] = responses
    survey_pick = session[KEY_CURR_SURVEY]
    survey = surveys[survey_pick]

    if (len(responses) == len(survey.questions)):
    
        return redirect("/complete")

    else:
        return redirect(f"/questions/{len(responses)}")


@app.route("/questions/<int:id>")
def show_question(id):
    """Display current question."""

    responses = session.get(KEY_RESPONSES)
    survey_pick = session[KEY_CURR_SURVEY]
    survey = surveys[survey_pick]

    if (responses is None):
     
        return redirect("/")

    if (len(responses) == len(survey.questions)):
    
        return redirect("/complete")

    if (len(responses) != id):
       
        flash(f"Invalid question id: {id}.")
        return redirect(f"/questions/{len(responses)}")

    question = survey.questions[id]

    return render_template(
        "survey_question.html", question_num=id, question=question)


@app.route("/complete")
def say_thanks():
    """Thank user and list responses."""

    survey_id = session[KEY_CURR_SURVEY]
    survey = surveys[survey_id]
    responses = session[KEY_RESPONSES]

    html = render_template("completion_thanks_page.html", survey=survey, responses=responses)


    response = make_response(html)
    response.set_cookie(f"completed_{survey_id}", "yes")
    return response
