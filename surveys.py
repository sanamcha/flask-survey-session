class Question:
    """Question on a questionnaire."""

    def __init__(self, question, choices=None, allow_text=False):
        """Create question (assume Yes/No for choices."""

        if not choices:
            choices = ["Yes", "No"]

        self.question = question
        self.choices = choices
        self.allow_text = allow_text


class Survey:
    """Questionnaire."""

    def __init__(self, title, instructions, questions):
        """Create questionnaire."""

        self.title = title
        self.instructions = instructions
        self.questions = questions



hobby_survey = Survey(
    "Hobbies Question",
    "Lets find some of your hobbies..",
    [
        Question("Do you like to read story books, what kind of stories do you like most? ", allow_text=True),
        Question("Do you play sports, which sports do you like to play?", allow_text=True),
        Question("Do you like to watch movies?"),
        Question("Which one is your favorite places as listed below and why?",["San Fransisco", "Las Vagas", "Yosomete Park", "Lake Tahoe"], allow_text=True),
    ]
)
satisfaction_survey = Survey(
    "Customer Satisfaction Survey",
    "Please fill out a survey about your experience with us.",
    [
        Question("Have you shopped here before?"),
        Question("Did someone else shop with you today?"),
        Question("On average, how much do you spend a month on frisbees?",
                 ["Less than $10,000", "$10,000 or more"]),
        Question("Are you likely to shop here again?"),
    ])



personality_quiz = Survey(
    "Rithm Personality Test",
    "Learn more about yourself with our personality quiz!",
    [
        Question("Do you ever dream about code?"),
        Question("Do you ever have nightmares about code?"),
        Question("Do you prefer porcupines or hedgehogs?",
                 ["Porcupines", "Hedgehogs"]),
        Question("Which is the worst function name, and why?",
                 ["do_stuff()", "run_me()", "wtf()"],
                 allow_text=True),
    ]
)

surveys = {
    "hobbies": hobby_survey,
    "satisfaction": satisfaction_survey,
    "personality": personality_quiz,
    
}