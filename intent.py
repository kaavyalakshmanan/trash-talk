from google.cloud import dialogflow
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file('C:/Users/Amy George/PycharmProjects/trash-talk/recyclebot-3b638be41671.json')


def create_intent(project_id, display_name, training_phrases_parts,
                  message_texts):
    """Create an intent of the given intent type."""
    # intents_client = dialogflow.IntentsClient(credentials=credentials)
    # session_client = dialogflow.SessionsClient(credentials=credentials)


def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""
    from google.cloud import dialogflow

    session_client = dialogflow.SessionsClient(credentials=credentials)
    print(session_client)

    session = session_client.session_path(project_id, session_id)
    print("Session path: {}\n".format(session))

    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)

        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

        print("=" * 20)
        print("Query text: {}".format(response.query_result.query_text))
        print(
            "Detected intent: {} (confidence: {})\n".format(
                response.query_result.intent.display_name,
                response.query_result.intent_detection_confidence,
            )
        )
        print("Fulfillment text: {}\n".format(response.query_result.fulfillment_text))



detect_intent_texts("propane-analogy-270422", "123456789", "I know french", "en-US")