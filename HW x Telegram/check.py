import aspose.words as aw
# load the Word document
def extract(path):
    print("Gone func_")
    #path="D:\HW x Telegram\guides\guide2\ex.docx"
    doc = aw.Document(path)
    print("Gone func? bye&")
    # retrieve all shapes
    shapes = doc.get_child_nodes(aw.NodeType.SHAPE, True)
    imageIndex = 0
    # loop through shapes
    for shape in shapes :
        shape = shape.as_shape()
        print("dead")
        if (shape.has_image) :
            print("Gone")
            # set image file's name
            imageFileName = f"Image.ExportImages.{imageIndex}_{aw.FileFormatUtil.image_type_to_extension(shape.image_data.image_type)}"
            # save image
            shape.image_data.save("D:\HW x Telegram\guides\guide2\ "+imageFileName)
            imageIndex += 1 