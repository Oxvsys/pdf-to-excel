import io

from google.cloud import vision

from extract import extract

client = vision.ImageAnnotatorClient()

file = open("final.csv", "w")

file.write("Box-ID,Voter ID,Name,Parent Name,House No.,Age,Gender\n")

for row_idx in range(10):
    for col_idx in range(3):
        with io.open("output/5/" + str(col_idx) + "_" + str(row_idx) + ".png", 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        response = client.text_detection(image=image)
        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))
        texts = response.text_annotations

        print(texts[0].description)
        file.write(extract(texts[0].description))
