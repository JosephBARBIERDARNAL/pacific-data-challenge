import numpy as np

def get_label_rotation(angle, offset):
   # Rotation must be specified in degrees :(
   rotation = np.rad2deg(angle + offset)
   if angle <= np.pi:
      alignment = "right"
      rotation = rotation + 180
   else: 
      alignment = "left"
   return rotation, alignment

def add_labels(angles, values, labels, offset, ax):
   
   # This is the space between the end of the bar and the label
   padding = 4
   
   # Iterate over angles, values, and labels, to add all of them.
   for angle, value, label, in zip(angles, values, labels):
      angle = angle
      
      # Obtain text rotation and alignment
      rotation, alignment = get_label_rotation(angle, offset)

      # And finally add the text
      ax.text(
         x=angle, 
         y=value + padding, 
         s=label, 
         ha=alignment, 
         va="center", 
         rotation=rotation, 
         rotation_mode="anchor"
      )