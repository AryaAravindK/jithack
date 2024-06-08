from django.shortcuts import render, redirect

# Dictionary to store survey responses
survey_responses = []

def survey(request):
    if request.method == 'POST':
        # Extract data from POST request
        question_1 = request.POST.get('question-1')
        question_2 = request.POST.get('question-2', '')
        question_3 = request.POST.get('question-3', '')

        # Save data to the in-memory dictionary
        response = {
            'question_1': question_1,
            'question_2': question_2 if question_1 == 'yes' else None,
            'question_3': question_3 if question_1 == 'yes' else None,
        }
        survey_responses.append(response)

        # Redirect to a success page or another view
        return redirect('survey_success')  # You need to define this view and URL

    else:
        return render(request, 'survey.html')

def survey_success(request):
    return render(request, 'survey_success.html')
