import get_image_and_labels_from_one_image as labim

for i in range (9,29):
    print('I am reading the file', i)
    labim.get_images_and_labels(i)
    print('the file has been read')
