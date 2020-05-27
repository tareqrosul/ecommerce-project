from PIL import Image
var="protein.jpg"
image = Image.open(var)
new_image = image.resize((960, 796))
new_image.save(var)
