import speech_recognition as sr
import MeCab


def SP_rec(AUDIO_FILE):
    r = sr.Recognizer()
    try:
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)
            text = r.recognize_google(audio, language='ja')
            #t = MeCab.Tagger("mecabrc")#デフォルト
            #t = MeCab.Tagger("-Owakati")#分かち書きのみを出力
            t = MeCab.Tagger("-Ochasen")#ChaSen 互換形式
            #t = MeCab.Tagger("-Oyomi")#読みのみを出力
            nouns = [line.split()[0] for line in t.parse(text).splitlines()
               if "名詞" in line.split()[-1]]
            for odd in nouns:
                print('Transcription result of voice data:\n\n\n', odd)
                print('\n')
                #return t.parse(text)

    except sr.UnknownValueError:
        print("could not understand audio\n")
            

