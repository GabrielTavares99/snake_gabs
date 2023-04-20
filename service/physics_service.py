class PhysicsService:

    @staticmethod
    def has_collision(item1, item2):
        return item1[0] == item2[0] and item1[1] == item2[1]
