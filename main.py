import os

from pdf2image import convert_from_path

from image import segment_image

pages = convert_from_path("input/demo.pdf")
page_count = 0
for page in pages:
    page_count += 1
    final_path = os.path.join("temp", str(page_count) + ".jpg")
    page.save(final_path, "JPEG")

for page_idx in range(3, 31):
    segment_image("temp/" + str(page_idx) + ".jpg", str(page_idx))
