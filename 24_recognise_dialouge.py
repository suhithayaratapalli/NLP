
import re

dialog_act={
    "greetings":r"hello|hi|hey",
    "inquiry":r"how are you| what",
    "request":r"can you please|could you",
    "response":r"ok|sure"
}
def classify(utt):
    utt.lower()
    for act, pt in dialog_act.items():
        if re.search(pt,utt):
            return act
    return "unknown"
conv=[
    "hello! how are you",
    "im doing well, How about you",
    "can you please pass the salt",
    "sure , here you go"
]
res=[]
for utt in conv:
    res.append((utt,classify(utt)))

print(res)