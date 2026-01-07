import google.generativeai as genai

# 1. Provide your API Key
genai.configure(api_key="AIzaSyAgftoSJQeC5kdhpM8foOV66FgfUGGCvQY")

# 2. Define the 'Identity' (Step 2 & 4 of your project)
system_instruction = (
    "You are a specialized Event Management Explainer Bot. "
    "Your ONLY goal is to provide information about event planning, roles, and setup. "
    "RESTRICTIONS: "
    "- Do NOT book venues or suggest specific dates for booking. "
    "- Do NOT register participants or ask for personal user data. "
    "- Do NOT handle payments or pricing calculations. "
    "- If asked to do any of the above, say: 'I am an information-only bot and cannot perform actions.'"
)

# 3. Initialize the Gemini 1.5 Flash Model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_instruction
)
