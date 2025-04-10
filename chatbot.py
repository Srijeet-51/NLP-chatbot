import random
import pickle

# Load the trained model, vectorizer, and intents
with open("model.pkl", "rb") as f:
    model, vectorizer, intents = pickle.load(f)

def predict_intent(user_input):
    user_vec = vectorizer.transform([user_input])
    prediction = model.predict(user_vec)[0]
    return prediction

def get_response(intent_tag):
    for intent in intents['intents']:
        if intent['tag'] == intent_tag:
            return random.choice(intent['responses'])
    return "Sorry, I didn't understand that."

def chatbot_response(message):
    intent = predict_intent(message)
    response = get_response(intent)
    return response

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print("Bot:", chatbot_response(user_input))
