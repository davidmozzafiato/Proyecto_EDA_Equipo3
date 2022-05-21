def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / x, dis_height / y])