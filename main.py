import gtts
import pdfplumber


def convert_pdf_audio():
    data = get_pdf_with_plumber('lacerillera.pdf')
    save_text_to_audio(data)
    save_txt(data)
    print('finalizo')

def get_pdf_with_plumber(pdf_file_path):
    reader = pdfplumber.open(pdf_file_path)

    data_text = ''
    for page in reader.pages:
        data_text += page.extract_text()

    return data_text

def save_txt(data):
    with open('sample.txt', 'w') as writer:
        writer.writelines(data)

def save_text_to_audio(txt):
    tts = gtts.gTTS(txt, lang='es')
    tts.save('audio.mp3')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    convert_pdf_audio()

