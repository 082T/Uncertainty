import matplotlib.pyplot as plt
import matplotlib.patches as patches
from KittiLabel import KittiLabel

label_colors = {
    "Car": "red",
    "Truck": "green",
    "Pedestrian": "blue",
    "default": "yellow",
}


def draw_labeled_image(image, labels, fig_size=(25, 25), font_size=14, include_dontcare=False, plot_fig=True,
                       save_fig_path=None):
    fig, ax = plt.subplots(figsize=fig_size)
    ax.imshow(image)

    for label in labels:
        kitti_label = KittiLabel(label)
        x_min, y_min, x_max, y_max = kitti_label.bbox

        class_name = kitti_label.class_label
        if not include_dontcare and class_name == "DontCare":
            continue
        width, height = kitti_label.get_cwh()[1]
        color = label_colors.get(class_name) if class_name in label_colors else label_colors.get("default")
        rect = patches.Rectangle((x_min, y_min), width, height, linewidth=1, edgecolor=color, facecolor=color,
                                 alpha=0.3)
        ax.add_patch(rect)
        ax.text(x_min, y_min, class_name, fontsize=font_size, bbox=dict(facecolor=color, alpha=0.5))
    if save_fig_path:
        plt.savefig(save_fig_path)
    if plot_fig:
        plt.show()