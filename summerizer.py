import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text="""Steven Paul Jobs (February 24, 1955 – October 5, 2011) was an American business magnate, inventor, and investor. He was the co-founder, chairman, and CEO of Apple; the chairman and majority shareholder of Pixar; a member of The Walt Disney Company's board of directors following its acquisition of Pixar; and the founder, chairman, and CEO of NeXT.
He was a pioneer of the personal computer revolution of the 1970s and 1980s, along with his early business partner and fellow Apple co-founder Steve Wozniak.Jobs was born in San Francisco to a Syrian father and German-American mother. He was adopted shortly after his birth. Jobs attended Reed College in 1972 before withdrawing that same year. In 1974, he traveled through India seeking enlightenment before later studying Zen Buddhism. 
He and Wozniak co-founded Apple in 1976 to sell Wozniak's Apple I personal computer. Together the duo gained fame and wealth a year later with production and sale of the Apple II, one of the first highly successful mass-produced microcomputers. Jobs saw the commercial potential of the Xerox Alto in 1979, which was mouse-driven and had a graphical user interface (GUI). This led to the development of the unsuccessful Apple Lisa in 1983, followed by the breakthrough Macintosh in 1984, the first mass-produced computer with a GUI. The Macintosh introduced the desktop publishing industry in 1985 with the addition of the Apple LaserWriter, the first laser printer to feature vector graphics."""

def summerizer(rawdocs):
    stopwords=list(STOP_WORDS) #removing stopwords

    # print(stopwords)

    nlp=spacy.load('en_core_web_sm')

    doc=nlp(rawdocs)

    print(doc)

    token=[token.text for token in doc]

    print(token)

    word_freq={}

    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text]=1
            else:
                word_freq[word.text]+=1
            
    # print(word_freq)

    max_freq=max(word_freq.values())
    # print(max_freq)

    for word in word_freq.keys():
        word_freq[word]=word_freq[word]/max_freq

    # print(word_freq)

    sent_tokens=[sent for sent in doc.sents]
    # print(sent_tokens)

    sent_scores={}

    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent]=word_freq[word.text]
                else:
                    sent_scores[sent]+=word_freq[word.text]

    # print(sent_scores)

    select_len=int(len(sent_tokens)*0.3)

    # print(select_len)

    summary = nlargest(select_len,sent_scores,key=sent_scores.get)

    # print(summary)

    final_summary=[word.text for word in summary]
    summary=' '.join(final_summary)
    # print(summary)

    # print("Length of original text ",len(text.split(' ')))
    # print("Length of summerized text ",len(summary.split(' ')))

    return summary,doc,len(rawdocs.split(' ')),len(summary.split(' '))