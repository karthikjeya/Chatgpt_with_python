import openai
openai.api_key="paste the api key created using chatgpt"

def chatgpt():
    print("hello! how can i help you")
    while True:
        user_input=input("you:")
        if user_input.lower() in ["quit","exit"]:
            print("goodbye!")
            break
        try:
            response=openai.ChatCompletion.create(Model="gpt-4",messages=[{"role":"system","content":"you are a resume builder"},
                                                                          {"role":"user","content":user_input}])
            reply=response["choices"][0]["message"]["content"]
            print(f"chatgpt:{reply}")
        except Exception as e:
            print("error:",e)
if __name__=="__main__":
    chatgpt()
