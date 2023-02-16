FROM python:3.9-alpine

RUN mkdir /a2
WORKDIR /a2

COPY word_count.py .
COPY IF.txt .
COPY Limerick.txt .

#CMD [ "python", "word_count.py" ]
CMD [ "sh", "-c", "python /a2/word_count.py && cat /a2/result.txt" ]