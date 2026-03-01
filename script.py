import os
import collections
import re
import socket

if_path = '/home/data/IF.txt'
always_path = '/home/data/AlwaysRememberUsThisWay.txt'
output_dir = '/home/data/output'
os.makedirs(output_dir, exist_ok=True)
result_path = os.path.join(output_dir, 'result.txt')

contractions = {
    "i'm": "i am",
    "can't": "can not",
    "don't": "do not",
    "you're": "you are",
    "i'll": "i will",
    "that's": "that is",
    "you've": "you have",
    "he's": "he is",
    "it's": "it is",
    "won't": "will not",
    "couldn't": "could not",
    # Add more common contractions if needed
}

def clean_text(text, split_contractions=False):
    text = text.lower()
    text = text.replace("’", "'").replace("‘", "'").replace("—", "-")

    if split_contractions:
        # Split contractions: don't -> don t, i'm -> i m, you're -> you re
        text = re.sub(r"([a-z0-9])'([a-z0-9])", r"\1 \2", text)

    text = re.sub(r"[^\w\s]", "", text)
    return text.split()

with open(if_path, 'r') as f:
    if_text = f.read()
if_words = clean_text(if_text, split_contractions=False)
word_count_if = len(if_words)

with open(always_path, 'r') as f:
    always_text = f.read()
always_words = clean_text(always_text, split_contractions=True)
word_count_always = len(always_words)

grand_total = word_count_if + word_count_always

counter_if = collections.Counter(if_words)
top3_if = counter_if.most_common(3)

counter_always = collections.Counter(always_words)
top3_always = counter_always.most_common(3)

ip = socket.gethostbyname(socket.gethostname())

with open(result_path, 'w') as f:
    f.write(f"Total words in IF.txt: {word_count_if}\n")
    f.write(f"Total words in AlwaysRememberUsThisWay.txt: {word_count_always}\n")
    f.write(f"Grand total: {grand_total}\n")
    f.write("Top 3 words in IF.txt:\n")
    for w, c in top3_if:
        f.write(f"{w}: {c}\n")
    f.write("Top 3 words in AlwaysRememberUsThisWay.txt:\n")
    for w, c in top3_always:
        f.write(f"{w}: {c}\n")
    f.write(f"IP address: {ip}\n")

with open(result_path, 'r') as f:
    print(f.read())
