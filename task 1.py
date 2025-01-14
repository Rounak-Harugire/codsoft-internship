import re
from datetime import datetime

# Function to process user input and respond based on predefined rules
def chatbot_response(user_input):
    # Convert user input to lowercase for easier matching
    user_input = user_input.lower()

    # Check for common greetings
    if re.search(r'\bhello\b|\bhi\b|\bhey\b', user_input):
        return "Hello! How can I assist you today?"
    
    # Check for farewell
    elif re.search(r'\bbye\b|\bgoodbye\b|\bsee you\b', user_input):
        return "Goodbye! Have a great day!"

    # Check for asking about chatbot capabilities
    elif re.search(r'\bwhat can you do\b|\bwhat is your purpose\b|\bwhat is your function\b', user_input):
        return "I am a simple chatbot, and I can assist you with answering basic questions, telling jokes, and giving time updates."

    # Check for user asking for help
    elif re.search(r'\bhelp\b|\bassist\b|\bproblem\b', user_input):
        return "How can I assist you? Please tell me your issue."

    # Check for user asking their name
    elif re.search(r'\bwhat is your name\b|\bwho are you\b', user_input):
        return "I am your friendly chatbot! You can call me Chatbot."

    # Check for asking about the weather
    elif re.search(r'\bweather\b|\bforecast\b', user_input):
        return "I am sorry, I can't provide weather updates right now."

    # Check for asking the current time
    elif re.search(r'\btime\b|\bwhat time is it\b|\bcurrent time\b', user_input):
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."

    # Check for asking a joke
    elif re.search(r'\bjoke\b|\btell me a joke\b', user_input):
        return "Why don't skeletons fight each other? They don't have the guts!"

    # Check for asking about famous places
    elif re.search(r'\bfamous places\b|\btop tourist spots\b', user_input):
        return "Some popular tourist spots are the Eiffel Tower, Great Wall of China, and the Taj Mahal."

    # Check for asking about technology
    elif re.search(r'\btechnology\b|\bAI\b|\bmachine learning\b', user_input):
        return "Technology is constantly evolving. AI and Machine Learning are revolutionizing industries by automating tasks and providing smarter solutions."

    # Check for asking about movies
    elif re.search(r'\bmovie\b|\bfilms\b|\bwhat movies do you recommend\b', user_input):
        return "Some popular movies are 'Inception', 'The Dark Knight', and 'The Shawshank Redemption'. What type of movies do you like?"

    # If input does not match any predefined rules
    else:
        return "I'm sorry, I didn't understand that. Can you please clarify?"

# Chatbot interaction loop
print("Chatbot: Hello! I am here to assist you. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    
    # Exit the loop if the user says goodbye
    if re.search(r'\bbye\b|\bgoodbye\b|\bsee you\b', user_input.lower()):
        print("Chatbot: Goodbye! Have a great day!")
        break
    
    # Respond based on user input
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
