import google.generativeai as genai   # pip install -q -U google-generativeai

API_KEY = 'AIzaSyCWSTzDbV4y9M5iSiVPlbYWBq4djZ-p3Sg'
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

def recommend_sentences(user_input):
  prompt = f"Write 3 different grammatically correct and simple sentences that contain with the following words: '{user_input}'"
  response = model.generate_content(prompt)
  sentences = response.text
  return sentences

user_input = ["Hello", "Goodbye", "Peace", "Won"]
recommendations = recommend_sentences(user_input)
print(recommendations)