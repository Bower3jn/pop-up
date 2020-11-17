from guizero import App, Text, Picture
import random
from PIL import Image

app = App(title="System Sustainability Assistant")
printinglmt = app.yesno("S.S.A", "Are you sure you need to print?")
if printinglmt == True:
    img= [
        "deforest.gif",
        "cutwood.gif",
        "deforestation-brazil.gif",
        "view.gif"
    ]
    picture = Picture(app,image=random.choice(img))
    arg = [
        "Trees help us breathe",
        "Trees are important"
    ]
    message = Text(app,text=random.choice(arg))
    app.warn("S.S.A", "Continue to print")
else:
    display = Picture(app,image= "ecofriendly.gif")
    app.info("S.S.A", "Good job!")
    
app.display()