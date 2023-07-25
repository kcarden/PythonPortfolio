import requests

class ChatGPTWrapper:
    def __init__(self, api_key, model_name="gpt-3.5-turbo", api_url="https://api.openai.com/v1/engines"):
        """
        Initialize the ChatGPTWrapper.

        :param api_key: Your OpenAI API key.
        :param model_name: Name of the language model. Defaults to "gpt-3.5-turbo".
        :param api_url: Base URL for OpenAI API. Defaults to "https://api.openai.com/v1/engines".
        """
        self.api_key = api_key
        self.model_name = model_name
        self.api_url = api_url

    def _create_request_headers(self):
        """
        Create the request headers including the Authorization token.

        :return: Dictionary containing request headers.
        """
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def _send_prompt(self, prompt, max_tokens=150):
        """
        Send a user prompt to the GPT-3.5 model for completion.

        :param prompt: The user input prompt.
        :param max_tokens: The maximum number of tokens to generate in the response. Defaults to 150.
        :return: JSON response from the OpenAI API.
        :raises Exception: If the API request fails.
        """
        data = {
            "engine": self.model_name,
            "prompt": prompt,
            "max_tokens": max_tokens
        }

        response = requests.post(f"{self.api_url}/{self.model_name}/completions", headers=self._create_request_headers(), json=data)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Request failed with status code {response.status_code}: {response.text}")

    def chat(self, prompt):
        """
        Initiate a conversation with the ChatGPT model.

        :param prompt: The user input prompt.
        :return: The generated response from the ChatGPT model.
        """
        try:
            response = self._send_prompt(prompt)
            return response["choices"][0]["text"].strip()
        except Exception as e:
            return str(e)

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual OpenAI API key
    api_key = "YOUR_API_KEY"
    chat_gpt = ChatGPTWrapper(api_key)

    while True:
        user_input = input("You: ")
        if user_input.lower() in ("exit", "quit"):
            print("Exiting.")
            break
        response = chat_gpt.chat(user_input)
        print("ChatGPT:", response)
