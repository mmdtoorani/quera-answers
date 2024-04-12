# Exceptions
class AbstractLengthError(Exception):
    pass

class KeywordInvalid(Exception):
    pass

class PaperSizeInvalid(Exception):
    pass


paper_file_path = "paper2_sample.txt"

with open(paper_file_path, encoding="utf-8") as f:
    paper = f.read()


def extract_paper(paper_file_path: str, font_size: int) -> dict:
    with open(paper_file_path, encoding="utf-8") as f:
        paper = f.read()
    
    title = paper.split("ABSTRACT")[0].removeprefix("TITLE\n").removesuffix("\n")
    abstract = paper.split("KEYWORDS")[0].split("ABSTRACT")[1].removeprefix("\n").removesuffix("\n")
    if len(abstract.split(" ")) > 150:
        raise AbstractLengthError("The abstract section can't be more than 150 words")
    
    keywords = paper.split("INTRODUCTION")[0].split("KEYWORDS")[1].removeprefix("\n").removesuffix("\n").split(",")
    if len(keywords) > 5:
        raise KeywordInvalid("You can't put more than 5 keywords")
    if keywords != sorted(keywords):
        raise KeywordInvalid("Keywords are not sorted")
    
    introduction = paper.split("BODY")[0].split("INTRODUCTION")[1].removeprefix("\n").removesuffix("\n")
    body = paper.split("CONCLUSION")[0].split("BODY")[1].removeprefix("\n").removesuffix("\n")
    conclusion = paper.split("REFERENCES")[0].split("CONCLUSION")[1].removeprefix("\n").removesuffix("\n")

  
    refs = paper.split("REFERENCES")[1].removeprefix("\n").split("\n")
    references = []
    count = 0
    for i in refs:
        try:
            count += 1
            if i[0] == '[' and i[2] == ']':
                references.append(i[4:])
        except IndexError:
            continue


    word_count = 0
    for line in paper.split("\n"):
        for word in line.split(" "):
            if word not in ["ABSTRACT","TITLE","KEYWORDS","INTRODUCTION","BODY","CONCLUSION","REFERENCES"]:
                print(word)
                word_count += 1
        
        if word == "":
            word_count -= 1
            

    if font_size >= 16 and word_count <= 512:
        page_count = 1
    elif 16 < font_size <= 32 and 256 <= word_count < 512:
        page_count = 2
    
    if page_count > 9:
        raise PaperSizeInvalid("The whole paper can't be more than 9 pages")
    
    return {"title": title,
            "abstract": abstract,
            "keywords": keywords,
            "introduction": introduction,
            "body": body,
            "conclusion":conclusion,
            "references": references,
            "word_count": word_count,
            "page_count": page_count}
