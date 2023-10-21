from survey import AnonymousSurvey as Asurvey

question = 'What language did you first learn to speak?'

lang_survey = Asurvey(question)

lang_survey.show_question()
print("Enter 'q' at any time to quit.\n")

while True:
    resp = input('Language: ').lower()
    if resp == 'q':
        break
    lang_survey.store_response(resp.strip().title())

print("\nThank you to everyone who participate in the survey!")
lang_survey.show_results()
