import numpy as np
import cv2

"""
0-7: w-pawns
8: w-queen
9: w-king
20,21: w-rooks
30,31: w-knights
40,41: w-bishops

10-17: b-pawns
18: b-queen
19: b-king
22,23: b-rooks
32,33: b-knights
42,43: b-bishops
"""
PIECE_IDS = dict()
PIECE_IDS.update({i: f"w-pawn-{i}" for i in range(8)})
PIECE_IDS.update({i + 10: f"b-pawn-{i}" for i in range(8)})
PIECE_IDS.update({i + 20: f"w-rook-{i}" for i in range(2)})
PIECE_IDS.update({i + 22: f"b-rook-{i}" for i in range(2)})
PIECE_IDS.update({i + 30: f"w-knight-{i}" for i in range(2)})
PIECE_IDS.update({i + 32: f"b-knight-{i}" for i in range(2)})
PIECE_IDS.update({i + 40: f"w-bishop-{i}" for i in range(2)})
PIECE_IDS.update({i + 42: f"b-bishop-{i}" for i in range(2)})
PIECE_IDS.update({
    8: "w-queen",
    9: "w-king",
    18: "b-queen",
    19: "b-king"
})

def generate_marker(dictionary, id, image_size, output_file):
    # load specified aruco dictionary 
    dict = cv2.aruco.getPredefinedDictionary(dictionary)

    # create array to draw aruco marker onto
    tag = np.zeros((image_size, image_size, 1), dtype="uint8")

    # draw aruco marker onto tag array
    cv2.aruco.generateImageMarker(dict, id, image_size, tag, 1)

    # save marker image to disk
    cv2.imwrite(output_file, tag)


def generate_all_chess_markers():
    dictionary = cv2.aruco.DICT_7X7_50
    
    for id in PIECE_IDS:
        generate_marker(dictionary, id, 800, f"tags/{PIECE_IDS[id]}.png")

generate_all_chess_markers()