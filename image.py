import os

import cv2

x_start = 68
y_start = 116

box_width = 501
box_height = 192

x_gap = 1
y_gap = 3

rows = 10
col = 3


def segment_image(image_path, output_dir_name):
    img = cv2.imread(image_path)

    for col_idx in range(col):
        curr_x_start = x_start + (col_idx * (box_width + x_gap))

        curr_x_end = x_start + ((col_idx + 1) * (box_width + x_gap))

        for row_idx in range(rows):
            curr_y_start = y_start + (row_idx * (box_height + y_gap))
            curr_y_end = y_start + ((row_idx + 1) * (box_height + y_gap))

            cv2.circle(img, (curr_x_start, curr_y_start), 2, (255, 0, 0), -1)
            cv2.circle(img, (curr_x_start, curr_y_end), 2, (255, 0, 0), -1)
            cv2.circle(img, (curr_x_end, curr_y_start), 2, (255, 0, 0), -1)
            cv2.circle(img, (curr_x_end, curr_y_end), 2, (255, 0, 0), -1)

            cropped_img = img[curr_y_start:curr_y_end, curr_x_start:curr_x_end]
            output_final_dir = os.path.join("output", output_dir_name)
            os.makedirs(output_final_dir, exist_ok=True)

            filename = str(col_idx) + "_" + str(row_idx) + ".png"
            cv2.imwrite(os.path.join(output_final_dir, filename),
                        cropped_img)

    cv2.imwrite("test.png", img)
