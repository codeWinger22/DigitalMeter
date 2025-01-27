# from flask import Flask, render_template, request, redirect, url_for, session

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# # Questions and scenarios
# scenarios = [
#     {
#         'scenario': 'You see a social media post that is clearly spreading misinformation about a public health crisis. What do you do?',
#         'options': ['Share it without thinking', 'Report it to the platform', 'Ignore it', 'Comment to correct the information'],
#         'correct': 1
#     },
#     {
#         'scenario': 'Your friend asks for your account password to access a shared streaming service. What do you do?',
#         'options': ['Give the password', 'Refuse and explain why', 'Change your password after sharing', 'Ignore the request'],
#         'correct': 1
#     },
#     {
#         'scenario': 'A stranger sends you a direct message asking for your personal information in exchange for a prize. How do you respond?',
#         'options': ['Give them your info', 'Report the account', 'Block the user', 'Ask for more information'],
#         'correct': 1
#     },
#     {
#         'scenario': 'You come across a website that offers free downloads of expensive software. What do you do?',
#         'options': ['Download the software', 'Check if the site is legitimate', 'Share the link with others', 'Close the website immediately'],
#         'correct': 3
#     },
#     {
#         'scenario': 'Your teacher sends you an email asking for an assignment submission. The email address looks unusual. What do you do?',
#         'options': ['Reply and attach the assignment', 'Ignore the email', 'Verify the email with your teacher in person', 'Open the attachment'],
#         'correct': 2
#     },
#     {
#         'scenario': 'You receive a pop-up message claiming your computer is infected with a virus. What’s your next step?',
#         'options': ['Click on the pop-up to fix the issue', 'Run your own antivirus software', 'Ignore the warning', 'Search the issue online'],
#         'correct': 1
#     },
#     {
#         'scenario': 'You overhear someone spreading rumors about your friend online. How do you handle the situation?',
#         'options': ['Join the conversation and spread it further', 'Confront them online', 'Privately warn your friend', 'Ignore the situation'],
#         'correct': 2
#     },
#     {
#         'scenario': 'You are signing up for a new app that requires several permissions, including access to your camera, microphone, and contacts. How do you respond?',
#         'options': ['Grant all permissions', 'Deny all permissions', 'Only allow necessary permissions', 'Look for an alternative app'],
#         'correct': 2
#     },
#     {
#         'scenario': 'You notice that a new app you installed is draining your phone’s battery quickly. What’s your action?',
#         'options': ['Uninstall the app', 'Ignore the issue', 'Disable the app’s permissions', 'Restart your phone'],
#         'correct': 0
#     },
#     {
#         'scenario': 'You’re using a public Wi-Fi network to log into your bank account. What should you do?',
#         'options': ['Proceed as normal', 'Use a VPN or secure connection', 'Log in later on a secure network', 'Avoid using public Wi-Fi altogether'],
#         'correct': 1
#     }
# ]


# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/start_quiz')
# def start_quiz():
#     session['current_question'] = 0
#     session['trust_score'] = 0  # Set initial meter value to 0
#     return redirect(url_for('quiz'))

# @app.route('/quiz', methods=['GET', 'POST'])
# def quiz():
#     current_question = session.get('current_question', 0)
#     trust_score = session.get('trust_score', 0)
    
#     if request.method == 'POST':
#         selected_option = request.form.get('option')
#         correct_option = scenarios[current_question]["correct"]
        
#         # Update the trust score based on the answer
#         if selected_option == correct_option:
#             session['trust_score'] += 10
#         else:
#             session['trust_score'] -= 10
        
#         # Move to the next question
#         session['current_question'] += 1
#         current_question = session['current_question']
    
#     # Check if the quiz is completed
#     if current_question >= len(scenarios):
#         return redirect(url_for('summary'))

#     return render_template('quiz.html', scenario=scenarios[current_question], question_num=current_question + 1, trust_score=session['trust_score'])

# @app.route('/summary')
# def summary():
#     trust_score = session.get('trust_score', 0)
#     return render_template('summary.html', trust_score=trust_score)

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Questions and scenarios
scenarios = [
    {
        'scenario': 'You see a social media post that is clearly spreading misinformation about a public health crisis. What do you do?',
        'options': ['Share it without thinking', 'Report it to the platform', 'Ignore it', 'Comment to correct the information'],
        'correct': 1
    },
    {
        'scenario': 'Your friend asks for your account password to access a shared streaming service. What do you do?',
        'options': ['Give the password', 'Refuse and explain why', 'Change your password after sharing', 'Ignore the request'],
        'correct': 1
    },
    {
        'scenario': 'A stranger sends you a direct message asking for your personal information in exchange for a prize. How do you respond?',
        'options': ['Give them your info', 'Report the account', 'Block the user', 'Ask for more information'],
        'correct': 1
    },
    {
        'scenario': 'You come across a website that offers free downloads of expensive software. What do you do?',
        'options': ['Download the software', 'Check if the site is legitimate', 'Share the link with others', 'Close the website immediately'],
        'correct': 3
    },
    {
        'scenario': 'Your teacher sends you an email asking for an assignment submission. The email address looks unusual. What do you do?',
        'options': ['Reply and attach the assignment', 'Ignore the email', 'Verify the email with your teacher in person', 'Open the attachment'],
        'correct': 2
    },
    {
        'scenario': 'You receive a pop-up message claiming your computer is infected with a virus. What’s your next step?',
        'options': ['Click on the pop-up to fix the issue', 'Run your own antivirus software', 'Ignore the warning', 'Search the issue online'],
        'correct': 1
    },
    {
        'scenario': 'You overhear someone spreading rumors about your friend online. How do you handle the situation?',
        'options': ['Join the conversation and spread it further', 'Confront them online', 'Privately warn your friend', 'Ignore the situation'],
        'correct': 2
    },
    {
        'scenario': 'You are signing up for a new app that requires several permissions, including access to your camera, microphone, and contacts. How do you respond?',
        'options': ['Grant all permissions', 'Deny all permissions', 'Only allow necessary permissions', 'Look for an alternative app'],
        'correct': 2
    },
    {
        'scenario': 'You notice that a new app you installed is draining your phone’s battery quickly. What’s your action?',
        'options': ['Uninstall the app', 'Ignore the issue', 'Disable the app’s permissions', 'Restart your phone'],
        'correct': 0
    },
    {
        'scenario': 'You’re using a public Wi-Fi network to log into your bank account. What should you do?',
        'options': ['Proceed as normal', 'Use a VPN or secure connection', 'Log in later on a secure network', 'Avoid using public Wi-Fi altogether'],
        'correct': 1
    }
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_quiz')
def start_quiz():
    session['current_question'] = 0
    session['trust_score'] = 0  # Set initial meter value to 0
    return redirect(url_for('quiz'))

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    current_question = session.get('current_question', 0)
    trust_score = session.get('trust_score', 0)
    
    if request.method == 'POST':
        selected_option = request.form.get('option')
        correct_option = scenarios[current_question]["correct"]
        
        # Update the trust score based on the answer
        if int(selected_option) == correct_option:
            session['trust_score'] += 10
        else:
            session['trust_score'] -= 10
        
        # Cap trust score between 0 and 100
        if session['trust_score'] > 100:
            session['trust_score'] = 100
        elif session['trust_score'] < 0:
            session['trust_score'] = 0

        # Move to the next question
        session['current_question'] += 1
        current_question = session['current_question']
    
    # Check if the quiz is completed
    if current_question >= len(scenarios):
        return redirect(url_for('summary'))

    return render_template('quiz.html', scenario=scenarios[current_question], question_num=current_question + 1, trust_score=session['trust_score'])

@app.route('/summary')
def summary():
    trust_score = session.get('trust_score', 0)
    feedback = "Great job!" if trust_score >= 70 else "Keep practicing!"
    return render_template('summary.html', trust_score=trust_score, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
