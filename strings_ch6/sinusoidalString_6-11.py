# Write a string in sinusoidal fashion
# Hello_World!
#   e       _      l  
# H   l   o   W  r   d
#       l       o      !
# 
# Prints as snakestring: e_lHloWrdlo

# LUL python is a joke, slicing is amazing
# Just count the snake string where it begins and how often it skips
def snakeString(s):
    return s[1::4] + s[::2] + s[3::4]

if __name__ == "__main__":
    print(snakeString('Hello_World!'))