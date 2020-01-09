data_list = []
with open("QA.txt","r") as f:
    text = f.readlines()
    for line in text:
        if line == '\n': continue
        line = line.replace('.','')
        line = line.replace('"','')
        line = line.replace('?','')
        line = line.replace(',','')
        data_list.append(line.replace('\n', ''))
vocab_list = []
for data in data_list:
    words = data.split(' : ')[1] # 이 부분 주목!
    words = words.split(' ')
    for word in words:
        vocab_list.append(word)
vocab_set = set(vocab_list) # 이런 부분 정말 주의할 것. 수업 내용 연상할 것..!
vocab_list = list(vocab_set)
vocab_list.sort()
textdict = dict()
with open("output_vocab", "w") as f:
    for i in vocab_list:
        textdict[i] = vocab_list.index(i)
        f.write("{key} \t {value}".format(key=i, value=textdict[i]))


text=[]
with open('QA.txt','r') as f:
    while True:
        line = f.readline()
        if not line: break
        text.append(line.replace('\n',''))
vocab = dict()
with open('output.vocab', 'r') as f:
    while True:
        line = f.readline()
        if not line: break
        line = line.replace('\n','')
        key = line.split(' \t ')[0]
        value = line.split(' \t ')[1]
        vocab[key] = value

def word2idx(texts, dic):
    embed_list = []
    for text in texts:
        words = text.split(' : ')[1]
        for word in words.split(' '):
            word = word.replace('.','')
            word = word.replace('"','')
            word = word.replace('?','')
            word = word.replace('.','')
            embed_list.append(dic[word])
    return embed_list

result = word2idx(text,vocab)

with open('embed.txt','w') as f:
    f.write(str(result))