import tkinter as tk

class ChatbotGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Chatbot")

        self.chat_frame = tk.Frame(self.root)
        self.chat_frame.pack(fill=tk.BOTH, expand=True)

        self.chat_text = tk.Text(self.chat_frame, width=80, height=20)
        self.chat_text.pack(fill=tk.BOTH, expand=True)

        self.user_input = tk.Entry(self.root, width=80)
        self.user_input.pack(fill=tk.X, expand=True)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(fill=tk.X)

        self.root.mainloop()

    def send_message(self):
        user_message = self.user_input.get().strip()
        self.chat_text.insert(tk.END, f"User: {user_message}\n")

        # Process user message and generate chatbot response
        chatbot_response = "Chatbot: Hello!"
        self.chat_text.insert(tk.END, f"{chatbot_response}\n")

        # Clear user input field
        self.user_input.delete(0, tk.END)

if __name__ == "__main__":
    gui = ChatbotGUI()
