from PIL import Image

from enums.CellType import CellType

images = {
    CellType.Bunny:     Image.open("res/cell_images/bunny.png"),
    CellType.Carrot:    Image.open("res/cell_images/carrot.png"),
    CellType.Empty:     Image.open("res/cell_images/empty.png"),
    CellType.Trap:      Image.open("res/cell_images/trap.png")
}
