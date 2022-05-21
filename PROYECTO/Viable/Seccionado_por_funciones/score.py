def Your_score(score):
    value = score_font.render("Tu puntuación: " + str(score), True, yellow)
    dis.blit(value, [0, 0])