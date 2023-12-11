import pygame

def get_minimum_distance_side(rect1, rect2):
    dr = abs(rect1.right - rect2.left)
    dl = abs(rect1.left - rect2.right)
    db = abs(rect1.bottom - rect2.top)
    dt = abs(rect1.top - rect2.bottom)

    if min(dl, dr) < min(dt, db):
        direction = "left" if dl < dr else "right"
    else:
        direction = "bottom" if db < dt else "top"
    return direction

def get_collision_side(ball, paddle):
    bounding_box_ball = pygame.Rect(ball["position"][0] - ball["radius"],
                                    ball["position"][1] - ball["radius"],
                                    ball["radius"] * 2,
                                    ball["radius"] * 2)

    bounding_box_paddle = pygame.Rect(paddle["position"][0],
                                      paddle["position"][1],
                                      paddle["width"],
                                      paddle["height"])

    if bounding_box_ball.colliderect(bounding_box_paddle):
        return get_minimum_distance_side(bounding_box_paddle, bounding_box_ball)
    else:
        return "none"
