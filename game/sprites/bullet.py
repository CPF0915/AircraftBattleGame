class Bullet(pygame.sprite.Sprite):
    def __init__(self, image_path, position):
        super(Bullet, self).__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self):
        pass