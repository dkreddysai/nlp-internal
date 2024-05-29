import Augmentor
p = Augmentor.Pipeline(r"C:\Users\devak\Downloads\download.jpg")
p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
p.zoom(probability=0.3, min_factor=1.1, max_factor=1.6)
p.sample(10000)
