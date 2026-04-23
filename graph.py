from intent import classify_intent
from rag import format_pricing
from tools import mock_lead_capture

class AgentState:
    def __init__(self):
        self.intent = None
        self.name = None
        self.email = None
        self.platform = None


state = AgentState()


def process_message(user_input):
    state.intent = classify_intent(user_input)

    if state.intent == "greeting":
        return "Hello! Ask me about pricing or features."

    if state.intent == "product":
        return format_pricing()

    if state.intent == "high_intent":

        if not state.name:
            state.name = user_input
            return "Great! Can I have your email?"

        if not state.email:
            state.email = user_input
            return "Which platform do you create content on? "

        if not state.platform:
            state.platform = user_input

            mock_lead_capture(state.name, state.email, state.platform)

            return "Thank you! "

    return "I can help you with pricing, features or signup!"