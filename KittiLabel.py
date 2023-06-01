class KittiLabel:
    def __init__(self, label_string):
        label_parts = label_string.strip().split(' ')
        
        self.class_label = label_parts[0]
        self.truncation = float(label_parts[1])
        self.occlusion = int(label_parts[2])
        self.alpha = float(label_parts[3])
        self.bbox = [float(coord) for coord in label_parts[4:8]]
        self.dimensions = [float(dimension) for dimension in label_parts[8:11]]
        self.location = [float(coord) for coord in label_parts[11:14]]
        self.rotation = float(label_parts[14])
        
    def to_string(self):
        bbox_str = ' '.join([f'{coord:.2f}' for coord in self.bbox])
        dimensions_str = ' '.join([str(dimension) for dimension in self.dimensions])
        location_str = ' '.join([str(coord) for coord in self.location])

        label_str = f"{self.class_label} {self.truncation:.2f} {self.occlusion} {self.alpha:.2f} {bbox_str} {dimensions_str} {location_str} {self.rotation:.2f}\n"
        return label_str
    
    def resize(self, prev_dimensions, new_dimensions, padding_tuple):
        x_ratio = new_dimensions[0] / prev_dimensions[0]
        y_ratio = new_dimensions[1] / prev_dimensions[1]

        self.bbox[0] *= x_ratio
        self.bbox[1] *= y_ratio
        self.bbox[2] *= x_ratio
        self.bbox[3] *= y_ratio
        
        self.bbox[0] += padding_tuple[0]
        self.bbox[1] += padding_tuple[1]
        self.bbox[2] += padding_tuple[0]
        self.bbox[3] += padding_tuple[1]