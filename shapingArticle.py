import re
import glob
from itertools import chain
from functools import reduce
import MeCab
from joblib import Parallel, delayed

target_name = "みりあ"
tagger = MeCab.Tagger("-Owakati -d /usr/lib/mecab/dic/mecab-ipadic-neologd")


def extract_conversation(line):
    # print(f"extrcting now from {line[:10]}...")
    return re.findall(r"([^「]*\s*「.*?」)", line)


def split_speaker(conv):
    # print(f"spliting speaker now from {conv[:10]}...")
    speaker, sentence = re.search(r"(.*)\s*「(.*)」", conv).groups()
    return {"speaker": speaker, "sentence": sentence}


def convs_integrate(convs, cursor, width):
    return reduce(lambda x, y: {'speaker':x['speaker']+y['speaker'], 'sentence':x['sentence']+y['sentence']}, 
                  convs[cursor:cursor+width+1])

def shape_conversation(lines):
    convs = ([split_speaker(conv) for conv in list(chain.from_iterable(Parallel(n_jobs=-1, verbose=7)([delayed(extract_conversation)(line) for line in lines])))])
    return [generate_conv_pair(convs, target_cursor) for target_cursor in [cursor for cursor, conv in enumerate(convs) if target_name in conv['speaker']]]
    # return [split_speaker(conv) for conv in convs if conv["speaker"] is target_name]


def generate_conv_pair(convs, a_cursor):
    q_cursor = a_cursor-1
    if q_cursor < 0:
        return None
    else:
    	while convs[q_cursor]['speaker'] == convs[a_cursor]['speaker']:
            q_cursor = q_cursor-1
            if q_cursor < 0:
                break
    if q_cursor < 0:
        return None
    
    conv_pair = {"q": convs[q_cursor], 
                 "a": convs_integrate(convs, q_cursor+1, a_cursor-(q_cursor+1))}

    print_interaction(conv_pair)
    return conv_pair


def print_interaction(conv):
    print()
    print(f"{conv['q']['speaker']} ... {conv['q']['sentence']}")
    print("----------------------------------")
    print(f"{conv['a']['speaker']} ... {conv['a']['sentence']}")
    print()


def dump_interaction(convs, number):
    questions = [tagger.parse(conv['q']['sentence']) for conv in convs]
    answers = [tagger.parse(conv['a']['sentence']) for conv in convs]
    with open(f"dialogue_data/input_style_{number}.txt", "w") as f:
        for q in questions:
            f.write(q + "\n")
    with open(f"dialogue_data/output_style_{number}.txt", "w") as f:
        for a in answers:
            f.write(a + "\n")


files = list(glob.iglob("./articles/**/*.dat", recursive=True))[27290:]
convs = []
for number, file_name in enumerate(files):
    print(file_name)
    with open(file_name, "r") as f:
        lines = f.readlines()
    convs = [conv for conv in shape_conversation(lines) if not isinstance(conv, type(None))]
    dump_interaction(convs, number)
