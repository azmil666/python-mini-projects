with open('story.txt','r') as f:
    story = f.read()


words = set()

index1=-1
start_char="<"
final_char=">"

for i,char in enumerate(story):
    if char == start_char:
        index1=i
    if (char == final_char and index1 != -1):
        word = story[index1:i+1]
        words.add(word)
        index1 = -1

answer={}
for word in words:
    a=input(f"Enter your choice of word for {word} : ")
    answer[word]=a
for word in words:
    story=story.replace(word,answer[word]) 

print(story)