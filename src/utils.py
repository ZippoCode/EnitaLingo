from src.download_datasets import download_hugging_face_sentences, save_sentences_to_files


def build_dataset():
    english_sentences, italian_sentences = download_hugging_face_sentences()
    with open('ita.txt') as file:
        lines = file.readlines()

    for line in lines:
        english_sentences.append(line.split("\t")[0])
        italian_sentences.append(line.split("\t")[1])

    save_sentences_to_files(english_sentences, italian_sentences)
    assert len(english_sentences) == len(italian_sentences)
    print(f"Downloaded {len(english_sentences)} sentence")
