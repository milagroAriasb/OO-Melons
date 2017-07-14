import cs1graphics as cg 

paper = cg.Canvas()
melon = cg.Circle()

def make_paper():
    
    paper.setWidth(100)
    paper.setHeight(100)
    paper.setBackgroundColor("white")
    paper.setTitle("Ube")


def make_melon():
    
    melon.setRadius(25)
    melon.setFillColor("darkGreen")
    melon.moveTo(50, 50)
    paper.add(melon)

msg = cg.Text("Ubermelon", 10)
msg.moveTo(50, 80)
paper.add(msg)
make_paper()
make_melon()
