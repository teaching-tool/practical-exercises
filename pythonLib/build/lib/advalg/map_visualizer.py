import matplotlib.pyplot as plt
import matplotlib.image as mpimg

pos = {
    "Copenhagen": (687,517),
    "Aarhus": (383,407),
    "Odense": (408,576),
    "Aalborg": (346,199),
    "Esbjerg": (158,564),
    "Horsens": (336,475),
    "Randers": (360,336),
    "Kolding": (288,557),
    "Vejle": (296,510),
    "Greve": (654,534),
    "Svendborg": (435,656),
    "Thisted": (190,220),
    "Holstebro": (180,360),
    "Aabenraa": (281,664),
    "Faaborg": (388,649),
    "Grenaa": (470,347)
}

def plot_tour(tour, title):
    """
    Visualizes the given tour of danish cities on a map.
    The given title is shown on top of the map.
    """
    xs = [pos[city][0] for city in tour]
    ys = [pos[city][1] for city in tour]

    img = mpimg.imread("data/Denmark.png")
    plt.title(title)
    plt.imshow(img)
    plt.axis("off")
    plt.plot(xs,ys, color="red", marker=".", mfc="blue", mec="blue", linewidth=3)
    plt.show()