Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from sklearn.feature_extraction.text import CountVectorizer
>>> text = "Hello world this is a text document. We are learning python for machine learning"
>>> vectorizer = CountVectorizer()
>>> vectorizer.fit(text)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    vectorizer.fit(text)
  File "C:\Python36\lib\site-packages\sklearn\feature_extraction\text.py", line 836, in fit
    self.fit_transform(raw_documents)
  File "C:\Python36\lib\site-packages\sklearn\feature_extraction\text.py", line 860, in fit_transform
    "Iterable over raw text documents expected, "
ValueError: Iterable over raw text documents expected, string object received.
>>> text = ["Hello world this is a text document. We are learning python for machine learning"]
>>> vectorizer.fit(text)
CountVectorizer(analyzer='word', binary=False, decode_error='strict',
        dtype=<class 'numpy.int64'>, encoding='utf-8', input='content',
        lowercase=True, max_df=1.0, max_features=None, min_df=1,
        ngram_range=(1, 1), preprocessor=None, stop_words=None,
        strip_accents=None, token_pattern='(?u)\\b\\w\\w+\\b',
        tokenizer=None, vocabulary=None)
>>> x = vectorizer.fit(text)
>>> x.vocabulary_
{'hello': 3, 'world': 11, 'this': 9, 'is': 4, 'text': 8, 'document': 1, 'we': 10, 'are': 0, 'learning': 5, 'python': 7, 'for': 2, 'machine': 6}
>>> x = vectorizer.fit_transform(text)
>>> x
<1x12 sparse matrix of type '<class 'numpy.int64'>'
	with 12 stored elements in Compressed Sparse Row format>
>>> x.toarray()
array([[1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1]], dtype=int64)
>>> text
['Hello world this is a text document. We are learning python for machine learning']
>>> text_1 = 'Hello world this is a text document. We are learning python for machine learning'
>>> text_list = text_1.split()
>>> text_list
['Hello', 'world', 'this', 'is', 'a', 'text', 'document.', 'We', 'are', 'learning', 'python', 'for', 'machine', 'learning']
>>> text_unique = set(text_list)
>>> text_unique
{'for', 'text', 'learning', 'is', 'document.', 'a', 'are', 'python', 'this', 'machine', 'world', 'We', 'Hello'}
>>> text_list = list(text_unique)
>>> len(text_list)
13
>>> 1/13
0.07692307692307693
>>> import math
>>> idf = math.log(10/4)
>>> idf
0.9162907318741551
>>> tf = 1/13
>>> tf * idf
0.0704839024518581
>>> from sklearn.feature_extraction.text import TfidfTransformer
>>> x
<1x12 sparse matrix of type '<class 'numpy.int64'>'
	with 12 stored elements in Compressed Sparse Row format>
>>> tfidf = TfidfTransformer()
>>> tfidf_vect = tfidf.fit(x)
>>> tfidf_vect
TfidfTransformer(norm='l2', smooth_idf=True, sublinear_tf=False, use_idf=True)
>>> tfidf = TfidfTransformer()
>>> tfidf_vect = tfidf.fit_transform(x)
>>> tfidf_vect
<1x12 sparse matrix of type '<class 'numpy.float64'>'
	with 12 stored elements in Compressed Sparse Row format>
>>> tfidf_vect.toarray()
array([[ 0.25819889,  0.25819889,  0.25819889,  0.25819889,  0.25819889,
         0.51639778,  0.25819889,  0.25819889,  0.25819889,  0.25819889,
         0.25819889,  0.25819889]])
>>> 
