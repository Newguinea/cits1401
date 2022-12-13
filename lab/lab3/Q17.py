def can_jump(speed, power, name, injured):
    jumpLenth = speed * power * (0.8**injured)
    if jumpLenth < 1:
        return "{0} made a false attempt!".format(name)
    else:
        return "{0} can jump {1:.2f}m!".format(name, jumpLenth)