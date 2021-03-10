from polylabel import polylabel

# Interesting thing about polylabel --> The vertices need to go around the shape!
print(polylabel([[[0, 0], [0, 1], [1, 1], [1, 0]]]))
