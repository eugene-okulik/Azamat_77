class Flower:
    def __init__(self, name, color, freshness, stem_length, cost, lifespan_in_days):
        self.name = name
        self.color = color
        self.freshness = freshness
        self.stem_length = stem_length
        self.cost = cost
        self.lifespan_in_days = lifespan_in_days


class Rose(Flower):
    def __init__(self, color, freshness, stem_length, cost, lifespan_in_days):
        super().__init__("Роза", color, freshness, stem_length, cost, lifespan_in_days)


class Tulip(Flower):
    def __init__(self, color, freshness, stem_length, cost, lifespan_in_days):
        super().__init__("Тюльпан", color, freshness, stem_length, cost, lifespan_in_days)


class Romashka(Flower):
    def __init__(self, color, freshness, stem_length, cost, lifespan_in_days):
        super().__init__("Ромашка", color, freshness, stem_length, cost, lifespan_in_days)


class Bouquet:
    def __init__(self, flowers):  # При создании букета передаём список цветов
        self.flowers = flowers

    def get_total_cost(self):
        total_cost = 0
        for _ in self.flowers:
            total_cost += flower.cost
        return total_cost

    def get_average_lifespan(self):
        average_lifespan = 0
        if not self.flowers:
            return 0
        for _ in self.flowers:
            average_lifespan += flower.lifespan_in_days
        return average_lifespan / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda x: x.freshness, reverse=True)

    def sort_by_cost(self):
        self.flowers.sort(key=lambda x: x.cost)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda x: x.stem_length)

    def sort_by_color(self):
        self.flowers.sort(key=lambda x: x.color)

    def find_by_lifespan(self, days):
        found_flowers = []
        for _ in self.flowers:
            if flower.lifespan_in_days >= days:
                found_flowers.append(flower)
        return found_flowers


rose = Rose("Красная", 9, 80, 250, 7)
tulip = Tulip("Желтая", 8, 35, 150, 5)
romashka= Romashka("Белый", 10, 25, 80, 4)
bouquet = Bouquet([rose, tulip, romashka])

result = bouquet.find_by_lifespan(3)
for flower in result:
    print(flower.name)

print(bouquet.get_average_lifespan())
print(bouquet.get_total_cost())
print(rose.name)
print(rose.cost)
print(tulip.name)
print(tulip.cost)
print(romashka.name)
print(romashka.cost)
print(len(bouquet.flowers))
